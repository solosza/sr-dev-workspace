# Write Customer Routes (routes_customers.py)

## Context
Backlog 202: customer list + create — the simplest CRUD surface, exercised by the CustomersPage exemplar later.

## Type
BUILD
## Execution
inline
## Dependencies
- 004
## Phase Gate
- [ ] main.py exists

## Requirements
- Write `harness/orderly/routes_customers.py`: GET /customers (list), POST /customers (create from form), auth-guarded; renders customers.html

## Acceptance Criteria
- [ ] File exists; router registered in main.py

## Gates Satisfied
- (feeds HUI-03)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
