# Copy kernel commands and hooks to master repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Copy kernel infrastructure from sr-dev-workspace to master:

```bash
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/commands/kernel
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/hooks
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/state
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/protocols
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/lessons

cp C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/commands/kernel/*.md C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/commands/kernel/
cp C:/Users/solos/my_ai_projects/sr-dev-workspace/.claude/hooks/*.py C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/hooks/
```

## Acceptance Criteria
- [ ] `session-start.md` exists in `.claude/commands/kernel/`
- [ ] `anchor.md` exists in `.claude/commands/kernel/`
- [ ] `complete.md` exists in `.claude/commands/kernel/`
- [ ] `universal-gate-enforcer.py` exists in `.claude/hooks/`
