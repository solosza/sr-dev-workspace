# Run inner test batch in test repo

## Type
TEST

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Execute the inner test tasks by running run-task.sh inside the test repo:

```bash
bash C:/Users/solos/my_ai_projects/platform-ssh-test/run-task.sh C:/Users/solos/my_ai_projects/platform-ssh-test 12 prod-test
```

This spawns inner claude -p agents that execute L1/L2/L3 tests inside the test repo under kernel enforcement.

## Acceptance Criteria
- [ ] run-task.sh exits 0 (or reports ALL_TASKS_COMPLETE)
- [ ] Test repo workflow state shows completed tasks
- [ ] `_test/validation-report.json` exists in test repo
