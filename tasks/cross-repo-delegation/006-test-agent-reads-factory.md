# Test: spawned agent can read factory repo files

## Context
L2: verify agent can access factory repo from sr-dev-workspace.

## Type
TEST

## Execution
agent

## Dependencies
- None

## Requirements
- Spawn agent. Have it read C:/Users/solos/my_ai_projects/domain-spec-factory/CLAUDE.md and C:/Users/solos/my_ai_projects/domain-spec-factory/.claude/skills/spec-factory/SKILL.md. Report contents.

## Acceptance Criteria
- [ ] Agent successfully reads both files (verify: agent reports content)

## Gates Satisfied
FUNC-01

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
