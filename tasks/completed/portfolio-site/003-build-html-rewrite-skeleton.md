# Rewrite HTML Skeleton

## Context
Complete rewrite of `index.html` to implement the new 4-anchor-moment narrative structure. The old site had 9 technical sections (Architecture, Kernel, Factory, etc.). The new site has: Nav → Hero → Seed → Growth → Self-Extension → This Page → Provenance → Footer. This task writes the skeleton with empty section stubs.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-css-strip-old-sections

## Phase Gate
- [ ] Old section CSS removed from `styles.css`

## Requirements
- Rewrite `D:\my_ai_projects\isagawa-portfolio-site\index.html` completely
- DOCTYPE, html lang="en", head with charset, viewport, title "Isagawa — Conversational Agent Factory", link to styles.css
- Nav: `ISAGAWA` wordmark + links to `#seed`, `#growth`, `#self-extension`, `#provenance` + hamburger button
- Section stubs with IDs: `hero`, `seed`, `growth`, `self-extension`, `this-page`, `provenance`
- Footer stub
- Each section has class `anchor-section` (except hero and provenance which have their own styling)
- Add `<!-- Section content added by subsequent tasks -->` placeholder in each stub

## Acceptance Criteria
- [ ] `index.html` contains `<title>Isagawa — Conversational Agent Factory</title>`
- [ ] `index.html` contains `id="seed"`
- [ ] `index.html` contains `id="growth"`
- [ ] `index.html` contains `id="self-extension"`
- [ ] `index.html` contains `id="this-page"`
- [ ] `index.html` contains `id="provenance"`
- [ ] `index.html` does NOT contain `id="architecture"` or `id="kernel"` (old sections)

## Gates Satisfied
- BUILD-01, BUILD-04, BUILD-05, BUILD-06, BUILD-07, BUILD-08, BUILD-13

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
