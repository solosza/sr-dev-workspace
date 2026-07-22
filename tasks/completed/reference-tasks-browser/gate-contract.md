# Gate Contract — 206 _reference Browser Tasks

Deliverable: framework/_reference/tasks/order_workup_tasks.py on branch build/206-qa-build-reference-tasks-browser.

## Gates

| Gate | Check | Method |
|------|-------|--------|
| TSK-01 | Feature branch exists; main untouched | run_code: `git -C <target> branch --list build/206-*` non-empty; main HEAD unchanged |
| TSK-02 | order_workup_tasks.py exists with OrderWorkupTasks class | file_exists + run_code import |
| TSK-03 | Contract semantics (AST ONLY — see Test-Script Requirements) | run_test |
| TSK-04 | Sequence-spy behavioral proof | run_test: Task executed against recording stub pages; asserted call sequence matches design (open_order: nav → locate → open detail; change_status: select → submit; capture_order_id returns str) |
| TSK-05 | Live against Orderly — ENV-GATED | run_test: bare-selenium two-page click probe FIRST. Probe green → full live flow (open order 3, change status, capture id, assert on real DOM). Probe red → live read-path only (capture_order_id via navigate+read), report ENV-BLOCKED residue for click-path; DO NOT fake, DO NOT weaken, DO NOT JS-click inside framework code |
| TSK-06 | Commit on branch; porcelain clean | run_code |

## TSK-03 Semantics Rules (contract v2.3 L3 + Browser addendum)

- Constructor: Page Objects/Components via DI — NO BrowserInterface param, NO internal page construction (`ast.Call` on page classes inside `__init__` is a violation)
- `@trace("Task")` on every public method; NO decorator on `__init__`
- `-> None` on all public methods EXCEPT the one documented typed-return (capture_order_id -> str)
- NO try/except; NO locators/testid literals; NO screenshot machinery
- One domain operation per method; navigation and submission are separate methods

## Test-Script Requirements (lesson #39 — MANDATORY method)

Semantics test scripts MUST be AST-based: `ast.parse`, walk nodes; docstrings excluded by construction. String-grep semantics checks are BANNED (docstrings quoting rules + templated locators guarantee false positives). Decorator detection via `ast.FunctionDef.decorator_list`; return annotations via `ast.FunctionDef.returns`. Dynamic identifiers (if any) must be compared against template-side Jinja patterns, never flagged raw.

## Copy-First Rule (lesson #38)

Code copied from platform-selenium predates contract v2.3 (e.g., @autologger not @trace; BrowserInterface-in-constructor; login-as-task). Every copied pattern is gated against the CURRENT contract — "proven source" means proven behavior, not proven compliance. Login/identity belongs to L4 Roles (207), NOT this deliverable.

## Env Rule (lessons #41/#42)

The selenium stack currently drops post-navigation clicks machine-locally. TSK-05's probe decides the live scope honestly. A skipped/partial TSK-05 ALWAYS blocks merge pending orchestrator validation — skip-after-3 never waives a gate.
