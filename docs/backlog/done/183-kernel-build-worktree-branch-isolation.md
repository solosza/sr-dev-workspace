# Build Worktree Branch Isolation for Execute-Pipeline

## Status
Open

## Priority
High — agents currently write directly to main, no rollback if work is bad, no isolation between concurrent agents

## Summary
Integrate git worktrees into execute-pipeline so each pipeline run creates a feature branch in an isolated worktree. Agents work in the worktree, not on main. After gap check + prod test + human review (via review-queue), the feature branch merges to main. This is the branch isolation layer that prevents untested work from landing on main.

Prior research (backlog 123) was incomplete — task folder was archived but research tasks (002-008) were never executed. This backlog picks up where 123 left off: research EnterWorktree behavior, confirm state isolation, then build the integration.

## Requirements
- Research Claude Code's `EnterWorktree` tool behavior (does it create branches? how does state isolate?)
- Confirm `.claude/state/` files are isolated per worktree (or design around it if not)
- Design the lifecycle: create worktree + feature branch → run pipeline → gap check → prod test → merge gate
- Integrate into execute-pipeline as an optional mode (default for BUILD scope, skip for RESEARCH)
- Update run-task.sh to work inside worktrees
- Handle edge cases: pipeline fails mid-run, merge conflicts, concurrent agents on same repo
- Build the merge command or integrate into review-queue accept action

## References
- Prior research (incomplete): `projects/worktree-research/README.md`, `tasks/completed/worktree-research/`
- Original backlog: `docs/backlog/done/123-kernel-research-worktree-pipeline-isolation.md`
- Execute-pipeline skill: `.claude/skills/execute-pipeline/`
- Review-queue research: `projects/velocity-management-research/final-report.md`
- State isolation research: `docs/backlog/done/146-kernel-research-state-isolation-and-ci-solutions.md`

## Task Builder Input
- **Deliverable:** Worktree integration in execute-pipeline + merge gate in review-queue
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Must not break existing non-worktree pipeline runs. RESEARCH scope backlogs should skip worktree isolation (no merge needed for research). Must work with run-task.sh one-shot mode. Must handle concurrent agents (swarm pattern).
