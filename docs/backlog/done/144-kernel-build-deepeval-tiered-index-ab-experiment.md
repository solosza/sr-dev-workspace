# DeepEval Tiered Index A/B Validation Experiment

## Status
Open

## Priority
Medium-High — Depends on backlog 143 (read-tracking metric). This is the experiment that proves or disproves the tiered indexing design's core claims.

## Summary

Design and execute an A/B experiment comparing agent performance on **flat documentation** (single large files) vs **tiered indexed documentation** (index/payload split per the tiered indexing design). Uses the DeepEval harness with the ReadComplianceMetric from backlog 143 to measure attention control, failure modes, and output quality across identical tasks.

This is the empirical test of the claim: "Tiered indexing forces agents to read the right information at the right time."

## Problem

The tiered indexing design has been validated by usage (the kernel runs on it) but never by controlled experiment. We don't know:
- How much better tiered indexing actually is vs flat docs (if at all)
- Whether the improvement comes from the index/payload split, the 200-line threshold, or both
- What the failure mode difference looks like (silent drift vs detectable skip)
- Whether the overhead of maintaining indexes is justified by measurable reliability gains
- At what document size the tiered advantage appears (is it only for 500+ line files, or even at 200?)

## Design Documents

| Document | Purpose |
|----------|---------|
| [[144-kernel-build-deepeval-tiered-index-ab-experiment/experiment-design]] | Hypothesis, variables, controls, sample size, statistical method |
| [[144-kernel-build-deepeval-tiered-index-ab-experiment/test-fixture-design]] | Flat vs tiered fixture sets: identical content, different structure |
| [[144-kernel-build-deepeval-tiered-index-ab-experiment/task-catalog]] | 20+ tasks spanning: single-file lookup, cross-reference, contradiction handling, multi-step workflow, memory retrieval |
| [[144-kernel-build-deepeval-tiered-index-ab-experiment/metrics-and-scoring]] | Metric battery: ReadCompliance + Faithfulness + TaskCompletion + failure mode classification |
| [[144-kernel-build-deepeval-tiered-index-ab-experiment/execution-plan]] | Run protocol, token budget, iteration count, result collection |
| [[144-kernel-build-deepeval-tiered-index-ab-experiment/analysis-template]] | Report template: per-task scores, aggregate comparison, failure mode breakdown, cost analysis |

## Architecture

```
Test Fixture Generation
  ├─ Flat fixtures: single large .md files (300-800 lines each)
  ├─ Tiered fixtures: same content split into index + payloads (each < 200 lines)
  ├─ Content is IDENTICAL — only structure differs
  └─ 5+ domains (coding, research, workflow, memory, contradiction)
       ↓
Task Catalog (20+ tasks)
  ├─ Category 1: Single-file lookup (find specific info in docs)
  ├─ Category 2: Cross-reference (combine info from multiple sections)
  ├─ Category 3: Contradiction handling (doc says X, prompt says Y)
  ├─ Category 4: Multi-step workflow (follow sequential instructions)
  ├─ Category 5: Memory retrieval (recall prior decision, apply to new context)
  ├─ Category 6: Large-file stress (500+ line single file vs 3-level tiered split)
  └─ Each task has: input, expected_output, required_reads (for tiered), context
       ↓
A/B Execution
  ├─ Group A: Agent runs tasks against FLAT fixtures
  ├─ Group B: Agent runs tasks against TIERED fixtures
  ├─ Same model, same prompt template, same tasks
  ├─ Multiple runs per task (5+ for statistical significance)
  └─ Instrumented with read-tracking from backlog 143
       ↓
Metric Battery (per task execution)
  ├─ ReadComplianceMetric (backlog 143) — did it read the right files?
  ├─ FaithfulnessMetric — is the output grounded in the docs?
  ├─ TaskCompletionMetric — did it finish the task correctly?
  ├─ AnswerRelevancyMetric — does the output address the question?
  ├─ Failure mode classification (new) — HOW did it fail?
  │   ├─ Silent drift (wrong answer, no indication of uncertainty)
  │   ├─ Partial read (read some required files, skipped others)
  │   ├─ Hallucination (fabricated content not in any source file)
  │   └─ Contradiction ignored (prompt conflicts with docs, agent didn't flag)
  └─ Cost metrics — token count, completion time per task
       ↓
Analysis & Report
  ├─ Per-task comparison (flat score vs tiered score)
  ├─ Per-category aggregate (which task types benefit most from tiered?)
  ├─ Failure mode distribution (flat: mostly silent drift? tiered: mostly detectable skip?)
  ├─ Read efficiency (flat: reads everything? tiered: reads only what index points to?)
  ├─ Cost comparison (tiered may cost more tokens due to multiple reads)
  └─ Verdict: does tiered indexing measurably improve agent reliability?
```

## Task Categories — Detail

### Category 1: Single-File Lookup
Agent must find a specific fact buried in documentation.
- **Flat:** Fact is on line 347 of a 500-line file
- **Tiered:** Fact is in `topic-b/subtopic-2.md` (40 lines), linked from index
- **Measures:** Does the agent find the fact? How long does it take?

### Category 2: Cross-Reference
Agent must combine information from two separate sections to answer a question.
- **Flat:** Both sections in one file, 200 lines apart
- **Tiered:** Each section in its own payload, both linked from same index
- **Measures:** Does the agent read both sources? Does it synthesize correctly?

### Category 3: Contradiction Handling
Documentation says one thing, the user prompt says another.
- **Flat:** Contradicting info buried in a large file the agent may skim
- **Tiered:** Contradicting info in a focused payload the agent is directed to read
- **Measures:** Does the agent detect the contradiction? Does it flag it or silently follow the prompt?

### Category 4: Multi-Step Workflow
Agent must follow sequential instructions across multiple steps.
- **Flat:** All steps in one file, with dependencies between them
- **Tiered:** Each step in its own file, index specifies execution order
- **Measures:** Does the agent follow all steps? Does it skip any? Does it follow them in order?

### Category 5: Memory Retrieval
Agent must recall a prior decision and apply it to a new context.
- **Flat:** Decision documented in a large "decisions log" file
- **Tiered:** Decision in a focused payload under `decisions/topic.md`
- **Measures:** Does the agent find and apply the prior decision? Does it contradict it?

### Category 6: Large-File Stress
Stress test with intentionally oversized documentation (500-800 lines).
- **Flat:** One monolithic file
- **Tiered:** Same content split into 3-level index hierarchy
- **Measures:** At what size does the tiered advantage appear? Is there a crossover point?

## Key Questions

- **Model variable:** Should we test on multiple models (Opus, Sonnet, Haiku) or hold model constant? Multiple models would show whether tiered indexing helps more for weaker models.
- **Run count:** How many runs per task for statistical significance? 5 minimum, 10 ideal, but token cost is real. Budget analysis needed.
- **Fixture realism:** Should flat fixtures be realistic (how docs actually look in the wild) or synthetic (controlled content)? Synthetic is more rigorous but less convincing.
- **Failure mode taxonomy:** The 4 failure modes listed (silent drift, partial read, hallucination, contradiction ignored) may not be exhaustive. Should we discover failure modes from data rather than pre-defining them?
- **Baseline question:** What's the null hypothesis threshold? If tiered scores 5% higher, is that meaningful? Need to define minimum meaningful difference before running.
- **Hook-level tests:** Should this experiment also test whether kernel hooks (gate enforcer, anchor) behave differently with flat vs tiered structures? Or keep the experiment pure (no hooks, just docs)?

## Existing Infrastructure to Build On

- **Backlog 143 deliverables:** ReadComplianceMetric, instrumentation, read-tracking test fixtures
- `framework/_reference/metrics/` — All existing metrics (Faithfulness, Relevancy, Agent metrics)
- `framework/_reference/roles/agent_evaluator.py` — Agent eval role, extend for A/B comparison
- `framework/_reference/tests/conftest.py` — Fixture loading pattern
- `framework/resources/eval_config.py` — Eval configuration, extend for A/B experiment config
- `.claude/skills/deepeval-management-layer/workflow.md` — Workflow for generating eval suites
- `projects/cognitive-design/tiered_indexing_design_v1.md` — Design under test
- `projects/isagawa-kernel/design/tiered-index-architecture.md` — Architecture under test

## Deliverables

1. Experiment design document with hypothesis, variables, controls, and statistical method
2. Flat fixture set — 5+ domains, 20+ tasks, single-file format (300-800 lines each)
3. Tiered fixture set — identical content restructured as index/payload (each file < 200 lines)
4. Task catalog — 20+ tasks across 6 categories with golden expected outputs
5. Failure mode classifier — custom GEval metric that categorizes HOW a failure occurred
6. A/B execution harness — pytest suite that runs both groups, collects all metrics
7. Analysis report template — structured output comparing flat vs tiered across all metrics
8. Final report with verdict, data, and recommendations

## References

- **Backlog 143:** DeepEval Read-Tracking Custom Metric (DEPENDENCY — must complete first)
- **Backlog 133:** Harness Design Pattern Optimization (performance gap research, context for why this matters)
- **Backlog 134:** Cross-Harness Testing Framework (testing methodology, overlapping concerns)
- **Tiered Indexing Design:** `projects/cognitive-design/tiered_indexing_design_v1.md`
- **Tiered Index Architecture:** `projects/isagawa-kernel/design/tiered-index-architecture.md`
- **Harness Design Pattern:** `docs/harness-design-pattern/HARNESS-DESIGN-PATTERN.md`
- **DeepEval Platform:** `test-platform-deepeval/` (GitHub: isagawa-qa/test-platform-deepeval)
- **DeepEval Domain Spec:** `test-platform-deepeval/.claude/skills/deepeval-management-layer/SKILL.md`

## Task Builder Input

- **Deliverable:** A/B experiment infrastructure + fixture sets + task catalog + execution harness + analysis report
- **Location:** `test-platform-deepeval:tests/experiments/tiered-index-ab/` (experiment), `test-platform-deepeval:tests/fixtures/` (fixtures), `test-platform-deepeval:framework/_reference/metrics/` (failure mode classifier)
- **Scope:** BUILD + RESEARCH (build the harness, run the experiment, analyze results)
- **Constraints:**
  - Flat and tiered fixtures must contain IDENTICAL content — only structure differs
  - Tasks must be runnable by the agent without human intervention (autonomous execution)
  - Must use ReadComplianceMetric from backlog 143 (hard dependency)
  - Must use existing DeepEval metrics alongside custom metrics (not replace them)
  - Results must include per-task and aggregate scoring with statistical significance
  - Failure mode classification must be external (LLM-as-judge on agent trace, not self-reported)
  - Token budget estimate required before execution (experiment could be expensive)
  - Report must include a clear verdict: does tiered indexing measurably improve agent reliability, and by how much?
