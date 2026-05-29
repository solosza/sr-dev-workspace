# Pipeline 107 — Unified Nav Across All Pages

**Backlog:** `docs/backlog/107-market-fix-nav-consistency.md`
**Depends on:** Pipeline 106 research report at `projects/nav-consolidation-research/research-report.md`

| # | Task | Type | Depends |
|---|------|------|---------|
| 001 | Read 106 research, extract nav spec | BUILD | 106 complete |
| 002 | Add nav CSS for dropdown + active state | BUILD | 001 |
| 003 | Update index.html nav | BUILD | 002 |
| 004 | Update feed.html nav | BUILD | 002 |
| 005 | Update attestation.html nav | BUILD | 002 |
| 006 | Update qa-platforms.html nav | BUILD | 002 |
| 007 | Update ssh-compliance.html nav | BUILD | 002 |
| 008 | Update vibe-coder.html nav | BUILD | 002 |
| 009 | Update story.html nav | BUILD | 002 |
| 010 | Test nav consistency across all pages | TEST | 003-009 |
| 011 | Commit + push | BUILD | 010 |
