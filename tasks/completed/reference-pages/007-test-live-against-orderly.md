# Test: Pages Live Against Orderly (L3)

## Context
Backlog 204: the page objects drive the real app through the real interface — the first two-layer stack running live.

## Type
TEST
## Execution
inline
## Dependencies
- 002, 003, 004, 005
## Phase Gate
- [ ] All four page files exist; contract semantics test (006) green

## Requirements
- Script: seed + start Orderly; headless Chrome; BrowserInterface; then THROUGH PAGE OBJECTS ONLY: LoginPage.navigate → enter_username/enter_password (seeded clerk) → click_login; CustomersPage: is_customer_listed(seeded name) True; OrdersPage: navigate, is_order_listed(seeded id) True; OrderDetailPage: open a seeded order, get_displayed_status matches seed; cleanup in finally (driver quit + server stop)
- L3-BLOCKED honestly if env broken; non-zero exit otherwise = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 — full login→browse→detail flow through page objects on the live app

## Gates Satisfied
- PAG-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
