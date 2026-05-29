# Task Index — Fix Attestation Bundle Task Count

**Backlog:** `docs/backlog/104-market-fix-attestation-bundle-task-count.md`
**Goal:** Fix `lib/attestation/attest.py` to emit correct `task_count` at write time; backfill May 27 bundles.

## Tasks

| # | File | Type | Description |
|---|------|------|-------------|
| 001 | `001-diagnose-write-findings.md` | BUILD | Write diagnosis findings to projects/ |
| 002 | `002-fix-attest-py-task-count.md` | BUILD | Fix attest.py to use task-folder file count as fallback |
| 003 | `003-backfill-may27-bundles.md` | BUILD | Backfill task_count in 5 May 27 local bundle JSONs |
| 004 | `004-test-attest-dry-run.md` | TEST | Verify fix with dry-run attestation |
| 005 | `005-commit-changes.md` | BUILD | Commit all changes to workspace |

## Dependencies

- 001 → (none) — diagnosis first
- 002 → 001 — fix after confirming diagnosis
- 003 → 002 — backfill after fix is in place
- 004 → 002 — test the new behavior
- 005 → 003, 004 — commit after all changes verified
