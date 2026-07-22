# Test: Live Against Orderly — ENV-GATED (lessons #40/#41/#42)

## Context
Backlog 206: honest L3. The machine currently drops selenium clicks after the first navigation (lesson #41); the probe decides scope — never fake, never weaken, never JS-click inside framework code.

## Type
TEST
## Execution
inline
## Dependencies
- 003, 004
## Phase Gate
- [ ] TSK-03 and TSK-04 green

## Requirements
- Boot Orderly: seed (`python -m harness.orderly.seed` from target-repo cwd) + `uvicorn harness.orderly.main:app --port 8017` subprocess (cwd = target repo so the relative sqlite path resolves). LOGIN REDIRECTS TO /customers, NOT /orders (lesson #40 — verified in main.py)
- PROBE FIRST: bare-selenium two-page click test (login click on first document → navigate → click `[data-testid='button-delete-3']` → is `[data-testid='modal-confirm-delete']` displayed?)
- IF PROBE GREEN (env recovered): full live flow — construct real pages + `OrderWorkupTasks` via DI, login via LoginPage, `open_order("3")` → assert detail URL/field, `change_status("PROCESSING")` → assert status shown, `capture_order_id()` == "3"
- IF PROBE RED: live read-path only — navigate to /orders/3 directly, construct task with real pages, `capture_order_id()` == "3" live; then report exactly: `TSK-05 PARTIAL: click-path ENV-BLOCKED (selenium input regression, lesson #41) — sequence proven by TSK-04; full-stack click proof deferred to 208 E2E` and treat the task as COMPLETE (partial is the honest full scope under this env)
- Cleanup server in finally; failure (other than documented ENV-BLOCKED path) → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 on either path, with the path taken stated in output

## Gates Satisfied
- TSK-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
