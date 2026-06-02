# Research: Pricing Strategy — Landed Cost and Margin Model

## Context
Produce a landed cost model and retail pricing structure for T-shirts and hoodies at 12, 36, and 72 unit batches. This uses the logistics cost data from task 005 and sourcing cost data from task 003. Output: `projects/hoi-an-knockoff-shirts/pricing-strategy.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-knockoff-shirts/` directory exists

## Requirements
- Research realistic per-unit product cost from China suppliers for a replica T-shirt and hoodie at 12, 36, and 72 unit quantities
- Build landed cost model: product cost + freight (per unit at each batch size) + import duty + platform fee + packaging
- Research platform fee structures: Depop (~10%), eBay (~13.25% + $0.30), Poshmark, TikTok Shop
- Calculate retail price at 50%, 60%, and 70% gross margin targets for each SKU
- Compare replica branded vs private label (blank premium tee from Bella+Canvas/AS Colour + custom printing) — what is the cost delta and margin profile?
- Calculate break-even unit count to recover initial sourcing + setup investment (assume $500-1000 sample/setup cost)

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/pricing-strategy.md` exists
- [ ] File contains a landed cost model table (product + freight + duty + fees)
- [ ] File contains per-unit cost at 12, 36, and 72 unit batches for both T-shirt and hoodie
- [ ] File contains retail price recommendations at 3 margin targets
- [ ] File contains a replica vs private label cost comparison
- [ ] File contains break-even analysis
- [ ] `grep -qi "landed cost" projects/hoi-an-knockoff-shirts/pricing-strategy.md` passes

## Gates Satisfied
- DOC-11, DOC-12

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
