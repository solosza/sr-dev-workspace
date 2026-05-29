# Portfolio Feed Server Render — Task Index

## Goal
Pre-render feed entries into static HTML so crawlers and no-JS fetchers see all entries in the raw response.

## Source
`docs/backlog/101-market-fix-portfolio-feed-server-render.md`

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-market-build-add-feed-marker]] | BUILD | none | pending |
| 002 | [[002-market-build-add-static-renderer]] | BUILD | 001 | pending |
| 003 | [[003-market-build-run-generator]] | BUILD | 002 | pending |
| 004 | [[004-market-test-verify-raw-html]] | BUILD | 003 | pending |
| 005 | [[005-market-build-commit-push]] | BUILD | 004 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `D:\my_ai_projects\isagawa-co.github.io\feed.html` — entries present in raw HTML without JS execution
- `D:\my_ai_projects\isagawa-co.github.io\generate-feed.py` — updated with static rendering + injection
