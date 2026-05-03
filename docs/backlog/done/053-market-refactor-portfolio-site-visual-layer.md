# Portfolio Site Visual Layer Refactor (2nd Iteration)

## Status
Open

## Priority
High — site is live but reads as unstyled white-on-black; visual layer never landed because Shader canvas-rendered typography defaulted to 16px/400

## Summary
The portfolio site at `D:\my_ai_projects\isagawa-portfolio-site` has correct copy and structure but no visual hierarchy. The Suero structural extraction worked. The Shader aesthetic extraction came back thin. This refactor applies 14 targeted CSS-and-HTML changes to land the visual layer: typography hierarchy, bold emphasis, whitespace, texture, card interactivity, tag labels, stat consistency, chain list climax, provenance upgrade, nav fix, CTA polish, footer redesign, and em dash cleanup.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[053-market-refactor-portfolio-site-visual-layer/typography-hierarchy]] | Hero, section, card, body type scale with clamp() |
| [[053-market-refactor-portfolio-site-visual-layer/bold-emphasis]] | Suero-derived bold word pattern inside prose |
| [[053-market-refactor-portfolio-site-visual-layer/anchor-numbers]] | Massive translucent section number treatment |
| [[053-market-refactor-portfolio-site-visual-layer/whitespace]] | Section padding, narrative width, CTA spacing |
| [[053-market-refactor-portfolio-site-visual-layer/visual-texture]] | Radial gradient background + grain overlay |
| [[053-market-refactor-portfolio-site-visual-layer/card-interactivity]] | Hover depth, shadow, border transitions |
| [[053-market-refactor-portfolio-site-visual-layer/tag-lists]] | Suero-derived category tags above card titles |
| [[053-market-refactor-portfolio-site-visual-layer/stat-consistency]] | Missing stats for Workspaces, Cloner, Attestation |
| [[053-market-refactor-portfolio-site-visual-layer/chain-list]] | This Page climax list + closing line treatment |
| [[053-market-refactor-portfolio-site-visual-layer/provenance-upgrade]] | Third attestation card (#047), badge pulse, subtitle |
| [[053-market-refactor-portfolio-site-visual-layer/navigation]] | This Page nav link, logo spacing, underline hover |
| [[053-market-refactor-portfolio-site-visual-layer/hero-cta]] | Button sizing, arrow rotation, scroll caption |
| [[053-market-refactor-portfolio-site-visual-layer/footer-redesign]] | Shader-derived 4-column footer with Rekor links |
| [[053-market-refactor-portfolio-site-visual-layer/em-dash-cleanup]] | Replace all em dashes with natural punctuation |

## Reference Sites

- Suero: https://www.ethansuero.com/ (bold emphasis, all-caps labels, numbered sections, tag lists)
- Shader: https://www.shader.se/ (dark surface, typographic weight, generous margins, dense footer)

## Requirements
- CSS-and-HTML-only changes, no JS libraries
- No new fonts beyond STIX Two Text serif + existing mono stack
- No images or external assets (grain is inline SVG)
- Existing CSS `:root` variable architecture stays intact
- Do not change section structure, four-anchor framework, attestation card JS, or existing IDs
- Use CSS `clamp()` for fluid typography
- Test responsive at 1920px, 1400px, 991px, 767px, 479px
- Remove conflicting media query overrides that fight clamp()

## References
- Pipeline #047 (portfolio site build): `docs/backlog/done/047-market-build-portfolio-site-loop-theme.md`
- Attestation bundle #047: `.claude/state/attestations/047-20260426T071022Z.json` (Rekor #1387966928)
- Extraction data: `D:\my_ai_projects\isagawa-portfolio-site\extraction\` (13 files, 122 token categories)
- Signed pipelines: #046, #047, #050, #051, #052 (5 total)

## Task Builder Input
- **Deliverable:** Visually polished `index.html` + `styles.css` with all 14 refactor items applied
- **Location:** `new-repo:D:\my_ai_projects\isagawa-portfolio-site`
- **Scope:** REFACTOR
- **Constraints:** Two files only (styles.css, index.html). No new dependencies. Must preserve all existing JS (bundle viewer, mobile nav, Rekor verification). Sign artifacts via attestation pipeline after completion.
