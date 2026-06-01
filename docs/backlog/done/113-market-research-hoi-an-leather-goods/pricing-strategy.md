# Pricing Strategy — Landed Cost Model & Retail Pricing

## Status
NEW

## Known Costs (from trip)
- Shoulder bag: ~$40 USD (1M dong) custom, 1-day turnaround
- Duffel bag: ~$80 USD (2M dong)
- Tote/smaller bag: est. $20-40 USD

## Research Questions
- What do comparable handmade leather shoulder bags sell for on Etsy? (target: $120-200 range?)
- What do comparable duffels sell for? (target: $250-350?)
- What multiplier do premium leather goods brands use? (typically 4-6x landed cost for DTC)
- How does "made in Vietnam, artisan family shop" positioning affect willingness to pay vs "made in Italy"?

## What to Produce
- Landed cost model for 3 SKUs: product cost + freight per unit + import duty + platform fee + packaging
- Retail price recommendation per SKU with margin %
- Break-even analysis: how many units to sell to recover first import batch cost
- Pricing comparison vs Etsy competitors

## Sample Model Structure
| SKU | Product Cost | Freight/unit | Duty | Platform Fee | Total Landed | Retail Price | Margin |
|-----|-------------|-------------|------|-------------|-------------|-------------|--------|
| Shoulder Bag | $40 | $8 | $4 | $12 | $64 | $165 | 61% |
| Duffel | $80 | $12 | $7 | $18 | $117 | $295 | 60% |
| Tote | $25 | $6 | $2 | $9 | $42 | $110 | 62% |

(Numbers are estimates — research should validate)

## Dependencies
- Logistics costs (from logistics-fulfillment)
- Competitor pricing (from market-analysis)
