# Restructure isagawa.co Nav — Products + Games Split

## Status
Open

## Priority
High — nav is the site's spine; adding more pages without restructuring makes it unreadable

## Summary
The current pill-nav has one Products dropdown with 4 items. With job-application and catalog coming, it becomes 6+ items — too many. The fix is to split into Products (enterprise tools) and Games (game harnesses), add a Catalog link, and assess whether Kernel needs its own nav entry. Research the pill-nav.js/css implementation first to determine whether multiple dropdowns require a refactor or just config additions.

## Requirements
- **Research gate (MUST run before any HTML/CSS changes):**
  - Read `pill-nav.js` and `pill-nav.css` in full
  - Determine: does the current implementation support multiple independent dropdowns, or is it hardcoded for one?
  - If refactor required: scope the change before implementing
- **Proposed final nav structure:**
  - `Home` (→ index.html)
  - `Feed` (→ feed.html)
  - `Products ▾` dropdown: Attestation, QA Platforms, SSH Compliance, Vibe Coder, Job Application
  - `Games ▾` dropdown: DnD Game Engine, Football Coach Sim, Terminal Game Builder
  - `Catalog` (→ catalog.html, flat link — no dropdown)
  - `The Story` (→ story.html)
- Kernel either gets a nav entry (→ Kernel page, if one exists) or remains the homepage link (ISAGAWA logo)
- Nav update applied consistently across ALL pages: index.html, feed.html, story.html, attestation.html, qa-platforms.html, ssh-compliance.html, vibe-coder.html, job-application.html (110), catalog.html (111)
- Mobile behavior preserved (pill-nav collapses on ≤767px)

## References
- `D:/my_ai_projects/isagawa-co.github.io/pill-nav.js` — current dropdown implementation
- `D:/my_ai_projects/isagawa-co.github.io/pill-nav.css` — current dropdown styles
- Related backlog: 110-market-build-job-application-product-page.md
- Related backlog: 111-market-build-spec-catalog-page.md
- Depends on: 110 and 111 should be complete before this ships (so all 9 pages are updated in one pass)

## Task Builder Input
- **Deliverable:** Updated `pill-nav.js` + `pill-nav.css` supporting multiple dropdowns, nav HTML updated in all pages
- **Location:** `new-repo:D:\my_ai_projects\isagawa-co.github.io`
- **Scope:** BUILD (research gate required before implementation tasks)
- **Constraints:** Research pill-nav.js/css before writing any tasks. If multi-dropdown requires refactor, add refactor task before build tasks. Ideally runs after 110 and 111 are merged so all pages are updated in one pass. All changes on a feature branch.
