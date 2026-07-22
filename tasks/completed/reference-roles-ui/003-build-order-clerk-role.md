# Build order_clerk.py — L4 Persona (COPY-FIRST)

## Context
Backlog 207: the lead Role exemplar. COPY-FIRST: read `D:/my_ai_projects/project_test_repos/platform-selenium/framework/_reference/roles/employee_manager.py` for the persona shape, then apply the MANDATORY contract v2.3 divergences (lesson #38 — the source takes BrowserInterface, constructs tasks internally, passes loose credentials; ALL of that gets replaced). Design canonical: `projects/hmsa-qa-platform/02-reference-patterns/roles-ui.md`.

## Type
BUILD
## Execution
inline
## Dependencies
- 002

## Requirements
- File: `framework/_reference/roles/order_clerk.py` (+ roles/__init__.py export) with class `OrderClerk`
- Constructor `@trace("Role Constructor")`: `__init__(self, common: CommonTasks, order_workup: OrderWorkupTasks, identity: dict)` — tasks via DI, identity stored on self; NOTHING constructed internally
- Workflow `@trace("Role")`: `work_order_status_change(self, order_id: str, status: str) -> None`:
  1. `self.common.login(self.identity["username"], self.identity["password"])` — SELF-AUTH FIRST (the multi-user mechanism)
  2. `self.order_workup.open_order(order_id)`
  3. `self.order_workup.change_status(status)`
- Module docstring documents the multi-user pattern: the TEST sequences personas; each Role's workflow self-authenticates; login owns the session switch; no logout choreography in tests (ROL-07 greps for this)
- NO try/except, no pages, no interfaces, no credential literals

## Acceptance Criteria
- [ ] Imports cleanly; workflow calls MULTIPLE task modules with self-auth first; zero ROL-04 violations

## Gates Satisfied
- ROL-03 (clerk half), ROL-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
