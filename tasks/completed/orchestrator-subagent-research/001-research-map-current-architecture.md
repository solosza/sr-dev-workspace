# Map the Current Command Architecture

## Context
Backlog 230: before recommending orchestrator/subagent architecture, map what exists honestly — the workspace ALREADY runs the pattern at two tiers (pipeline: orchestrator session + one-shot run-task.sh agents; prod-test) while a standing lesson (2026-04-04) forbids spawning elsewhere.

## Type
RESEARCH
## Execution
inline
## Dependencies
- None

## Requirements
- READ: .claude/lessons/lessons.md (esp. 2026-04-04 no-spawn, 2026-06-14 orchestration + state-isolation, sequential-pipeline lessons), .claude/skills/spawn-agent-swarm/SKILL.md, .claude/skills/spawn-subagent/SKILL.md, .claude/skills/prod-test/SKILL.md, .claude/commands/kernel/ (inventory), projects/hmsa-qa-platform/README.md (Process + project-run note)
- Check prior research for overlap: projects/multi-persona-architecture/, projects/loop-composability-research/
- Write `projects/orchestrator-subagent-research/01-current-state.md`: table of every command/skill → inline vs orchestrator today → why; the two-tier reality; what each recorded lesson protects against (cite dates); what has changed since each lesson (per-agent state files, worktree support)

## Acceptance Criteria
- [ ] 01-current-state.md exists, cites 2026-04-04 and 2026-06-14 lessons explicitly
- [ ] Command inventory table present

## Gates Satisfied
- OSR-01, OSR-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
