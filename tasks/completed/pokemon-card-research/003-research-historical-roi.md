# Research: Pokemon card historical ROI data

## Context
Gather historical price data on Pokemon card sealed product and graded singles to assess actual investment returns. Focus on data, not hype.

## Type
RESEARCH

## Execution
agent

## Requirements
- Use WebSearch to research Pokemon card price history and investment returns
- Research sealed product appreciation: booster boxes by set/era (WOTC Base Set, Neo, ex, Diamond & Pearl, Sword & Shield, Scarlet & Violet)
- Research graded singles ROI: PSA 10 chase cards (Charizards, trophy cards, modern alt arts)
- Find data on which percentage of product actually appreciates vs depreciates
- Research typical holding periods for meaningful returns
- Document hidden costs: storage, grading fees (PSA/BGS), insurance, transaction fees (eBay ~13%, TCGPlayer fees)
- Note the collectibles tax rate (28% capital gains vs 15-20% for stocks)
- Research market saturation risk: Pokemon Company print run trends

## Acceptance Criteria
- [ ] `projects/pokemon-card-research/03-historical-roi-data.md` exists
- [ ] File includes price appreciation data for at least 5 sets across different eras
- [ ] File includes graded singles ROI examples
- [ ] File includes hidden cost breakdown (grading, storage, fees, taxes)
- [ ] File addresses print run trends and saturation risk

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
