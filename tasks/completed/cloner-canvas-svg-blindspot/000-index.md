# Cloner Canvas/SVG Blind Spot Fix — Task Index

## Goal
Add non-DOM rendering detection and fallback extraction strategies to the website cloner skill.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-add-sanity-check]] | BUILD | none | pending |
| 002 | [[002-build-add-hydration-wait]] | BUILD | none | pending |
| 003 | [[003-build-add-svg-text-extraction]] | BUILD | none | pending |
| 004 | [[004-build-add-canvas-detection]] | BUILD | none | pending |
| 005 | [[005-build-add-css-divergence-resolution]] | BUILD | none | pending |
| 006 | [[006-build-update-skill-edge-cases]] | BUILD | 001-005 | pending |
| 007 | [[007-test-l1-verify-sections-exist]] | TEST | 001-006 | pending |
| 008 | [[008-test-l2-sanity-check-js]] | TEST | 001 | pending |
| 009 | [[009-test-l3-live-extraction]] | TEST | 001-006 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- Updated `.claude/skills/website-cloner/references/extraction.md` with sanity check, hydration wait, SVG text extraction, canvas detection, and CSS divergence resolution
- Updated `.claude/skills/website-cloner/SKILL.md` edge cases table
