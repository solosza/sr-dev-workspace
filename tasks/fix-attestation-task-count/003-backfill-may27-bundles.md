# Task 003 — Backfill May 27 Bundle Task Counts

**Type:** BUILD
**Depends on:** 002

## Objective

Patch the 5 May 27 attestation bundle JSON files to correct their `task_count` and `completed_count` fields. Backfill only the local bundle JSONs — do NOT touch signed Rekor entries or `.sigstore.json` files.

## Affected Bundles

| Bundle File | Task Folder | Actual Task Count |
|-------------|-------------|-------------------|
| `087-20260527T103244Z.json` | `tasks/completed/multi-model-routing` | 6 |
| `088-20260527T103258Z.json` | `tasks/completed/ssh-compliance-spec-migration` | 17 |
| `089-20260527T103310Z.json` | `tasks/completed/universal-hook-validator-system` | 36 |
| `090-20260527T103323Z.json` | `tasks/completed/fix-execute-pipeline-cycling` | 8 |
| `091-20260527T103156Z.json` | `tasks/completed/sync-model-router` | 5 |

## Deliverable

Write a Python script `projects/fix-attestation-task-count/backfill.py` that:
1. Opens each bundle JSON
2. Sets `predicate.metadata.task_count` to the correct count
3. Sets `predicate.metadata.completed_count` to the same count (all tasks completed for these pipelines)
4. Saves the file

Then RUN the script to apply the backfill.

## Constraints

- ONLY edit `NNN-*.json` files (not `*.sigstore.json` files)
- Do NOT submit new Rekor entries — this is local-only correction
- The signed Rekor entries remain unchanged (they signed the old bundle hash, which is fine — local bundle is the source of truth for the feed renderer)

## Acceptance Criteria

- [ ] Backfill script written at `projects/fix-attestation-task-count/backfill.py`
- [ ] Script ran successfully (exit 0)
- [ ] 087 bundle has `task_count: 6, completed_count: 6`
- [ ] 088 bundle has `task_count: 17, completed_count: 17`
- [ ] 089 bundle has `task_count: 36, completed_count: 36`
- [ ] 090 bundle has `task_count: 8, completed_count: 8`
- [ ] 091 bundle has `task_count: 5, completed_count: 5`
- [ ] No `.sigstore.json` files were modified
