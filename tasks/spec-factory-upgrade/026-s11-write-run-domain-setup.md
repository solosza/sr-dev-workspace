# Write run-domain-setup.md

## Context
Step-11 sub-reference: Write domain-setup task, spawn run-task.sh, capture session_id, handle restart

## Type
BUILD

## Dependencies
- 024 (validation directory exists)

## Phase Gate
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/` directory exists

## Requirements
- Write `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/run-domain-setup.md`
- Must be self-contained with full implementation detail
- Content: Write domain-setup task, spawn run-task.sh, capture session_id, handle restart

## Acceptance Criteria
- [ ] `run-domain-setup.md` exists at validation path (verify: file_exists)

## Gates Satisfied
S11-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
