# Fix step-04 — Add pipeline_mode Guard

## Context
If step 3 fails to clear `pipeline_mode` (agent drift, context compaction), step 4 should detect and clear it rather than silently proceeding with stale flags. This is a safety net for Defect 1.

## Type
BUILD

## Execution
inline

## Dependencies
None

## Requirements
- In `.claude/skills/execute-pipeline/references/step-04-execute-tasks.md`:
  - Add a guard at the top of the Process section (before step 1 "Read pipeline state")
  - Guard checks: if `pipeline_mode` exists in session_state.json, clear it to null and log a warning
  - This ensures step 4 never runs with stale pipeline_mode flags

## Acceptance Criteria
- [ ] `grep -q 'pipeline_mode' .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` exits 0

## Gates Satisfied
BUILD-06

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
