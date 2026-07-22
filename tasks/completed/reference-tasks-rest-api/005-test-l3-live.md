# Test: L3 Live vs Orderly

## Type
TEST
## Execution
inline
## Dependencies
- 003, 004

## Requirements
- Fresh seed + boot on PORT 8018; real stack: ApiInterface → OrdersApiObject → OrderManagementTasks (all DI)
- Full flow through the TASK layer per the design doc's dry-run scenario; assert typed returns carry real data
- Cleanup idempotency LIVE: create an order, call the cleanup method twice — first removes, second no-ops, neither raises; order verifiably gone (404 via object)
- Cleanup server in finally; env problem → L3-BLOCKED honestly; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Flow + double-cleanup green through the task layer

## Gates Satisfied
- RT-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
