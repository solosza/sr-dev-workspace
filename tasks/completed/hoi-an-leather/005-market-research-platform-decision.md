# Research: Platform Decision — Etsy vs Shopify

## Context
Research where to sell. Etsy vs Shopify comparison for handmade leather goods targeting US buyers. Incorporate competitor platform data from task 003. Output is `platform-decision.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir
- 003-market-research-competitor-analysis

## Phase Gate
- [ ] `projects/hoi-an-leather/` directory exists
- [ ] `projects/hoi-an-leather/market-analysis.md` exists

## Requirements
- Research Etsy fees: listing ($0.20), transaction (6.5%), payment processing (~3%), offsite ads
- Research Shopify fees: plan cost, payment processing, no per-listing fee
- Confirm Etsy Production Partner policy — does commissioning goods from an overseas workshop qualify as "handmade"? Cite policy source.
- Research time-to-first-sale: organic Etsy traffic vs cold Shopify
- Confirm Etsy + Shopify can run simultaneously
- Name a recommended starting platform with clear rationale
- Write fee comparison table + recommendation to `projects/hoi-an-leather/platform-decision.md`

## Acceptance Criteria
- [ ] `projects/hoi-an-leather/platform-decision.md` exists
- [ ] Contains fee comparison table (Etsy vs Shopify)
- [ ] Contains Etsy Production Partner policy section
- [ ] Names a recommended starting platform with rationale
- [ ] Addresses running both simultaneously

## Gates Satisfied
- BUILD-05, DOC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
