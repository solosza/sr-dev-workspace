# Verify kernel commands exist in master

## Type
TEST

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
ls C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/commands/kernel/
```

## Acceptance Criteria
- [ ] `session-start.md` exists
- [ ] `anchor.md` exists
- [ ] `complete.md` exists
