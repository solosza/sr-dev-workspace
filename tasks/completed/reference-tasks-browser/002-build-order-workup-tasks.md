# Build order_workup_tasks.py — COPY-FIRST from platform-selenium

## Context
Backlog 206: the Layer 3 Browser Tasks exemplar. COPY-FIRST: READ `D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/tasks/task_management_tasks.py` and `employee_management_tasks.py` FIRST — reuse their proven shape (one domain operation per method, fluent page chaining inside, docstring discipline). Then adapt to contract v2.3 + Orderly. The design doc `projects/hmsa-qa-platform/02-reference-patterns/tasks-browser.md` GOVERNS every divergence.

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File: `framework/_reference/tasks/order_workup_tasks.py` (+ `__init__.py` export) with class `OrderWorkupTasks`
- MANDATORY divergences from the copy source (lesson #38 — source predates contract):
  - Constructor takes PAGE OBJECTS via DI: `__init__(self, orders_page: OrdersPage, detail_page: OrderDetailPage)` — NOT BrowserInterface; NEVER construct pages internally
  - `@trace("Task")` on every public method; NO decorator on `__init__` — replaces the source's @autologger. VERIFY the trace import path by READING how existing _reference files import it (204 pages / trace.py location) — do not assume
  - NO login method — identity/auth is L4 Roles territory (207)
- Methods (orders domain, per design doc canonical):
  - `open_order(self, order_id: str) -> None` — navigate to orders, locate the order, open its detail — via page-object methods only (no locators here)
  - `change_status(self, status: str) -> None` — select the new status and submit on the detail page — via page methods; navigation and submission stay separate methods
  - `capture_order_id(self) -> str` — THE one typed-return exception: read the order id from the detail page for downstream verification
- NO try/except, no locators/testids, no screenshot calls, no hardcoded domain values (order_id/status are params)
- READ the actual OrdersPage/OrderDetailPage method names on the branch before writing calls — do not invent page methods; if a needed page method is missing, note it and use the closest existing method

## Acceptance Criteria
- [ ] File imports cleanly with framework paths; class + 3 methods with the exact signatures above
- [ ] Zero contract violations per gate-contract TSK-03 rules

## Gates Satisfied
- TSK-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
