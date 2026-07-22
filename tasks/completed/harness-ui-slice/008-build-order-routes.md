# Write Order Routes (routes_orders.py)

## Context
Backlog 202: the main workload surface — order list/create/detail/status-change/delete. The GridComponent flagship and ModalComponent lead bind here.

## Type
BUILD
## Execution
inline
## Dependencies
- 004
## Phase Gate
- [ ] main.py exists

## Requirements
- Write `harness/orderly/routes_orders.py`: GET /orders (list w/ status filter query param), POST /orders (create), GET /orders/{id} (detail), POST /orders/{id}/status (transition per data-model rules: PENDING→PROCESSING→COMPLETE; CANCELLED from any non-terminal), POST /orders/{id}/delete — all auth-guarded

## Acceptance Criteria
- [ ] File exists; router registered; status transition rules enforced server-side

## Gates Satisfied
- (feeds HUI-03)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
