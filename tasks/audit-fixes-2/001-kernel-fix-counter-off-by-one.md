# Fix Counter Off-by-One on Block

## Context
Audit gap #4: universal-gate-enforcer.py increments the counter BEFORE checking the limit. When the agent hits action 10, counter becomes 11, then gets blocked. After anchor resets to 0, the blocked action was consumed without executing. True working window is 9, not 10.

## Dependencies
- None

## Requirements
- Read universal-gate-enforcer.py to understand current increment logic
- Move the limit check BEFORE the increment, OR increment only if the action will proceed (not be blocked)
- Alternative: check `actions_since >= actions_limit` (not `>`) so action 10 triggers the block before incrementing to 11
- Preserve all other gate logic (session, learn, anchor checks)

## Acceptance Criteria
- [ ] Counter check happens at the right point — action 10 blocks, counter stays at 10 (not 11)
- [ ] After anchor reset to 0, next action starts at 1 (full 10-action window)
- [ ] All other gates still work (session, learn, anchor)
- [ ] Read the modified function — confirm logic is correct

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
