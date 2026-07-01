# Write step-04/component-decision-table.md

## Context
Layer 4 reference payload for Step 4 (Dynamic Component Check). Provides the decision matrix for determining whether to reuse existing _reference/ components or create new ones.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- File: `.claude/skills/eval/references/step-04/component-decision-table.md`
- Must contain:
  - **Decision table** with columns: What's Needed, Exists in _reference/?, Action
  - **Known existing components**: agent_metrics.py (ToolCorrectness, TaskCompletion), faithfulness_metrics.py (Faithfulness, contextual), custom_metrics.py (GEval template), test_rag_pipeline.py (RAG eval pattern), conftest.py (fixture loading), run_agent_eval.py (agent eval task), run_rag_eval.py (RAG eval task)
  - **Known missing components** (expected to be created): kernel-specific metrics (protocol faithfulness, step ordering), kernel eval task (multi-step command eval), test file for kernel commands
  - **Creation rules**: (1) read closest _reference/ implementation, (2) follow same class/naming/return patterns, (3) place in test repo's `framework/`, (4) document what was created
  - **Pattern adherence checklist**: DeepEvalInterface methods first, Metric Objects return self, Tasks return None, golden datasets are fixtures not hardcoded
- Source material: `docs/backlog/157-kernel-build-deepeval-command-testing/dynamic-components.md` (The Check + Decision sections)
- Must be under 200 lines

## Acceptance Criteria
- [ ] File exists at `.claude/skills/eval/references/step-04/component-decision-table.md`
- [ ] `grep -q "ToolCorrectness" .claude/skills/eval/references/step-04/component-decision-table.md` passes
- [ ] `grep -q "GEval" .claude/skills/eval/references/step-04/component-decision-table.md` passes
- [ ] `grep -q "_reference" .claude/skills/eval/references/step-04/component-decision-table.md` passes
- [ ] File is under 200 lines

## Gates Satisfied
BUILD-15

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
