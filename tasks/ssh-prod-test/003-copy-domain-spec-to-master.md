# Copy domain spec to master repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Copy the SSH domain spec:

```bash
mkdir -p C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/skills
cp -r C:/Users/solos/my_ai_projects/platform-ssh-verify/.claude/skills/ssh-management-layer C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/skills/ssh-management-layer
```

## Acceptance Criteria
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/skills/ssh-management-layer/SKILL.md` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/skills/ssh-management-layer/workflow.md` exists
- [ ] `C:/Users/solos/my_ai_projects/platform-ssh-master/.claude/skills/ssh-management-layer/gate-contract.md` exists
