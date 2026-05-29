# Task 005 — Commit All Changes

**Type:** BUILD
**Depends on:** 003, 004

## Objective

Commit all changes from pipeline 104 to the sr_dev_workspace git repository.

## Files to Commit

- `lib/attestation/attest.py` — fixed task_count derivation
- `.claude/state/attestations/087-20260527T103244Z.json` — backfilled
- `.claude/state/attestations/088-20260527T103258Z.json` — backfilled
- `.claude/state/attestations/089-20260527T103310Z.json` — backfilled
- `.claude/state/attestations/090-20260527T103323Z.json` — backfilled
- `.claude/state/attestations/091-20260527T103156Z.json` — backfilled
- `projects/fix-attestation-task-count/diagnosis.md` — findings
- `projects/fix-attestation-task-count/backfill.py` — backfill script

## Commit Message Format

```
fix: emit correct task_count in attestation bundles

- attest.py: derive task_count from task-folder file count (not workflow state)
- Backfill May 27 bundles 087-091 with correct task counts
- Root cause: Python dict.get() returns None for null values (not the default)
```

## Acceptance Criteria

- [ ] All changed files staged
- [ ] Commit created with message matching the format above
- [ ] `git status` shows clean working tree for these files
- [ ] No `.sigstore.json` files committed
