# Research Velocity Management and Review System

## Status
Open

## Priority
High — Pipeline velocity exceeds human review capacity. Completed work accumulates without review, iteration, or acceptance. Need a system to manage the output of execute-pipeline and other autonomous work.

## Summary

Research how to manage the output of high-velocity autonomous agent work. The problem: execute-pipeline and agent swarms complete backlogs faster than the user can review, iterate, and accept the results. Work gets done but piles up — no review loop, no acceptance gate, no iteration tracking. Need a system that:

1. Tracks what's been completed and what still needs human review
2. Surfaces the most important items for review (priority-based)
3. Enables quick iteration (approve, request changes, or reject)
4. Doesn't slow down the pipeline — review happens async, not as a gate

This is different from the existing `/kernel/complete` command (which gates task-level completion) — this is about managing the PORTFOLIO of completed work across multiple pipelines.

## Research Questions

1. **What's the right abstraction?** Is this a dashboard, a queue, a kanban board, a report, or something else?
2. **What state already exists?** Backlog items in `done/`, agent-swarm.json, completed_tasks in workflow state, anchor logs — can we build on these?
3. **How do other systems handle this?** CI/CD review queues, PR review workflows, production deployment pipelines — what patterns apply?
4. **What's the minimum viable version?** A single command (`/review-queue`) that shows completed-but-unreviewed work? Or does it need more structure?
5. **Should review be per-backlog or per-deliverable?** A backlog might produce a whole repo, a set of files, or a research report. What's the review unit?
6. **How does iteration work?** If the user says "redo this part" — does that create a new backlog? A follow-up task? An edit-in-place?

## References
- Execute-pipeline: `.claude/skills/execute-pipeline/`
- Agent swarm: `.claude/skills/spawn-agent-swarm/`
- Complete command: `.claude/commands/kernel/complete.md`
- Backlog done folder: `docs/backlog/done/`

## Task Builder Input
- **Deliverable:** Research report with recommended system design, minimum viable version, and backlog for implementation
- **Location:** `subproject:velocity-management-research`
- **Scope:** RESEARCH
- **Constraints:** Must integrate with existing kernel infrastructure (backlogs, state files, commands). Must not add gates that slow pipeline execution. Review is async, not blocking.
