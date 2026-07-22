# Build api_objects/models/ — Pydantic Models

## Context
Backlog 211. READ FIRST (RULE ZERO): (1) design doc `projects/hmsa-qa-platform/02-reference-patterns/api-objects.md` — models/ subfolder conventions; (2) the ACTUAL JSON shapes: `harness/orderly/routes_api_customers.py` + `routes_api_orders.py` docstrings AND a live GET against a booted app (port 8018) — field-exact, do not invent.

## Type
BUILD
## Execution
inline
## Dependencies
- 001

## Requirements
- `framework/_reference/api_objects/models/` with pydantic models for Customer, Order (incl. items), OrderItem — matching Orderly's response fields exactly; follow the design doc's naming/structure conventions
- Package __init__ exports; no domain vocabulary beyond the generic commerce entities themselves (Customer/Order ARE the demo domain — allowed at L2 reference layer per contract; healthcare terms are not)

## Acceptance Criteria
- [ ] Models validate real seeded responses without error

## Gates Satisfied
- AO-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
