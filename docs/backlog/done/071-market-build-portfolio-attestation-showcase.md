# Build Portfolio Showcase — Attestation Pipeline

## Status
Open

## Priority
High — the attestation pipeline is the most differentiated product in the portfolio; no other AI agent system has cryptographic proof of work. This is the trust layer.

## Summary
Build a product showcase page for the agent-attestation-spec on isagawa.co. The page presents attestation as its own product: a drop-in spec that gives any AI coding agent cryptographic proof of every pipeline run. No private keys, no infrastructure — just Sigstore. The "built by the loop" message leads (this product was produced by the same factory that produced everything else on the site), then the product stands on its own merits.

## Framing

### Up front — built by the loop
This product was produced from a domain spec, decomposed into tasks, executed autonomously, and signed with Sigstore — by the same system described on the homepage. One sentence, one link back to the main site's Self-Extension section. Then move on to the product.

### The product — what it does for YOU
- **You tell your AI agent to build something. It says "done." But how do you know?**
- Drop in the attestation spec. Every pipeline run now produces tamper-evident proof: what was requested (intent chain), what was produced (artifact hashes), who attested (Sigstore OIDC), when it happened (Rekor transparency log).
- Works with any AI coding agent. No key management. No infrastructure.

### Target users
- Solo developers using AI agents who want accountability
- Teams adopting coding agents who need audit trails
- Enterprises in regulated industries (SOC2, HIPAA) needing agent compliance

## Requirements

### Content Sections
- **Built by the loop** — one line + link establishing this came from the factory
- **Hero:** "Prove your AI agent did what it said it did." + terminal showing attestation bundle output
- **Problem:** AI agents produce work with no audit trail, no proof of who/what/when. You trust the output because you have no choice.
- **How it works:** Flow diagram — agent work → hash collection → bundle creation → Sigstore signing → Rekor log. Each step explained in plain terms.
- **What's in a bundle:** Annotated JSON showing intent chain, artifact hashes, timestamps, Rekor entry
- **Drop-in setup:** 3 steps — install sigstore, copy lib/, run `python lib/attest.py`. That's it.
- **Demo:** Embedded terminal or GIF showing `--dry-run` attestation with real bundle output
- **Tech stack:** Sigstore, Rekor, OIDC, Python, SHA-256 — badges
- **Results:** Live count from feed page (links to 075's feed), verification success rate, time per attestation

### Design Constraints
- Match existing isagawa.co visual language (dark theme, terminal aesthetic)
- Mobile responsive
- Static (GitHub Pages compatible)
- **Feature branch:** `feature/showcase-attestation` in `isagawa-co.github.io` repo. Do not merge to main until user approves.
- Links back to main site Self-Extension section and to the live feed page (from 075)

### Reference Designs
- Linear.app case studies (clean developer storytelling)
- Vercel customer showcases (technical depth + visual polish)
- Stripe developer docs (architecture diagrams)

## References
- Portfolio site (live): `D:\my_ai_projects\isagawa-co.github.io` (deploys to www.isagawa.co)
- Agent attestation spec: `D:\my_ai_projects\agent-attestation-spec`
- Attestation spec README: `D:\my_ai_projects\agent-attestation-spec\README.md`
- Attestation spec SKILL.md: `D:\my_ai_projects\agent-attestation-spec\SKILL.md`
- Attestation architecture: `D:\my_ai_projects\agent-attestation-spec\docs\architecture.md`
- Live feed page: backlog [075](075-market-build-portfolio-live-feed-update.md) (ships first)
- Portfolio visual refactor: backlog [053](done/053-market-refactor-portfolio-site-visual-layer.md) (done)
- Website cloner skill: `.claude/skills/website-cloner/`

## Task Builder Input
- **Deliverable:** Attestation pipeline showcase page on isagawa.co — product page with "built by the loop" lead-in, hero, problem, how-it-works flow, bundle anatomy, setup steps, demo, results. On feature branch `feature/showcase-attestation`.
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Feature branch only — do not merge to main. Must match existing dark theme terminal aesthetic. Static HTML/CSS (GitHub Pages). Content written from attestation spec's README.md, SKILL.md, and architecture.md. Product-first framing — the attestation spec is its own product, not just a kernel feature.
