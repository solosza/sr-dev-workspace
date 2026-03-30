# Copy Spec Files into Validation Workspace

## Context
Copy factory output into test workspace for isolated testing.

## Type
TEST

## Dependencies
- 081

## Phase Gate
- [ ] Validation workspace exists (task 081)

## Requirements
- Copy all files from `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/` into workspace
- Preserve directory structure
- Use cp -r with absolute paths

## Acceptance Criteria
- [ ] `.claude/skills/ssh-management-layer/SKILL.md` exists in workspace (verify: file_exists)

## Gates Satisfied
VAL-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
