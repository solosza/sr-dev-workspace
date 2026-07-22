# Test: Sequence-Spy Behavioral Proof (L2)

## Context
Backlog 207: prove the Roles' real job — workflow ORCHESTRATION with self-auth first — by executing real Role code against recording stubs (the mechanism that carried 206).

## Type
TEST
## Execution
inline
## Dependencies
- 003, 004
## Phase Gate
- [ ] ROL-04 green

## Requirements
- Script: recording stubs for CommonTasks and OrderWorkupTasks (journal of (module, method, args)); instantiate `OrderClerk(stub_common, stub_workup, {"username": "clerk", "password": "clerk123"})` and `OrderManager(..., {"username": "manager", "password": "manager123"})` — REAL role code, stub tasks
- Assert for `clerk.work_order_status_change("3", "PROCESSING")`:
  - FIRST journal entry is common.login with ("clerk", "clerk123") — identity flows from the injected dict
  - then workup.open_order("3"), then workup.change_status("PROCESSING"), in order; returns None; no extra calls
- Assert for `manager.cancel_order("3")`:
  - FIRST entry common.login("manager", "manager123"); then open_order("3"); then change_status("CANCELLED"); returns None
- Failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All sequence assertions pass; exit 0

## Gates Satisfied
- ROL-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
