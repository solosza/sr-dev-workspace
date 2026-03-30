# Run domain-setup in master repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Spawn a claude -p session in the master repo to run domain-setup:

```bash
claude -p --dangerously-skip-permissions --cwd C:/Users/solos/my_ai_projects/platform-ssh-master "Read CLAUDE.md. Then read and follow .claude/commands/kernel/domain-setup.md to discover the SSH domain spec and build protocol + hooks. Output DOMAIN_SETUP_COMPLETE when done."
```

This generates protocol file, hooks in settings, and initialized state.

## Acceptance Criteria
- [ ] Protocol file exists in `.claude/protocols/`
- [ ] State file exists in `.claude/state/`
- [ ] Command completed without errors
