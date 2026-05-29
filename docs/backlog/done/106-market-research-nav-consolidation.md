# Research: Nav Consolidation Patterns for isagawa.co

## Status
Open

## Priority
High — home page nav has too many items; adding story.html makes it worse; research gates the build

## Summary
The home page nav currently lists 8+ items flat: section anchors (Seed/Growth/Self-Extension), Feed, Attestation, QA Platforms, SSH Compliance, Vibe Coder, story.html, plus the attested counter. It will keep growing as more products ship. Research best-practice patterns for collapsing product links into an overflow/ellipsis menu or grouped dropdown — monochrome, minimal, consistent with the existing aesthetic — before building.

## Research Questions
- What are the leading patterns for nav overflow on portfolio/product sites? (ellipsis menu, mega menu, grouped dropdown, "More ↓", tab-overflow scroll)
- How do Linear, Vercel, Stripe, and similar monochrome sites handle many nav items without visual bloat?
- What is the right split between primary nav items (always visible) vs secondary/products (collapsed)?
- Does a "Products" or "Work" dropdown pattern preserve the hub-spoke architecture (factory → products) better than flat overflow?
- Mobile behavior: how does the collapsed nav interact with the existing hamburger menu?
- Any accessibility constraints on dropdown/overflow nav patterns?

## References
- `D:\my_ai_projects\isagawa-co.github.io\index.html` — current nav (home page)
- `D:\my_ai_projects\isagawa-co.github.io\styles.css` — existing nav CSS
- Backlog 107: fix nav consistency across pages (depends on research finding)
- Backlog 108: hub-spoke relationship visibility (may inform nav grouping)
- AJ feedback: flat nav reads as "too many things" to a cold visitor

## Task Builder Input
- **Deliverable:** `projects/nav-consolidation-research/research-report.md` — pattern analysis + recommendation for which nav pattern to implement, with annotated examples and implementation sketch
- **Location:** `subproject:nav-consolidation-research`
- **Scope:** RESEARCH
- **Constraints:** Must stay consistent with existing monochrome aesthetic; no JS framework; vanilla JS + CSS only; recommendation must specify exact nav items to keep visible vs collapse
