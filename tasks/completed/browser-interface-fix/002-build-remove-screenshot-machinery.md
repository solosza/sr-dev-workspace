# Remove Screenshot Machinery from the Interface

## Context
16 `_take_screenshot` references live inside browser_interface.py. Contract (Browser addendum rule 5 + conftest rule 5): screenshot-on-failure is conftest's job via pytest_runtest_makereport — the Interface must not know reports exist. The interface MAY keep a single generic `take_screenshot(path)` SDK primitive (it wraps driver.save_screenshot — that's a legitimate primitive the conftest hook will call); what must go is the automatic on-failure screenshot side-effects inside other methods.

## Type
BUILD
## Execution
inline
## Dependencies
- None
## Phase Gate
- [ ] On branch build/203-qa-build-browser-interface

## Requirements
- Remove the `_take_screenshot` helper and ALL on-failure screenshot calls from except blocks
- KEEP (or add) one public primitive: `take_screenshot(path: str)` wrapping the SDK call directly — one SDK call, no report-path logic, no directory management
- No other behavior changes

## Acceptance Criteria
- [ ] Zero `_take_screenshot` references; at most one public take_screenshot primitive wrapping the SDK call

## Gates Satisfied
- FIX-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
