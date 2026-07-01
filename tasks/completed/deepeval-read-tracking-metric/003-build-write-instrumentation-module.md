# Write Instrumentation Module

## Context
Module that extracts `actual_reads` from agent execution traces. Parses a trace log (JSONL or structured text) to identify which files the agent read during task execution. This is the bridge between agent behavior and the ReadComplianceMetric.

## Type
BUILD

## Execution
inline

## Dependencies
- 001-build-create-feature-branch

## Phase Gate
- [ ] Branch `feature/143-read-tracking-metric` is checked out

## Requirements
- File: `D:/my_ai_projects/project_test_repos/test-platform-deepeval/framework/_reference/metrics/instrumentation.py`
- Class `ReadTraceParser` with:
  - `__init__(self, trace_source: str | list[dict])` — accepts file path to JSONL trace or pre-parsed list of action dicts
  - `parse(self) -> list[str]` — extracts file paths from Read tool calls in the trace. Returns list of absolute paths that were read.
  - `from_actions_jsonl(cls, filepath: str) -> "ReadTraceParser"` — class method, parses kernel `actions.jsonl` format (each line: `{"timestamp": "...", "tool": "Read", "entry": "Read: filepath"}`)
  - `from_action_list(cls, actions: list[dict]) -> "ReadTraceParser"` — class method, parses list of action dicts
- Handles both Read tool entries and file paths embedded in Bash commands (e.g., `cat file.md`)
- Returns deduplicated, sorted list of file paths
- Docstring: `"""ReadTraceParser — Extracts actual_reads from agent execution traces."""`

## Acceptance Criteria
- [ ] File exists at `framework/_reference/metrics/instrumentation.py`
- [ ] `grep -q "class ReadTraceParser" framework/_reference/metrics/instrumentation.py` passes
- [ ] `grep -q "def parse" framework/_reference/metrics/instrumentation.py` passes

## Gates Satisfied
- BUILD-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
