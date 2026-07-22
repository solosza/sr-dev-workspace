# Register API Routers in main.py

## Context
Backlog 209. READ FIRST: `harness/orderly/main.py` — it already imports routes via importlib loop over `("routes_customers", "routes_orders")`.

## Type
BUILD
## Execution
inline
## Dependencies
- 002, 003

## Requirements
- Extend the module registration so `routes_api_customers` and `routes_api_orders` are included (extend the existing importlib tuple if the routers attach the same way — READ how the existing modules expose/attach their router and match it exactly)
- API routes must NOT be behind the UI session redirect (if main.py or the routes enforce login redirects, /api/* stays open; document the choice per gate contract)
- App still boots: `uvicorn harness.orderly.main:app` clean

## Acceptance Criteria
- [ ] All /api endpoints reachable on a booted app; UI routes unchanged

## Gates Satisfied
- API-02/03 (wiring)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
