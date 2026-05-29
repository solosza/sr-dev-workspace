# Research Sales Channels and Pricing for Game Icon Packs

## Context
If there's a gap, the next question is whether there's a viable business. This task researches where indie game asset creators sell icon/emoji packs, what pricing looks like, what revenue is realistically achievable, and how discoverability and distribution work.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 001-market-build-create-project-dir

## Phase Gate
- [ ] `projects/custom-game-emoji-research/` directory exists

## Requirements
Research and document the following using web search (current pricing data required):

1. **itch.io** — how does the game asset marketplace work? Revenue share (itch takes what %?), discoverability (tags, featured, bundles), average sales for mid-tier asset packs, pricing norms for icon sets (100-500 icons)
2. **Gumroad** — how does it compare to itch.io for game assets? Revenue share, audience type, pricing norms
3. **Direct licensing to game devs** — is there a model for licensing icon packs to individual game developers or studios? What's the pricing structure (per-seat, per-project, per-game)?
4. **Game asset bundles** — Humble Bundle, itch.io bundles — how do creators participate? Revenue impact
5. **Pricing norms** — find at least 5 real current prices for indie icon/sprite/emoji packs on itch.io or similar. Range, median, what factors affect price (quantity, exclusivity, license type)
6. **TAM estimate** — how many indie game developers build grid-based/tactical/RPG games? Any data on this segment size?
7. **Subscription model viability** — is there precedent for subscription icon libraries in the indie game space?

Write findings to `projects/custom-game-emoji-research/03-sales-channels-pricing.md` with a channel comparison table and pricing data.

## Acceptance Criteria
- [ ] `projects/custom-game-emoji-research/03-sales-channels-pricing.md` exists
- [ ] File covers at least 3 sales channels (itch.io, Gumroad, direct licensing)
- [ ] File includes concrete price examples (at least 5 real or researched data points)
- [ ] File includes revenue share percentages for each channel
- [ ] File includes a channel comparison table with columns: Channel, Revenue Share, Audience, Discoverability, Best For
- [ ] File has a section estimating realistic revenue potential for a first pack

## Gates Satisfied
- DOC-06, DOC-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
