# Build /api/customers Routes

## Context
Backlog 209. READ FIRST: `harness/orderly/routes_customers.py` + `db.py` (match their idiom — plain FastAPI + SQLAlchemy Core; harness code, NOT contract code) and `projects/hmsa-qa-platform/04-test-harness/data-model.md` (Customer fields).

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File: `harness/orderly/routes_api_customers.py` — APIRouter with prefix `/api/customers`:
  - GET `/` → JSON list of customers `{id, name, email}`
  - GET `/{customer_id}` → one customer or 404 JSON `{detail}`
  - POST `/` → create from JSON body `{name, email}` → 201 with created object (validate presence → 422/400 JSON on missing)
- Same tables via db.py — no parallel data layer
- Docstring at top listing the JSON shapes (API-05 stability contract)
- Generic commerce vocabulary only

## Acceptance Criteria
- [ ] Router imports cleanly; shapes documented

## Gates Satisfied
- API-02 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
