# Build session_state.json

## Context
047:Session state template with domain field set

## Type
BUILD

## Dependencies
- /Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/.claude/state

## Phase Gate
- [ ] SKILL.md and workflow.md exist in spec output

## Requirements
- Create `C/session_state.json`
- 047:Session state template with domain field set

## Acceptance Criteria
- [ ] `session_state.json` exists (verify: file_exists)

## Gates Satisfied
FAC-21

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
