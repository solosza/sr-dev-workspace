# Diagnosis: Attestation Bundle Task Count Bug

**Pipeline:** 104
**Date:** 2026-05-29
**Status:** Confirmed root cause — fix designed

---

## Observed Behavior

5 May 27 attestation bundles have `task_count: null` (and `completed_count: 0`) in `predicate.metadata`:

| Bundle | Pipeline | Actual Task Count | Stored task_count |
|--------|----------|-------------------|-------------------|
| `087-20260527T103244Z.json` | multi-model-routing | 6 | null |
| `088-20260527T103258Z.json` | ssh-compliance-spec-migration | 17 | null |
| `089-20260527T103310Z.json` | universal-hook-validator-system | 36 | null |
| `090-20260527T103323Z.json` | fix-execute-pipeline-cycling | 8 | null |
| `091-20260527T103156Z.json` | sync-model-router | 5 | null |

The portfolio feed renderer (backlog 099) added a `null → "0 tasks"` fallback. This masked the bug cosmetically, but "0 tasks" is misleading — these pipelines each had 5–36 actual tasks.

---

## Root Cause

### Layer 1: Python `dict.get()` with null values

In `lib/attestation/attest.py`, the task_count was read from workflow state:

```python
# Old code (at commit 8fd7abd):
task_count = workflow.get("total_tasks", 0)
```

Python's `dict.get(key, default)` only substitutes the default when the **key is absent**. When the key is present but its value is `None` (JSON null), it returns `None` — not the default.

```python
d = {"total_tasks": None}
d.get("total_tasks", 0)  # Returns None, NOT 0
```

At May 27 attestation time, `sr_dev_workflow.json` had `"total_tasks": null` (the pipeline was already complete and state was reset).

### Layer 2: Workflow state timing

The May 27 bundles were created via a **batch attestation run** that happened AFTER all 5 pipelines had completed and their workflow state had been reset. At that point:

- `total_tasks` was `null` in `sr_dev_workflow.json`
- `completed_tasks` was `[]` (empty list)

The fix `workflow.get("total_tasks") or 0` (added later) handles `None` correctly, but still returns `0` when workflow has been reset — which is still wrong data.

### Layer 3: Fundamental design issue

`_read_workflow_state()` reads the **current global workflow state** — a single shared file that gets overwritten with each pipeline. It has no per-pipeline history. Attestation called after a pipeline resets state will always get stale/zero counts.

---

## Fix Approach

**Primary source: count task files in the task folder**

The task folder is immutable after pipeline completion (it moves to `tasks/completed/` but the files remain). Counting `NNN-*.md` files (excluding `000-index.md` and `gate-contract.md`) gives the authoritative task count:

```python
def _count_tasks_in_folder(task_folder: str) -> int:
    import re
    if not os.path.isdir(task_folder):
        return 0
    return sum(
        1 for f in os.listdir(task_folder)
        if re.match(r'^\d{3,}-', f) and f.endswith('.md')
        and f != '000-index.md' and 'gate-contract' not in f
    )
```

**Workflow state as fallback only:**

```python
task_count = _count_tasks_in_folder(task_folder)
if task_count == 0:
    task_count = workflow.get("total_tasks") or 0
```

This is robust because:
- Task folder files persist after workflow state is reset
- File count is deterministic and doesn't depend on timing
- Workflow state is used as a safety net for edge cases

---

## Backfill Plan

For the 5 May 27 bundles:
1. Use the task folder (now in `tasks/completed/`) to get authoritative counts
2. Update `predicate.metadata.task_count` and `predicate.metadata.completed_count` in the local JSON files
3. Do NOT touch `.sigstore.json` files or submit new Rekor entries
4. The local JSON is the source of truth for `generate-feed.py` — Rekor is for cryptographic audit, not feed rendering

After backfill, regenerate `feed-data.json` to update the live feed.
