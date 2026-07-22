# 5-Layer Framework Contract

**Status:** Complete
**Version:** 1.0
**Source of truth:** Extracted from platform-selenium `_reference/` directory
**Purpose:** Codifies structural rules for any platform built on the 5-layer architecture

---

## Global Rules

### Baseline Standards (by reference)

- **PEP 8** — naming, formatting, imports
- **SOLID Principles** — single responsibility, open/closed, Liskov substitution, interface segregation, dependency inversion
- **Fluent API** — Component atomic methods return `self` for method chaining (rationale: readability for non-technical stakeholders)

### Framework-Specific Additions

| # | Rule |
|---|------|
| 1 | Module-level docstring states the file's purpose and layer |
| 2 | Class docstring lists the layer's structural rules as bullet points |
| 3 | Docstring on every method |
| 4 | Inline comments only when explanation is needed |
| 5 | Methods organized by category with section header comments (`# === CATEGORY ===`) |
| 6 | Composition over inheritance — constructor takes dependencies, no subclassing |
| 7 | Imports only from the layer directly below or from utilities (exception: type annotation imports from any lower layer are permitted) |
| 8 | Logging on every operation |
| 9 | Constants as class-level attributes, config-driven defaults via constructor |
| 10 | Type hints on all parameters and return types |

### Error Handling

| # | Rule |
|---|------|
| 1 | Interface catches SDK exceptions, logs them, then re-raises — never swallows |
| 2 | Layers above Interface do not catch exceptions — let them propagate up to the test runner |

### Business Logic Boundaries

| Layer | Owns | Changes When |
|-------|------|-------------|
| Interface | No business logic — pure SDK wrapper | SDK API changes |
| Component (POM / Metric) | No business logic — mechanics only (one operation per method, state reads) | Identifiers or domain entity definitions change |
| Task | Operational logic — the steps within one domain operation | The operation's steps change (e.g., new form field) |
| Role | Workflow logic — which operations to run, in what order | The business workflow changes (e.g., new approval step) |
| Test | No business logic — Arrange, Act, Assert only | Requirements change |

---

## Per-Layer Rules

### Layer 1: Interface

**Return value conventions:** SDK primitives only (`WebElement`, `bool`, `str`, `dict`). Never domain objects.

**Structural rules:**

| # | Rule |
|---|------|
| 1 | Wraps the SDK/driver — no business logic, no domain vocabulary |
| 2 | Constructor (`__init__` in Python) takes SDK instance + config + logger |
| 3 | Config-driven defaults (timeouts, directories, flags) |
| 4 | Return types are SDK primitives — never domain objects |
| 5 | No knowledge of layers above (Components, Tasks, Roles) |

### Layer 2: POM / Metric

**Return value conventions:**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Atomic methods return `self` for chaining | Fluent API — non-technical stakeholders can read the method chain as a sentence describing the workflow |
| 2 | State-check methods return `bool` or primitive (`str`, `float`, `int`) | State-checks are assertion targets — tests need concrete values to assert on |

**Structural rules:**

| # | Rule |
|---|------|
| 1 | Constructor (`__init__` in Python) takes Interface instance only — composition, no inheritance |
| 2 | No decorators on any methods |
| 3 | Identifiers (locators, criteria, templates) as class-level constants (not buried in methods). When identifiers are numerous or complex (e.g., compliance rules with multiple fields), they may be externalized to a fixture file (JSON) and loaded in the constructor — the fixture is a storage format, not a different pattern |
| 4 | One atomic operation or state-check per method |
| 5 | Method names use domain vocabulary (e.g., `click_create_employee`, `evaluate_security`), not generic SDK terms |
| 6 | Only imports from Interface layer (layer directly below) or utilities |
| 7 | No knowledge of Tasks, Roles, or Tests |

### Layer 3: Task

**Return value conventions:**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Task methods return `None` — side effects only | Command pattern — Tasks do work, they don't return data. State is on the objects they compose. |

**Structural rules:**

| # | Rule |
|---|------|
| 1 | Constructor (`__init__` in Python) takes Interface instance, creates Component instances internally |
| 2 | `@automation_logger("Task")` on all methods, NOT on constructor |
| 3 | One domain operation per method |
| 4 | Uses fluent Component chaining inside methods (the Task method is the chain boundary) |
| 5 | Method parameters are domain values (`name`, `email`), not UI elements or SDK objects |
| 6 | Only imports from Component layer and Interface layer |
| 7 | No knowledge of Roles or Tests |

### Layer 4: Role

**Return value conventions:**

| # | Rule | Rationale |
|---|------|-----------|
| 1 | Role workflow methods return `None` — state stored on `self` | Command pattern — Roles orchestrate workflows, results are observable via POM/Metric state-checks |

**Structural rules:**

| # | Rule |
|---|------|
| 1 | Constructor (`__init__` in Python) takes Interface instance (pass-through) + workflow config (credentials, URLs, settings) |
| 2 | Creates Task module instances in constructor (passes Interface to each Task) |
| 3 | Workflow methods call MULTIPLE Tasks — orchestrates across Task modules |
| 4 | Stores workflow config on `self` — does NOT store Interface on `self` (Interface is pass-through only) |
| 5 | Only imports from Task layer (type annotation imports from Interface layer are permitted) |
| 6 | No knowledge of Tests |

### Layer 5: Test

**Return value conventions:** None — pytest collects test methods by naming convention. Test methods implicitly return `None`.

**Structural rules:**

| # | Rule |
|---|------|
| 1 | `@pytest.fixture(autouse=True) def setup` wires dependencies (Interface, config, test data) |
| 2 | Setup fixture creates POM/Metric instances on `self` for assertions |
| 3 | `@automation_logger("Test")` on test methods |
| 4 | `@pytest.mark` tags for categorization |
| 5 | Test creates Role(s) in Arrange |
| 6 | Test calls Role workflow method in Act |
| 7 | Test asserts via POM/Metric state-check methods in Assert |
| 8 | One AAA block per test method (one scenario) |
| 9 | Test never calls Task or POM action methods directly — always through Role |

### Decorator Usage

**Shared utility:** `resources/utilities/autologger.py` — must exist in every platform with the same implementation. Platform-agnostic (pure Python: `logging`, `functools`, `datetime`).

| Layer | Decorator | Rationale |
|-------|-----------|-----------|
| Interface | None | Already logs internally via `self.logger` — decorator would double-log |
| Component | None | Atomic one-liners that chain — decorating each would flood CLI with noise. The Task decorator wraps the entire chain at the right granularity. |
| Task | `@automation_logger("Task")` on methods, NOT on constructor | Traces operational logic — you see each domain operation start/end |
| Role | `@automation_logger("Role")` on workflow methods, `@automation_logger("Role Constructor")` on `__init__` | Traces workflow orchestration — you see the full workflow hierarchy |
| Test | `@automation_logger("Test")` on test methods | Traces test execution — you see which test is running and its duration |

**Runtime output (example):**
```
[Role Constructor] EmployeeManager.__init__ - START
[Role] create_employee - START
[Task] login - START
[Task] login - END (2.1s)
[Task] create_employee - START
[Task] create_employee - END (3.4s)
[Role] create_employee - END (5.5s)
[Test] test_e2e_create_employee - END (5.8s)
```

### Method Scope

| Layer | Scope | Rule |
|-------|-------|------|
| Interface | One SDK primitive per method | `click()` clicks, `execute()` executes — never combines multiple SDK calls |
| Component | One atomic operation or state-check per method | `click_create_employee()` does one action. `is_above_threshold()` reads one state. |
| Task | One domain operation per method | Navigate to a page = one operation. Submit a form = another. Even if part of the same flow, split by action concept. A Task method can span multiple Components but stays within one action. |
| Role | One complete workflow per method | Login → navigate → submit = one workflow. Roles orchestrate across Task modules. A Role method that wraps a single Task call probably shouldn't be a Role. |
| Test | One scenario per method | One test method = one AAA block (Arrange → Act → Assert) |

**Operation boundary rule (from v2 production code):** Navigation and form submission are SEPARATE Task methods even when they're part of the same flow. The split is by domain action concept, not by page or screen.

**Role composition rule (from v2 production code):** Roles exist to orchestrate ACROSS Task modules (e.g., `CommonTasks.login()` + `AssignmentBasedPaysTasks.navigate()` + `AssignmentBasedPaysTasks.submit()`). If a Role only calls one Task from one module, the workflow likely belongs in the Task layer.

---

## Pattern Lineage

### Classification

The 5-layer architecture is a **Screenplay pattern derivative** with codified contracts. It shares Screenplay's SOLID foundation and layered composition model, but adds explicit rules that Screenplay implementations leave implicit.

### Layer Mapping to Screenplay

| 5-Layer | Screenplay | Relationship |
|---------|-----------|-------------|
| Interface | Ability | Direct — wraps SDK/driver, gives actors the capability to interact with a system |
| POM / Metric | Interaction + Question | Combined — Interactions are atomic actions (`click`, `type`), Questions are state-checks (`is_displayed`, `get_score`) |
| Task | Task | Exact — sequences of domain operations composed from lower-level interactions |
| Role | Actor | Evolved — a domain-specific Actor with workflow orchestration responsibilities |
| Test | Scenario | Direct — AAA (Arrange/Act/Assert) maps to Given/When/Then |

### What This Pattern Adds Beyond Screenplay

| Addition | What It Does | Why Screenplay Doesn't Have It |
|----------|-------------|-------------------------------|
| Business logic boundaries | Codifies which layer owns which logic (Interface = none, Task = operational, Role = workflow) | Screenplay describes responsibilities but doesn't enforce ownership rules |
| Return value contracts | Fluent API for POM/Metric (`self`), Command pattern for Task/Role (`None`) | Screenplay has no per-layer return conventions |
| Runtime observability | `@autologger` decorator conventions per layer produce a hierarchical execution trace | Screenplay relies on framework-specific reporting (Serenity reports), not decorator-based tracing |
| Error handling rules | Interface catches/re-raises SDK exceptions; all layers above propagate | Screenplay has no codified error boundary rules |
| Method scope rules | One SDK call, one action, one operation, one workflow, one scenario — per layer | Screenplay recommends single responsibility but doesn't specify granularity per layer |

### Industry Context

- **Page Object Model (POM)** remains the dominant pattern (~80% of enterprise frameworks) due to simplicity and widespread adoption
- **Screenplay** is recognized as the SOLID evolution of POM, endorsed by Serenity BDD (Java) and Serenity/JS — but adoption remains limited due to perceived complexity
- This pattern occupies the **sweet spot** — it retains POM's familiar vocabulary (pages, locators, elements) while adding Screenplay's layered composition (Tasks, Roles, Actors) and going further with explicit contracts
- The pattern is **interface-agnostic** by design: swap the Interface layer (Selenium → API → deepeval → database), keep everything above it

### References

- [Screenplay Pattern — Serenity/JS Handbook](https://serenity-js.org/handbook/design/screenplay-pattern/)
- [Beyond Page Objects — InfoQ (Serenity + Screenplay)](https://www.infoq.com/articles/Beyond-Page-Objects-Test-Automation-Serenity-Screenplay/)
- [Designing SOLID Actors — DZone](https://dzone.com/articles/serenity-bdd-and-the-screenplay-pattern-designing)
- [POM vs Screenplay: Lessons from the Field — Skipper (2026)](https://www.skippersoft.services/2026/03/08/page-object-model-vs-screenplay-pattern-lessons-from-the-field/)

---

## Layer Mapping (Generic Vocabulary)

The contract uses generic terms. Each platform maps its own vocabulary to these layers.

### Layer Structure

| Layer | Generic Term | What It Is |
|-------|-------------|-----------|
| 1 | Interface | Wraps the SDK/driver — the only layer that touches external systems |
| 2 | Component | Atomic operations + state-checks on one domain entity (no business logic) |
| 3 | Task | One domain operation composed from Components |
| 4 | Role | One complete workflow composed from Tasks |
| 5 | Test | One scenario — Arrange, Act, Assert |

### Layer 2 Vocabulary (varies by platform)

| Concept | Generic Term | Description |
|---------|-------------|-------------|
| Layer 2 class | Component | A class that wraps one domain entity's operations and state |
| Constants | Identifiers | Class-level constants that locate/identify targets (locators, criteria, query templates, command templates) |
| Atomic action | Operation | One indivisible action through the Interface (click, evaluate, execute, insert) |
| State query | State-check | Returns `bool` or primitive — used by Tests for assertions |

### Interface SDK Examples (by platform type)

| Platform Type | Interface Wraps | Identifiers | Atomic Operations | State-Checks |
|--------------|----------------|-------------|-------------------|--------------|
| Browser (Selenium/Playwright) | WebDriver / Playwright | CSS/XPath locators | `click`, `enter_text`, `fill` | `is_element_displayed()` |
| LLM Eval (DeepEval) | DeepEval SDK (GEval) | Metric criteria + thresholds | `evaluate` | `is_above_threshold()`, `get_score()` |
| Remote (SSH) | SSH client (Paramiko) | Command templates, paths | `execute_command`, `upload_file` | `file_exists()`, `service_running()` |
| Database | DB connection (psycopg2, etc.) | Table names, query templates | `execute_query`, `insert_row` | `row_exists()`, `get_value()` |
| API | HTTP client (requests, httpx) | Endpoint URLs, headers | `send_request`, `post` | `status_ok()`, `response_contains()` |

### Resolution Rule

The audit command resolves vocabulary by reading the target platform's Interface layer. The Interface class tells you what SDK is wrapped, which determines what Layer 2 "Identifiers" and "Operations" look like for that platform. Layers 3-5 (Task, Role, Test) are universal — same vocabulary regardless of platform.

---

## Contract Status

- [x] Global Rules (baseline standards, framework additions, error handling, business logic boundaries)
- [x] Per-Layer Rules (all 5 layers — return value conventions + structural rules)
- [x] Decorator Usage
- [x] Method Scope (with operation boundary + Role composition rules)
- [x] Pattern Lineage (Screenplay mapping + industry context)
- [x] Layer Mapping (generic vocabulary + platform resolution rule)
