# Reconcile Locator Configs with orders_page Constants

## Context
Backlog 205: 204's orders_page.py already carries the grid/modal locator VALUE constants. The component config dataclasses must be instantiable from those constants unchanged — page owns values, component owns mechanics, fixtures wire (shared-components settle).

## Type
BUILD
## Execution
inline
## Dependencies
- 002, 003
## Phase Gate
- [ ] Both components exist on the branch

## Requirements
- READ orders_page.py's grid/modal constants; verify shape-compatibility with GridLocators/ModalLocators; adjust the PAGE constants (value side) if shapes mismatch — never bend the component contract to one page
- Update orders_page.py constants to construct the dataclasses directly (e.g. `RESULTS_GRID = GridLocators(...)`) if not already shaped that way

## Acceptance Criteria
- [ ] `GridLocators`/`ModalLocators` instantiate from orders_page constants without modification (import + construct succeeds)

## Gates Satisfied
- CMP-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
