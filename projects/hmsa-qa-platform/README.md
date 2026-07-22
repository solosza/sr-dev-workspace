# HMSA QA Platform — Project Plan

## Purpose

Multi-interface QA test platform for enterprise healthcare testing. Flagship case study for the Isagawa Platform. Generic demo app proves architecture; POC phase adapts to client domain.

## Target Repo

`D:\my_ai_projects\project_test_repos\hmsa-qa-platform`

## Source Material

| Source | What We Take | Status |
|--------|-------------|--------|
| platform-selenium | BrowserInterface, `_reference/` patterns, autologger, conftest | Copy (clean — no IP overlap) |
| platform-playwright | ApiClient pattern (TypeScript) | Translate to Python |
| hmsa-healthcare-qa | SqlServerInterface concept | Rewrite from scratch (IP overlap with Oracle version) |
| v2 legacy framework | Multi-role workflow patterns | Architecture reference only |

## Governing Contract

All interfaces and layers follow the existing 5-layer contract:
`.claude/docs/design/check-5-layer/references/5-layer-contract.md`

This contract gets copied into the target repo at build time — it's a deliverable, not just a reference. Lives at `framework/docs/5-layer-contract.md` in the built platform. Every interface, component, task, role, and test is validated against it.

Design docs are lean decision records — what SDK, what's different from BrowserInterface, any non-obvious choices. The contract covers everything else. Enterprise documentation (developer guide, API reference, architecture docs) gets written after the code exists, documenting reality.

## Process

1. **Design** — short decision record per component (what to build, key choices)
2. **Backlog** — convert each design doc to a backlog item
3. **Build** — execute-pipeline per backlog (outputs to target repo)
4. **Validate** — check output against 5-layer contract
5. **Document** — write enterprise docs referencing the built code
6. **Track** — update status below

Future: steps 2-4 are mechanical and repeatable. Candidate for a `/kernel/project-run` outer loop that reads this manifest, iterates DESIGNED items in dependency order, and calls existing commands (backlog → execute-pipeline → validate → update status). All inner pieces exist — only the thin orchestrator is missing. Don't backlog yet — let the pattern evolve through this project first.

---

## Phase 1: Interfaces

Build the framework foundation — one interface per SDK.

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 1.1 | BrowserInterface | [browser-interface.md](01-interface-design/browser-interface.md) | 203 | DESIGNED |
| 1.2 | ApiInterface (REST) | [api-interface.md](01-interface-design/api-interface.md) | 210 | DESIGNED |
| 1.3 | SqlServerInterface | [sql-server-interface.md](01-interface-design/sql-server-interface.md) | 215 | DESIGNED |
| 1.4 | SoapInterface | [soap-interface.md](01-interface-design/soap-interface.md) | 221 | DESIGNED |

**References:**
- 1.1: `platform-selenium/framework/interfaces/browser_interface.py` (674 lines, clean — copy and adapt)
- 1.2: `platform-playwright/framework/interfaces/api-client.ts` (TypeScript — translate to Python)
- 1.3: `hmsa-healthcare-qa/framework/interfaces/sql_server_interface.py` (concept only — rewrite from scratch, IP overlap with v2 OracleInterface)
- 1.3 anti-pattern: `v2/framework/interfaces/oracle_interface.py` (what NOT to copy — 80% code similarity)
- 1.3 SDK: `mssql-python` (Microsoft official, GA Nov 2025 — replaces pyodbc, no ODBC driver dependency, 2-8x faster)
- 1.4: No existing reference — design from scratch using `zeep` SDK
- All: `v2/framework/interfaces/web_interface.py` (430-line monolith anti-pattern — what to avoid)

## Phase 2: Reference Patterns

Canonical `_reference/` examples — one per layer per interface. The 5-layer contract governs all; per-interface addenda document where behavior diverges.

### 2.0 — Unified Contract + Interface Addenda

ONE contract governs all interfaces. Short addenda per interface where behavior diverges (return types, constant formats, SQL ownership) live as sections INSIDE the contract file — one md, one backlog, one pipeline deliverable. This replaces 4 separate contracts.

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 2.0.1 | 5-Layer Contract (unified, incl. per-interface addenda) | [5-layer-contract.md](02-reference-patterns/5-layer-contract.md) | 201 | DESIGNED |

**Key contract decisions (resolved):**
- Tasks receive Layer 2 objects via DI (not Interface directly)
- Tasks return typed results when data must flow upstream; `-> None` when UI state is observable on the page
- Roles receive Tasks via DI (not Interface)
- platform-selenium is a valid UI-only simplification, not the general pattern

### 2.1 — Layer 2 Components (per interface)

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 2.1.1 | Page Objects (Browser) | [page-objects.md](02-reference-patterns/page-objects.md) | 204 | DESIGNED |
| 2.1.2 | API Objects (REST) | [api-objects.md](02-reference-patterns/api-objects.md) | 211 | DESIGNED |
| 2.1.3 | Data Objects (SQL Server) | [data-objects.md](02-reference-patterns/data-objects.md) | 216 | DESIGNED |
| 2.1.4 | SOAP Objects (SOAP) | in [api-objects.md](02-reference-patterns/api-objects.md) | 211 | DESIGNED |
| 2.1.5 | Shared Components (Browser) | [shared-components.md](02-reference-patterns/shared-components.md) | 205 | DESIGNED (set deferred — trigger: Phase 4 or first client) |

### 2.2 — Layer 3 Tasks (per interface + hybrid)

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 2.2.1 | Browser Tasks (`-> None`) | [tasks-browser.md](02-reference-patterns/tasks-browser.md) | 206 | DESIGNED |
| 2.2.2 | REST API Tasks (`-> model`) | [tasks-rest-api.md](02-reference-patterns/tasks-rest-api.md) | 212 | DESIGNED |
| 2.2.3 | DB Tasks (`-> model`) | [tasks-db.md](02-reference-patterns/tasks-db.md) | 217 | DESIGNED |
| 2.2.4 | SOAP Tasks (`-> model`) | [tasks-soap.md](02-reference-patterns/tasks-soap.md) | 222 | DESIGNED |
| 2.2.5 | Hybrid Tasks (multi-interface) | [hybrid-tasks.md](02-reference-patterns/hybrid-tasks.md) | 225 | DESIGNED |

### 2.3 — Layer 4 Roles (per composition type)

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 2.3.1 | UI Role (composes Browser Tasks) | [roles-ui.md](02-reference-patterns/roles-ui.md) | 207 | DESIGNED |
| 2.3.2 | System Role (composes DB/API Tasks) | [roles-system.md](02-reference-patterns/roles-system.md) | 218 | DESIGNED |
| 2.3.3 | Hybrid Role (composes mixed Tasks) | [roles-hybrid.md](02-reference-patterns/roles-hybrid.md) | 226 | DESIGNED |

### 2.4 — Layer 5 Tests (per interface + hybrid)

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 2.4.1 | UI Test (asserts page state) | [tests-ui.md](02-reference-patterns/tests-ui.md) | 208 | DESIGNED |
| 2.4.2 | API Test (asserts response) | [tests-api.md](02-reference-patterns/tests-api.md) | 213 | DESIGNED |
| 2.4.3 | DB Test (asserts query result) | [tests-db.md](02-reference-patterns/tests-db.md) | 219 | DESIGNED |
| 2.4.4 | SOAP Test (asserts response) | [tests-soap.md](02-reference-patterns/tests-soap.md) | 223 | DESIGNED |
| 2.4.5 | Hybrid Test (multi-interface) | [tests-hybrid.md](02-reference-patterns/tests-hybrid.md) | 227 | DESIGNED |

### 2.5 — Cross-Cutting

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 2.5.1 | Cross-Layer Notes | [cross-layer-notes.md](02-reference-patterns/cross-layer-notes.md) | 228 | DESIGNED |
| 2.5.2 | Fixture Wiring (Conftest) | [fixture-wiring.md](02-reference-patterns/fixture-wiring.md) | 229 | DESIGNED |
| 2.5.3 | Retry Utility | [retry-utility.md](02-reference-patterns/retry-utility.md) | 200 | DESIGNED |

**References:**
- 2.0: `.claude/docs/design/check-5-layer/references/5-layer-contract.md` (existing contract — baseline to reconcile against)
- 2.1.1: `platform-selenium/framework/_reference/pages/` (login_page.py, employees_page.py, tasks_page.py)
- 2.1.2: `platform-playwright/framework/_reference/api-objects/` (TypeScript — translate pattern to Python)
- 2.1.3: `hmsa-healthcare-qa/framework/_reference/data_objects/` (concept — rewrite from scratch)
- 2.1.5: `v2/framework/pages/components/` (GridComponent, NavbarComponent, DashboardComponent, ActivityGuideComponent — architecture reference only)
- 2.2.1: `platform-selenium/framework/_reference/tasks/` (employee_management_tasks.py — UI-only, `-> None` pattern)
- 2.2.5: `v2/tests/assignment_based_pays/tests/test_command_pay.py` (DB→UI→SOAP→UI→DB hybrid flow — architecture reference)
- 2.3: `platform-selenium/framework/_reference/roles/` (employee_manager.py, task_manager.py — UI-only Role pattern)
- 2.4: `platform-selenium/framework/_reference/tests/` (test_e2e_create_employee_and_assign_task.py — AAA pattern)
- 2.4: `v2/tests/assignment_based_pays/tests/test_assignment_incentive_pay.py` (DB discovery → multi-role UI → DB verify)

## Phase 3: Architecture

Config, fixtures, data-driven patterns, and shared infrastructure. These are cross-cutting — they affect every interface and every test. Must be our own implementation — no code carried from legacy v2.

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 3.1 | Config & Environment | [config-environment.md](03-architecture/config-environment.md) | — | NOT STARTED |
| 3.2 | Conftest Hierarchy | [conftest-hierarchy.md](03-architecture/conftest-hierarchy.md) | — | NOT STARTED |
| 3.3 | Data-Driven Strategy | [data-driven-strategy.md](03-architecture/data-driven-strategy.md) | — | NOT STARTED |
| 3.4 | Project Scaffold | [project-scaffold.md](03-architecture/project-scaffold.md) | — | NOT STARTED |
| 3.5 | Driver & Client Factory | [driver-client-factory.md](03-architecture/driver-client-factory.md) | — | NOT STARTED |
| 3.6 | Retry & Parallel Strategy | [retry-parallel-strategy.md](03-architecture/retry-parallel-strategy.md) | — | NOT STARTED |
| 3.7 | CI/CD Pipeline | [cicd-pipeline.md](03-architecture/cicd-pipeline.md) | — | NOT STARTED |
| 3.8 | Logging Strategy | [logging-strategy.md](03-architecture/logging-strategy.md) | — | NOT STARTED |

**Component scope:**

- **3.1 Config & Environment** — environment JSON structure (URLs, env IDs, feature flags), `.env` for secrets (gitignored), `.env.example` committed as template, `pyproject.toml` for pytest settings, credential resolution pattern (`password_env` references env var name, fixture resolves at runtime). No passwords in committed files.
- **3.2 Conftest Hierarchy** — root conftest (shared CLI options, config, credentials), per-interface conftest (browser/api/db fixtures with correct scoping), hybrid conftest (multi-interface composition), nested conftest per test domain. Fixture scope discipline: session for expensive read-only, function for test isolation. Screenshot-on-failure via `pytest_runtest_makereport` hook. Centralized logging setup (file + console handlers, formatters).
- **3.3 Data-Driven Strategy** — role-keyed JSON scenario files, `@pytest.mark.parametrize` for tabular data, per-scenario `data/` directories (input JSON + SQL templates + document uploads), parameterized SQL (no regex-on-file), dynamic test subject discovery via DB queries, replayability flag. Factory fixtures for dynamic data creation.
- **3.4 Project Scaffold** — directory layout, `__init__.py` placement, `sys.path` strategy, marker registration, reporting (pytest-html + Allure optional), `trace.py` / `@trace("Task")` decorator (renamed from autologger — same 52-line implementation, new name), `pyproject.toml` full config, `requirements.txt` with pinned versions (dev/test dependency groups).
- **3.5 Driver & Client Factory** — browser driver factory (Chrome, Brave, Firefox, Edge, headless toggle), API client factory (requests/httpx session with base URL + auth), DB connection factory (pyodbc connection string builder). All configurable per environment via 3.1.
- **3.6 Retry & Parallel Strategy** — `pytest-rerunfailures` for infrastructure flakiness, `@pytest.mark.flaky` quarantine, `pytest-xdist` parallel config, worker-safe fixture discipline (no shared mutable state across workers). Skip if not needed for initial delivery.
- **3.7 CI/CD Pipeline** — GitHub Actions workflow, Docker-based test execution, artifact collection (reports, screenshots, logs), environment selection via workflow dispatch. Skip if not needed for initial delivery.
- **3.8 Logging Strategy** — Correlation ID (trace ID per test execution, threaded through all layers for multi-interface tracing), structured logging (JSON for file/CI handlers, human-readable for console), sensitive data masking (PII/credentials never in logs — filter-based redaction), log level strategy (ERROR=failures, WARNING=retries, INFO=operations, DEBUG=SDK detail), Allure integration (logs attach to test steps in report), `trace.py` enhanced to emit structured JSON with correlation ID. Lives at `framework/resources/utilities/logging_config.py`.

**References:**
- 3.1: `platform-selenium/framework/resources/config/environment_config.json` (URL-keyed env structure)
- 3.1: `v2/framework/resources/config/environment_config.json` (5 environments with IDs, URLs, passwords — anti-pattern: passwords committed)
- 3.1: `v2/framework/resources/config/elevated_user_config_*.json` (per-env user files — anti-pattern: separate files per env)
- 3.1: `v2/framework/resources/config/db_config.json` + `oracle_config.json` (DB config — architecture reference)
- 3.1: `platform-selenium/.env.example` (dotenv template pattern)
- 3.1: `platform-playwright/playwright.config.ts` (dotenv + env var resolution)
- 3.2: `platform-selenium/tests/conftest.py` (root conftest — CLI options, driver fixture, config fixture, HTML report hooks, dynamic marker registration)
- 3.2: `hmsa-healthcare-qa/tests/conftest.py` (root — env config + DB fixture)
- 3.2: `hmsa-healthcare-qa/tests/readmissions/conftest.py` (domain conftest — SP names, table names, parametrize tuples as Python constants)
- 3.2: `v2/tests/conftest.py` (legacy root conftest — web_interface, driver, environment, elevated_users, data_dir fixtures)
- 3.3: `v2/tests/assignment_based_pays/data/` (complete data composition pattern — input JSON + SQL templates + document uploads)
- 3.3: `v2/tests/assignment_based_pays/data/input/command_pay.json` (role-keyed JSON — keys are `role.method_name`, values are parameters)
- 3.3: `v2/tests/assignment_based_pays/data/sql/` (4 SQL files for dynamic test subject discovery — anti-pattern: regex-on-file instead of parameterized queries)
- 3.3: `v2/tests/sailing_diary/data/input_data.json` (list-based scenario data — sailing details, locations, support units, passengers)
- 3.3: `v2/framework/resources/utilities/test_data.py` (TestData class — auto-parses directory of JSON/Excel files — over-engineered, use plain json.load + fixtures instead)
- 3.3: `hmsa-healthcare-qa/projects/30-day-readmissions/autodeny/data-setup-guide.md` (7-step manual data creation process — shows real-world data setup complexity: SP constraints, claim import from prod, DOS date assignment, QNXT field changes, Test Ops coordination)
- 3.4: `platform-selenium/framework/resources/utilities/autologger.py` (decorator factory — clean implementation, rename to `trace.py` / `@trace("Task")` to distance from v2 naming)
- 3.5: `platform-selenium/framework/resources/chromedriver/driver.py` (browser driver factory — Chrome/Brave, headless, webdriver-manager)
- 3.5: `v2/framework/resources/chromedriver/driver.py` (legacy driver factory — architecture reference)

## Phase 4: Test Harness

Docker stack — web app, API, DB, all wired together as a target for demo tests.

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 4.1 | Data Model (Orderly, generic commerce) | [data-model.md](04-test-harness/data-model.md) | 202/214 | DESIGNED |
| 4.2 | Harness App (Orderly — UI/API/DB/SOAP slices per vertical) | [harness-app.md](04-test-harness/harness-app.md) | 202/209/214/220 | DESIGNED |
| 4.3 | Docker Composition | [docker-composition.md](04-test-harness/docker-composition.md) | 224 | NOT STARTED (design at V5 start) |

## Phase 5: Demo Tests

Actual pytest scenarios exercising all interfaces against the test harness.

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 5.1 | UI Tests | [ui-tests.md](05-demo-tests/ui-tests.md) | — | NOT STARTED |
| 5.2 | API Tests | [api-tests.md](05-demo-tests/api-tests.md) | — | NOT STARTED |
| 5.3 | DB Tests | [db-tests.md](05-demo-tests/db-tests.md) | — | NOT STARTED |
| 5.4 | Hybrid Tests | [hybrid-tests.md](05-demo-tests/hybrid-tests.md) | — | NOT STARTED |

**References:**
- 5.1: `platform-selenium/framework/_reference/tests/test_e2e_create_employee_and_assign_task.py` (AAA pattern, Role-driven)
- 5.3: `hmsa-healthcare-qa/tests/readmissions/` (44+ DB test cases — SP validation, data pipeline testing)
- 5.4: `v2/tests/assignment_based_pays/tests/test_command_pay.py` (DB→UI→SOAP→UI→DB — most complex hybrid flow reference, 208 lines)
- 5.4: `v2/tests/assignment_based_pays/tests/test_assignment_incentive_pay.py` (DB discovery → multi-role UI → DB verify — cleaner hybrid example)
- 5.4: `v2/tests/sailing_diary/` (multi-step UI workflow with list-based data input)
- All: `hmsa-healthcare-qa/projects/30-day-readmissions/autodeny/data-setup-guide.md` (real-world data setup complexity — 7 steps, multi-system, multi-tool)

## Phase 6: Enterprise Documentation

Written after code exists. References built code, not speculation.

| # | Component | Design Doc | Backlog | Status |
|---|-----------|-----------|---------|--------|
| 6.1 | Architecture Overview | [architecture.md](06-documentation/architecture.md) | — | NOT STARTED |
| 6.2 | Developer Guide | [developer-guide.md](06-documentation/developer-guide.md) | — | NOT STARTED |
| 6.3 | Setup Guide | [setup-guide.md](06-documentation/setup-guide.md) | — | NOT STARTED |
| 6.4 | Test Strategy | [test-strategy.md](06-documentation/test-strategy.md) | — | NOT STARTED |

---

## Status Legend

| Status | Meaning |
|--------|---------|
| NOT STARTED | Design doc not yet written |
| DESIGNING | In discussion — design in progress |
| DESIGNED | Design doc complete, ready for backlog |
| BACKLOGGED | Backlog item created (number in Backlog column) |
| BUILDING | Pipeline executing |
| BUILT | Code delivered to target repo |
| VALIDATED | Passes 5-layer contract + acceptance criteria |

## Dependencies

```
Phase 1 (interfaces) ──→ Phase 2 (reference patterns) ──→ Phase 5 (demo tests)
                                                              ↑
Phase 3 (architecture) ──→ Phase 4 (test harness) ───────────┘

Phase 6 (documentation) — after all code is built
```

## Build Plan — Vertical Slices (supersedes wave execution, 2026-07-14)

**Build and test one whole interface + its dependencies before moving to the next.** Each vertical front-loads its harness slice (Layer 2 identifiers bind to the real app), ends with its E2E test as the exit gate, and the next vertical is blocked until that gate is green and accepted. Execution: `/kernel/execute-pipeline` per backlog, strictly sequential (no parallel pipelines — shared target working tree). Every BUILD lands on a target-repo feature branch `build/NNN-*`, merged via `/kernel/review-queue accept`.

**Demo product: "Orderly" — generic commerce (orders domain). NO HMSA/healthcare vocabulary in shipped code** (user constraint, 2026-07-14). Harness design: [data-model.md](04-test-harness/data-model.md) + [harness-app.md](04-test-harness/harness-app.md).

| Slice | Backlogs (strict internal order) | Exit gate |
|-------|----------------------------------|-----------|
| ✅ Wave 0 | 198 git baseline (done, accepted) | merged |
| V-BASE | 199 trace → 200 retry → 201 contract copy | all accepted |
| V1 Browser | 202 harness-ui → 203 interface → 204 pages → 205 components → 206 tasks → 207 role → 208 **UI E2E** | 208 green vs live Orderly |
| V2 REST | 209 harness-api → 210 interface → 211 api-objects → 212 tasks → 213 **API E2E** | 213 green |
| V3 DB | 214 harness-db (Docker SQL Server + SP) → 215 interface → 216 data-objects → 217 tasks → 218 role → 219 **DB E2E** | 219 green |
| V4 SOAP | 220 harness-soap → 221 interface → 222 tasks → 223 **SOAP E2E** | 223 green |
| V5 Integration | 224 compose (4.3 design-first) → 225 hybrid tasks → 226 hybrid role → 227 **HYBRID E2E** → 228 notes doc | 227 green = platform thesis demonstrated |
| Blocked | 229 conftest | Phase 3.1 + 3.5 |

**Build-order exceptions (design in any order; builds flow bottom-up):**

- **2.5.2 Fixture Wiring** builds only after Phase 1 (interfaces exist to import), **3.1** (config schema it consumes), and **3.5** (factories it calls). Backlogging it earlier produces stubs or failed gates. Design decisions recorded in [docs/walkthroughs/2026-07-13-conftest-design.md](../../docs/walkthroughs/2026-07-13-conftest-design.md).
- Open question parked before any claim-injection code: 837BT tool vs EDI file drop (whether a FileInterface is needed) — resolve during Phase 4 / client intake design. See walkthrough ledger notes.

---

## Product Vision: Repeatable Build Loops

HMSA is client #1. When client #2, #3, #4 come in, the interfaces and architecture are reusable — what changes is the client-specific code (pages, API objects, data objects, tasks, roles, tests, config).

### What's Reusable vs Custom

| Component | Reusable | Custom Per Client |
|-----------|----------|-------------------|
| Interfaces (Browser, API, DB, SOAP) | Yes — same every time | DB type may vary (SQL Server vs Oracle) |
| `_reference/` pattern architecture | Yes — same 5-layer contract | Domain-specific examples |
| Page Objects | No | Their app, their locators |
| API Objects | No | Their endpoints, their schemas |
| Data Objects | No | Their tables, their queries |
| Tasks / Roles / Tests | No | Their workflows, personas, scenarios |
| Test Harness | No | Their infra (Docker, VPN, cloud) |
| Config | No | Their URLs, creds, environments |

### How Client Code Gets Built

The agent IS the generator. No dedicated build loops or tooling needed.

Each interface type gets canonical `_reference/` patterns. The agent reads the reference, generates client-specific code following the pattern, validates against the 5-layer contract. This is the same approach that works in platform-selenium today — less infra, more leverage from the agent.

| Component | Agent Input | Agent Reads | Agent Produces |
|-----------|------------|-------------|----------------|
| Page Objects | URL + creds (Playwright MCP discovers elements) | `_reference/pages/` | POM class per page |
| API Objects | Swagger spec or endpoint list | `_reference/api_objects/` | API Object class per resource |
| Data Objects | Table schema | `_reference/data_objects/` | Data Object class per table |
| Tasks | Domain operation description | `_reference/tasks/` | Task class composing L2 objects |
| Roles | Persona description | `_reference/roles/` | Role class orchestrating Tasks |
| Tests | Scenario description | `_reference/tests/` | Test class with AAA pattern |

### Client Engagement Pattern

1. **Onboard** — discover their app (URLs, APIs, DB schemas)
2. **Configure** — set up environments, creds, Docker targets
3. **Generate** — agent reads `_reference/`, builds client-specific code
4. **Validate** — run against their environment
5. **Deliver** — hand off the repo

No generators to build or maintain. The `_reference/` patterns are the product.

### Interface Extension Pattern

The base interfaces ship with the platform. Client integrations add custom methods. No inheritance, no mixins — just add methods to the interface file in the client's repo following the same conventions.

**The monolith guard:** Interfaces must stay focused on SDK primitives. If a method composes multiple SDK calls or uses domain vocabulary, it belongs in a higher layer.

| Belongs in Interface (Layer 1) | Belongs in Component (Layer 2) | Belongs in Task (Layer 3) |
|-------------------------------|-------------------------------|--------------------------|
| One SDK call + logging + error handling | Multiple Interface calls composed | Multiple Components orchestrated |
| Returns SDK primitive | Returns `self` for chaining | Returns typed result (or `None` for UI when state is page-observable) |
| Generic — any app could use it | App-specific but reusable per page/resource | Domain operation spanning multiple Components |
| No locators, no endpoints, no table names | Owns its locators/endpoints/schemas | No identifiers — delegates to Components |

### Lesson from Legacy Framework (v2)

The v2 framework (PeopleSoft/military) put everything in one `WebInterface` class — 430 lines mixing generic SDK wrappers with PeopleSoft-specific composed methods. This is the monolith anti-pattern.

**What was in WebInterface that shouldn't have been:**

```
WebInterface (430 lines — monolith)
│
├── Generic SDK wrappers (CORRECT — these belong here)
│   click(), send_keys(), find_element(), wait_for_element_*(),
│   select_by_text(), scroll_to_element(), get_attribute()
│
├── PeopleSoft loading circle wait (WRONG — domain-specific utility)
│   wait() — wraps wait_for_element_invisible with hardcoded
│   PeopleSoft partial ID "WAIT_win"
│   → Should be: utility or base Component method
│
├── PeopleSoft modal switching (WRONG — composes multiple SDK calls)
│   switch_ptmodframe() — switch_frame + find_elements + retry loop
│   → Should be: PeopleSoftModalComponent (Layer 2)
│
├── PeopleSoft grid operations (WRONG — domain-specific, complex logic)
│   _get_grid_col_header_names() — hardcoded CSS classes
│   _get_grid_rows_as_cell_lists() — PeopleSoft row patterns
│   get_grid_row_nums_by_col_vals() — multi-method composition
│   → Should be: PeopleSoftGridComponent (Layer 2)
│
└── File upload with hardcoded locators (WRONG — has locators + composes operations)
    upload_attachment() — contains "HR_OBD_ATT_WRK_ATTACHADD",
    "PT_ATTACH_BUTTON_DEF" — locators in the Interface
    → Should be: AttachmentTasks (Layer 3)
```

**What correct layering looks like:**

```
Layer 1: BrowserInterface (PURE — generic SDK wrapper)
│   click(), send_keys(), find_element(), wait_for_*(),
│   switch_frame(), select_by_text(), scroll_to_element()
│
│   No domain vocabulary. No composed operations. No locators.
│
└──→ Layer 2: Components (app-specific, owns identifiers)
    │
    ├── PeopleSoftGridComponent
    │   Locators: PSLEVEL1GRIDCOLUMNHDR, ps_grid-col, etc.
    │   Methods: get_row_by_column_values(), get_column_headers()
    │   Composes: BrowserInterface.find_elements() + matching logic
    │
    ├── PeopleSoftModalComponent
    │   Locators: ptModFrame_*
    │   Methods: switch_to_modal(index), close_modal()
    │   Composes: BrowserInterface.switch_frame() + retry
    │
    ├── LoginPage, HomePage, etc.
    │   (same as platform-selenium today)
    │
    └──→ Layer 3: Tasks (domain operations)
        │
        ├── AttachmentTasks
        │   Methods: upload_document(file_path)
        │   Composes: ModalComponent + click attachment button +
        │             select file + confirm
        │
        └── SailingDiaryTasks, PayrollTasks, etc.
```

The rule is simple: if you're adding a method and it uses domain vocabulary or calls multiple Interface methods, it goes in Layer 2 or Layer 3 — not in the Interface.

### Shared Components (Layer 2)

The v2 legacy framework already had shared components — this isn't a new concept:

```
v2 framework/pages/components/
├── GridComponent              ← grid column/row lookup, reused across pages
├── NavbarComponent            ← top nav (logout, menu), reused across pages
├── DashboardComponent         ← left-nav PSD tabs/links, reused across workflows
├── ActivityGuideComponent     ← save/next/submit wizard, reused across features
├── MyWorkGridSuperclass       ← approval grid, reused across dashboards
└── [domain]-specific dashboards
```

These were correctly placed at Layer 2 — they compose Interface calls, own their locators, return `self` for chaining, and get reused by multiple Tasks.

**What went wrong:** Some operations that belonged alongside these components got trapped in the Interface instead:

```
v2 WebInterface (monolith — 430 lines)
│
│  Grid logic duplicated here          GridComponent also exists
│  ├── _get_grid_col_header_names()    ├── get_col_names()        ← SAME THING
│  ├── _get_grid_rows_as_cell_lists()  ├── get_row_elements()     ← SAME THING
│  └── get_grid_row_nums_by_col_vals() └── get_row_num_by_col_vals() ← SAME THING
│
│  These never got extracted:
│  ├── wait()                    → should be a utility (PeopleSoft loading circle)
│  ├── switch_ptmodframe()       → should be ModalComponent
│  ├── upload_attachment()       → should be AttachmentTasks (Layer 3)
│  └── select_file_from_dialog() → should be DesktopInterface (different SDK)
```

**The correct structure for this platform:**

```
framework/
├── interfaces/                          Layer 1 — SDK primitives only
│   ├── browser_interface.py               click, type, wait, find — generic
│   ├── api_interface.py                   get, post, put, delete — generic
│   ├── sql_server_interface.py            query, execute, execute_sp — generic
│   └── soap_interface.py                  send_envelope, parse_response — generic
│
├── _reference/
│   ├── components/                      Layer 2 — shared, reusable
│   │   ├── grid_component.py              any app with HTML grids
│   │   ├── modal_component.py             any app with modals/dialogs
│   │   ├── navbar_component.py            any app with top navigation
│   │   ├── wizard_component.py            any app with multi-step wizards
│   │   └── file_upload_component.py       any app with file uploads
│   │
│   ├── pages/                           Layer 2 — app-specific
│   │   ├── login_page.py                  one per page in client app
│   │   └── dashboard_page.py
│   │
│   ├── api_objects/                     Layer 2 — app-specific
│   │   └── users_api.py                   one per API resource
│   │
│   ├── data_objects/                    Layer 2 — app-specific
│   │   └── claims_table.py                one per DB table
│   │
│   ├── tasks/                           Layer 3 — domain operations
│   │   ├── ui_tasks.py                    compose pages + components
│   │   ├── api_tasks.py                   compose api_objects
│   │   └── hybrid_tasks.py               compose across interfaces
│   │
│   ├── roles/                           Layer 4 — user personas
│   │   └── admin_role.py                  orchestrate tasks
│   │
│   └── tests/                           Layer 5 — scenarios
│       └── test_e2e_workflow.py            AAA pattern
```

**Key distinction:**

```
components/ = shared across apps (grid, modal, wizard, navbar)
              ↑ reusable — ship with the platform

pages/      = app-specific objects (login, dashboard, claims form)
api_objects/ = app-specific objects (users API, claims API)
data_objects/ = app-specific objects (claims table, audit table)
              ↑ custom — built per client

All are Layer 2 (Object layer). All compose Interface. All own their identifiers.
The difference is reusability scope.
```

**Why the Interface never needs extension:**

The Interface is a pure SDK wrapper. Every SDK primitive is exposed. Any operation you'd ever need — no matter how complex or client-specific — can be composed from those primitives in Layer 2 or above. No client will ever need to modify Layer 1.

```
Need custom iframe handling?  → compose browser.switch_to_frame() + browser.find_elements()
                                in a FrameComponent (Layer 2)

Need paginated API calls?     → compose api.get() in a loop
                                in a PaginationComponent (Layer 2)

Need stored proc with params? → compose db.execute() with param binding
                                in a DataObject (Layer 2)

The Interface exposes the SDK. Upper layers compose it.
Layer 1 is closed. Layer 2+ is open.
```

**Decision: no subclasses, no mixins, no abstract base.** The interface file is the interface. Add methods, follow conventions. The 5-layer contract and the existing methods in the file are the guide. The agent reads them as examples and writes new ones in the same style.
