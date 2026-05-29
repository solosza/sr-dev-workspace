# Portfolio Feed — Duplicate Grouping — Task Index

## Goal
Group consecutive same-title entries in the feed into expandable "N runs" UI — preserving all Rekor links and all data, no deletions.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-group-feed-entries]] | BUILD | none | pending |
| 002 | [[002-test-verify-grouping]] | TEST | 001 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `feed.html` updated — grouping logic + `<details>/<summary>` renderer
- `feed.css` updated — group header styles
- Feed deployed to GitHub Pages
- Playwright verified: groups visible, all Rekor links alive, no entries deleted
