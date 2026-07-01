# Agent Output Capture: Getting actual_output for DeepEval

## Status
NEW

## Purpose

DeepEval needs `actual_output` to score against `expected_output`. For kernel commands, the "output" is: files written, state changes, and agent reasoning displayed to the user. Define how to capture this for evaluation.

## The Problem

A kernel command like check-data produces:
- **Files written:** xlsx updates (Col H, R, S), state JSON updates
- **State changes:** date registry entries, TC queue modifications
- **Agent reasoning:** displayed text ("HISTORY: Claim ID: ...", "CONSTRAINTS: PASS")
- **Decisions made:** DRG lookup results, date assignments, violation flags

DeepEval's LLMTestCase needs a single `actual_output` string. How do we capture the above into that?

## Capture Strategy

### Option A: State diff (recommended for file-producing commands)

1. **Snapshot state before command runs.** Copy all state files, xlsx, contracts.
2. **Run command** (inner task execution via run-task.sh).
3. **Snapshot state after.** Copy updated files.
4. **Diff = actual_output.** The diff between before/after state is the command's output.

```json
{
  "actual_output": {
    "files_changed": ["check-data-state.json", "test-cases-sit.xlsx"],
    "state_diff": {
      "date_registry": {"R00002417147200": [{"admit": "11/01/2025", "discharge": "11/03/2025", "tc": "TC-002"}]},
      "completed": ["TC-002"],
      "tc_queue": ["TC-005", "TC-007", ...]
    },
    "xlsx_diff": {
      "row_4_col_H": "1. 837BT: pull X34216393333...",
      "row_4_col_S": "History claim: 837BT: change DOS..."
    }
  }
}
```

### Option B: Agent trace capture (for reasoning evaluation)

Use Claude Code's `--output-format json` or transcript logging to capture the agent's reasoning output. Parse into `actual_output`.

More complex but enables faithfulness evaluation ("did the agent mention checking the exclusion list?").

### Option C: Hybrid (recommended)

- **State diff** for correctness metrics (ToolCorrectness, TaskCompletion)
- **Agent trace** for faithfulness metrics (GEval: "did the agent follow the protocol?")

Both are captured, different metrics use different sources.

## Implementation

1. **Pre-command snapshot:** L3 inner task saves state files before execution
2. **Command execution:** Standard inner task runs the command
3. **Post-command snapshot:** L3 inner task saves state files after execution
4. **Diff generation:** Python script diffs before/after, produces `actual_output.json`
5. **DeepEval ingestion:** Eval suite reads `actual_output.json` as the test case input

## Dependencies

- Inner task execution must support pre/post hooks for snapshots
- Agent trace capture depends on Claude Code output format capabilities
- Diff script must handle xlsx (openpyxl) and JSON diffs
