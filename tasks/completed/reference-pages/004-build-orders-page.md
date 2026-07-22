# Write orders_page.py

## Context
Backlog 204: the orders list page object — the grid page. NOTE: grid and modal MECHANICS belong to 205's shared components; this page object owns the page-level actions (filter, create, open detail) and the locator VALUES its grid/modal configs will supply to 205.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/204-qa-build-reference-pages

## Requirements
- READ harness/orderly/templates/orders.html for actual testids
- Write framework/_reference/pages/orders_page.py: navigation, create-order form atomics, status filter select, click_order_detail(order_id) via dynamic locator, delete-button atomic (modal handling itself comes with 205); state-checks: is_order_listed(order_id), get_row_count-style primitive reads
- Include class constants for the grid/modal locator VALUES (root, header cells, rows, cell template; modal ids) — 205's fixtures will inject them into the generic components (shared-components design)
- Contract semantics rules as in 002

## Acceptance Criteria
- [ ] File exists; real testids only; grid/modal locator constants present; semantics rules hold

## Gates Satisfied
- PAG-02, PAG-03/04/05/06 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
