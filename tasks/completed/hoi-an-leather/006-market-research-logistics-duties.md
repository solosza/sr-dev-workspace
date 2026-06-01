# Research: Logistics & Import Duties — Freight, Duties, 3PL

## Context
Research the import and fulfillment logistics for bringing leather goods from Da Nang to US customers. Cover HTS duty rates, air freight costs, de minimis rules, and 3PL options for low-volume artisan goods.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-leather/` directory exists

## Requirements
- Research HTS Chapter 42 duty rates for: handbags (4202.21), shoulder bags (4202.22), travel bags/duffels (4202.12)
- Research air freight cost: 10-unit and 25-unit batch from Da Nang (SGN) via DHL/FedEx International
- Determine at what volume sea freight becomes viable vs air
- Research de minimis rule ($800 threshold) — is per-shipment splitting viable for small batches?
- Research 3PL options for <100 orders/month: ShipBob minimums, Shipmonk minimums, self-fulfillment from home viability
- Recommend Phase 1 fulfillment path (use existing inventory, no import yet)
- Recommend Phase 2 fulfillment path (first 25-unit import)
- Write to `projects/hoi-an-leather/logistics-fulfillment.md`

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/logistics-fulfillment.md` exists
- [ ] Contains HTS duty rates for at least 2 bag types
- [ ] Contains air freight estimate for 25-unit batch
- [ ] Contains 3PL comparison with at least 2 options
- [ ] Contains Phase 1 and Phase 2 fulfillment recommendations

## Gates Satisfied
- BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
