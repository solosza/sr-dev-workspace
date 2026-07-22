# Test: Re-run L2 Stub + L3 Live After Surgery

## Context
The fix touched 5+ except blocks and removed 16 references — regressions are plausible. Both test tiers must still pass.

## Type
TEST
## Execution
inline
## Dependencies
- 001, 002
## Phase Gate
- [ ] FIX-01 and FIX-02 patterns verified in the file

## Requirements
- L2: stub-driver delegation test (import, instantiate, call navigate_to + click + enter_text against a recording stub; assert delegation AND that a stub-raised exception now PROPAGATES out of navigate_to)
- L3: run the committed test_l3_browser_interface.py (boots Orderly + headless Chrome + real login) — exit 0
- Non-zero exit = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Both scripts exit 0; the propagation assertion (new) passes

## Gates Satisfied
- FIX-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
