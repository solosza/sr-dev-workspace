# Write step-05/golden-translation-patterns.md

## Context
Layer 4 reference payload for Step 5 (Generate Tests). A reference pattern the eval agent consults when it determines golden datasets are appropriate. NOT a hardcoded pipeline — the agent dynamically decides whether and how to use this based on the artifact.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-05/golden-translation-patterns.md`
- Must contain:
  - **When this reference applies**: target has contract JSONs with soft_validation_rules, success_criteria, or expected_artifacts
  - **When NOT to use**: no contracts, artifact better served by structural/behavioral metrics only
  - **Contract-to-golden mapping table**: contract field -> golden field -> how
    - Step file instruction -> `input` (what LLM is asked)
    - `success_criteria` -> `expected_output` (correct behavior)
    - Step references -> `context` (reference material)
    - `soft_validation_rules` -> GEval criteria (each rule becomes scoring criterion)
    - `expected_artifacts` -> ToolCorrectness assertions (expected files)
  - **DeepEval golden schema**: LLMTestCase(input, expected_output, context, retrieval_context)
  - **Severity-to-threshold mapping**: high=0.80, medium=0.70, low=0.60
  - **Example**: step-03-contract.json with SV-301 translated to LLMTestCase + GEvalMetric
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/golden-dataset-translation.md`
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-05/golden-translation-patterns.md`
- [ ] `grep -q "LLMTestCase" .claude/skills/eval/references/step-05/golden-translation-patterns.md` passes
- [ ] `grep -q "soft_validation_rules" .claude/skills/eval/references/step-05/golden-translation-patterns.md` passes
- [ ] `grep -q "0.80" .claude/skills/eval/references/step-05/golden-translation-patterns.md` passes (threshold)
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-16

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
