# Research: Deliverable-Based Barrier Gates in run-task.sh

## Status
Open

## Priority
Medium — task-level alternative/complement to the orchestrator-level wave engine (backlog 241); enforces dependencies at the gate contract where they are already declared per-task.

## Summary
Instead of (or in addition to) orchestrator wave sorting, enforce dependency barriers at the individual task level: gate contracts or task files declare file-existence prerequisites (`## Prerequisites — file_exists: projects/x/005-final-report.md`), and run-task.sh checks them before firing `claude -p` — entering a wait/poll loop with timeout if they are missing, giving upstream agents time to finish. Research the design and produce a yah/nay verdict.

## Requirements
- Prerequisite declaration format: extend gate-contract.md (new Prerequisites section) vs. per-task `## Prerequisites` block — pick one, define parse rules for run-task.sh (bash-parseable)
- Wait/poll loop design: poll interval, timeout, and timeout behavior (skip task per 3-attempt cycling contract vs. abort run vs. mark BLOCKED in per-agent state for the monitor to surface)
- Deadlock analysis: two agents waiting on each other's outputs — detection or prevention (timeout as backstop; compare with 241's cycle detection at sort time)
- Staleness: file_exists proves presence, not correctness — should prerequisites optionally assert content (grep/word_count, reusing existing gate types)?
- Cost: polling agents hold a run-task.sh process open doing nothing — quantify vs. 241's approach where downstream agents simply are not spawned yet
- Interaction with the swarm monitor: a waiting agent looks identical to a stalled agent — per-agent state must expose WAITING vs RUNNING to avoid false failure detection
- **Verdict: yah or nay** — add barrier gates to run-task.sh, standalone or only as a defense-in-depth layer under 241, with implementation spec if yah

## References
- `run-task.sh` (task selection + iteration loop), task gate-contract format in `.claude/skills/task-builder/references/verification-methods.md`
- Backlogs 241 (orchestrator waves — primary comparison), 243 (artifact bus — what prerequisites would point at)
- `.claude/lessons/lessons.md` — cycling contract (skip after 3 attempts), swarm monitor error-detection rules
- Live evidence 2026-07-21: swarm 237-240 flat-parallel run; 240 portfolio task read sibling outputs "if present" — a prerequisite gate would have made that ordering explicit

## Task Builder Input
- **Deliverable:** Research report — prerequisite format, wait-loop + timeout design, deadlock/staleness analysis, comparison vs 241, yah/nay verdict
- **Location:** subproject:kernel-barrier-gate-research
- **Scope:** RESEARCH
- **Constraints:** Research only. Any proposed run-task.sh changes must stay bash-parseable and keep the one-shot agent contract unchanged (the WAIT happens before agent spawn, not inside the agent).
