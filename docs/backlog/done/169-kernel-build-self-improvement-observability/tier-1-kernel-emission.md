# Tier 1: Kernel Emission Hooks

## Status
NEW

## Location
`D:\my_ai_projects\isagawa-kernel`

## What It Does
Adds 1-2 line metric emission statements to core kernel commands so they append structured JSON events to `.claude/state/metrics.jsonl` at key lifecycle boundaries.

## Commands to Modify

### `/kernel/learn` (learn.md)
After lesson is recorded and files are modified:
```
Append to .claude/state/metrics.jsonl:
{"schema_version":1,"timestamp":"...","event":"learn","trigger":"...","lesson_topic":"...","files_modified":["..."]}
```

### `/kernel/complete` (complete.md)
After completion validation:
```
Append to .claude/state/metrics.jsonl:
{"schema_version":1,"timestamp":"...","event":"pipeline_complete","pipeline_id":"...","result":"PASS|PARTIAL|FAIL","tasks_total":N,"tasks_completed":N,"tasks_skipped":N,"violations":0}
```

### `/kernel/anchor` (anchor.md)
After anchor ceremony completes (Part C):
```
Append to .claude/state/metrics.jsonl:
{"schema_version":1,"timestamp":"...","event":"anchor","actions_count":N,"violations_found":N}
```

## Implementation Pattern
Each emission is a single bash command appended to the command's instruction flow:
```bash
echo '{"schema_version":1,...}' >> .claude/state/metrics.jsonl
```

Or a Python one-liner for JSON serialization:
```bash
python -c "import json,sys; print(json.dumps({...}))" >> .claude/state/metrics.jsonl
```

## Constraints
- NO new dependencies added to isagawa-kernel
- NO new files created (metrics.jsonl is created on first append)
- NO logic changes to existing command behavior
- Emission is append-only — failure to emit does not block the command
- Each modification is 1-2 lines added to the existing command markdown

## Dependencies
- None — this tier is independently shippable

## Acceptance Criteria
- learn.md emits a learn event after every lesson recording
- complete.md emits a pipeline_complete event after every completion
- anchor.md emits an anchor event after every anchor ceremony
- metrics.jsonl is valid JSONL (one JSON object per line)
- Existing kernel tests (platform-deepeval) still pass after changes
