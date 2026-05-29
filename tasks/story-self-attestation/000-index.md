# Pipeline 109 — Fix story.html Self-Attestation

**Backlog:** `docs/backlog/109-market-fix-story-self-attestation.md`
**Phase:** 1 (all tasks sequential)

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | Fix verify links in story.html | BUILD | — |
| 002 | Verify no dead href="#" | TEST | 001 |
| 003 | Commit + push | BUILD | 002 |
