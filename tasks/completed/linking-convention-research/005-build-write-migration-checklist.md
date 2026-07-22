# Write Migration Checklist

## Context
Create a checklist for migrating existing files to the chosen linking convention.

## Type
BUILD

## Execution
inline

## Dependencies
- 004-build-write-design-decision

## Phase Gate
- [ ] `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/linking-convention.md` exists

## Requirements
- Read the design decision document
- Read the current usage analysis (task 003 output)
- Write migration checklist to `D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/docs/design/tiered-index-architecture/linking-migration-checklist.md`
- Checklist must include:
  - Files that need updating (from current usage analysis)
  - Before/after examples for each change
  - Priority order (high-traffic files first)
  - Verification method (grep command to confirm migration)

## Acceptance Criteria
- [ ] Migration checklist exists at the specified path
- [ ] Lists specific files to update
- [ ] Contains before/after examples
- [ ] Contains verification grep commands

## Gates Satisfied
- BUILD-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
