# Kernel Metrics Database — Research Report

**Backlog:** 164-kernel-research-metrics-database
**Date:** 2026-06-28
**Status:** Complete

## Executive Summary

The kernel already has 433 anchor logs spanning 90 days, tracking 7,320 actions with 16 violations. This data is rich but unstructured for trend analysis. A metrics database would formalize what's already captured and add the missing quantitative dimensions: task completion rate, time-to-complete, actions-per-task, and failure rate. The recommended approach is a JSONL append log (`metrics.jsonl`) emitted at pipeline boundaries, with a Python aggregator script for trend analysis.

## Part 1: Existing State File Analysis

### What Exists Today

| State File | Data Points | Capturable Metrics |
|-----------|------------|-------------------|
| `actions.jsonl` | timestamp, tool, entry | Actions per session, tool distribution, action frequency |
| `anchor-logs/` | anchor_timestamp, actions_count, violations_found, actions[] | Actions per anchor, violation rate, violation trend, tool usage |
| `sr_dev_workflow.json` | completed_tasks, skipped_tasks, cycling state | Task completion rate, skip rate, cycling duration |
| `session_state.json` | context, pipeline_state, anchor_ceremony | Pipeline throughput, context persistence |
| `lessons.md` | lesson entries by date | Lessons per period, recurring patterns, lesson categories |
| `attestations/` | signed attestation receipts | Pipeline completion rate, attestation coverage |

### Quantitative Snapshot (from 433 anchor logs)

| Metric | Value |
|--------|-------|
| Total anchor logs | 433 |
| Active dates | 34 |
| Total actions tracked | 7,320 |
| Total violations | 16 |
| Avg actions/anchor | 16.9 |
| Min/Max actions/anchor | 0 / 200 |
| Tool distribution | Bash: 3,551 (48.5%), Write: 1,265 (17.3%), Edit: 579 (7.9%) |
| Completed backlogs | 197 |
| Completed task folders | 161 |
| Violation dates | 4 (concentrated in Apr 28, May 26-29) |

### Gap Analysis: Capturable vs Requires Instrumentation

**Capturable today (no new code):**
- Actions per anchor (from anchor-logs)
- Violation rate over time (from anchor-logs)
- Tool usage distribution (from anchor-logs)
- Total backlogs completed (from docs/backlog/done/)
- Total tasks completed (from tasks/completed/)

**Requires new instrumentation:**
- Time-to-complete per pipeline (need start/end timestamps per pipeline)
- Actions-per-task (need per-task action counting, not just per-anchor)
- Failure rate per pipeline (need structured success/failure recording)
- Lessons-per-pipeline (need linking lessons to pipelines)
- Cost per pipeline (need token usage tracking — not available in Claude Code CLI)

## Part 2: Prior Art Comparison

### LangSmith (LangChain)
- **Metrics:** Token usage, latency (P50/P99), error rates, cost, feedback scores
- **Agent-level:** Resolution rate, escalation frequency, goal completion
- **Storage:** Cloud-hosted, SQL backend, dashboard visualizations
- **Relevance:** Session-level outcomes model maps to kernel pipeline-level metrics. Dashboard patterns applicable.

### MLflow
- **Metrics:** Parameters, metrics time series, artifact versioning
- **Storage:** File-system or SQL (PostgreSQL/MySQL). Experiment → Run → Metrics hierarchy.
- **Architecture:** Tracking Server + Model Registry + Evaluation Engine + Tracing System
- **Relevance:** Experiment → Run hierarchy maps to Pipeline → Task. Metrics time series pattern directly applicable.

### Weights & Biases
- **Metrics:** Loss curves, system metrics, custom logged values
- **Approach:** `wandb.log({"metric": value})` at any point — append-only logging
- **Relevance:** Simple append-only logging pattern is closest to kernel's JSONL architecture.

### OpenAI Self-Evolving Agents Cookbook
- **Approach:** Track adaptivity (learning curve), consistency scores, drift detection, recovery metrics
- **Pattern:** 30-60 day improvement cycles with quantitative before/after comparison
- **Relevance:** Directly applicable to experiment tracking (backlog 165). Adaptivity metric = kernel's violation rate trend.

### Key Takeaway

All major frameworks use append-only event streams with SQL or time-series backends for aggregation. The kernel's JSONL pattern is architecturally aligned with W&B's approach. No need for external infrastructure — a local JSONL + Python aggregator achieves the same result.

## Part 3: Metrics Schema Design

### Pipeline Metric Record

Emitted once per pipeline completion (in `/kernel/complete` or `run-task.sh` exit):

```json
{
  "schema_version": 1,
  "timestamp": "2026-06-28T19:30:00Z",
  "event": "pipeline_complete",
  "pipeline_id": "164",
  "backlog_path": "docs/backlog/164-kernel-research-metrics-database.md",
  "scope": "RESEARCH",
  "result": "PASS",
  "tasks_total": 3,
  "tasks_completed": 3,
  "tasks_skipped": 0,
  "actions_total": 15,
  "violations": 0,
  "lessons_recorded": 0,
  "anchors_performed": 2,
  "start_timestamp": "2026-06-28T19:30:00Z",
  "end_timestamp": "2026-06-28T20:15:00Z",
  "duration_minutes": 45,
  "execution_mode": "inline"
}
```

### Anchor Metric Record

Already exists in anchor-logs. Add to metrics.jsonl for unified querying:

```json
{
  "schema_version": 1,
  "timestamp": "2026-06-28T19:30:00Z",
  "event": "anchor",
  "actions_count": 10,
  "violations_found": 0,
  "tool_distribution": {"Bash": 5, "Write": 3, "Edit": 2}
}
```

### Learn Metric Record

Emitted when `/kernel/learn` records a lesson:

```json
{
  "schema_version": 1,
  "timestamp": "2026-06-28T19:30:00Z",
  "event": "learn",
  "trigger": "test_failure",
  "lesson_topic": "kernel-compliance",
  "pipeline_id": "164",
  "hooks_modified": false,
  "protocol_modified": false
}
```

### Storage Location

`.claude/state/metrics.jsonl` — append-only, one JSON object per line.

### Why JSONL Over SQLite

| Factor | JSONL | SQLite |
|--------|-------|--------|
| Simplicity | Append with echo/python | Requires sqlite3 module |
| Git-friendly | Diffable, mergeable | Binary blob |
| Query | Python script | SQL queries |
| Existing pattern | Matches actions.jsonl | New dependency |
| Overhead | Near-zero | Schema setup, connection management |
| Cross-agent safety | Append-only, no locks | WAL mode needed for concurrent writes |

**Recommendation: JSONL.** The kernel already uses JSONL for actions. Same pattern, same tooling. A Python aggregator script replaces SQL queries.

## Part 4: Instrumentation Plan

### Emission Points (where metrics get written)

| Kernel Event | Metric Event | Instrumentation |
|-------------|-------------|-----------------|
| `/kernel/complete` | `pipeline_complete` | Add metric append after completion validation |
| `/kernel/anchor` (Part C) | `anchor` | Already captured in anchor-logs; add to metrics.jsonl |
| `/kernel/learn` | `learn` | Add metric append after lesson is recorded |
| `run-task.sh` exit | `task_complete` | Add metric append in run-task.sh cleanup |

### Aggregator Script

`lib/metrics/aggregate.py` — reads `metrics.jsonl`, produces trend reports:

```
python lib/metrics/aggregate.py --last 30d
python lib/metrics/aggregate.py --pipeline 164
python lib/metrics/aggregate.py --trend violations
```

Output: JSON or markdown table with computed metrics (averages, trends, rates).

### Implementation Phases

| Phase | Work | Dependency |
|-------|------|-----------|
| 1 | Create `metrics.jsonl`, add emission to `/kernel/complete` | None |
| 2 | Add emission to `/kernel/anchor` and `/kernel/learn` | Phase 1 |
| 3 | Build `aggregate.py` with trend reports | Phase 2 |
| 4 | Backfill from 433 existing anchor-logs | Phase 3 |
| 5 | Wire into experiment tracking (backlog 165) | Phase 3 + backlog 165 |

### Cost and Overhead

- **Write cost:** One JSONL append per pipeline (~200 bytes). Negligible.
- **Read cost:** Aggregator reads full file. At 1 pipeline/day for a year = ~73KB. Trivially small.
- **No external services.** No API keys. No infrastructure.
- **Token cost:** Zero — metrics are structural, not LLM-evaluated.

## Conclusion

The kernel has rich qualitative data (433 anchor logs, 7,320 actions, 197 completed backlogs) but no quantitative trend analysis. A JSONL metrics database with 3 event types (pipeline_complete, anchor, learn) and a Python aggregator script closes this gap with minimal overhead. Phase 1 (pipeline metrics) can ship independently. Phases 2-4 build incrementally. Phase 5 connects to experiment tracking (backlog 165).

## Sources

- [LangSmith Observability Platform](https://www.langchain.com/langsmith/observability)
- [MLflow AI Platform — Experiment Tracking](https://mlflow.org/docs/latest/ml/tracking/)
- [W&B — Evaluating Autonomous AI Agents](https://wandb.ai/site/articles/evaluating-autonomous-ai-agents/)
- [OpenAI Self-Evolving Agents Cookbook](https://developers.openai.com/cookbook/examples/partners/self_evolving_agents/autonomous_agent_retraining)
- [AI Agent Observability in 2026](https://dev.to/chunxiaoxx/ai-agent-observability-in-2026-openai-agents-sdk-langsmith-and-opentelemetry-3ale)
- [Microsoft AI Agent Performance Measurement](https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/02/04/ai-agent-performance-measurement/)
- [DataRobot — How to Measure Agent Performance](https://www.datarobot.com/blog/how-to-measure-agent-performance/)
