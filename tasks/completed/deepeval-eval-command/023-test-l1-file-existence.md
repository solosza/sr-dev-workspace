# L1 Test: All Eval Command Files Exist

## Context
Level 1 verification — confirm every file in the eval command's 6-layer structure exists at the correct path. This is a mechanical file-existence check, no content validation.

## Type
TEST

## Execution
agent

## Dependencies
- 001 through 022 (all BUILD tasks)

## Phase Gate
- [ ] All 22 BUILD tasks completed

## Requirements
- Verify ALL of the following files exist:
  - `.claude/commands/kernel/eval.md`
  - `.claude/skills/eval/SKILL.md`
  - `.claude/skills/eval/workflow.md`
  - `.claude/skills/eval/gate-contract.md`
  - `.claude/skills/eval/steps/step-01-create-test-repo.md`
  - `.claude/skills/eval/steps/step-02-compile-harness.md`
  - `.claude/skills/eval/steps/step-03-copy-artifact.md`
  - `.claude/skills/eval/steps/step-04-component-check.md`
  - `.claude/skills/eval/steps/step-05-generate-tests.md`
  - `.claude/skills/eval/steps/step-06-run-and-score.md`
  - `.claude/skills/eval/references/INDEX.md`
  - `.claude/skills/eval/references/step-02/kernel-file-list.md`
  - `.claude/skills/eval/references/step-02/deepeval-file-list.md`
  - `.claude/skills/eval/references/step-03/dependency-resolution.md`
  - `.claude/skills/eval/references/step-04/component-decision-table.md`
  - `.claude/skills/eval/references/step-05/golden-translation-patterns.md`
  - `.claude/skills/eval/references/step-06/metric-selection.md`
  - `.claude/skills/eval/references/step-06/report-format.md`
  - `.claude/skills/eval/contracts/step-02-contract.json`
  - `.claude/skills/eval/contracts/step-03-contract.json`
  - `.claude/skills/eval/contracts/step-05-contract.json`
  - `.claude/skills/eval/contracts/step-06-contract.json`
- Run `test -f [path]` for each file
- Report any missing files

## Acceptance Criteria
- [ ] All 22 files exist (0 missing)
- [ ] All BUILD gates (BUILD-01 through BUILD-22) satisfied

## Gates Satisfied
BUILD-01 through BUILD-22 (verification), INT-07 (200-line check)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
