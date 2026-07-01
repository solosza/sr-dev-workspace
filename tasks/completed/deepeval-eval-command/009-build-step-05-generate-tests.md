# Write step-05-generate-tests.md

## Context
Layer 3 step file for test generation. The agent dynamically builds deepeval tests based on what it's testing and what it found in Step 4. Consults _reference/ patterns for golden datasets, metrics, and test structure — but adapts to the artifact, not the other way around.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/steps/step-05-generate-tests.md`
- Must contain:
  - **What to do**: generate pytest-based deepeval test suite dynamically based on artifact analysis from Step 4
  - **Pre-generation checkpoint**: read `references/step-05/golden-translation-patterns.md` for golden dataset patterns (when contracts exist)
  - **What to produce**: conftest.py (fixture loading), test file(s) with parametrized test cases, metric instances with thresholds
  - **Golden dataset generation**: when contracts exist with soft_validation_rules/success_criteria, translate to LLMTestCase instances (input from step instructions, expected_output from success_criteria, context from references)
  - **Metric selection**: choose metrics based on pipeline type and artifact analysis (ToolCorrectness for agent pipelines, GEval for custom contract rules, etc.)
  - **Threshold mapping**: high severity = 0.80, medium = 0.70, low = 0.60 (defaults, adjustable)
  - **Verification**: conftest.py exists, fixtures load without error, at least one test case exists
  - **Error handling**: if no contracts exist, use structural/behavioral metrics instead of golden datasets
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/golden-dataset-translation.md`
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/steps/step-05-generate-tests.md`
- [ ] `grep -q "golden" .claude/skills/eval/steps/step-05-generate-tests.md` passes
- [ ] `grep -q "conftest" .claude/skills/eval/steps/step-05-generate-tests.md` passes
- [ ] `grep -q "threshold" .claude/skills/eval/steps/step-05-generate-tests.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-09

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
