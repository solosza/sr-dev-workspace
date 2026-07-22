# Write customers_page.py

## Context
Backlog 204: customers list + create form page object, bound to customers.html's real testids.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/204-qa-build-reference-pages

## Requirements
- READ harness/orderly/templates/customers.html for the actual data-testids
- Write framework/_reference/pages/customers_page.py: same structure/rules as 002 (design doc + contract semantics); atomic: enter_name, enter_email, click_create_customer, navigation; state-checks: is_customer_listed(name), get_customer_count
- Dynamic locators (per-name row lookup) built in method bodies, not constants

## Acceptance Criteria
- [ ] File exists; real testids only; semantics rules hold

## Gates Satisfied
- PAG-02, PAG-03/04/05/06 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
