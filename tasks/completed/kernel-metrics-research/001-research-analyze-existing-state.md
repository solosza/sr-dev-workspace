# Task 001: Analyze Existing Kernel State Files

## Type
RESEARCH

## Description
Analyze the existing kernel state files to determine what metrics are capturable today without new instrumentation. Read actions.jsonl, anchor-logs, workflow.json, session_state.json, and lessons.md to catalog available data points.

## Acceptance Criteria
- [ ] List of all data points capturable from existing state files
- [ ] Sample data extraction from at least 3 anchor-log archives
- [ ] Gap analysis: what's capturable vs what requires new instrumentation

## References
- `.claude/state/actions.jsonl` — action log
- `.claude/state/anchor-logs/` — archived action batches
- `.claude/state/sr_dev_workflow.json` — workflow state
- `.claude/state/session_state.json` — session state
- `.claude/lessons/lessons.md` — lessons log
