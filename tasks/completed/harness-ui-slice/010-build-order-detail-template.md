# Write order_detail.html

## Context
Backlog 202: order detail with status transition — the OrderWorkupTasks exemplar's target (open order → change status → confirm).

## Type
BUILD
## Execution
inline
## Dependencies
- 008
## Phase Gate
- [ ] routes_orders.py exists

## Requirements
- Write `harness/orderly/templates/order_detail.html` (extends base): order fields display (data-testid per field incl. order-status), items table, status-change form (select-status offering only legal transitions + button-update-status), save confirmation flash element (data-testid="flash-saved")
- Full data-testid coverage

## Acceptance Criteria
- [ ] Template exists; status form + confirmation flash present; full coverage

## Gates Satisfied
- (feeds HUI-03/04)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
