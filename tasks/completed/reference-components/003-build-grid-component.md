# Write grid_component.py (FLAGSHIP)

## Context
Backlog 205: the pattern at full stress — most identifiers, most mechanics; the component enterprise clients copy hardest. Dry-tested in design against QNXT + platform-selenium; now built against Orderly.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/205-qa-build-reference-components

## Requirements
- READ FIRST: 2.1.5 design doc canonical GridLocators/GridComponent example — implement it faithfully
- Write framework/_reference/components/grid_component.py: frozen dataclass GridLocators (root, header_cells, rows, cell_template); GridComponent(browser, locators) — get_column_names() / get_row_count() / find_row_by_values(**column_values) state-checks; click_row(index) atomic returning self; dynamic per-cell locators built in method bodies from the injected cell_template
- `SCOPE = 'universal'`; same contract-semantics rules as 002

## Acceptance Criteria
- [ ] File exists; canonical example implemented; mechanics-only; semantics hold

## Gates Satisfied
- CMP-02/03/04 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
