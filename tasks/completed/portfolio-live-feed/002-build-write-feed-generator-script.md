# 002 — Write Feed Generator Script

**Type:** BUILD
**Depends on:** 001

## Requirements
Write `D:\my_ai_projects\isagawa-co.github.io\generate-feed.py` — a Python script that:

1. Scans `D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\state\attestations\` for `*.json` files (exclude `*.sigstore.json`)
2. Parses each attestation bundle JSON to extract:
   - `predicate.metadata.pipeline_backlog` → extract backlog title (human-readable from filename)
   - `predicate.timestamp.start` → timestamp
   - `predicate.metadata.task_count` and `completed_count`
   - `predicate.invocation.intent_chain` → length = intent revision count
   - `predicate.rekor.entryUrl` and `logIndex` (if present)
   - Category tag derived from backlog filename (kernel/market/domain/test)
3. Sorts entries newest first by timestamp
4. Generates `feed.html` using a template with:
   - Header: "Every entry below was produced from a sentence of natural language, executed under kernel governance, and signed with Sigstore."
   - Each entry as a `div.feed-entry` with category color class
   - Nav link back to main site
   - Footer: "This feed updates automatically. Come back tomorrow and there will be more."
   - Total count injected as a data attribute for the nav counter
5. Writes the count to a file `feed-count.txt` (just the number) for the nav counter to read at build time

The script must work with absolute paths and be runnable from any directory.

## Acceptance Criteria
- [ ] `D:\my_ai_projects\isagawa-co.github.io\generate-feed.py` exists
- [ ] Script uses only Python stdlib (json, os, glob, datetime)
- [ ] Script reads from attestation directory and writes `feed.html` + `feed-count.txt`
