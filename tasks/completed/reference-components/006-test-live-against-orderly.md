# Test: Components Live Against Orderly (L3)

## Context
Backlog 205: the generic components drive Orderly's REAL grid and modal through injected configs — proving the locator-contract pattern on a live app.

## Type
TEST
## Execution
inline
## Dependencies
- 002, 003, 004
## Phase Gate
- [ ] Semantics test (005) green

## Requirements
- Script: seed + start Orderly; headless Chrome; login via LoginPage (existing); construct GridComponent(browser, orders_page grid config): get_row_count() > 0, find_row_by_values on a SEEDED order id returns the right row index, click_row lands on that order's detail URL; back to /orders: click a delete button, ModalComponent(browser, modal config): is_open() True → click_cancel → is_open() False and the order still listed
- Cleanup in finally; L3-BLOCKED honestly if env broken; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 — generic components, injected configs, real app

## Gates Satisfied
- CMP-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
