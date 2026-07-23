# Gate Contract — 271 Worktree Isolation Completion

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| WI-01 | Worktrees are created from CURRENT main HEAD at spawn time (fresh base). The runner's `git reset --hard main` workaround is no longer REQUIRED for correctness; a guarded merge-base==main-HEAD assertion remains as a safety check | grep + read code | 001 | fresh-base spawn + retained assertion |
| WI-02 | When KERNEL_AGENT_ID is set, ALL workflow/session writes (task_folder, total_tasks, anchored, completed_tasks, current_task) route to agent-{id}-*.json — the PARENT sr_dev_workflow.json / session_state.json are NEVER written by a routed agent. Audit run-task.sh state pre-init + any write paths and route the strays | grep + read code | 002 | zero parent writes when routed |
| WI-03 | L2: a routed agent (KERNEL_AGENT_ID set) performing an anchor/state update writes ONLY agent-{id}-workflow.json; a throwaway parent file is byte-identical before/after | live pytest/bash | 003 | parent untouched, agent file updated |
| WI-04 | L3: spawn a real worktree runner on a 1-task folder; assert (a) it branched from current main HEAD, (b) the parent sr_dev_workflow.json `anchored` is unchanged during AND after the run, (c) no stray test/state artifacts land in the main working tree | live run | 004 | 3/3 asserts live |

## Rules
- READ run-task.sh (worktree spawn, state pre-init, KERNEL_AGENT_ID routing) + anchor.md (State File Routing table) + agent-identity-model.md FIRST (RULE ZERO)
- The PARENT anchored flag is owned by the interactive session ONLY. A routed/one-shot agent must never write it (root cause of this session's repeated "Protocol not anchored" blocks)
- State writes Python/Write only (no PowerShell); accept utf-8-sig on read (BOM defensive)
- Must not break the non-routed (agent_id null) interactive path. One action per task.
- L3 (004) is a LIVE run, not a simulation (lessons #39/#49). Any RED -> fix -> /kernel/learn.
