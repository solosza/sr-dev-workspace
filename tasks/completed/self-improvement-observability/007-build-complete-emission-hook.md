# Add emission hook to complete.md

## Context
Adds a metric emission statement to /kernel/complete so it appends a pipeline_complete event to .claude/state/metrics.jsonl after every completion validation. Tier 1.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Requirements
- Edit `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/complete.md`
- Add emission instruction after step 5 (update state) and before step 6 (report):
  ```
  5b. **Emit pipeline_complete metric (append-only, failure does not block):**
      Append to `.claude/state/metrics.jsonl`:
      ```json
      {"schema_version":1,"timestamp":"<ISO>","event":"pipeline_complete","pipeline_id":"<current_task or 'single'>","result":"<PASS|PARTIAL|FAIL>","tasks_total":<N>,"tasks_completed":<N>,"tasks_skipped":<N>,"violations":0}
      ```
  ```
- Emission is append-only — failure to emit must NOT block the complete command
- No new dependencies added

## Acceptance Criteria
- [ ] `D:/my_ai_projects/isagawa-kernel/.claude/commands/kernel/complete.md` contains `metrics.jsonl`
- [ ] Emission instruction is placed after state update, before report
- [ ] Instruction specifies append-only and non-blocking

## Gates Satisfied
- BUILD-07

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
