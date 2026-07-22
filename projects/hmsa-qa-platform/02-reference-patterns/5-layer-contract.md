# 5-Layer Framework Contract (Unified)

**Status:** Complete
**Version:** 2.3 (2.1 added cross-cutting sections: conftest architecture, environment & config management, test data management; 2.2 merged the four interface addenda into this file; 2.3 narrowed L2 constructor rule 1 for generic shared components — identifier config and composed L2 components may be injected, never constructed internally)
**Supersedes:** `.claude/docs/design/check-5-layer/references/5-layer-contract.md` (v1.0) for the HMSA QA Platform
**Scope:** ONE contract governs all four interfaces — Browser, REST API, SQL Server, SOAP. Per-interface divergence lives in short addenda, not separate contracts.
**Deliverable location:** copied to `framework/docs/5-layer-contract.md` in the built platform at build time.

## Addenda

Per-interface divergences live in the **Per-Interface Addenda** section of this document (Browser, REST API, SQL Server, SOAP) — sections of one file, not separate contracts or separate files.

**Precedence rule:** the core contract governs everything; an addendum section may only *specialize* a contract rule for its interface (narrower, never contradictory). If an addendum appears to conflict with the core contract, the core wins and the addendum is a bug.

---

## What Changed from v1.0 (Resolved Decisions)

| # | v1.0 Rule | v2.0 Rule | Why |
|---|-----------|-----------|-----|
| 1 | Four implicit contract variants (one per platform repo) | ONE contract + per-interface addenda | Divergence was in return types, constant formats, SQL ownership — not structure. One source of truth. |
| 2 | Task constructor takes Interface, creates Components internally | Task constructor takes **Layer 2 objects via DI** | Testability, explicit dependencies, hybrid Tasks compose objects from multiple interfaces |
| 3 | Task methods return `None` — side effects only | Tasks return **typed results** (pydantic model, dict, primitive) when data must flow upstream; `-> None` when the outcome is observable via Layer 2 state-checks | DB/API results have no page to observe — discovery and verification data must flow up |
| 4 | Role constructor creates Task instances internally | Role constructor takes **Tasks via DI** | Same rationale as #2 — conftest wires the stack |
| 5 | `@automation_logger` decorator | `@trace` decorator (`trace.py`) | Same 52-line implementation, renamed to distance from legacy v2 naming |
| 6 | Tests always act through Roles | Tests act through the **highest applicable layer** (see Layer 5 rules) | A Role that wraps a single Task is a pass-through — the existing Role composition rule already forbids it |
| 7 | Conftest, config/env, and test data ungoverned (implicit per-platform practice) | Contract-level rules for **conftest architecture, environment & config management, test data management** | These are cross-cutting — every interface and every test touches them; leaving them implicit reproduced v2 anti-patterns (committed passwords, regex-on-SQL, hardcoded subjects) |

platform-selenium (v1.0 style: Tasks take Interface, return `None`, tests assert via POM state-checks) remains a **valid UI-only simplification** — it is not wrong, it is a special case where every outcome is page-observable. It is NOT the general pattern for this platform. HMSA uses DI and typed returns everywhere.

---

## Global Rules

### Baseline Standards (by reference)

- **PEP 8** — naming, formatting, imports
- **SOLID Principles** — single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion
- **Fluent API** — Layer 2 atomic methods return `self` for method chaining (rationale: readability for non-technical stakeholders)

### Framework-Specific Additions

| # | Rule |
|---|------|
| 1 | Module-level docstring states the file's purpose and layer |
| 2 | Class docstring lists the layer's structural rules as bullet points |
| 3 | Docstring on every method |
| 4 | Inline comments only when explanation is needed |
| 5 | Methods organized by category with section header comments (`# === CATEGORY ===`) |
| 6 | Composition over inheritance — constructor takes dependencies, no subclassing, no mixins, no abstract bases |
| 7 | Imports only from the layer directly below, from `models/`, or from utilities (exception: type annotation imports from any lower layer are permitted) |
| 8 | Logging on every operation |
| 9 | Constants as class-level attributes, config-driven defaults via constructor |
| 10 | Type hints on all parameters and return types |
| 11 | Pydantic v2 models for typed data crossing layer boundaries — defined in `models/` subfolders at Layer 2, imported (never defined) by Layers 3+ |

### Dependency Injection & Construction

Who constructs what. This is the core v2.0 change — construction happens in conftest fixtures, not inside layer classes.

| Layer | Receives via constructor | Constructs internally |
|-------|-------------------------|----------------------|
| Interface | SDK instance + config + logger | Nothing above SDK session objects |
| Component (L2) | Interface instance(s) | Nothing |
| Task (L3) | Layer 2 object instances (+ other Tasks for composition) | Nothing — never instantiates Layer 2 objects or other Tasks |
| Role (L4) | Task instances + workflow config (credentials, URLs, settings) | Nothing — never instantiates Tasks |
| Test (L5) | Fixtures (pytest) | Nothing — conftest wires the whole stack |

**Fixture wiring pattern** (conftest builds the stack bottom-up):

```python
# Layer 1
@pytest.fixture(scope="session")
def db(db_connection, config, logger):
    return SqlServerInterface(db_connection, config, logger)

# Layer 2
@pytest.fixture
def orders_data(db):
    return OrdersDataObject(db)

# Layer 3
@pytest.fixture
def discovery(orders_data):
    return DiscoveryTasks(orders_data)

# Layer 4
@pytest.fixture
def system_validator(discovery, verification):
    return SystemValidator(discovery, verification)
```

**Task composition rule:** a Task may receive another Task via constructor (injected). Chain depth max 2 (Task → Task → Layer 2). Deeper = refactor.

### Conftest Architecture

Conftest is where the object graph lives — the only place layer objects are constructed. Detailed design: Phase 3.2 (conftest-hierarchy.md) and 2.5.2 (fixture-wiring.md).

| # | Rule |
|---|------|
| 1 | Hierarchy: root conftest (CLI options, config, credentials, logging setup) → per-interface conftest (browser/api/db/soap fixtures) → hybrid conftest (multi-interface composition) → nested conftest per test domain (domain constants, parametrize tuples) |
| 2 | Fixture scope discipline: `session` for expensive read-only resources (connections, drivers, config); `function` for anything a test can mutate — test isolation wins over speed |
| 3 | Layer objects are constructed ONLY in fixtures — never inline in tests, Tasks, or Roles |
| 4 | Fixtures build the stack bottom-up: Interface → Component → Task → Role (see DI table above) |
| 5 | Cross-cutting hooks live in conftest, never in layers: screenshot-on-failure (`pytest_runtest_makereport`), HTML report wiring, dynamic marker registration |
| 6 | Centralized logging setup in root conftest (file + console handlers, formatters) — layers receive the logger, never configure it |
| 7 | Worker safety: no shared mutable state across pytest-xdist workers — session-scoped fixtures must be read-only or per-worker |

### Environment & Config Management

Config flows down through fixtures; secrets never touch the repo. Detailed design: Phase 3.1 (config-environment.md).

| # | Rule |
|---|------|
| 1 | Environment definitions in committed JSON (URLs, environment IDs, feature flags) — one structure, keyed per environment, selected via CLI option/env var |
| 2 | Secrets in `.env` (gitignored); `.env.example` committed as the template. NO passwords, tokens, or connection strings in committed files — ever (v2 anti-pattern: passwords in environment_config.json) |
| 3 | Credential resolution by indirection: config stores the env-var NAME (`"password_env": "HMSA_ADMIN_PW"`), the fixture resolves the value at runtime |
| 4 | Config enters the stack once — root conftest loads it, fixtures pass it down; layers never read config files or env vars directly |
| 5 | Interface defaults (timeouts, directories, flags) are config-driven via constructor — no hardcoded environment values in any layer |
| 6 | One config structure for all environments — never separate per-env files (v2 anti-pattern: elevated_user_config_*.json per environment) |
| 7 | Connection/driver/client construction belongs to factories (Phase 3.5) wired through conftest — never mid-test, never in layers |

### Test Data Management

Data is discovered or declared — never hardcoded in test bodies. Detailed design: Phase 3.3 (data-driven-strategy.md).

| # | Rule |
|---|------|
| 1 | Scenario data in role-keyed JSON files (keys are `role.method_name`, values are parameters) — the data file mirrors the workflow it drives |
| 2 | Tabular variations via `@pytest.mark.parametrize`; per-scenario `data/` directories for composite inputs (input JSON + SQL templates + document uploads) |
| 3 | Dynamic test subjects discovered via DB queries (Discovery Tasks) — never hardcoded IDs (subjects age out; discovery doesn't) |
| 4 | Parameterized SQL only (`?` placeholders) — never regex-on-file, never f-string interpolation (v2 anti-pattern) |
| 5 | Factory fixtures for dynamic data creation; pydantic models validate test data on creation (`Model(**factory_data)`) |
| 6 | Replayability: scenario data carries a replay flag/cleanup contract so a test can run twice without manual resets |
| 7 | Test data loading is plain `json.load` + fixtures — no auto-parsing frameworks (v2 `TestData` class anti-pattern) |
| 8 | Data files live with the tests that use them (per-domain `data/` dirs), not in a global pool |

### Error Handling

| # | Rule |
|---|------|
| 1 | Interface catches SDK exceptions, logs them, then re-raises — never swallows |
| 2 | Layers above Interface do not catch exceptions — let them propagate up to the test runner |
| 3 | Exception to rule 2: Layer 3 retry logic may catch *transient* exceptions (timeouts, connection blips) via the shared retry utility — it retries or re-raises, never swallows |
| 4 | Domain exceptions (e.g., `NoEligibleSubjectError`) are defined at Layer 3 and raised when a domain operation cannot proceed |

### Business Logic Boundaries

| Layer | Owns | Changes When |
|-------|------|-------------|
| Interface | No business logic — pure SDK wrapper | SDK API changes |
| Component | No business logic — mechanics only (one operation per method, state reads) | Identifiers or domain entity definitions change |
| Task | Operational logic — steps, decisions, filtering, selection, retry within one domain operation | The operation's steps change (e.g., new form field, new eligibility rule) |
| Role | Workflow logic — which operations to run, in what order, as which persona | The business workflow changes (e.g., new approval step) |
| Test | No business logic — Arrange, Act, Assert only | Requirements change |

**Decision matrix (Layer 2 vs Layer 3):**

| Responsibility | Layer 2 (Object) | Layer 3 (Task) |
|---------------|------------------|----------------|
| Execute one query/action/call | YES | NO |
| Filter results in Python | NO | YES |
| Pick a subject (random, first-match) | NO | YES |
| Retry with a different subject | NO | YES |
| Sequence multiple operations | NO | YES |
| Compose across interfaces | NO | YES |
| Return typed domain results | NO (raw parse only, e.g. `get_results_as`) | YES |

### Data Flow

```
Layer 5 (Test)      → passes params DOWN            → asserts on results/state-checks
Layer 4 (Role)      → orchestrates Tasks            → returns typed results UP (or None)
Layer 3 (Task)      → orchestrates L2, decides      → returns typed results UP (or None)
Layer 2 (Component) → executes one operation        → returns self; state-checks return primitives
Layer 1 (Interface) → executes one SDK call         → returns SDK primitive
```

- **Down:** configuration, parameters, criteria
- **Up:** typed results, verification outcomes, primitives
- **Decisions (filtering, retry, selection):** Layer 3 only
- **Assertions:** Layer 5 only

---

## Per-Layer Rules

### Layer 1: Interface

**Return value conventions:** SDK primitives only (`WebElement`, `bool`, `str`, `dict`, rows, response objects). Never domain objects.

| # | Rule |
|---|------|
| 1 | Wraps the SDK/driver — no business logic, no domain vocabulary |
| 2 | Constructor takes SDK instance + config + logger |
| 3 | Config-driven defaults (timeouts, directories, flags) |
| 4 | Return types are SDK primitives — never domain objects |
| 5 | One SDK primitive per method — never composes multiple SDK calls |
| 6 | No locators, no endpoints, no table names, no operation names — identifiers live at Layer 2 |
| 7 | No knowledge of layers above |
| 8 | Layer 1 is **closed** — clients extend at Layer 2+, never by modifying the Interface |

### Layer 2: Component (Page / API / Data / SOAP Object)

**Return value conventions:**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Atomic methods return `self` for chaining | Fluent API — the method chain reads as a sentence |
| 2 | State-check methods return `bool` or primitive (`str`, `float`, `int`, `dict`) | State-checks are assertion targets |
| 3 | Typed-parse helpers (`get_results_as(Model)`, `get_last_body_as(Model)`) return pydantic instances | Mechanical parse, not a decision — stays at Layer 2 |

| # | Rule |
|---|------|
| 1 | Constructor takes Interface instance(s) — plus injected identifier config or composed L2 components where the component is generic (shared components) — all injected, never constructed internally; composition, no inheritance |
| 2 | NO decorators on any methods |
| 3 | Identifiers as class-level constants (locators, endpoint paths, SQL, operation names). Complex identifiers may be externalized (`.sql` files, JSON fixtures) and loaded in the constructor or lazily — storage format, not a different pattern. See addenda for per-interface formats. |
| 4 | One atomic operation or state-check per method. Atomicity = one business question / one action, regardless of internal complexity |
| 5 | Method names use domain vocabulary, not generic SDK terms |
| 6 | Only imports from Interface layer, own `models/`, or utilities |
| 7 | No filtering, no retry, no subject selection, no multi-step orchestration |
| 8 | No knowledge of Tasks, Roles, or Tests |

**Layer 2 uniform pattern across interfaces:**

| Layer 2 Type | Constants | Atomic Methods | State-Check Methods |
|-------------|-----------|----------------|---------------------|
| Page Object | Locators `(By, selector)` | UI action → `self` | `is_*()`, `has_*()` → bool |
| API Object | Endpoint paths | HTTP call → `self` | `get_last_status()`, `get_last_body_as()` |
| Data Object | SQL (constants + files) | Query/write → `self` | `get_count()`, `get_results_as()`, `has_results()` |
| SOAP Object | Operation names | `call_operation` → `self` | `get_last_body_as()`, `is_last_status_ok()` |

### Layer 3: Task

**Return value conventions:**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Return a **typed result** (pydantic model, dict, named tuple, primitive) when data must flow upstream — discovery subjects, verification outcomes, computed values | DB/API outcomes have no page to observe; Tests and Roles need the data |
| 2 | Return `None` when the outcome is fully observable via Layer 2 state-checks (typical for UI-only Tasks) | Command pattern still applies where observation is possible |
| 3 | Never return SDK objects or Layer 2 instances | Layer boundary — upstream consumers see domain data only |

| # | Rule |
|---|------|
| 1 | Constructor takes **Layer 2 object instances via DI** (and optionally other Tasks) — never an Interface, never constructs Layer 2 objects internally |
| 2 | `@trace("Task")` on all public methods, NOT on constructor |
| 3 | One domain operation per method |
| 4 | Makes the decisions: filtering, selection, retry, sequencing |
| 5 | Uses fluent Layer 2 chaining inside methods (the Task method is the chain boundary) |
| 6 | Method parameters are domain values (`name`, `order_id`), not UI elements or SDK objects |
| 7 | Hybrid Tasks (composing Layer 2 objects from multiple interfaces) follow the identical pattern — the constructor just receives more objects |
| 8 | Only imports from Layer 2 and `models/` (type annotations from lower layers permitted) |
| 9 | No knowledge of Roles or Tests |
| 10 | No identifiers (locators, SQL, endpoints) — delegates to Layer 2 |

### Layer 4: Role

**Return value conventions:**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Workflow methods return typed results when verification data flows up to the Test; `None` when outcomes are observable via Layer 2 state-checks | Mirrors Layer 3 — Roles pass Task results through, they don't bury them |

| # | Rule |
|---|------|
| 1 | Constructor takes **Task instances via DI** + workflow config (credentials, URLs, settings) — never constructs Tasks, never receives an Interface |
| 2 | Represents a persona — a user or system actor performing a workflow |
| 3 | Workflow methods call MULTIPLE Tasks — orchestrates across Task modules |
| 4 | Stores workflow config on `self` |
| 5 | `@trace("Role")` on workflow methods, `@trace("Role Constructor")` on `__init__` |
| 6 | Only imports from Task layer and `models/` (type annotations from lower layers permitted) |
| 7 | No knowledge of Tests |

**Role composition rule:** Roles exist to orchestrate ACROSS Task modules. If a Role method would wrap a single Task call, the Role adds nothing — the Test consumes the Task directly (see Layer 5 rule 9).

### Layer 5: Test

**Return value conventions:** None — pytest collects by naming convention; test methods implicitly return `None`.

| # | Rule |
|---|------|
| 1 | `@pytest.fixture(autouse=True) def setup` or explicit fixture parameters wire dependencies |
| 2 | Conftest fixtures build the full layer stack (see DI section) — tests never construct layer objects inline |
| 3 | `@trace("Test")` on test methods |
| 4 | `@pytest.mark` tags for categorization |
| 5 | One AAA block per test method (one scenario) |
| 6 | Asserts via Layer 2 state-check methods AND/OR typed results returned by Tasks/Roles |
| 7 | Every assert carries a failure message |
| 8 | No business logic — filtering, selection, and retry live at Layer 3 |
| 9 | Acts through the **highest applicable layer**: through a Role when the scenario has persona/workflow semantics (multi-Task orchestration, multi-user flows); directly through a Task when a Role would be a single-call pass-through. Never calls Layer 2 action methods or Interface methods to *act* (Layer 2 state-checks for *asserting* are correct). |

---

## Decorator Usage

**Shared utility:** `framework/resources/utilities/trace.py` — must exist in every platform with the same implementation (52 lines, pure Python: `logging`, `functools`, `datetime`). Renamed from legacy `autologger.py`; same behavior.

| Layer | Decorator | Rationale |
|-------|-----------|-----------|
| Interface | None | Already logs internally via `self.logger` — decorator would double-log |
| Component | None | Atomic one-liners that chain — decorating each floods the CLI. The Task decorator wraps the chain at the right granularity. |
| Task | `@trace("Task")` on public methods, NOT constructor | Traces each domain operation start/end |
| Role | `@trace("Role")` on workflow methods, `@trace("Role Constructor")` on `__init__` | Traces workflow orchestration hierarchy |
| Test | `@trace("Test")` on test methods | Traces which test runs and its duration |

**Runtime output (example):**
```
[Role Constructor] SystemValidator.__init__ - START
[Role] validate_sp_execution - START
[Task] find_test_subject - START
[Task] find_test_subject - END (1.2s)
[Task] verify_outcome - START
[Task] verify_outcome - END (0.8s)
[Role] validate_sp_execution - END (2.0s)
[Test] test_eligible_order_gets_processed - END (2.3s)
```

---

## Method Scope

| Layer | Scope | Rule |
|-------|-------|------|
| Interface | One SDK primitive per method | `click()` clicks, `execute_query()` executes — never combines SDK calls |
| Component | One atomic operation or state-check per method | One business question = one method; internal complexity (50-line SQL, 6 joins) is irrelevant to atomicity |
| Task | One domain operation per method | Navigate = one operation, submit = another. A Task method can span multiple Components (and multiple interfaces) but stays within one action concept |
| Role | One complete workflow per method | Discover → configure → execute → verify = one workflow |
| Test | One scenario per method | One AAA block |

**Operation boundary rule (from v2 production code):** navigation and form submission are SEPARATE Task methods even within the same flow. Split by domain action concept, not by page or screen.

---

## Utilities

| Utility | Location | Used By | Rule |
|---------|----------|---------|------|
| `trace.py` | `framework/resources/utilities/` | L3, L4, L5 | Identical implementation in every platform |
| `retry.py` | `framework/resources/utilities/` | L3 only | Transient-failure retry with backoff; catches only declared exception types, re-raises after max attempts |
| Pydantic models | `models/` subfolder per Layer 2 package | Defined at L2; imported by L2/L3/L4/L5 | Layers 3+ import, never define |

---

## Per-Interface Addenda

### Addendum: Browser

**Interface:** `BrowserInterface` (Selenium WebDriver) · **Layer 2 type:** Page Object (+ Shared Components — grid, modal, navbar, wizard, file upload)

**Identifier format (Layer 2):**
- Locators as class-level constants: `EMAIL_INPUT = (By.CSS_SELECTOR, "[data-testid='input-email']")`
- Section header order: `# === LOCATORS ===`, `NAVIGATION`, `ATOMIC METHODS`, `STATE-CHECK METHODS`
- **Dynamic locators:** when a locator depends on runtime data, build it in the method body (e.g., `is_employee_displayed_in_list(name)` constructs XPath with the name) — never a class constant with placeholders

**Return-type divergence (Layer 3):** Browser Tasks typically return `-> None` — the UI outcome is observable on the page, so Tests assert via Page Object state-checks. This is contract rule L3-2, and it is the norm here rather than the exception. Return a typed result only when a Browser Task *produces data* a downstream step needs (e.g., an ID scraped from a confirmation page feeding a DB verification).

| # | Browser-specific rule |
|---|------|
| 1 | One UI action per method — `click_log_in()` clicks ONE element, never click-then-wait combined |
| 2 | Waits are separate methods (`wait_for_email_visible()`), not baked into actions |
| 3 | No pydantic models — Page Objects deal in primitives and page state, not payloads |
| 4 | Shared UI patterns (grids, modals, navbars, wizards, uploads) live in `_reference/components/` — Layer 2, reusable across apps, same rules as Page Objects |
| 5 | Screenshot-on-failure is conftest's job (`pytest_runtest_makereport` hook), never a layer concern |

**Lineage note:** platform-selenium's `_reference/` is the source pattern and remains a valid **UI-only simplification** (Tasks take Interface, return `None`). In this platform, Browser Tasks still follow the general DI rule — constructor takes Page Objects/Components, wired by conftest.

### Addendum: REST API

**Interface:** `ApiInterface` (wraps `requests.Session`, synchronous) · **Layer 2 type:** API Object

**Identifier format (Layer 2):**
- Endpoint paths as class constants: `BASE_PATH = "/api/users"`
- Parameterized paths as `@staticmethod` builders: `single_path(user_id) -> f"/api/users/{user_id}"` — a path builder is identifier construction, not an operation
- Section header order: `# === ENDPOINT CONFIG ===`, `CRUD METHODS`, `STATE-CHECK METHODS`

**Response state convention (Layer 2):** every atomic call stores its result on `self.last_response: ApiResponse | None` and returns `self`. State-checks read from `last_response`:

| State-check | Returns |
|-------------|---------|
| `get_last_status()` | `int` HTTP status |
| `get_last_body()` | raw `dict` |
| `get_last_body_as(Model)` | validated pydantic instance (raises `ValidationError` on contract break) |
| `get_last_response_time()` | `float` seconds |
| `is_last_status_ok()` | `bool` (2xx) |

**Pydantic models:** request AND response models, in `models/` subfolder per API Object package. Requests serialize via `data.model_dump()` (`exclude_unset=True` for PATCH/PUT partials). Layers 3+ import models for typing; never define them.

**Return-type divergence (Layer 3):** REST Tasks return **typed results** — there is no page to observe; discovery, creation, and verification outcomes flow up (contract rule L3-1 is the norm here).

| # | REST-specific rule |
|---|------|
| 1 | Synchronous only — matches `requests`; no async/await |
| 2 | Auth token management is Interface or conftest concern, never API Object |
| 3 | Pagination orchestration (looping pages) is Layer 3 or a dedicated component — one call per atomic method |
| 4 | Retry on transient HTTP failures via the shared `retry.py` at Layer 3 only |

### Addendum: SQL Server

**Interface:** `SqlServerInterface` (wraps `mssql_python.Connection`) · **Layer 2 type:** Data Object

**SQL ownership (Layer 2):** the Data Object **owns** its queries. Storage by complexity: 1–5 lines → class constant; 6+ lines → `.sql` file in co-located `sql/` folder, loaded via `@cached_property`. **Parameterized queries only** — `?` placeholders. Never f-strings, never regex replacement on SQL files (v2/hmsa-healthcare-qa anti-patterns). Section header order: `# === TABLE CONFIG ===`, `SQL`, `DISCOVERY METHODS`, `VALIDATION METHODS`, `SETUP METHODS`, `VERIFICATION METHODS`, `STATE-CHECK METHODS`.

**Result state convention (Layer 2):**

| Interface method | Use for | Stores to |
|-----------------|---------|-----------|
| `execute_query` | Result sets | `self.last_results: list` |
| `execute_query_one` | Single row | `self.last_results` |
| `execute_scalar` | Counts, sums | `self.last_count: int` |
| `execute_non_query` | INSERT/UPDATE/DELETE | `self.last_count` (rows affected) |
| `execute_many` | Batch writes | `self.last_count` |
| `execute_sproc` | Stored procedures | per result shape above |

State-checks: `get_count()`, `has_results()`, `result_count()`, `get_results_as(Model)`, `get_first_as(Model)` — the `*_as` helpers map positional rows to pydantic row models (columns default to model field order).

**Atomicity divergence (Layer 2):** one business question = one method. SQL complexity is irrelevant — a 50-line query with 6 joins is atomic if it answers one question. NOT atomic: query-then-insert, validate-then-archive, run-SP-then-verify in one method.

**Return-type divergence (Layer 3):** DB Tasks return **typed results** — discovery subjects, verification outcomes, counts. Nothing is page-observable; everything flows up.

| # | SQL-specific rule |
|---|------|
| 1 | Pydantic row models in `models/` per Data Object package — one model per distinct result shape |
| 2 | Data Object never filters results in Python — broad query at L2, narrowing at L3 |
| 3 | Connection management belongs to the factory/conftest (session-scoped fixture) — never created mid-test |
| 4 | Dynamic test-subject discovery via queries, never hardcoded subjects |

### Addendum: SOAP

**Interface:** `SoapInterface` (wraps `zeep.Client`) · **Layer 2 type:** SOAP Object

**Identifier format (Layer 2):**
- Operation names as class constants: `GET_MEMBER_OP = "GetMemberInfo"`
- WSDL URL and service/port binding are Interface config (constructor + environment config), never Layer 2 constants
- Section header order: `# === OPERATION CONFIG ===`, `OPERATION METHODS`, `STATE-CHECK METHODS`

**Response state convention (Layer 2):** same shape as REST — every operation call stores to `self.last_response` and returns `self`. zeep deserializes XML → dict, so pydantic validates SOAP responses exactly like REST bodies (`get_last_body_as(Model)` → `model.model_validate(self.last_response)`).

**Return-type divergence (Layer 3):** SOAP Tasks return **typed results** — same as REST and DB. Nothing is page-observable.

| # | SOAP-specific rule |
|---|------|
| 1 | Complex request payloads built via `soap.create_object(type_name, **fields)` (zeep factory) — the SOAP Object composes the payload, the Interface exposes the factory primitive |
| 2 | SOAP faults are SDK exceptions — Interface catches, logs, re-raises (contract error rule 1); Layer 2 never interprets fault XML |
| 3 | Pydantic models in `models/` per SOAP Object package — validate zeep dicts, one model per response shape |
| 4 | No raw XML handling above the Interface — if a payload can't be built via `create_object`, extend the Interface's primitive surface, not Layer 2 |

---

## Layer Mapping (Generic Vocabulary)

| Layer | Generic Term | What It Is |
|-------|-------------|-----------|
| 1 | Interface | Wraps the SDK — the only layer that touches external systems |
| 2 | Component | Atomic operations + state-checks on one domain entity (no business logic) |
| 3 | Task | One domain operation composed from Components — decisions live here |
| 4 | Role | One complete workflow composed from Tasks — persona lives here |
| 5 | Test | One scenario — Arrange, Act, Assert |

### This Platform's Four Interfaces

| Interface | Wraps | Layer 2 Type | Identifiers | Atomic Operations | State-Checks |
|-----------|-------|-------------|-------------|-------------------|--------------|
| BrowserInterface | Selenium WebDriver | Page Object | `(By, selector)` tuples | `click`, `send_keys`, `wait_for_*` | `is_element_displayed()` |
| ApiInterface | `requests.Session` | API Object | Endpoint paths | `get`, `post`, `put`, `patch`, `delete` | `get_last_status()`, `is_last_status_ok()` |
| SqlServerInterface | `mssql_python.Connection` | Data Object | SQL constants + `.sql` files | `execute_query`, `execute_scalar`, `execute_non_query`, `execute_sproc` | `has_results()`, `get_count()` |
| SoapInterface | `zeep.Client` | SOAP Object | Operation names, WSDL config | `call_operation`, `create_object` | `is_last_status_ok()`, `get_last_body_as()` |

**Resolution rule:** vocabulary resolves by reading the target platform's Interface layer — the SDK wrapped determines what Layer 2 identifiers and operations look like. Layers 3–5 are universal: same vocabulary regardless of interface.

---

## Pattern Lineage

The 5-layer architecture is a **Screenplay pattern derivative** with codified contracts (see v1.0 baseline for the full industry analysis).

| 5-Layer | Screenplay | Relationship |
|---------|-----------|-------------|
| Interface | Ability | Direct — wraps SDK/driver |
| Component | Interaction + Question | Combined — atomic actions + state-checks |
| Task | Task | Exact — sequences of domain operations |
| Role | Actor | Evolved — domain-specific Actor with workflow orchestration |
| Test | Scenario | Direct — AAA maps to Given/When/Then |

What v2.0 adds beyond v1.0: explicit DI/construction rules (conftest owns the object graph), typed-result contracts per layer, and a single-contract-plus-addenda governance model for multi-interface platforms.

---

## Contract Status

- [x] Per-interface addenda (Browser, REST API, SQL Server, SOAP) merged in-file + precedence rule
- [x] v1.0 → v2.0 divergence record (7 resolved decisions)
- [x] Global rules (standards, DI/construction, error handling, boundaries, data flow)
- [x] Conftest architecture (hierarchy, scope discipline, construction-only-in-fixtures)
- [x] Environment & config management (env JSON, .env secrets, credential indirection)
- [x] Test data management (role-keyed scenarios, discovery, parameterized SQL, factories)
- [x] Per-layer rules (all 5 layers — return conventions + structural rules)
- [x] Decorator usage (`@trace`)
- [x] Method scope
- [x] Utilities (trace, retry, models)
- [x] Layer mapping (four interfaces + resolution rule)
- [x] Pattern lineage
