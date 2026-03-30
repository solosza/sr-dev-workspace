# Write retry-cleanup.md

## Context
Step-11 sub-reference: Failure categorization, retry scopes, max 3 retries, cleanup rules

## Type
BUILD

## Dependencies
- 024 (validation directory exists)

## Phase Gate
- [ ] `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/` directory exists

## Requirements
- Write `C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/references/validation/retry-cleanup.md`
- Must be self-contained with full implementation detail
- Content: Failure categorization, retry scopes, max 3 retries, cleanup rules

## Acceptance Criteria
- [ ] `retry-cleanup.md` exists at validation path (verify: file_exists)

## Gates Satisfied
S11-11

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
