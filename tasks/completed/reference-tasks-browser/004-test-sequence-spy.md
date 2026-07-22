# Test: Sequence-Spy Behavioral Proof (L2)

## Context
Backlog 206: Tasks are click-centric and the selenium stack currently drops post-navigation clicks (lessons #41/#42) — so the Task layer's real job (correct ORCHESTRATION of page calls) is proven by execution against recording stubs. This is a behavioral gate, not a mock formality.

## Type
TEST
## Execution
inline
## Dependencies
- 002
## Phase Gate
- [ ] TSK-03 (semantics) green

## Requirements
- Script: define recording stub classes exposing the SAME method names as the real OrdersPage/OrderDetailPage (read the real pages first — stub must mirror actual API); each method appends `(object, method, args)` to a shared journal and returns self (fluent)
- Instantiate `OrderWorkupTasks(stub_orders_page, stub_detail_page)` — real Task code, stub pages
- Execute and assert:
  - `open_order("3")` → journal shows navigation call(s) then locate/open-detail call(s), in order, with "3" passed through; returns None
  - `change_status("PROCESSING")` → selection call then submission call, in order, "PROCESSING" passed through; returns None
  - `capture_order_id()` → exactly the detail-page read call; returns the stub's string
  - No unexpected extra calls in the journal
- Failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All sequence assertions pass; script exits 0

## Gates Satisfied
- TSK-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
