# Create Execute-Pipeline Skill Directory Structure

## Context
The execute-pipeline skill follows the standard kernel skill layout: SKILL.md at root, step references in references/ subdirectory.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Create directory: `.claude/skills/execute-pipeline/`
- Create directory: `.claude/skills/execute-pipeline/references/`

## Acceptance Criteria
- [ ] `test -d .claude/skills/execute-pipeline/references` exits 0

## Gates Satisfied
- BUILD-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
