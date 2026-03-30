# Build ssh-workflow.md

## Context
048, 049:Main command invoking SSH management layer skill

## Type
BUILD

## Dependencies
- /Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/.claude/commands

## Phase Gate
- [ ] SKILL.md and workflow.md exist in spec output

## Requirements
- Create `C/ssh-workflow.md`
- 048, 049:Main command invoking SSH management layer skill

## Acceptance Criteria
- [ ] `ssh-workflow.md` exists (verify: file_exists)

## Gates Satisfied
FAC-21

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
