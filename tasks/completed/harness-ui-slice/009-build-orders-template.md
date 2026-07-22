# Write orders.html

## Context
Backlog 202: the order list — a REAL table grid (thead th headers, tbody rows) because GridComponent's locator contract binds to it, plus the delete-confirmation modal ModalComponent binds to.

## Type
BUILD
## Execution
inline
## Dependencies
- 008
## Phase Gate
- [ ] routes_orders.py exists

## Requirements
- Write `harness/orderly/templates/orders.html` (extends base): orders table (data-testid="orders-grid", header cells, row cells incl. id/customer/status/total), create form, per-row detail link + delete button opening a confirmation MODAL (data-testid="modal-confirm-delete", button-confirm, button-cancel — plain HTML/CSS toggle, no JS framework), status filter select
- Full data-testid coverage

## Acceptance Criteria
- [ ] Template exists; grid + modal structures present; full coverage

## Gates Satisfied
- (feeds HUI-03/04)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
