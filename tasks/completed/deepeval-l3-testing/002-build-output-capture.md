# Build Agent Output Capture

## Type
BUILD

## Phase Gate
None (no dependencies).

## Deliverable
`framework/agent_output_capture.py`

## Instructions
1. Read the agent-output-capture design doc: `docs/backlog/154-kernel-build-deepeval-l3-testing/agent-output-capture.md`
2. Create `framework/agent_output_capture.py` implementing:
   - `snapshot_state(repo_path, snapshot_dir)` — copies all state files (JSON, xlsx) to a snapshot directory
   - `diff_states(before_dir, after_dir)` — computes diff between two snapshots, returns structured diff
   - `capture_actual_output(before_dir, after_dir)` — produces `actual_output` dict suitable for DeepEval's LLMTestCase
   - Handle JSON diffs (state files) and xlsx diffs (openpyxl cell comparison)
   - Output format: `{ "files_changed": [...], "state_diff": {...}, "xlsx_diff": {...} }`
3. The hybrid approach: state diff for correctness metrics, agent trace for faithfulness metrics

## Verification
- File exists at `framework/agent_output_capture.py`
- Contains `snapshot_state`, `diff_states`, `capture_actual_output` functions
