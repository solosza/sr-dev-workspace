# Fix Execute-Pipeline Autonomous Cycling Defects

## Status
Open

## Priority
High — every execute-pipeline invocation hits at least one of these defects, causing the pipeline to stop mid-execution

## Summary
Five defects in the execute-pipeline → task-builder → run-task.sh chain cause autonomous cycling to break. These were discovered during backlog 089 execution where the pipeline stopped after task decomposition, produced empty claude -p outputs, set premature completion flags, and aborted after 2 transient failures. Three blocking defects (complete.md premature `complete: true`, `anchored: false` leak, no lock file) were hotfixed. Four remaining defects need permanent fixes.

## Requirements

### Defect 1: `pipeline_mode.no_execute` never cleared after task-builder
- **Where:** execute-pipeline step 3 → step 4 transition
- **Issue:** Step 3 sets `no_execute: true` so task-builder stops before cycling. After task-builder returns, the flag must be cleared to `null` and step 4 must run immediately. Instead, the agent reports status and stops.
- **Fix:** Add mechanical enforcement — step 3 MUST clear `pipeline_mode` and proceed to step 4 in the same execution flow. Consider making the flag-clear + step-4-invocation atomic (single code block, not separate agent decisions).

### Defect 2: Task-builder in background agent stops mid-execution
- **Where:** Task-builder spawned as background agent during execute-pipeline
- **Issue:** Background agents have context window limits. Task-builder writing 35+ task files can exhaust context, leaving incomplete task sets (27/35 written for backlog 089). `total_tasks` gets set based on files found, not files planned.
- **Fix:** (a) Task-builder should write `total_tasks` from the decomposition plan BEFORE writing individual files. (b) Add a post-write verification: count files vs plan, report discrepancy. (c) Consider chunking large task sets (write in batches of 10).

### Defect 3: Multiple concurrent run-task.sh invocations
- **Where:** run-task.sh has no mutex/lock mechanism (HOTFIXED — lock file added)
- **Issue:** When parent session context compacts and spawns a new background agent, old agent may still be running. Two run-task.sh processes write to same state files causing contention. 3/4 iterations produced 0-byte output.
- **Status:** Hotfixed with PID lock file. Needs testing to confirm fix works on Windows (Git Bash).

### Defect 4: MAX_CONSECUTIVE_FAILS=2 too aggressive
- **Where:** run-task.sh line 29 (`MAX_CONSECUTIVE_FAILS=2`)
- **Issue:** 2 consecutive empty outputs (from transient contention, rate limits, or slow startup) kills the entire pipeline. With state contention causing 3/4 empty outputs, this triggers immediately.
- **Fix:** (a) Increase to `MAX_CONSECUTIVE_FAILS=4`. (b) Add distinction between "empty output" (transient, retry-worthy) vs "explicit failure" (task error, skip-worthy). (c) Add exponential backoff on empty output retries.

### Defect 5: Duplicate entries in `completed_tasks` cause premature completion
- **Where:** run-task.sh pre-iteration exit guard (line 248-277) and complete.md Mode A
- **Issue:** Background agent created a spurious duplicate entry (`027-phase-6b-integration-l2-consistency.md` alongside `027-phase-6b-integration-l2-debug.md`), inflating `len(completed_tasks)` to match `total_tasks` before all tasks were actually done. The pre-check guard uses `len(completed_tasks)` not `len(set(completed_tasks))`, so duplicates trick it into early exit.
- **Fix:** (a) Pre-check guard should deduplicate: `done = len(set(w.get('completed_tasks', [])))`. (b) complete.md should check for existing entry before appending to `completed_tasks`. (c) Consider adding a `completed_tasks` dedup step in `pre_init_state()`.

## References
- Backlog 089 (where defects were discovered): `docs/backlog/089-domain-build-universal-hook-validator-system/`
- Hotfixes applied: `complete.md` (defects 4+5 from analysis), `run-task.sh` (lock file)
- Lessons: `autonomous-cycling-lesson.md`, `state-contention.md`, `nested-session-nesting.md`
- Related: execute-pipeline skill (`SKILL.md`, `step-03-run-task-builder.md`, `step-04-execute-tasks.md`)

## Task Builder Input
- **Deliverable:** Fixed execute-pipeline skill files, run-task.sh, complete.md — all defects resolved and tested
- **Location:** workspace
- **Scope:** FIX
- **Constraints:** Must not break existing cycling behavior. Hotfixes already applied must be validated. Test with a real pipeline run (e.g., re-run 089 or a small test backlog).
