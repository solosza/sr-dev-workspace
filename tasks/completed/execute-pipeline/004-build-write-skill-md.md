# Write Execute-Pipeline SKILL.md

## Context
The SKILL.md is the index file for the execute-pipeline skill. It follows the standard kernel skill layout: step table with wikilinks to reference files, key principles, outcome description. Must NOT contain inline implementation — only pointers.

## Type
BUILD

## Execution
inline

## Dependencies
- 003 (skill directory must exist)

## Requirements
- Write `.claude/skills/execute-pipeline/SKILL.md`
- Include: Type (Prescriptive), Style (Indexed — SKILL.md + references/)
- Step table with 5 steps, each linking to `references/step-NN-*.md`
- Steps: 1-parse-input, 2-create-backlog, 3-run-task-builder, 4-execute-tasks, 5-validate-report
- Key principles section: fully autonomous, outer-agent pattern, run-task.sh outside loop, all context passes through
- Outcome section: what exists after completion
- Follow prod-test SKILL.md as structural reference
- File must be an INDEX — no inline implementation, only step table + pointers

## Acceptance Criteria
- [ ] `test -f .claude/skills/execute-pipeline/SKILL.md` exits 0
- [ ] `grep -q 'step-01-parse-input' .claude/skills/execute-pipeline/SKILL.md` exits 0
- [ ] `grep -q 'step-05-validate-report' .claude/skills/execute-pipeline/SKILL.md` exits 0
- [ ] File has step table with 5 entries

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
