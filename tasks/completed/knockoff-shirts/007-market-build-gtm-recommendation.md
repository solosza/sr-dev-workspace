# Build: Go-to-Market Recommendation

## Context
Synthesize all 5 research documents into a single actionable go-to-market recommendation. This is the final deliverable — a clear recommended path with risk rating, starting steps, and decision points the user must make. Output: `projects/hoi-an-knockoff-shirts/gtm-recommendation.md`.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-research-market-analysis
- 003-market-research-sourcing-suppliers
- 004-market-research-legal-compliance
- 005-market-research-logistics-fulfillment
- 006-market-research-pricing-strategy

## Phase Gate
- [ ] `projects/hoi-an-knockoff-shirts/market-analysis.md` exists
- [ ] `projects/hoi-an-knockoff-shirts/sourcing-suppliers.md` exists
- [ ] `projects/hoi-an-knockoff-shirts/legal-compliance.md` exists
- [ ] `projects/hoi-an-knockoff-shirts/logistics-fulfillment.md` exists
- [ ] `projects/hoi-an-knockoff-shirts/pricing-strategy.md` exists

## Requirements
- Read all 5 research documents before writing
- State the recommended path clearly (replica underground / inspired-by / private label) with risk rating
- For the recommended path: list the first 5 concrete actions to start (supplier contact, platform setup, sample order, etc.)
- For the non-recommended paths: state why they are rejected (risk too high, margin too low, etc.)
- Include a decision log: what the user must decide that the research cannot decide for them (risk tolerance, capital available, target volume)
- Include a 90-day launch outline: what to do in the first 3 months

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/gtm-recommendation.md` exists
- [ ] File contains a recommended path with explicit risk rating
- [ ] File contains first 5 concrete launch actions
- [ ] File contains rationale for rejected paths
- [ ] File contains a decisions-required list (what only the user can decide)
- [ ] File contains a 90-day launch outline
- [ ] `grep -qi "recommend\|path\|go-to-market" projects/hoi-an-knockoff-shirts/gtm-recommendation.md` passes

## Gates Satisfied
- DOC-13, DOC-14

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
