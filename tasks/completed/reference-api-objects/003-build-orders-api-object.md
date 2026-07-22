# Build orders_api_object.py

## Context
Backlog 211. THE canonical L2 REST exemplar. READ FIRST: api-objects.md's canonical example — copy its structure EXACTLY (constructor shape, last_response convention, method naming, return types). The design doc governs; where it and this task disagree, the design doc wins.

## Type
BUILD
## Execution
inline
## Dependencies
- 002

## Requirements
- `framework/_reference/api_objects/orders_api_object.py`: constructor takes ApiInterface via DI (plus whatever the design doc's canonical adds); endpoint paths owned here as constants — SLASH-CANONICAL (`/api/orders/`, 209 flag); last_response convention per doc; methods per doc's canonical (list/get/create/change status/process/delete shapes) returning models or self exactly as the doc prescribes
- Also `customers_api_object.py` ONLY if the design doc's canonical set includes it — otherwise Orders only (don't pad scope)
- No try/except; no interface construction; match _reference import style

## Acceptance Criteria
- [ ] Structure byte-faithful to the design doc canonical; imports clean

## Gates Satisfied
- AO-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
