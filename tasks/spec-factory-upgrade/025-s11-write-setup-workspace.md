# Write setup-workspace.md

## Context
Step-11 sub-reference: Create clean workspace, copy kernel + spec + fixtures, NO git init, state init

## Type
BUILD

## Dependencies
- 024 (validation directory exists)

## Phase Gate
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/` directory exists

## Requirements
- Write `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/setup-workspace.md`
- Must be self-contained with full implementation detail
- Content: Create clean workspace, copy kernel + spec + fixtures, NO git init, state init

## Acceptance Criteria
- [ ] `setup-workspace.md` exists at validation path (verify: file_exists)

## Gates Satisfied
S11-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
