# Write modal_component.py (LEAD exemplar)

## Context
Backlog 205: the simplest complete demonstration of locator-contract injection — the file future agents learn the shared-component pattern from. Keep it minimal and immaculate.

## Type
BUILD
## Execution
inline
## Dependencies
- 001
## Phase Gate
- [ ] On branch build/205-qa-build-reference-components

## Requirements
- READ FIRST: 2.1.5 design doc (workspace shared-components.md) + shipped contract L2 rules + v2.3 rule-1 injection clause
- Write framework/_reference/components/modal_component.py (+ components/__init__.py): frozen dataclass ModalLocators (root, confirm_button, cancel_button — tuples of (By, selector)); class ModalComponent(browser, locators) — mechanics only: is_open() state-check, click_confirm()/click_cancel() atomics returning self
- `SCOPE = 'universal'` class constant (genericity declaration)
- NO concrete data-testid values anywhere; NO try/except; NO decorators; docstring states the pattern (identifiers injected, never owned)

## Acceptance Criteria
- [ ] File exists; mechanics-only; scope declared; contract semantics hold

## Gates Satisfied
- CMP-02/03/04 (partial)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
