# Portfolio Feed Server Render — Task Index

## Goal
Fix feed.html so all entries appear in raw HTML without JS execution — a curl fetch returns full entry list, not "Loading..."

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-market-build-create-branch]] | BUILD | none | pending |
| 002 | [[002-market-fix-feed-count-static]] | BUILD | 001 | pending |
| 003 | [[003-market-fix-feed-js-guard]] | BUILD | 002 | pending |
| 004 | [[004-market-fix-generate-feed-markers]] | BUILD | 003 | pending |
| 005 | [[005-market-test-verify-no-js-fetch]] | TEST | 004 | pending |
| 006 | [[006-market-build-commit-push-pr]] | BUILD | 005 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `D:/my_ai_projects/isagawa-co.github.io/feed.html` — static count in raw HTML, entries pre-rendered, JS does NOT overwrite entries
- `D:/my_ai_projects/isagawa-co.github.io/generate-feed.py` — updated to use start/end markers and update static count
- All changes on feat/ branch, merged to main via PR
