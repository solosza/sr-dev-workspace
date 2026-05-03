# Update CLAUDE.md in Spec Factory

## Context
Add new commands (task-builder, audit-workflow, backlog) and skills to CLAUDE.md command tree.

## Type
BUILD

## Dependencies
- 005-019 (commands + skills copied)

## Phase Gate
- [ ] task-builder.md exists in spec factory commands dir

## Phase Gate
- [ ] All 11 command .md files exist in `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/commands/kernel/`
- [ ] All 4 skill SKILL.md files exist in `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/`

## Requirements
- Read `C:/Users/solos/my_ai_projects/domain-spec-factory/CLAUDE.md`
- Add task-builder.md, audit-workflow.md, backlog.md to command tree
- Add Task Builder + Audit Workflow skill sections
- Remove validate.md reference if present

## Acceptance Criteria
- [ ] CLAUDE.md has task-builder in command tree (verify: grep 'task-builder')

## Gates Satisfied
SYNC-24, SYNC-25, SYNC-26

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
