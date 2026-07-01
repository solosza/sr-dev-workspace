# Build Iteration Tracking

## Type
BUILD

## Phase Gate
None (no dependencies).

## Deliverable
`framework/iteration_tracking.py`

## Instructions
1. Read the iteration-tracking design doc: `docs/backlog/154-kernel-build-deepeval-l3-testing/iteration-tracking.md`
2. Create `framework/iteration_tracking.py` implementing:
   - `ScoreRecord` — dataclass with pass_number, timestamp, command, contract_id, metrics dict, overall_pass, failing_metrics, gaps_identified
   - `record_pass(score_history_path, score_record)` — appends a score record to score-history.json
   - `detect_regression(score_history_path)` — compares latest pass to previous, flags any metric drop > 0.1 or pass→fail
   - `generate_progression_report(score_history_path)` — produces the formatted progression table (Pass 1, Pass 2, Pass 3 columns per metric)
   - `is_production_ready(score_history_path)` — returns True if all metrics >= production_ready threshold (0.85)
3. Score history file format per design doc: `{ command, passes[], progression{}, production_ready, production_ready_at_pass }`

## Verification
- File exists at `framework/iteration_tracking.py`
- Contains `record_pass`, `detect_regression`, `generate_progression_report` functions
