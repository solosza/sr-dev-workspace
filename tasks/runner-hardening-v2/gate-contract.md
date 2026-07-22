# Gate Contract — 270 Runner Hardening v2

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| RH-01 | run-task.sh complete path write-verifies routed workflow.json: appends to completed_tasks, re-reads, confirms append landed; retries state write on failure before advancing | grep + read code; unit sim | 001 | write-verify + retry present |
| RH-02 | Heartbeat-staleness check: if HEARTBEAT_FILE older than threshold while iterations remain, marks run stalled in state + emits non-zero terminal signal (no silent exit-0 with work left) | grep + read code | 002 | stall path emits non-zero |
| RH-03 | Commit-on-complete: before ALL_TASKS_COMPLETE, asserts clean tree for the task output dir (git status --porcelain scoped); if dirty, commits deliverable or fails loudly naming files | grep + read code | 003 | gate present before complete banner |
| RH-04 | Empty-output 600s timeout root cause documented in a findings file (model-side vs harness-side); if harness-side, capture fixed | file_exists + content | 004 | findings file + verdict |
| RH-05 | L2: simulate a completed-but-unpersisted task; assert runner helper re-persists completion to routed state | live pytest/bash | 005 | test passes live |
| RH-06 | L3: run a real 1-task folder end to end; assert (a) completion in routed state, (b) deliverable committed, (c) clean tree | live run | 006 | 3/3 asserts live |

## Rules
- READ run-task.sh (esp. the 262 EMPTY-RETRY, HEARTBEAT_FILE, TASK_RESOLUTION blocks) FIRST — RULE ZERO; do not re-derive
- One action per task (never bundle) — a helper + its wiring are separate tasks if both non-trivial
- State writes Python/Write only; accept utf-8-sig on read (BOM defensive, lesson 2026-07-22)
- Must not weaken the cycling contract or break the non-routed (agent_id null) interactive path
- L3 (006) is a LIVE run, not a simulation (lessons #39/#49) — evidence must be re-runnable, non-empty
- Any RED → fix → /kernel/learn
