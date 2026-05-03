# Write execute-pipeline.md Command

## Context
The command file is the user-facing entry point. It's thin — points to SKILL.md for the full workflow. Follows the same pattern as prod-test.md and task-builder.md.

## Type
BUILD

## Execution
inline

## Dependencies
- 004 (SKILL.md must exist)

## Requirements
- Write `.claude/commands/kernel/execute-pipeline.md`
- Include: usage examples (natural language, existing backlog path, shorthand number)
- Include: "Load Skill" section pointing to `.claude/skills/execute-pipeline/SKILL.md`
- Include: quick reference step table (5 steps)
- Include: key principles (autonomous, outer-agent, no pause points, context pass-through)
- Include: composability section (standalone, or called by other commands)
- Follow prod-test.md command structure as reference

## Acceptance Criteria
- [ ] `test -f .claude/commands/kernel/execute-pipeline.md` exits 0
- [ ] `grep -q 'execute-pipeline/SKILL.md' .claude/commands/kernel/execute-pipeline.md` exits 0
- [ ] File has usage examples showing both input modes

## Gates Satisfied
- BUILD-10

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
