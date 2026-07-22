# Build common_tasks.py — L3 Auth Task (COPY-FIRST)

## Context
Backlog 207: Roles self-authenticate by calling a Task — the design's `common.login` (roles-ui.md canonical). COPY-FIRST: read the login method shape in `D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/tasks/task_management_tasks.py` (fluent page chaining), then adapt to contract v2.3.

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File: `framework/_reference/tasks/common_tasks.py` (+ export in tasks/__init__.py) with class `CommonTasks`
- Constructor: `__init__(self, login_page: LoginPage)` — page DI, no decorator, nothing constructed internally
- Method: `login(self, username: str, password: str) -> None` with `@trace("Task")` — full auth sequence via LoginPage fluent calls; owns the session switch (logout-if-needed is login mechanics, NOT test choreography — if LoginPage lacks a logout/navigate affordance, navigating to the login URL via the page's own method is the switch)
- RULE ZERO: READ `framework/_reference/pages/login_page.py` on the branch FIRST — use its actual method names; do not invent
- Match the trace import style used by order_workup_tasks.py (read it)
- NO try/except, no locators, no credential literals

## Acceptance Criteria
- [ ] Imports cleanly; CommonTasks.login exact signature; zero ROL-04 violations

## Gates Satisfied
- ROL-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
