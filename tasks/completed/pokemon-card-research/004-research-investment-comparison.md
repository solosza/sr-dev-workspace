# Research: Traditional investment comparison

## Context
Compare Pokemon card investing ROI against traditional investment vehicles. Honest, data-driven analysis with risk assessment.

## Type
RESEARCH

## Execution
agent

## Requirements
- Use WebSearch to gather comparison data for investment vehicles
- Compare Pokemon card ROI against:
  - S&P 500 (~10% nominal, ~7% real annual return)
  - Real estate (appreciation + rental income, REITs)
  - Gold / precious metals
  - Crypto (BTC, ETH — high volatility)
  - Other collectibles (sports cards, comic books, vintage toys, wine)
  - Bonds / fixed income
- Assess liquidity risk: can you actually sell Pokemon cards at "market price"? (eBay friction, auction timing)
- Assess counterfeiting risk
- Assess fad/bubble risk: is the current Pokemon market sustainable?
- Provide investment outlook: short-term (1-3yr), medium-term (5-10yr), long-term (10+yr)
- Evaluate Pokemon brand trajectory and its impact on card values

## Acceptance Criteria
- [ ] `projects/pokemon-card-research/04-investment-comparison.md` exists
- [ ] File includes side-by-side ROI comparison table (Pokemon vs at least 5 other vehicles)
- [ ] File includes risk assessment (liquidity, counterfeiting, bubble, tax)
- [ ] File includes short/medium/long-term outlook
- [ ] File provides a clear recommendation with caveats

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
