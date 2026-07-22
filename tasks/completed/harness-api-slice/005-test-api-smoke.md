# Test: API Smoke (L1/L2)

## Context
Backlog 209. Endpoint-by-endpoint verification against a booted app with fresh seed. Pure `requests` — no browser.

## Type
TEST
## Execution
inline
## Dependencies
- 004

## Requirements
- Script: fresh seed (delete db, `python -m harness.orderly.seed`, cwd=target repo), boot uvicorn subprocess, then assert:
  - GET /api/customers → 200, 4 seeded customers, exact field set {id, name, email}
  - GET /api/customers/1 → 200 Alice; GET /api/customers/999 → 404 JSON
  - POST /api/customers valid → 201 + object; missing field → 4xx JSON
  - GET /api/orders → 200, 8 seeded orders; ?status=PENDING filters correctly
  - GET /api/orders/3 → 200 with items array; /999 → 404
  - POST /api/orders → 201 PENDING; POST status invalid transition (e.g., COMPLETE→PROCESSING) → 400 JSON not 500
  - POST /api/orders/{new}/process → PROCESSING; again → COMPLETE; again → 400
  - DELETE new order → 204; re-GET → 404
- Field-set equality (not subset) — API-05 shape stability
- Kill server in finally; failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] All assertions green, exit 0

## Gates Satisfied
- API-02, API-03, API-04, API-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
