# Test: Live Against Orderly — ENV-GATED (lessons #40/#41/#42)

## Context
Backlog 207: honest L3 for click-centric Role workflows. Probe decides scope; never fake, never weaken, never JS-click inside framework code.

## Type
TEST
## Execution
inline
## Dependencies
- 005, 006
## Phase Gate
- [ ] ROL-04 and ROL-05 green

## Requirements
- Boot Orderly: fresh seed + uvicorn (cwd = target repo). Login redirects to /customers (lesson #40, main.py)
- PROBE FIRST: bare-selenium two-page click test (post-navigation delete-button click → modal displayed?)
- IF PROBE GREEN: full live — wire real stack (BrowserInterface → LoginPage/OrdersPage/OrderDetailPage → CommonTasks/OrderWorkupTasks → OrderClerk with clerk identity, OrderManager with manager identity); clerk.work_order_status_change("3", "PROCESSING") → assert status on real DOM; manager.cancel_order("3") → assert CANCELLED; the manager step live-proves the session switch
- IF PROBE RED: construction + wiring live scope — build the full real object graph (no clicks), verify identity dicts landed on each role, verify CommonTasks holds the real LoginPage instance; report exactly: `ROL-06 PARTIAL: click-path ENV-BLOCKED (lesson #41) — orchestration proven by ROL-05; full-stack proof deferred to 208 E2E` and treat as COMPLETE
- Cleanup server AND webdriver in finally (206 left a stray uvicorn on 8017 — kill your own processes); other failures → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 on either path, path taken stated in output, no stray processes left on 8017

## Gates Satisfied
- ROL-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
