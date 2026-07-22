# Write order_detail_page.py

## Context
Backlog 204: order detail page object — status transition form + confirmation flash, the OrderWorkupTasks target.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/204-qa-build-reference-pages

## Requirements
- READ harness/orderly/templates/order_detail.html for actual testids
- Write framework/_reference/pages/order_detail_page.py: select_status, click_update_status atomics; state-checks: get_displayed_status, is_save_confirmed (flash element), get_order_field(name)
- Contract semantics rules as in 002

## Acceptance Criteria
- [ ] File exists; real testids only; semantics rules hold

## Gates Satisfied
- PAG-02, PAG-03/04/05/06 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
