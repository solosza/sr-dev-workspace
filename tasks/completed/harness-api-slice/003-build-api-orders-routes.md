# Build /api/orders Routes

## Context
Backlog 209. READ FIRST: `harness/orderly/routes_orders.py` + `db.py` (idiom + existing status logic) and `data-model.md` (statuses PENDING→PROCESSING→COMPLETE/CANCELLED, Order/OrderItem fields).

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- File: `harness/orderly/routes_api_orders.py` — APIRouter prefix `/api/orders`:
  - GET `/` → JSON list `{id, customer_id, customer_name, status, total}`; optional `?status=` filter (same semantics as the UI filter)
  - GET `/{order_id}` → order + `items: [{id, product_name, qty, price}]` or 404
  - POST `/` → create `{customer_id, total}` → 201, status starts PENDING
  - POST `/{order_id}/status` body `{status}` → apply with the SAME transition rules the UI enforces (read routes_orders.py for them; if the UI enforces none, data-model.md rules govern: PENDING→PROCESSING→COMPLETE|CANCELLED, PENDING→CANCELLED; invalid → 400 JSON, never 500)
  - DELETE `/{order_id}` → 204 (matches UI delete semantics)
  - POST `/{order_id}/process` → advance one step along PENDING→PROCESSING→COMPLETE; on COMPLETE/CANCELLED → 400 JSON
- Docstring listing all JSON shapes; generic commerce only

## Acceptance Criteria
- [ ] Router imports cleanly; transition rules explicit in code; shapes documented

## Gates Satisfied
- API-03, API-04 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
