# Task 004: Queryable Run-Status View
**Type:** BUILD | **Gates:** OBS-04
## Action
Add a single command/script (e.g., lib/kernel_status.py or a /kernel/status command) that prints per-agent/per-pipeline status across the workspace.
## Spec
Read all .claude/state/agent-*-workflow.json + heartbeats + the git branch/merge state, and print a compact table: agent/pipeline -> status (running | stalled | dead | complete-unmerged | merged) + last-activity + task progress. Composes the 001/002/003 helpers. This is the 'operator reads status without tailing raw JSONL' deliverable — the missing 5th harness layer. Read-only; no state writes.
## Acceptance
A working status command that lists every agent/pipeline with a resolved status, run live.
