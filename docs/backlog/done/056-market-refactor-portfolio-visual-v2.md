# Visual Refactor: Portfolio Site V2 (Final Polish)

## Status
Open

## Priority
High — site is live on www.isagawa.co, these are the final visual refinements before sharing publicly

## Summary
Apply 14 visual refinements to the portfolio site (isagawa-portfolio-site-v2). This is the "final change list" covering typography hierarchy, bold word emphasis, section numbers, whitespace, texture, card interactivity, tag lists, stat numbers, chain list styling, provenance section, navigation, hero CTA, footer redesign, and em dash cleanup. All changes target `index.html` and its embedded CSS/JS.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[056-market-refactor-portfolio-visual-v2/typography-hierarchy]] | Font sizes, weights, letter-spacing, gradients for all heading levels |
| [[056-market-refactor-portfolio-visual-v2/bold-emphasis]] | Suero-pattern bold word emphasis in narrative paragraphs |
| [[056-market-refactor-portfolio-visual-v2/section-numbers]] | Anchor section number sizing, color, opacity, font |
| [[056-market-refactor-portfolio-visual-v2/whitespace-texture]] | Compositional padding, max-widths, background gradients, grain overlay |
| [[056-market-refactor-portfolio-visual-v2/cards-interactivity]] | Card hover effects, depth, tag lists above titles |
| [[056-market-refactor-portfolio-visual-v2/stat-numbers]] | Missing stat values for Growth and Self-Extension cards |
| [[056-market-refactor-portfolio-visual-v2/this-page-chain]] | Chain list styling, closing line, left border treatment |
| [[056-market-refactor-portfolio-visual-v2/provenance-section]] | Third attestation card, badge pulse, 3-column grid |
| [[056-market-refactor-portfolio-visual-v2/navigation-footer]] | Nav link hover animation, footer 4-column redesign |
| [[056-market-refactor-portfolio-visual-v2/hero-cta]] | CTA padding, arrow rotation, scroll caption |
| [[056-market-refactor-portfolio-visual-v2/em-dash-cleanup]] | Replace all em dashes with natural punctuation (14 instances) |

## Requirements
- All changes apply to `D:\my_ai_projects\isagawa-portfolio-site-v2\index.html`
- Must also push to `D:\my_ai_projects\isagawa-co.github.io\index.html` (GitHub Pages)
- No em dashes in any user-facing copy
- Responsive: all sizing uses clamp() for fluid scaling
- No new dependencies (pure CSS/HTML/JS)

## References
- Source: `D:\my_ai_projects\isagawa-portfolio-site-v2\index.html`
- Deploy: `D:\my_ai_projects\isagawa-co.github.io\`
- Prior: `docs/backlog/done/053-market-refactor-portfolio-site-visual-layer.md`
- Prior: `docs/backlog/done/055-market-build-portfolio-site-v2-terminal.md`

## Task Builder Input
- **Deliverable:** Updated `index.html` with all 14 visual refinements applied and pushed to GitHub Pages
- **Location:** `new-repo:D:\my_ai_projects\isagawa-portfolio-site-v2`
- **Scope:** BUILD
- **Constraints:** Single-file site (index.html). Changes are CSS + HTML + minimal JS. Must deploy to isagawa-co.github.io after. No em dashes anywhere.
