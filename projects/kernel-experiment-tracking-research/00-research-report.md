# Kernel Experiment Tracking — Research Report

**Backlog:** 165-kernel-research-experiment-tracking
**Date:** 2026-06-28
**Status:** Complete

## Executive Summary

The kernel changes protocols and hooks via `/kernel/learn` but never measures whether changes improved outcomes. An experiment tracking system would tag each learn event as an "experiment," define success criteria, then compare metrics before and after over a window of N pipelines. The recommended approach: a lightweight `experiments.jsonl` file linked to `metrics.jsonl` (backlog 164), using anchor-log data as the comparison window.

## Part 1: The Problem

When `/kernel/learn` modifies a hook or protocol, the change is assumed to be an improvement. Examples of unmeasured changes:

| Change | Question | Answer Today |
|--------|----------|-------------|
| Added cd blocker hook | Did cd violations drop to zero? | "Probably" (feeling) |
| Added tiered indexing | Did agent drift decrease? | Unknown |
| Added test failure detector | Do test failures always trigger learn? | Unknown |
| Increased actions_limit to 30 | Did anchor frequency change appropriately? | Unknown |

Violation data from anchor-logs shows improvement is possible to measure:
- **Before May 26:** 3 violations on Apr 28
- **May 26-29:** 13 violations (11 on May 26 alone — multi-agent swarm run)
- **After May 29:** 0 violations across 100+ anchor logs

This trend IS evidence — but it's captured accidentally, not systematically.

## Part 2: Prior Art

### MLflow Experiment → Run Model
- **Experiment** = a named container (e.g., "cd-blocker-hook")
- **Run** = one execution with parameters and metrics
- **Comparison** = `search_runs()` across experiments, filter by metric
- **Relevance:** Experiment → Run maps to Kernel Change → Pipeline. Each pipeline after a change is a "run" in the experiment.

### Feature Flag / Canary Model
- **Gradual rollout:** 1% → 5% → 25% → 100% with monitoring at each stage
- **Automated rollback:** If error rate exceeds threshold, revert instantly
- **Relevance:** Not directly applicable — kernel doesn't have traffic splits. But the "monitor at each stage" and "automated rollback trigger" patterns apply.
- **Note:** Statsig acquired by OpenAI in 2025 — agent experimentation is becoming first-class infrastructure.

### W&B / DataRobot 30-60 Day Cycles
- Track failures and successes, identify skill gaps, retrain within cycles
- Adaptivity metric: quantify learning curve as agent iterates
- **Relevance:** The kernel already operates in pipeline cycles. Experiment windows of 5-10 pipelines are the natural measurement unit.

## Part 3: Experiment Lifecycle Design

### 1. Experiment Creation (at `/kernel/learn` time)

When `/kernel/learn` modifies a hook or protocol, automatically create an experiment:

```json
{
  "experiment_id": "exp-2026-06-28-cd-blocker",
  "created_at": "2026-06-28T19:30:00Z",
  "trigger": "learn",
  "change_type": "hook_added",
  "change_description": "Added cd blocker to sr_dev-gate-enforcer.py",
  "files_modified": [".claude/hooks/sr_dev-gate-enforcer.py"],
  "hypothesis": "cd violations will drop to zero",
  "success_criteria": {
    "metric": "violations_with_cd",
    "target": 0,
    "window": 10,
    "comparison": "post_change_avg < pre_change_avg"
  },
  "status": "active",
  "baseline_window": {
    "start_pipeline": 150,
    "end_pipeline": 159,
    "baseline_value": 2.3
  }
}
```

### 2. Data Collection (automatic via metrics.jsonl)

Each pipeline completion writes to `metrics.jsonl` (backlog 164). The experiment system reads these entries and associates them with active experiments by timestamp.

### 3. Evaluation (after N pipelines)

When `window` pipelines have completed since experiment creation:

```python
pre_window = metrics_before(experiment.created_at, window=10)
post_window = metrics_after(experiment.created_at, window=10)

result = compare(pre_window, post_window, experiment.success_criteria)
# → "IMPROVED", "NO_CHANGE", "DEGRADED"
```

### 4. Verdict

```json
{
  "experiment_id": "exp-2026-06-28-cd-blocker",
  "verdict": "IMPROVED",
  "pre_avg": 2.3,
  "post_avg": 0.0,
  "improvement_pct": 100,
  "evaluated_at": "2026-07-08T19:30:00Z",
  "status": "concluded"
}
```

## Part 4: Integration with Metrics Database

### Data Flow

```
/kernel/learn → creates experiment in experiments.jsonl
                 ↓
pipelines run → emit metrics to metrics.jsonl
                 ↓
experiment evaluator → reads both files
                 ↓
verdict → update experiment status
          optionally trigger rollback (backlog 167)
```

### Success Criteria Patterns

| Change Type | Metric | Target | Window |
|------------|--------|--------|--------|
| Hook added (blocker) | Specific violation count | 0 | 5 pipelines |
| Protocol updated | Actions-per-task trend | Decrease | 10 pipelines |
| Lesson added | Recurring lesson count | 0 | 10 pipelines |
| Skill modified | Task completion rate | ≥ baseline | 5 pipelines |

### Anchor-Logs as Baseline Data

The 433 existing anchor-logs can serve as historical baseline for any experiment created today. The aggregator can compute:
- Pre-change violation rate from logs before the change date
- Pre-change actions-per-anchor from logs before the change date
- Pre-change tool distribution from logs before the change date

This means experiments can be created retroactively for past `/kernel/learn` events — if we can identify when each learn occurred (from lessons.md timestamps).

## Part 5: Storage Design

### `experiments.jsonl`

Location: `.claude/state/experiments.jsonl`

One JSON object per line. Append-only. Each experiment has:
- `experiment_id` — unique identifier
- `created_at` — when the change was made
- `change_description` — what changed
- `success_criteria` — how to measure
- `status` — active | concluded | abandoned
- `verdict` — null | IMPROVED | NO_CHANGE | DEGRADED

### Evaluator Script

`lib/metrics/evaluate_experiments.py`:
- Reads `experiments.jsonl` and `metrics.jsonl`
- For each active experiment past its window, computes verdict
- Updates experiment status
- Optionally triggers rollback signal (backlog 167)

## Part 6: Implementation Plan

| Phase | Work | Dependency |
|-------|------|-----------|
| 1 | Create `experiments.jsonl` schema | None |
| 2 | Add experiment creation to `/kernel/learn` | Phase 1 |
| 3 | Build evaluator script | Phase 2 + metrics.jsonl (backlog 164) |
| 4 | Backfill experiments from lessons.md timestamps | Phase 3 |
| 5 | Wire evaluator into `/kernel/anchor` or scheduled check | Phase 3 |
| 6 | Connect to rollback mechanism (backlog 167) | Phase 5 + backlog 167 |

## Conclusion

Experiment tracking transforms kernel changes from faith-based to evidence-based. The infrastructure is lightweight (one JSONL file, one Python script), builds directly on the metrics database (backlog 164), and can retroactively evaluate past changes using 433 existing anchor-logs. The MLflow Experiment → Run model maps cleanly to Kernel Change → Pipeline, and the W&B 30-60 day cycle pattern maps to 5-10 pipeline evaluation windows.

## Sources

- [MLflow Experiment Tracking](https://mlflow.org/docs/latest/ml/tracking/)
- [MLflow Run Comparison](https://apxml.com/courses/data-versioning-experiment-tracking/chapter-3-tracking-experiments-mlflow/comparing-mlflow-runs)
- [Feature Flags vs A/B Testing (2026)](https://pulsecro.com/blog/2026-04-27-feature-flag-ab-testing/)
- [A/B Testing AI Agents](https://www.buildmvpfast.com/blog/ab-testing-ai-agents-experiment-production-behavior-2026)
- [Feature Flag Rollout Strategies 2026](https://www.digitalapplied.com/blog/feature-flag-rollout-strategies-2026-engineering-playbook)
