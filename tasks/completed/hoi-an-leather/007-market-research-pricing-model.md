# Research: Pricing Strategy — Landed Cost Model for 3 SKUs

## Context
Build a landed cost model using duty rates from task 006 and competitor pricing from task 003. Produce retail price recommendations, margin analysis, and break-even calculation for 3 SKUs.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir
- 003-market-research-competitor-analysis
- 006-market-research-logistics-duties

## Phase Gate
- [ ] `projects/hoi-an-leather/market-analysis.md` exists
- [ ] `projects/hoi-an-leather/logistics-fulfillment.md` exists

## Requirements
- Known costs: shoulder bag ~$40 (1M dong), duffel ~$80 (2M dong), tote ~$25 (est.)
- Pull freight-per-unit and duty rates from logistics-fulfillment.md
- Add Etsy platform fees (6.5% + $0.20 + ~3% payment processing)
- Add packaging estimate ($2-4/unit)
- Calculate for each SKU: total landed cost, recommended retail price, gross margin %
- Validate retail prices against competitor pricing from market-analysis.md
- Calculate break-even: units to sell to recover a 25-unit import batch
- Write complete model to `projects/hoi-an-leather/pricing-strategy.md`

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/pricing-strategy.md` exists
- [ ] Contains landed cost table with all cost components for 3 SKUs
- [ ] Contains retail price recommendation for each SKU
- [ ] Contains margin % for each SKU (target: >55%)
- [ ] Contains break-even analysis for 25-unit batch

## Gates Satisfied
- BUILD-07, FUNC-02, DOC-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
