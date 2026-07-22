# Test: Import + Primitive Wrapping (L1/L2)

## Context
Backlog 203: verify the class imports, instantiates, and actually delegates to the driver — without needing a browser.

## Type
TEST
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] browser_interface.py exists on the branch

## Requirements
- Run python (PYTHONPATH → target framework/): import BrowserInterface; build a minimal stub driver object (recording attribute calls); instantiate BrowserInterface(stub, {}, logging.getLogger('t')); call 2-3 wrapped primitives; assert the stub recorded the delegated calls
- Non-zero exit = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0

## Gates Satisfied
- BRI-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
