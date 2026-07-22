# Runner Hardening v2 — Completion Persistence, Death Detection, Commit-on-Complete

## Status
Open

## Priority
High — the runner is the substrate every pipeline rides on; these are the failure modes that produce false "done" reports and lost deliverables. 262 fixed empty-output retry + heartbeat + task resolution; this closes the remaining category-1 gaps.

## Summary
`run-task.sh` still loses or misreports completion in three ways beyond what 262 fixed: (1) a task can finish work but the completion never persists to the routed workflow state, so the orchestrator sees "still running"; (2) a silently-dead runner is only *detectable* via the 262 heartbeat — nothing acts on it; (3) a deliverable edited during a task can be left uncommitted when the runner reports complete, so `review-queue accept` merges an empty branch. Harden the runner so completion is durable, death is acted upon, and complete implies committed.

## Requirements
- **Completion persistence:** the per-task complete path must write-verify the routed `{agent-}workflow.json` (`completed_tasks` append + re-read confirms the append landed) before advancing; on write-verify failure, retry the state write rather than proceeding. Covers the BOM/encoding class (lesson 2026-07-22) and shared-state clobber.
- **Death detection → action:** consume the 262 heartbeat. Add a lightweight supervisor step (in the runner loop or a companion checker) that, if the heartbeat is older than a threshold while iterations remain, marks the run `stalled` in state and emits a non-zero terminal signal the orchestrator can see — never a silent exit-0 with work remaining.
- **Commit-on-complete gate:** before the runner emits ALL_TASKS_COMPLETE, assert the worktree tree is clean for the deliverable paths (git status --porcelain scoped to the task's output dir). If dirty, commit the deliverable (or fail loudly naming the uncommitted files) — complete must never leave an uncommitted deliverable on the branch.
- **Empty-output timeout root cause:** investigate the 600s empty-output-at-timeout case 262 papers over with one retry. Determine whether it is model-side (no tokens) or harness-side (stream not captured); document the finding and, if harness-side, fix the capture rather than only retrying.
- **Regression coverage:** an L2 test that simulates a completed-but-unpersisted task and asserts the runner re-persists; an L3 that runs a real 1-task folder and asserts (a) completion in state, (b) deliverable committed, (c) clean tree.

## References
- `run-task.sh` (262 merge fcd52e1 — EMPTY-RETRY, HEARTBEAT_FILE, filesystem TASK_RESOLUTION)
- `docs/backlog/262-kernel-fix-runtask-hardening.md` (prior runner fix — this is v2)
- Lessons: 2026-07-22 UTF-8 BOM state write; 2026-07-21 0-byte-log gate skip (#49); ledger "run-task.sh batches lose completion signals"
- `.claude/skills/spawn-subagent/`, `.claude/skills/execute-pipeline/` (callers)

## Task Builder Input
- **Deliverable:** Hardened `run-task.sh` (+ any companion checker script and `lib/` helper) with durable completion persistence, heartbeat-driven stall detection that surfaces to the orchestrator, and a commit-on-complete gate; plus L2/L3 regression tests.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must stay backward-compatible with in-flight runners and per-agent `KERNEL_AGENT_ID` state routing. State writes are Python/Write only (no PowerShell). Do NOT weaken the cycling contract. This backlog edits `run-task.sh` — it must run STRICTLY SEQUENTIAL with 271/272 which also touch the runner/router (lesson #28).
