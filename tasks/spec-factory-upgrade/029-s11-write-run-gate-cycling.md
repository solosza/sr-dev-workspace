# Write run-gate-cycling.md

## Context
Step-11 sub-reference: Clear state, spawn run-task.sh for N iterations, wait, read logs

## Type
BUILD

## Dependencies
- 024 (validation directory exists)

## Phase Gate
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/` directory exists

## Requirements
- Write `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/run-gate-cycling.md`
- Must be self-contained with full implementation detail
- Content: Clear state, spawn run-task.sh for N iterations, wait, read logs

## Acceptance Criteria
- [ ] `run-gate-cycling.md` exists at validation path (verify: file_exists)

## Gates Satisfied
S11-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
