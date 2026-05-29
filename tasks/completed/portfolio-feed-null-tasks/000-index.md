# Portfolio Feed — Null Tasks Fix — Task Index

## Goal
Fix "null tasks" display on isagawa.co feed by patching the attestation writer (source), feed generator, and renderer.

## Tasks

| # | Task | Type | Dependencies | Status |
|---|------|------|-------------|--------|
| 001 | [[001-build-fix-attest-writer]] | BUILD | none | pending |
| 002 | [[002-build-fix-feed-generator]] | BUILD | 001 | pending |
| 003 | [[003-build-fix-feed-renderer]] | BUILD | 002 | pending |
| 004 | [[004-build-regenerate-feed-data]] | BUILD | 003 | pending |
| 005 | [[005-test-verify-no-null-tasks]] | TEST | 004 | pending |

## Gate Contract
→ [[gate-contract.md]]

## Deliverables
- `attest.py` patched — no future bundles will write null task_count
- `generate-feed.py` patched — null task_count handled gracefully
- `feed.html` patched — null task_count renders as "—" not "null tasks"
- `feed-data.json` regenerated — no null task_count values
- Feed verified via Playwright MCP — no "null tasks" text visible
