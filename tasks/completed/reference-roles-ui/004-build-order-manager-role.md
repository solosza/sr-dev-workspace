# Build order_manager.py — L4 Second Persona

## Context
Backlog 207: the second persona for 208's multi-user E2E (clerk creates/works, manager cancels). Same contract shape as OrderClerk (read order_clerk.py after 003 — stay consistent), different identity + workflow.

## Type
BUILD
## Execution
inline
## Dependencies
- 002

## Requirements
- File: `framework/_reference/roles/order_manager.py` (+ export) with class `OrderManager`
- Constructor `@trace("Role Constructor")`: `__init__(self, common: CommonTasks, order_workup: OrderWorkupTasks, identity: dict)` — same DI shape as OrderClerk
- Workflow `@trace("Role")`: `cancel_order(self, order_id: str) -> None`:
  1. self-auth via common.login with own identity (manager credentials come from the injected dict)
  2. `self.order_workup.open_order(order_id)`
  3. `self.order_workup.change_status("CANCELLED")` — CANCELLED is the workflow's semantic, allowed as the one workflow-owned constant (it IS the cancel operation, not scenario data)
- NO try/except, no pages, no interfaces, no credential literals

## Acceptance Criteria
- [ ] Imports cleanly; self-auth first; multiple task calls; zero ROL-04 violations

## Gates Satisfied
- ROL-03 (manager half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
