# Write step-04-component-check.md

## Context
Layer 3 step file for dynamic component checking. The agent reads the target artifact deeply, then checks platform-deepeval _reference/ for existing components that can be reused. If components are missing, it creates new ones following existing patterns. This is how the deepeval framework grows organically.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/steps/step-04-component-check.md`
- Must contain:
  - **Pre-generation checkpoint (directed reading)**:
    1. Read target SKILL.md — identity, workflow, critical rules, file index
    2. Read step files in order — what each step does, reads, produces
    3. Read contracts — validation rules, expected behaviors, soft_validation_rules
    4. Read references — canonical patterns
    5. Checkpoint: summarize pipeline type, contract rules, output type, step count
  - **What to do**: check `_reference/` for existing metrics, tests, tasks, fixtures
  - **Decision table**: reference `references/step-04/component-decision-table.md`
  - **Creating new components**: read closest _reference/ implementation as pattern, follow same class structure/naming/return patterns, place in test repo's `framework/` (not master platform-deepeval)
  - **What to produce**: decision log (what was reused, what was created, rationale)
  - **Pattern adherence rules**: DeepEvalInterface methods first, Metric Objects return self, Tasks return None, metrics match pipeline type
  - **Error handling**: if _reference/ is empty or inaccessible, abort with clear error
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/dynamic-components.md`
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/steps/step-04-component-check.md`
- [ ] `grep -q "_reference" .claude/skills/eval/steps/step-04-component-check.md` passes
- [ ] `grep -q "component-decision-table" .claude/skills/eval/steps/step-04-component-check.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-08

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
