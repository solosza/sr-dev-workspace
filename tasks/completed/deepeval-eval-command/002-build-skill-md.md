# Write SKILL.md (Eval Skill Identity)

## Context
Layer 2 of the 6-layer command-skill-pattern. SKILL.md is the skill's identity file — it defines who the eval agent is, its vocabulary, critical rules, file index, and a workflow summary table pointing to step files. This is an INDEX file (points to payloads, never contains payload itself).

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/SKILL.md`
- Must contain these sections:
  - **Identity**: "You are the eval agent. You test LLM artifacts using DeepEval."
  - **Vocabulary**: eval-specific terms (harness compilation, golden dataset, component check, artifact isolation, scored report, framework growth)
  - **File Index**: points to workflow.md, gate-contract.md, all 6 step files, references/INDEX.md, contracts/
  - **Critical Rules**: (1) read _reference/ before creating new components, (2) test repo is disposable, (3) adapt to what you're testing, (4) contracts validate eval's own behavior not the target, (5) 200-line threshold
  - **Workflow Summary**: 6-step table with step name, file pointer, one-line description
- Must reference workflow.md and gate-contract.md
- Must be under 200 lines
- Follows tiered-index Layer 1: this file is INDEX only, no payload

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/SKILL.md`
- [ ] `grep -q "workflow.md" .claude/skills/eval/SKILL.md` passes
- [ ] `grep -q "gate-contract.md" .claude/skills/eval/SKILL.md` passes
- [ ] `grep -q "step-01" .claude/skills/eval/SKILL.md` passes
- [ ] `grep -q "step-06" .claude/skills/eval/SKILL.md` passes
- [ ] `grep -q "INDEX.md" .claude/skills/eval/SKILL.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-02, INT-01, INT-02, INT-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
