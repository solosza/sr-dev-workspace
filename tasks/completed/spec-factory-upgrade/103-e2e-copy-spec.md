# Copy SSH Spec into E2E Workspace

## Context
Copy packaged spec for discovery.

## Type
TEST

## Dependencies
- 101

## Phase Gate
- [ ] E2E workspace exists (task 101)

## Requirements
- Copy SSH spec from `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/` into e2e workspace
- Preserve .claude/skills/ structure

## Acceptance Criteria
- [ ] SKILL.md exists in e2e workspace (verify: file_exists)

## Gates Satisfied
INT-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
