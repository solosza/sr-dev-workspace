# Write Command Entry Point (eval.md)

## Context
Layer 1 of the 6-layer command-skill-pattern. The command entry point is a minimal file that points to the skill. It defines usage syntax and examples. This is the file users invoke with `/kernel/eval`.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/commands/kernel/eval.md`
- Must contain:
  - Usage syntax: `/kernel/eval [target] [source-repo]`
  - At least 3 usage examples (check-data, deepeval-management-layer, prod-test)
  - Pointer to skill: `.claude/skills/eval/SKILL.md`
  - Brief description: tests any LLM artifact using DeepEval
  - Parameter descriptions for `target` and `source-repo`
- Must NOT contain implementation details (those live in the skill)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/commands/kernel/eval.md`
- [ ] `grep -q "SKILL.md" .claude/commands/kernel/eval.md` passes
- [ ] `grep -q "source-repo" .claude/commands/kernel/eval.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-01, INT-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
