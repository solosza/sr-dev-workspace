# Add YAML Frontmatter to Skill Files

## Context
Pre-packaging: add YAML frontmatter to all skill .md files.

## Type
BUILD

## Dependencies
- 094

## Phase Gate
- [ ] validation-report.json exists (task 094)

## Requirements
- For each .md in `C:/Users/solos/my_ai_projects/domain-spec-factory/output/ssh-image-testing/.claude/skills/ssh-management-layer/`:
- Add --- frontmatter at top if missing

## Acceptance Criteria
- [ ] `head -1 SKILL.md` is `---` (verify: grep)

## Gates Satisfied
PKG-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
