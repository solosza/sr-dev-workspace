# Write customers.html

## Context
Backlog 202: customer list table + inline create form.

## Type
BUILD
## Execution
inline
## Dependencies
- 006
## Phase Gate
- [ ] routes_customers.py exists

## Requirements
- Write `harness/orderly/templates/customers.html` (extends base): customers table (thead/tbody — a secondary grid target), create form (input-name, input-email, button-create-customer), all interactive elements with data-testid

## Acceptance Criteria
- [ ] Template exists; full data-testid coverage

## Gates Satisfied
- (feeds HUI-03/04)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
