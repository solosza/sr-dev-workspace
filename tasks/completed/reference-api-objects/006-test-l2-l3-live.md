# Test: L2/L3 Live vs Orderly API

## Type
TEST
## Execution
inline
## Dependencies
- 005

## Requirements
- Fresh seed + boot on PORT 8018; real ApiInterface + OrdersApiObject via DI
- L2: each object method against live endpoints; pydantic models validate every real response; last_response behaves per design doc
- L3 flow through the OBJECT: create order → process → process → verify COMPLETE (model-typed) → delete → confirm gone; assert model field values, not just status codes
- SOAP object: import + instantiate only (deferral documented) — NO live SOAP
- Cleanup in finally; env problem → L3-BLOCKED honestly; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] L2 + L3 green through the object layer

## Gates Satisfied
- AO-02, AO-03, AO-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
