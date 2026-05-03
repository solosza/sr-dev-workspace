# Collect validation report

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Read the validation report from the test repo and copy it to sr-dev-workspace:

```bash
cp C:/Users/solos/my_ai_projects/platform-ssh-test/_test/validation-report.json C:/Users/solos/my_ai_projects/sr-dev-workspace/tasks/ssh-prod-test/_test/validation-report.json
```

Also read and summarize the report contents.

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/sr-dev-workspace/tasks/ssh-prod-test/_test/validation-report.json` exists
- [ ] Report contains L1/L2/L3 gate results
