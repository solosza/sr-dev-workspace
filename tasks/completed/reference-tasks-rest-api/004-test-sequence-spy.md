# Test: Sequence-Spy Behavioral Proof

## Type
TEST
## Execution
inline
## Dependencies
- 002

## Requirements
- Recording stub mirroring OrdersApiObject's REAL fluent API (read it — stub must return self on operations and canned values on get_last_*); instantiate the real Task with the stub
- Assert per method: documented call order, args pass-through, TYPED value returned to caller (the REST-tasks difference from browser tasks); cleanup method: stub "absent" → no delete call issued; stub "present" → delete called once
- Failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All sequence + typed-return assertions green

## Gates Satisfied
- RT-05, RT-03 (behavioral half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
