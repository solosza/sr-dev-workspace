# Fix Attestation Writer — Null task_count at Source

## Context
`attest.py` reads `total_tasks` from the workflow JSON to populate `task_count` in the attestation bundle. The bug: `workflow.get("total_tasks", 0)` passes `None` through when the workflow has `"total_tasks": null` explicitly (the default only fires when the key is absent, not when it's null). The May 27 bundles were signed with `task_count: null` as a result. This task fixes the writer so future bundles never contain null.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- File: `D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/attest.py`
- Line 98: change `workflow.get("total_tasks", 0)` to `workflow.get("total_tasks") or 0`
- The `or 0` pattern catches both missing key AND explicit null/zero, ensuring an integer is always written

## Acceptance Criteria
- [ ] `attest.py` line 98 reads `workflow.get("total_tasks") or 0` (grep match)
- [ ] No other `workflow.get("total_tasks"` pattern remains with the old form
- [ ] File is valid Python (no syntax errors)

## Gates Satisfied
- BUILD-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
