# Portfolio Site — Task Index

## Goal
Build the Isagawa portfolio site with "the loop" theme — 4 anchor moments (Seed → Growth → Self-Extension → This Page), "conversational agent factory" framing, dual attestation provenance, dark terminal aesthetic. Rewrite existing site at `D:\my_ai_projects\isagawa-portfolio-site\`.

## Source
Backlog 047: `docs/backlog/047-market-build-portfolio-site-loop-theme.md`

## Design References
- `docs/backlog/047-market-build-portfolio-site-loop-theme/positioning.md`
- `docs/backlog/047-market-build-portfolio-site-loop-theme/theme-and-narrative.md`
- `docs/backlog/047-market-build-portfolio-site-loop-theme/build-phases.md`

## Tasks

### Phase 1: CSS Foundation Update
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-css-strip-old-sections]] | BUILD | none | pending |
| 002 | [[002-build-css-add-anchor-styles]] | BUILD | 001 | pending |

### Phase 2: HTML Rewrite
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 003 | [[003-build-html-rewrite-skeleton]] | BUILD | 001 | pending |
| 004 | [[004-build-html-hero]] | BUILD | 003 | pending |
| 005 | [[005-build-html-seed]] | BUILD | 003 | pending |
| 006 | [[006-build-html-growth]] | BUILD | 005 | pending |
| 007 | [[007-build-html-self-extension]] | BUILD | 006 | pending |
| 008 | [[008-build-html-this-page]] | BUILD | 007 | pending |
| 009 | [[009-build-css-section-detail]] | BUILD | 008 | pending |

### Phase 3: Provenance Component
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 010 | [[010-build-html-provenance]] | BUILD | 009 | pending |
| 011 | [[011-build-embed-bundle-050]] | BUILD | 010 | pending |
| 012 | [[012-build-embed-bundle-052]] | BUILD | 011 | pending |
| 013 | [[013-build-js-rekor-verification]] | BUILD | 012 | pending |
| 014 | [[014-build-css-provenance]] | BUILD | 013 | pending |

### Phase 4: Navigation + Footer
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 015 | [[015-build-html-footer]] | BUILD | 014 | pending |
| 016 | [[016-build-css-nav-footer]] | BUILD | 015 | pending |
| 017 | [[017-build-js-smooth-scroll]] | BUILD | 016 | pending |
| 018 | [[018-build-js-mobile-nav]] | BUILD | 017 | pending |

### Phase 5: Responsive + Polish
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 019 | [[019-build-css-responsive]] | BUILD | 018 | pending |
| 020 | [[020-test-phase-boundary]] | TEST | 019 | pending |

### Phase 6: Visual QA
| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 021 | [[021-test-l1-verify-structure]] | TEST | 020 | pending |
| 022 | [[022-test-l2-visual-qa-desktop]] | TEST | 021 | pending |
| 023 | [[023-test-l2-visual-qa-mobile]] | TEST | 022 | pending |
| 024 | [[024-test-l3-provenance-display]] | TEST | 021 | pending |
| 025 | [[025-test-l3-final-validation]] | TEST | 022, 023, 024 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- Static HTML/CSS portfolio site at `D:\my_ai_projects\isagawa-portfolio-site\`
- 4 anchor moment sections (Seed, Growth, Self-Extension, This Page)
- Dual attestation provenance component with client-side Rekor verification
- Dark terminal aesthetic, responsive at 3 breakpoints
- "Conversational agent factory" hero framing
