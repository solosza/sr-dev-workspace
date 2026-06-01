# Synthesize: Write Go-to-Market Plan

## Context
Final task. Reads all 5 research documents and writes a single actionable go-to-market plan in `go-to-market-plan.md`. Someone reading only this file should know exactly what to do, in what order, and why.

## Type
BUILD

## Execution
inline

## Dependencies
- 002-market-build-write-readme
- 003-market-research-competitor-analysis
- 004-market-research-supplier-terms
- 005-market-research-platform-decision
- 006-market-research-logistics-duties
- 007-market-research-pricing-model

## Phase Gate
- [ ] `projects/hoi-an-leather/market-analysis.md` exists
- [ ] `projects/hoi-an-leather/supplier-terms.md` exists
- [ ] `projects/hoi-an-leather/platform-decision.md` exists
- [ ] `projects/hoi-an-leather/logistics-fulfillment.md` exists
- [ ] `projects/hoi-an-leather/pricing-strategy.md` exists

## Requirements
- Read all 5 research documents before writing
- Write `projects/hoi-an-leather/go-to-market-plan.md` containing:
  - **Executive Summary** — the opportunity in 3 sentences
  - **Phase 1: Test with Existing Inventory** — specific action items using bags already on hand, no purchase required
  - **Phase 2: First Import Batch** — supplier outreach, spec sheets, 25-unit order, air freight, timeline + cost
  - **Phase 3: Scale** — triggers for scaling (sales velocity, review count), 3PL transition, sea freight
  - **Positioning Statement** — exact words to use in Etsy listings
  - **Key Risks & Mitigations** — consistency at scale, returns, supplier communication
  - **Decision Log** — platform choice, fulfillment path, why

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/go-to-market-plan.md` exists
- [ ] File is > 60 lines
- [ ] Contains "Phase 1" section
- [ ] Contains "Phase 2" section
- [ ] Contains a positioning statement
- [ ] Contains a risks section

## Gates Satisfied
- BUILD-08, FUNC-04, FUNC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
