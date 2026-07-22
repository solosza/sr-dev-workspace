# Fixture Wiring (Conftest) — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Conftest Architecture, Environment & Config Management, and Test Data Management rules apply. Every decision below was settled in a full design walkthrough: [docs/walkthroughs/2026-07-13-conftest-design.md](../../../docs/walkthroughs/2026-07-13-conftest-design.md) (11 sections, grounded in all three reference repos + v2 as anti-pattern evidence + a dry run against real autopend SIT data).

## Decision

Synthesize from proven sources; build fresh what no reference implements:
- **platform-selenium** (copy/extend): CLI options with env-var fallback, session config fixture, function-scoped driver with factory call, HTML report metadata, dynamic marker registration
- **hmsa-healthcare-qa** (copy pattern): session-scoped DB interface; readmissions domain conftest (constants + parametrize tuples)
- **Fresh design** (mandated by contract, no reference implements it): credentials resolution, logging setup, Layer 2–4 fixture stack
- **v2** (anti-pattern/architecture evidence only — clean-room rule): tools/conftest.py duplication proves sibling conftests don't compose; committed passwords and per-env user files are the banned patterns

## Pattern Structure

```
tests/
├── conftest.py                    ← ROOT: bootstrap, pytest_plugins, CLI options,
│                                     config, credentials, logger, report hooks, markers
└── [domain]/                      ← e.g. autopend/
    ├── conftest.py                ← domain constants, parametrize tuples, L2-L4 fixtures
    ├── data/                      ← committed scenario JSON (role-keyed where workflow-shaped)
    │   └── tc001-happy-path.json
    └── test_*.py

framework/fixtures/                ← fixture MODULES, loaded once via pytest_plugins
├── browser_fixtures.py            ← driver + browser (function-scoped)
├── api_fixtures.py                ← api (session-scoped)
├── db_fixtures.py                 ← db (session-scoped)
├── soap_fixtures.py               ← soap (session-scoped)
└── component_fixtures.py          ← truly generic shared components (grid, modal)
```

**Why modules, not directory conftests:** pytest only resolves conftests upward — sibling directories can't share fixtures, which is how v2 ended up with tools/conftest.py as a verbatim copy of tests/conftest.py. `pytest_plugins` in the root loads each module once; every test directory composes them.

## Canonical Example: Root Conftest

```python
"""Root conftest — bootstrap, wiring, cross-cutting hooks. No layer logic."""

import json
import logging
import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

# === BOOTSTRAP (runs at import, before everything) ===
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "framework"))
load_dotenv(PROJECT_ROOT / ".env")   # no-op if missing — CI injects real env vars

# === FIXTURE MODULES (the placement decision) ===
pytest_plugins = [
    "fixtures.browser_fixtures",
    "fixtures.api_fixtures",
    "fixtures.db_fixtures",
    "fixtures.soap_fixtures",
    "fixtures.component_fixtures",
]

# === CLI OPTIONS (precedence: CLI > env var > default) ===
def pytest_addoption(parser):
    parser.addoption("--env", action="store",
                     default=os.environ.get("TEST_ENV", "DEV"))
    parser.addoption("--headless", action="store_true",
                     default=os.environ.get("HEADLESS", "false").lower() == "true")
    parser.addoption("--browser", action="store",
                     default=os.environ.get("BROWSER", "chrome"))
    parser.addoption("--scenario-dir", action="store", default=None,
                     help="Directory overriding domain data/ (mirrors its layout)")

# === CONFIG (values only — secrets stay in .env) ===
@pytest.fixture(scope="session")
def config(request):
    env_id = request.config.getoption("--env")
    config_path = PROJECT_ROOT / "framework" / "resources" / "config" / "environment_config.json"
    environments = json.loads(config_path.read_text(encoding="utf-8"))
    if env_id not in environments:
        raise ValueError(f"No environment match found for environment ID: {env_id}")
    return environments[env_id]

# === CREDENTIALS (identity model: DB/API authenticate as USERS too) ===
@pytest.fixture(scope="session")
def credentials(config):
    """Resolve every user up front — config names the env var, .env holds the value."""
    resolved = {}
    for user_key, user in config["users"].items():
        password = os.environ.get(user["password_env"])
        if password is None:
            raise ValueError(f"Env var {user['password_env']} not set — check .env")
        resolved[user_key] = {"username": user["username"], "password": password}
    return resolved

# === LOGGER (console INFO + file DEBUG — the Phase 3.8 seam) ===
@pytest.fixture(scope="session")
def logger(worker_id="master"):
    log = logging.getLogger("hmsa-qa")
    if not log.handlers:                      # guard: never attach twice
        log.setLevel(logging.DEBUG)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))
        log.addHandler(console)
        suffix = "" if worker_id == "master" else f"_{worker_id}"
        file_handler = logging.FileHandler(
            PROJECT_ROOT / "reports" / f"test_run{suffix}.log", mode="w", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
        log.addHandler(file_handler)
    return log

# === REPORT HOOKS ===
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Screenshot on failure — UI tests only, while the driver still exists."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed and "browser" in item.fixturenames:
        browser = item.funcargs["browser"]
        shot_dir = PROJECT_ROOT / "reports" / "screenshots"
        shot_dir.mkdir(parents=True, exist_ok=True)
        browser.take_screenshot(str(shot_dir / f"{item.name}.png"))

# pytest_html_report_title + pytest_configure metadata + _register_dynamic_markers:
# copied verbatim from platform-selenium/tests/conftest.py
```

Curated core markers declared in `pyproject.toml`: `smoke`, `regression`, `ui`, `api`, `db`, `soap`. The dynamic AST scan registers domain markers as the agent creates them (typo trade-off accepted — see ledger §10).

## Canonical Example: Interface Fixture Module

```python
"""framework/fixtures/db_fixtures.py — Layer 1, session-scoped stateless pipe."""

import pytest
from interfaces.sql_server_interface import SqlServerInterface
from resources.factories.connections import create_sql_connection   # Phase 3.5

@pytest.fixture(scope="session")
def db(config, credentials, logger):
    """Session-scoped: connection is expensive; Interface holds no per-test state.
    Authenticates as a USER (config names which identity) — no service accounts."""
    identity = credentials[config["database"]["identity"]]
    connection = create_sql_connection(config["database"], identity)
    interface = SqlServerInterface(connection, config["database"], logger)
    yield interface
    interface.close()                          # explicit — never `del`
```

Browser variant is function-scoped end-to-end (driver factory + `quit()` in teardown) — the browser accumulates test state (cookies, DOM, login); DB/API/SOAP don't.

## Canonical Example: Domain Conftest (from the autopend dry run)

```python
"""tests/autopend/conftest.py — one domain's names, variations, crew, and data."""

import json
import pytest
from _reference.data_objects.claims_data_object import ClaimsDataObject
from _reference.pages.qnxt_claim_page import QnxtClaimPage
from _reference.tasks.claim_discovery_tasks import ClaimDiscoveryTasks
from _reference.tasks.claim_setup_tasks import ClaimSetupTasks
from _reference.tasks.autopend_verification_tasks import AutopendVerificationTasks
from _reference.roles.sit_examiner import SitExaminer

# === DOMAIN CONSTANTS (test-shaping values ONLY — identifiers like SP/table
#     names live in the Data Object's constants, not here; ratified 2026-07-13) ===
UPDATE_ID = "30DAYR"          # expected outcome value — test-shaping, stays here

# === PARAMETRIZE TUPLES (COLLECTION TIME — must be module constants,
#     pytest builds the test list before any fixture exists) ===
ALL_NEGATIVE_FILTERS = [
    ("tob_invalid", "tc002-tob-invalid.json"),
    ("status_07",   "tc003-status-07.json"),
]

# === SCENARIO DATA (RUNTIME — loads via fixture; --scenario-dir overrides) ===
@pytest.fixture
def scenario_dir(request):
    override = request.config.getoption("--scenario-dir")
    return Path(override) if override else Path(__file__).parent / "data"

@pytest.fixture
def tc001_scenario(scenario_dir):
    return json.loads((scenario_dir / "tc001-happy-path.json").read_text(encoding="utf-8"))

# === LAYER 2 — one per domain entity ===
@pytest.fixture
def claims_data(db):
    return ClaimsDataObject(db)

@pytest.fixture
def claim_page(browser):
    return QnxtClaimPage(browser)

# === LAYER 3 — one per domain operation ===
@pytest.fixture
def claim_discovery(claims_data):
    return ClaimDiscoveryTasks(claims_data)

@pytest.fixture
def claim_setup(claim_injection, claim_page):     # injection mechanism: see ledger note
    return ClaimSetupTasks(claim_injection, claim_page)

@pytest.fixture
def autopend_verification(claims_data):
    return AutopendVerificationTasks(claims_data)

# === LAYER 4 — one per persona ===
@pytest.fixture
def sit_examiner(claim_discovery, claim_setup, autopend_verification, credentials):
    return SitExaminer(claim_discovery, claim_setup,
                       autopend_verification, credentials["examiner"])
```

## The Same-Instance Rule (load-bearing — state it, don't imply it)

Tests assert through **the same fixture instances their Tasks consumed**. pytest builds each function-scoped fixture once per test and injects that one instance everywhere it's named — so `claims_data.get_count()` after a workflow reads the state the verification Task produced. A test that constructs its own Layer 2 object inline asserts against a fresh instance whose state is empty: a green test that verifies nothing. This is also why every L2/L3/L4 object gets its own *named* fixture — an object built inside another fixture's body is trapped there, unreachable for assertions.

**Dual assertion pattern (contract L5 rule 6):** tests assert on typed workflow results (`result.history_valid`) AND same-instance L2 state-checks (`claims_data.get_count() > 0`) — results for data the workflow computed, state-checks for system state after it ran.

## Rules

| # | Rule | Source |
|---|------|--------|
| 1 | Layer objects constructed ONLY in fixtures — never inline in tests, Tasks, or Roles | Contract conftest rule 3 |
| 2 | Scope: session = expensive stateless (db/api/soap, config, credentials, logger); function = anything holding test state (driver, browser, all L2–L4) | Ledger §7–8 |
| 3 | Explicit teardown (`yield` + `close()`/`quit()`) — never `del` | Ledger §7 |
| 4 | DB write discipline: explicit cleanup, never transaction rollback (uncommitted rows invisible to the app under test — breaks hybrid flows) | Ledger §7 |
| 5 | Parametrize tuples are module-level constants (collection); scenario content loads via fixture (runtime) | Ledger §11 |
| 6 | Fixtures call factories (Phase 3.5) — conftest owns scope and wiring, never construction detail | Ledger §7 |
| 7 | Domain markers match domain folder names (`-m autopend` ↔ `tests/autopend/`) | Ledger §10 |

## Contract Compliance

| Contract rule (Conftest Architecture) | Status |
|--------------------------------------------|--------|
| Hierarchy: root → fixture modules → domain conftest | PASS (modules via pytest_plugins replace per-interface directory conftests — composition-safe) |
| Scope discipline | PASS |
| Layer objects only in fixtures | PASS |
| Stack built bottom-up via DI | PASS |
| Cross-cutting hooks in conftest, not layers | PASS (screenshot, HTML metadata, markers) |
| Central logging; layers receive the logger | PASS |
| Credential indirection; no committed secrets | PASS (+ per-user DB/API identity model) |
| Worker-safe session fixtures | PASS (worker-suffixed log/screenshot paths) |

## Dependencies

- `pytest`, `pytest-html`, `python-dotenv`
- Phase 3.1 (environment config schema — consumed here), Phase 3.5 (factories — called here), Phase 3.3 (data strategy + cleanup mechanics), Phase 3.8 (logging strategy — plugs into the logger seam)

## What Does NOT Go Here

- No factory internals (3.5) — conftest calls, never builds drivers/connections inline
- No environment JSON schema design (3.1) — consumed, not defined
- No test data content or cleanup mechanics (3.3)
- No correlation IDs, structured logging, masking (3.8)
- No assertions, no orchestration, no identifiers (Layers 5, 3, 2)
- **Open (ledger):** claim-injection mechanism — likely the 837BT tool, not raw EDI drop; resolve in Phase 1/Phase 4 before `claim_injection` fixtures exist
