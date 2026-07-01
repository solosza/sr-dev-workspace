# Research: Pokemon card retail acquisition landscape

## Context
Research which retailers sell Pokemon TCG sealed product at MSRP online, their restock patterns, how quickly high-demand sets sell out, and the markup difference between retail and secondary market.

## Type
RESEARCH

## Execution
agent

## Requirements
- Use WebSearch to research: Pokemon Center, Target, Walmart, Best Buy, GameStop, Costco online Pokemon card availability
- Identify which retailers currently sell Pokemon booster boxes, ETBs, and special sets at MSRP
- Research typical restock patterns and schedules (day of week, time, frequency)
- Find data on sellout speeds for high-demand sets (e.g., Prismatic Evolutions, Surging Sparks)
- Calculate typical markup: retail MSRP vs eBay/TCGPlayer secondary market prices
- Document any purchase limits retailers impose

## Acceptance Criteria
- [ ] `projects/pokemon-card-research/01-retail-landscape.md` exists
- [ ] File covers at least 4 major retailers with MSRP availability info
- [ ] File includes restock pattern data (frequency, timing)
- [ ] File includes retail vs secondary market price comparison for at least 3 recent sets

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
