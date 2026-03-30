# Verify protocol file created in master

## Type
TEST

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
ls C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/protocols/*.md
```

Read the protocol file and verify it references the SSH domain spec.

## Acceptance Criteria
- [ ] At least one `.md` file exists in `.claude/protocols/`
- [ ] Protocol references `ssh-management-layer` or `ssh`
