# Research: Kernel Metrics Database

## Status
Open

## Priority
High — foundational for self-improvement claims; without metrics, "the system got smarter" is a feeling, not a fact

## Summary
Research how to add quantitative performance tracking to the kernel. Currently the kernel has lessons (qualitative) but no metrics (quantitative). Need to design a metrics database that tracks task completion rate, failure rate, actions-per-task, time-to-complete, and lessons-per-pipeline over time. This is the foundation for all other self-improvement capabilities (experiment tracking, auto-evaluation, rollback).

## Requirements
- Research what metrics to capture from existing kernel state (actions.jsonl, workflow.json, session_state.json, lessons.md)
- Research storage format: JSONL append log vs SQLite vs structured markdown
- Research how to instrument the kernel loop (session-start, anchor, complete, learn) to emit metrics without adding overhead
- Research visualization/reporting: how to surface trends (e.g., "failure rate declining over last 10 pipelines")
- Research how other agent frameworks track performance metrics (LangSmith, Weights & Biases, MLflow)
- Identify what's capturable today vs what requires new instrumentation

## References
- `.claude/state/actions.jsonl` — current action log (qualitative)
- `.claude/state/anchor-logs/` — archived action batches
- `.claude/state/sr_dev_workflow.json` — current workflow state
- Backlog 143-144 (DeepEval metrics work)
- LangSmith, W&B, MLflow for prior art

## Task Builder Input
- **Deliverable:** Research report with metrics schema design and instrumentation plan
- **Location:** subproject:kernel-metrics-research
- **Scope:** RESEARCH
- **Constraints:** Must not add overhead to the kernel loop. Must work with existing state file architecture.
