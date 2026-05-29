# Fix: Unified Nav Across All Site Pages

## Status
Open

## Priority
High — inconsistent nav across pages signals "unfinished" to any visitor who clicks around

## Summary
Each page on isagawa.co has a different nav. Home lists 8+ items. attestation.html shows only Home/Feed. ssh-compliance.html shows Home/Feed/Attestation. qa-platforms.html omits itself. A visitor clicking between pages hits a different, thinner menu each time — this is the primary "feels cheap" signal AJ picked up, not the color. Unify nav across all pages. Depends on backlog 106 (research) to know the final nav structure.

## Requirements
- All pages share the same nav HTML structure after 106 is resolved
- Nav must include: logo link (→ index.html), primary section links, collapsed products group (per 106 recommendation), attested counter
- story.html nav needs the same treatment (currently has its own bespoke nav)
- Mobile hamburger behavior consistent across all pages
- "Active" state (or none) handled consistently

## Pages to Update
- `index.html` — home (source of truth nav)
- `attestation.html`
- `feed.html`
- `qa-platforms.html`
- `ssh-compliance.html`
- `vibe-coder.html`
- `story.html`

## References
- Backlog 106 (research) — gates the final nav item list
- `D:\my_ai_projects\isagawa-co.github.io\styles.css` — nav CSS
- AJ feedback: nav inconsistency registered as "cheap" perception

## Task Builder Input
- **Deliverable:** All 7 pages updated with unified nav; `styles.css` updated if nav CSS changes needed
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD
- **Constraints:** Vanilla JS + CSS only; no framework; must not break existing section anchor links on index.html; depends on 106 research completing first
