# Test: L2 Primitives + Negative Path

## Type
TEST
## Execution
inline
## Dependencies
- 003

## Requirements
- Boot Orderly on PORT 8018 (fresh seed, cwd=target repo); construct ApiInterface with a real requests.Session
- Each verb against live endpoints (canonical slash paths — 209 flag): GET /api/customers/ (list), POST /api/customers/ (create), GET single, DELETE an order you create, POST status/process; assert ApiResponse.status correct, body parsed JSON, response_time > 0
- NEGATIVE PATH (AIF-04): ApiInterface pointed at an unbound port (e.g., 127.0.0.1:1) → assert the requests exception PROPAGATES to the test (pytest.raises / try-assert) AND a log line was emitted before the raise
- Kill server in finally; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All verb + negative-path assertions green

## Gates Satisfied
- AIF-04, AIF-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
