# 011 — L1: Verify All Modified Files Exist and Contain Expected Patterns

## Type
TEST

## Requirements
Verify all files modified by tasks 001-010 exist and contain expected patterns:

1. `step-03-run-task-builder.md` — contains `"skip_plan_review": false`
2. `run-task.sh` — contains `CURRENT_TASK`, `BACKLOG_PATH`, `docs/backlog/done`, `tasks/completed`
3. `step-09-execute.md` — contains mode clarification text
4. `complete.md` — contains `gate-contract.md` reference
5. `step-04-execute-tasks.md` — contains classification logic and autonomous-cycle reference
6. `granularity-reference.md` — exists in task-builder references
7. `step-05-decompose.md` — contains `granularity-reference`
8. `step-06-atomize.md` — contains `granularity-reference`

## Acceptance Criteria
- [ ] All 8 files exist at their expected paths
- [ ] Each file contains its expected key pattern (grep check)
