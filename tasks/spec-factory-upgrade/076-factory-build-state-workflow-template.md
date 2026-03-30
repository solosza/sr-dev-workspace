# Build ssh_workflow.json

## Context
047:Workflow state template

## Type
BUILD

## Dependencies
- /Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/.claude/state

## Phase Gate
- [ ] SKILL.md and workflow.md exist in spec output

## Requirements
- Create `C/ssh_workflow.json`
- 047:Workflow state template

## Acceptance Criteria
- [ ] `ssh_workflow.json` exists (verify: file_exists)

## Gates Satisfied
FAC-21

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
