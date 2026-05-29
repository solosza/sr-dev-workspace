# Task 004 — Test: Verify Fix with Dry-Run Attestation

**Type:** TEST
**Depends on:** 002

## Objective

Verify that the fixed `attest.py` correctly derives `task_count` from a task folder by running a dry-run attestation against a known task folder.

## Test Cases

### Test 1: Dry-run self-test mode
Run: `python lib/attestation/attest.py --dry-run`
Expected: exits 0, prints "ALL TESTS PASSED"

### Test 2: Dry-run against a real task folder
Run attestation in dry-run mode against `tasks/completed/multi-model-routing` (which has 6 tasks):
```python
from lib.attestation.attest import run_attestation
result = run_attestation(
    backlog_path="docs/backlog/done/087-kernel-research-multi-model-routing.md",
    task_folder="tasks/completed/multi-model-routing",
    dry_run=True,
)
# Read the bundle and verify task_count == 6
```
Expected: bundle has `task_count: 6` in `predicate.metadata`

### Test 3: Verify helper function directly
Import and call `_count_tasks_in_folder("tasks/completed/multi-model-routing")`
Expected: returns 6

## Acceptance Criteria

- [ ] `python lib/attestation/attest.py --dry-run` exits 0
- [ ] Dry-run bundle for multi-model-routing has `task_count == 6`
- [ ] `_count_tasks_in_folder` returns correct count for a known folder
- [ ] Dry-run bundle file is created at `.claude/state/attestations/` and removed after test
