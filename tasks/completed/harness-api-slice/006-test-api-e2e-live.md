# Test: API E2E Live + UI Unaffected (L3)

## Context
Backlog 209. One realistic business flow over HTTP, plus proof the UI slice didn't regress. No browser needed (UI check = GET renders).

## Type
TEST
## Execution
inline
## Dependencies
- 005

## Requirements
- Fresh seed + boot; `requests.Session()`:
  1. POST /api/customers {"name": "Eve Harper", "email": "eve@example.com"} → id
  2. POST /api/orders {customer_id: <id>, total: 49.99} → order PENDING
  3. GET /api/orders/<oid> → customer_name "Eve Harper", empty items
  4. POST /process → PROCESSING; GET confirms; POST /process → COMPLETE; GET confirms
  5. POST /{oid}/status {"status": "PROCESSING"} → 400 (COMPLETE is terminal)
  6. DELETE → 204; GET → 404
  7. GET /api/orders?status=COMPLETE no longer contains <oid>
- UI unaffected: GET /login → 200 with form markup; GET /orders (unauthed) → redirect to /login (same behavior as before — read main.py to confirm expected code 303/307 and assert that)
- Cleanup in finally; env problem → L3-BLOCKED honestly; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Full flow green; UI behavior byte-consistent with pre-slice

## Gates Satisfied
- API-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
