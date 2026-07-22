# Worktree Isolation Completion — Fresh Base, State Containment, Anchor-Flag Safety

## Status
Open

## Priority
High — worktree isolation is what makes parallel pipelines safe. Three gaps remain that currently require manual workarounds and cause the recurring "Protocol not anchored" blocks on the main session.

## Summary
Backlog 244 gave per-agent state routing via `KERNEL_AGENT_ID`, but worktree isolation is not complete. Three residual leaks: (1) worktrees are created from a possibly-stale base, worked around today by a mandatory `git reset --hard main` in every runner step 0 — fragile and easy to forget; (2) worktree agents still write shared-main fields (`task_folder`, `total_tasks`) and leave test artifacts in the main tree; (3) background/worktree agents flip the shared `anchored` flag on main's `sr_dev_workflow.json`, blocking the interactive session until a full re-anchor. Close all three so parallel runs never touch the main session's state.

## Requirements
- **Fresh base at creation:** worktrees must branch from current `main` HEAD at spawn time (fix the spawn so the base is correct), making the runner's `git reset --hard main` workaround unnecessary. Keep a guarded assertion (merge-base == main HEAD) as a safety check, but the default path should be correct without the reset.
- **State containment:** when `KERNEL_AGENT_ID` is set, ALL workflow writes route to `agent-{id}-workflow.json` — audit for any remaining writes of `task_folder`/`total_tasks`/`anchored` to the shared file and route them. Test artifacts a worktree agent produces must land under the worktree, never the main tree.
- **Anchor-flag safety:** an agent with `KERNEL_AGENT_ID` set must NEVER write `anchored` on the parent `sr_dev_workflow.json`. Enforce in the anchor path (already specced in anchor.md routing) AND, defensively, in the gate enforcer — a routed agent flipping the parent `anchored:false` is the direct cause of the interactive-session blocks. The parent's `anchored` state is owned by the interactive session only.
- **Regression coverage:** L2 test asserting a routed agent's anchor writes go to `agent-{id}-workflow.json` and the parent file is untouched; L3 spawning a real worktree runner and asserting (a) it branched from current main, (b) parent `anchored` unchanged during and after, (c) no stray artifacts in main tree.

## References
- `docs/backlog/244-*` (per-agent state isolation — this completes it), merge context in prior session
- `.claude/commands/kernel/anchor.md` (State File Routing table, KERNEL_AGENT_ID)
- `.claude/references/agent-identity-model.md`
- `.claude/hooks/universal-gate-enforcer.py`, `.claude/hooks/sr_dev-gate-enforcer.py`
- Lessons: State Contention (`state-contention.md`), Multi-Agent Orchestration (`multi-agent-orchestration.md`), 2026-07-07 anchor-skip finding on one_shot state clobber

## Task Builder Input
- **Deliverable:** Worktree spawn creating from fresh main base, complete `KERNEL_AGENT_ID` state routing (no shared-main writes), an enforcer guard preventing routed agents from flipping the parent `anchored` flag, plus L2/L3 regression tests.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not break the interactive (non-routed) path where `agent_id` is null. Edits `run-task.sh` spawn/state paths and the gate enforcer — STRICTLY SEQUENTIAL with 270/272 (shared runner files, lesson #28). Do not modify protocol/CLAUDE.md without the change tracing to a routing bug.
