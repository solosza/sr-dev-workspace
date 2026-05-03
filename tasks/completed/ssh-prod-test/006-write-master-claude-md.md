# Write CLAUDE.md for master repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Write `C:/Users/solos/my_ai_projects/platform-ssh-master/CLAUDE.md` with kernel bootstrap. Read `C:/Users/solos/my_ai_projects/sr-dev-workspace/CLAUDE.md` for reference structure, adapt for SSH platform domain.

Must include:
- Kernel loop (session-start → anchor → WORK → complete)
- Commands table pointing to `.claude/commands/kernel/`
- Domain spec reference to `.claude/skills/ssh-management-layer/`

## Acceptance Criteria
- [ ] `CLAUDE.md` exists in master repo
- [ ] Contains `session-start` reference
- [ ] Contains `ssh-management-layer` reference
