# Strip Non-Core Commands

## Type
BUILD

## Phase Gate
Task 001 must be complete.

## Deliverable
Only 7 core commands remain in `.claude/commands/kernel/`.

## Instructions
Working in `D:\my_ai_projects\project_test_repos\kernel-minimal`:

**Keep these 7 commands:**
- session-start.md
- anchor.md
- learn.md
- complete.md
- fix.md
- domain-setup.md
- reset.md (create if missing)

**Remove everything else from `.claude/commands/kernel/`:**
- audit-workflow.md
- backlog.md
- task-builder.md
- autonomous-cycle.md
- Any other commands not in the keep list

## Verification
- `ls .claude/commands/kernel/ | wc -l` = 7
