# Verify README Completeness

## Context
Check README has install + usage sections.

## Type
TEST

## Dependencies
- 095, 096

## Phase Gate
- [ ] Frontmatter added (095), paths fixed (096)

## Requirements
- Read `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/README.md`
- Verify install section
- Verify usage section

## Acceptance Criteria
- [ ] README has install + usage (verify: grep)

## Gates Satisfied
PKG-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
