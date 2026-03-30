# Write install-dependencies.md

## Context
Step-11 sub-reference: Detect manifest, install via pip/npm, fail if functional gates but no manifest

## Type
BUILD

## Dependencies
- 024 (validation directory exists)

## Phase Gate
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/` directory exists

## Requirements
- Write `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/install-dependencies.md`
- Must be self-contained with full implementation detail
- Content: Detect manifest, install via pip/npm, fail if functional gates but no manifest

## Acceptance Criteria
- [ ] `install-dependencies.md` exists at validation path (verify: file_exists)

## Gates Satisfied
S11-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
