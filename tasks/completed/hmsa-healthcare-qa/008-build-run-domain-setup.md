# Run Domain-Setup in Target Workspace

## Context
Domain-setup must run INSIDE the target workspace so the kernel discovers the spec, builds the protocol, and creates hooks. This requires spawning a sub-agent because domain-setup needs the kernel's CLAUDE.md as context. After domain-setup, hooks require a restart — but since run-task.sh spawns fresh claude -p sessions per task, the next task will pick up the new hooks automatically.

## Type
BUILD

## Execution
inline

## Dependencies
- 007

## Phase Gate
- [ ] Initial commit exists in target workspace
- [ ] CLAUDE.md and kernel .claude/ present

## Requirements
- Spawn a sub-agent that operates in the target workspace:
  - Agent reads `D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa\CLAUDE.md`
  - Agent invokes `/kernel/session-start` then `/kernel/domain-setup`
  - Domain-setup discovers the healthcare-qa spec, builds protocol + hooks
  - Agent sets `needs_restart: true` and exits
- After sub-agent returns, verify domain-setup artifacts exist
- NOTE: settings.local.json MUST use string matcher format (`"Write|Edit|Bash"`) with nested `"hooks"` arrays — NOT object matchers

## Acceptance Criteria
- [ ] `.claude/state/session_state.json` exists in target workspace with `domain` field set
- [ ] `.claude/protocols/` contains a protocol file
- [ ] `.claude/settings.local.json` exists with `hooks` key
- [ ] `needs_restart: true` is set (confirming domain-setup completed)

## Gates Satisfied
- FUNC-01, FUNC-02, FUNC-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
