# Worktree-Per-Agent Isolation — Every Concurrent Spawn Gets Its Own Tree

## Status
Open

## Priority
High — the concurrency failure class that contracts and hooks cannot touch. Two honest agents sharing one git tree WILL collide; only isolation fixes it. Third of the subagent-reliability set (with 290 prevention, 291 verification).

## Summary
Give **every concurrent spawn its own git worktree** (or fully isolated working dir), regardless of scope. Today BUILD/REFACTOR spawns get `isolation: "worktree"`, but RESEARCH/TEST spawns route to a Bash subfolder in the **shared** repo tree — so two of them collide. 271 isolated per-agent *state* (routed `agent-{id}-workflow.json`); it did **not** isolate the working *tree*. This closes that gap — Kun's Treehouse for the Isagawa harness.

## Evidence (this session)
- The swarm ran 288 (RESEARCH) + 289 (TEST) concurrently in `sr_dev`'s single tree. Agent 288's commit-on-complete did a broad commit that swept in **agent 289's in-progress files** and the `.claude/worktrees/agent-*` dirs as embedded git repos — a genuine tree-level collision. State isolation (271) was intact; the tree was not.
- No contract or hook prevents this — two agents obeying every rule still clobber a shared tree. Only separate trees do.

## Requirements
- **Worktree per concurrent spawn, all scopes:** RESEARCH/TEST spawns get their own git worktree (or isolated working copy) like BUILD/REFACTOR — not a subfolder in the shared tree.
- **Commit-scope safety:** an agent's commit-on-complete must only ever stage its own worktree, never the parent tree / sibling agents' files / nested worktree dirs (the embedded-repo mess). Prefer worktree isolation over broad `git add`.
- **Reuse/cleanup (Treehouse-style):** pool/reuse worktrees where possible; auto-remove on completion (unchanged worktrees), matching the auto-clean behavior BUILD spawns already have.
- **Merge gate parity:** isolated RESEARCH/TEST output lands via the same review/merge path (or reports only) without touching the parent tree until accepted.
- **`.gitignore` the worktree root:** `.claude/worktrees/` must be ignored so a stray broad commit can never embed them again (root cause of the swarm's embedded-repo commit).
- **Parity + portability:** land in `spawn-agent-swarm` + `run-task.sh` (sr_dev), then fold into kernel-minimal.

## References
- [[123-kernel-research-worktree-pipeline-isolation]] (research, done) + [[271-kernel-fix-worktree-isolation-completion]] (state isolation, done) — this is the tree-level completion neither covered.
- Reliability framework 2026-07-23: the "isolation" lever. Pairs with [[290-kernel-build-subagent-output-sandbox-hook]] + [[291-kernel-build-per-step-postcondition-contract]].
- Kun Chen's Treehouse (reusable worktrees so agents don't step on each other) — the reference implementation of this idea.

## Task Builder Input
- **Deliverable:** RESEARCH/TEST spawns run in their own git worktree; commit-on-complete confined to the agent's worktree; `.claude/worktrees/` gitignored; auto-cleanup on completion — with a test proving two concurrent same-repo agents no longer clobber each other's files.
- **Location:** workspace:.claude/skills/spawn-agent-swarm
- **Scope:** BUILD
- **Constraints:** Do not regress the working BUILD/REFACTOR worktree path. Keep per-agent state isolation (271) intact. Port to kernel-minimal after it proves out.
