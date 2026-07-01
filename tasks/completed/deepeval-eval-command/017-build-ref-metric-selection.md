# Write step-06/metric-selection.md

## Context
Layer 4 reference payload for Step 6 (Run and Score). Defines which deepeval metrics are appropriate for which pipeline/artifact types. The eval agent consults this when selecting metrics for the test suite.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-06/metric-selection.md`
- Must contain:
  - **Pipeline type to metric mapping table**:
    - Agent pipeline (kernel commands): ToolCorrectness, TaskCompletion, GEval (per contract rule)
    - RAG pipeline: Faithfulness, ContextualRelevancy, AnswerRelevancy
    - Hybrid (agent + RAG): all of the above
    - Structural (no contracts): file existence checks, output format validation
  - **Metric sources**: existing _reference/ metrics vs. newly created in Step 4
  - **Threshold defaults**: high=0.80, medium=0.70, low=0.60 (from contract severity)
  - **Metric combination rules**: always include at least one pipeline-type metric + one per-contract GEval metric (when contracts exist)
  - **Override guidance**: agent may adjust thresholds based on artifact context, but must document rationale
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-06/metric-selection.md`
- [ ] `grep -q "ToolCorrectness" .claude/skills/eval/references/step-06/metric-selection.md` passes
- [ ] `grep -q "Faithfulness" .claude/skills/eval/references/step-06/metric-selection.md` passes
- [ ] `grep -q "threshold" .claude/skills/eval/references/step-06/metric-selection.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-17

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
