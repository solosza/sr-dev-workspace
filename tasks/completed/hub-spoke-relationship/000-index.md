# Pipeline 108 — Hub-Spoke Relationship Visibility

**Backlog:** `docs/backlog/108-market-fix-hub-spoke-relationship.md`

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | Add factory-origin CSS to styles.css | BUILD | — |
| 002 | Add origin strip to product pages (5 pages) | BUILD | 001 |
| 003 | Test all 5 product pages have origin strip | TEST | 002 |
| 004 | Commit + push | BUILD | 003 |
