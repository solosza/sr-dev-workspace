# Research: Legal & Compliance — Trademark Risk and Private Label Path

## Context
This is the GATING document for the entire project. The sourcing approach, platform selection, and sales strategy all depend on which risk tier the user chooses. Must produce a clear risk rating per tier and fully scope the private label alternative. Output: `projects/hoi-an-knockoff-shirts/legal-compliance.md`.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/hoi-an-knockoff-shirts/` directory exists

## Requirements
- Research US trademark law exposure for importing + reselling replica goods (Lanham Act, Customs seizure rates, civil vs criminal thresholds)
- Identify the volume threshold where commercial infringement risk escalates (common heuristic: $1K+ commercial import value triggers Customs scrutiny)
- Research platform policies for each relevant channel: Etsy, eBay, Depop, Poshmark, TikTok Shop — what is banned, how enforcement works, account ban rates
- Research the "inspired by" / private label defense — what is legally defensible vs not
- Scope the private label path: what it costs to launch an original streetwear brand that captures the same aesthetic demand (blank premium tees from Bella+Canvas or AS Colour, custom graphics/labels, Shopify store)
- Produce a risk spectrum table: replica branded → inspired-by → private label — risk rating, platform availability, margin profile at each tier

## Acceptance Criteria
- [ ] `projects/hoi-an-knockoff-shirts/legal-compliance.md` exists
- [ ] File contains a risk spectrum table with at least 3 tiers
- [ ] File contains a platform policy matrix (which platforms ban replicas and how they enforce)
- [ ] File contains private label path scoping (what it takes + estimated cost to launch)
- [ ] File contains a go/no-go risk recommendation
- [ ] `grep -qi "risk" projects/hoi-an-knockoff-shirts/legal-compliance.md` passes
- [ ] `grep -qi "private label" projects/hoi-an-knockoff-shirts/legal-compliance.md` passes

## Gates Satisfied
- DOC-06, DOC-07, DOC-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
