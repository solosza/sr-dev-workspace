# Research: DAG Wave Execution Engine for Swarm Dispatch

## Status
Open

## Priority
High — the recommended proposal; today execute-pipeline/spawn-agent-swarm fire all agents simultaneously with zero runtime coupling, so any inter-backlog dependency risks failure, stale reads, or races.

## Summary
Extend `/spawn-agent-swarm` and `/kernel/execute-pipeline` to support dependency waves: backlog items declare prerequisites (`depends_on: [238]`), the orchestrator topologically sorts them into waves (Wave 0 = no deps; Wave N+1 dispatches only after all of Wave N exits COMPLETE), and the background monitor becomes the barrier that auto-dispatches the next wave. Research whether this is the right layer for dependency enforcement and produce a yah/nay verdict.

## Requirements
- Define the dependency metadata format: `depends_on` in backlog frontmatter/Task Builder Input vs. task index — and how the swarm's step-01 parser reads it
- Design topological wave sorting + cycle detection (reject circular deps with a clear error)
- Barrier monitor design: current monitor polls per-agent state files for 5 min max — waves need an unbounded (or long-timeout) barrier; reconcile with the existing monitor step and background-task notification flow
- Failure semantics: if an agent in Wave N fails or is skipped, does Wave N+1 dispatch, block, or partially dispatch (only unblocked children)?
- Interaction with the STRICTLY-SEQUENTIAL multi-backlog lesson: waves generalize it (sequence = degenerate DAG) — confirm the lesson's contention rationale is satisfied by per-agent state isolation before allowing intra-wave parallelism
- Compare against Proposals 2 (task-level barrier gates, backlog 242) and 3 (artifact bus, backlog 243): which layer owns ordering, and can they compose?
- **Verdict: yah or nay** — build the wave engine, and if yah: metadata schema + orchestrator changes + monitor changes, scoped to not break the outer-agent pattern

## References
- `.claude/skills/spawn-agent-swarm/` (steps 01-05), `.claude/skills/execute-pipeline/`
- `.claude/lessons/lessons.md` — EXECUTE-PIPELINE STRICTLY SEQUENTIAL; multi-agent state isolation; state contention
- Backlogs 242, 243 (sibling proposals — this backlog owns the cross-proposal recommendation), 237 (ephemeral sub-agents: handoff schema), 183 (worktree isolation)
- Live evidence 2026-07-21: swarm 237-240 ran flat-parallel; 240's portfolio-ranking task had a soft dependency on 237-239 outputs and only worked because it tolerated missing siblings

## Task Builder Input
- **Deliverable:** Research report — wave engine design, failure semantics, comparison vs backlogs 242/243, yah/nay verdict + implementation spec if yah
- **Location:** subproject:kernel-dag-wave-research
- **Scope:** RESEARCH
- **Constraints:** Research only — no skill/command changes in this backlog. Must preserve the outer-agent pattern (run-task.sh remains the only execution path) and per-agent state isolation.
