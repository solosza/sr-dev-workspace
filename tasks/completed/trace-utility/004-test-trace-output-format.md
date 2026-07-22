# Test: trace Output Format (L3)

## Context
Backlog 199 (V-BASE): the decorator's real job is the hierarchical START/END trace through the logging system — verify the actual output, not just that it runs.

## Type
TEST

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] trace.py exists on the feature branch (TRC-02)

## Requirements
- Run a python script: attach a logging handler capturing records, call a `@trace("Task")`-decorated function, assert captured output contains a `[Task]`-tagged `- START` line and `- END` line (with duration) — matching the contract's Runtime Output example shape
- Non-zero exit = failure → fix → /kernel/learn

## Acceptance Criteria
- [ ] Script exits 0 (START and END lines present, correctly tagged)

## Gates Satisfied
- TRC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
