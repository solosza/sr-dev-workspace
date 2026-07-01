# DeepEval Read-Tracking Custom Metric

## Status
Open

## Priority
High — Foundation for all tiered indexing validation. Backlogs 144 (A/B experiment) and future harness-level testing depend on this metric existing.

## Summary

Build a custom DeepEval metric that measures **procedure compliance** — specifically whether an agent read the required files before generating output. This extends the existing DeepEval harness (`test-platform-deepeval`) from standard LLM eval (faithfulness, relevance, hallucination) into **attention-control verification**, which is the core claim of the tiered indexing design.

Standard DeepEval metrics answer: "Was the output good?"
This metric answers: "Did the agent read the right files before producing the output?"

## Problem

The tiered indexing design (`projects/cognitive-design/tiered_indexing_design_v1.md`, `projects/isagawa-kernel/design/tiered-index-architecture.md`) claims that separating index files from payload files forces agents to read the right context. There is currently no way to verify this claim. The kernel has no instrumentation that proves the agent followed index links, read the correct payloads, or skipped files it should have read.

Without read-tracking:
- We assert the design works but can't measure it
- We can't detect index staleness (index points to file X, agent never reads X)
- We can't compare tiered vs flat structures empirically
- We can't identify which files agents consistently skip

## Design Documents

| Document | Purpose |
|----------|---------|
| [[143-kernel-build-deepeval-read-tracking-metric/read-tracking-metric-spec]] | Custom metric class spec: `ReadComplianceMetric` — inputs, scoring, threshold, integration with DeepEval's `GEval` base |
| [[143-kernel-build-deepeval-read-tracking-metric/instrumentation-design]] | How to capture `required_reads` vs `actual_reads` — hook-based logging, state file approach, or agent trace parsing |
| [[143-kernel-build-deepeval-read-tracking-metric/test-fixtures]] | Golden dataset for read-tracking: tasks with known required-read sets, expected pass/fail scenarios |
| [[143-kernel-build-deepeval-read-tracking-metric/integration-plan]] | How the metric fits into the existing 5-layer architecture (DeepEvalInterface, Metric Object, EvalTask, EvalRole, Test) |

## Architecture

```
Instrumentation Layer (new)
  ├─ Hook or wrapper that logs every file the agent reads
  ├─ Captures: file path, timestamp, task context
  ├─ Outputs: actual_reads[] per task execution
  │
  ↓
Read Compliance Metric (new Metric Object — Layer 2)
  ├─ Input: required_reads[] (from task spec or checkpoint)
  ├─ Input: actual_reads[] (from instrumentation)
  ├─ Score: |required_reads ∩ actual_reads| / |required_reads|
  ├─ Secondary: coverage = |actual_reads ∩ required_reads| / |actual_reads| (noise detection)
  ├─ Threshold: 1.0 (all required files must be read)
  ├─ Returns self (fluent pattern per SKILL.md rule 3)
  │
  ↓
Read Compliance EvalTask (new — Layer 3)
  ├─ Composes ReadComplianceMetric
  ├─ Loads required_reads from task checkpoint or gate contract
  ├─ Loads actual_reads from instrumentation log
  ├─ Runs metric, returns None
  │
  ↓
Integration into existing EvalRole (Layer 4)
  ├─ Agent evaluator role gains read-compliance step
  └─ Runs alongside existing agentic metrics (ToolCorrectness, TaskCompletion)
```

## Key Questions

- **Instrumentation method:** Hook-based (intercept Read tool calls via PostToolUse hook) vs state-file (agent self-reports reads) vs trace parsing (parse agent transcript for Read calls after execution)? Hook-based is most reliable but requires kernel hook changes. Trace parsing is non-invasive but brittle.
- **Required reads source:** Where does the "required_reads" list come from? Options: (a) gate contract JSON per step, (b) checkpoint header in task file, (c) protocol index links, (d) manually authored per test case.
- **Scoring granularity:** Binary (all-or-nothing) vs proportional (80% of required files = 0.8 score)? Proportional is more informative for diagnostics; binary is stricter for gating.
- **Noise metric:** Should we also score "read efficiency" — penalizing agents that read too many irrelevant files? This would test whether tiered indexing reduces unnecessary reads compared to flat structures.
- **External validator problem:** The agent is both executor and validator in gate contracts. The read-tracking metric must be validated externally (by the test harness, not the agent under test) to avoid self-grading bias.

## Existing Infrastructure to Build On

- `framework/_reference/metrics/custom_metrics.py` — GEval wrapper pattern, use as template for ReadComplianceMetric
- `framework/_reference/metrics/agent_metrics.py` — Agentic metric patterns (ToolCorrectness uses tools_called/expected_tools — same shape as actual_reads/required_reads)
- `framework/interfaces/deepeval_interface.py` — SDK wrapper layer, may need extension for read-log ingestion
- `.claude/hooks/universal-gate-enforcer.py` — Existing hook that tracks actions; could be extended to log Read tool calls
- `.claude/skills/deepeval-management-layer/` — Domain spec that governs how new metrics are built and integrated

## Deliverables

1. `ReadComplianceMetric` class (Layer 2 Metric Object) in `framework/_reference/metrics/`
2. `ReadComplianceEvalTask` (Layer 3) in `framework/_reference/tasks/`
3. Instrumentation module — captures actual_reads per task execution
4. Test fixtures — golden dataset with 10+ tasks, each specifying required_reads
5. pytest test file validating the metric against known pass/fail scenarios
6. Updated `metric-catalog.md` with ReadCompliance entry

## References

- **Tiered Indexing Design:** `projects/cognitive-design/tiered_indexing_design_v1.md`
- **Tiered Index Architecture:** `projects/isagawa-kernel/design/tiered-index-architecture.md`
- **Harness Design Pattern:** `docs/harness-design-pattern/HARNESS-DESIGN-PATTERN.md`
- **DeepEval Platform:** `test-platform-deepeval/` (GitHub: isagawa-qa/test-platform-deepeval)
- **DeepEval Domain Spec:** `test-platform-deepeval/.claude/skills/deepeval-management-layer/SKILL.md`
- **Backlog 133:** Harness Design Pattern Optimization (performance gap research)
- **Backlog 134:** Cross-Harness Testing Framework (testing methodology)
- **Backlog 144:** A/B Tiered Indexing Validation Experiment (depends on this backlog)

## Task Builder Input

- **Deliverable:** ReadComplianceMetric + instrumentation + test fixtures + integration into existing 5-layer architecture
- **Location:** `test-platform-deepeval:framework/_reference/metrics/` (metric), `test-platform-deepeval:framework/_reference/tasks/` (eval task), `test-platform-deepeval:tests/` (test file)
- **Scope:** BUILD
- **Constraints:**
  - Must follow existing 5-layer architecture (Interface → Metric Object → Task → Role → Test)
  - Metric Object returns self (fluent pattern per SKILL.md rule 3)
  - Golden datasets load from JSON fixtures via conftest.py (SKILL.md rule 5)
  - Instrumentation must work without modifying the agent under test (external observation)
  - Must integrate with pytest and existing `tests/run_coverage.py`
  - Read-tracking metric must be validated externally, not by the agent being evaluated
