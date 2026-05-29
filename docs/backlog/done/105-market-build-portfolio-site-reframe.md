# Build Solo-Founder Velocity Landing Page

## Status
Open

## Priority
High — the feed is the most convincing asset on the site, but the homepage buries it under a breadth list that reads as unfocused to a buyer. The story is already there; the framing isn't.

## Summary
A standalone landing page at `isagawa.co/story.html` (or similar) that tells the solo-founder-velocity thesis without touching the existing agent factory homepage. The existing site stays intact — this page gets shared directly to specific audiences (hiring managers, consulting prospects, collaborators). Visitors who want depth can traverse the full site from there. Non-destructive, targeted, testable.

**Phase 1 (RESEARCH):** Validate the message against how the market actually talks about agentic engineering, solo founders, and AI developer portfolios. Confirm the thesis is differentiated, not noise.

**Phase 2 (BUILD):** Build the landing page using the validated message, matching homepage scroll dynamics exactly.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[105-market-build-portfolio-site-reframe/conversation-origin]] | The verbatim conversation that produced this backlog — intent chain source of truth |
| [[105-market-build-portfolio-site-reframe/message-research]] | Web research to validate solo-founder-velocity thesis before building |
| [[105-market-build-portfolio-site-reframe/page-spec]] | Page structure, scroll mechanics, and implementation spec |

## The Proposed Framing (to be validated by research)
> "Not 'I built an agent factory' — everyone says that. It's 'I drop a sentence in a backlog and get an attested, mostly-finished project out, and here are 73 signed runs showing it.' The proof is the product. The completion percentage backed by Rekor is the claim no competitor can make casually because they'd have to produce the same evidence trail and they don't have one."

> "You're producing at a level that normally requires a small team, and the system itself is the multiplier. That's the actual story."

> "Most portfolios assert competence; yours evidences it cryptographically. I haven't seen another solo portfolio do that."

## Out of Scope
- Any changes to the existing homepage or agent factory theme
- Completion-percentage tracking (separate backlog item — kernel enhancement)
- Job application positioning or resume work

## References
- Portfolio site: `D:\my_ai_projects\isagawa-co.github.io`
- Feed: `https://www.isagawa.co/feed.html`
- Attestation page: `https://www.isagawa.co/attestation.html`
- Pipeline 101: `docs/backlog/done/101-market-fix-portfolio-feed-server-render.md`

## Task Builder Input
- **Deliverable:** (1) Research report confirming/refining the message; (2) New standalone page at `isagawa-co.github.io/story.html` built on validated message, with embedded feed entries and homepage scroll dynamics
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Research runs before any HTML is written; page is additive only (no changes to existing pages); must use `styles.css` from the existing site; feed embed server-rendered (pipeline 101 pattern); scroll animations mirror homepage exactly (see page-spec sub-doc)
