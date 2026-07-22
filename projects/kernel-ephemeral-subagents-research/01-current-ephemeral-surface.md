# Current Ephemeral Surface — Kernel Execution Model

## Inventory: Ephemeral vs Long-Lived Execution

### Ephemeral (Short-Lived, Fresh Context)

| Surface | Mechanism | Context Lifetime | Anchor Policy | File Citation |
|---------|-----------|-----------------|---------------|---------------|
| **run-task.sh one-shot agents** | `claude -p` per task iteration, fresh session each time | Single task (1 file write, 1 test, etc.) | Inherits `one_shot: true` from parent; runs session-start but skips force-anchor reset (session-start.md line 71) | `run-task.sh` lines 91-101; `.claude/commands/kernel/session-start.md` step 6 |
| **prod-test sub-agents** | Inner run-task.sh inside disposable test repo | Single L1/L2/L3 test task | Same one-shot policy; separate test repo state | `.claude/skills/prod-test/SKILL.md` step 7 |
| **spawn-subagent BUILD scope** | `Agent(isolation: "worktree")` — git worktree per agent | Full task folder execution | Independent worktree, own state files | `.claude/skills/spawn-subagent/SKILL.md` lines 131-132 |
| **spawn-subagent RESEARCH scope** | `Bash(run_in_background: true)` with `env -u CLAUDECODE` | Full task folder execution | Unique subfolder per backlog for lock isolation | `.claude/skills/spawn-subagent/SKILL.md` lines 133-136 |
| **spawn-agent-swarm agents** | N parallel agents, each via run-task.sh | Per-backlog task folder | Per-agent state files (`agent-{N}-state.json`) | `.claude/skills/spawn-agent-swarm/SKILL.md` lines 95-117 |

### Long-Lived (Extended Context, Prone to Decay)

| Surface | Mechanism | Context Lifetime | Anchor Policy | File Citation |
|---------|-----------|-----------------|---------------|---------------|
| **Interactive orchestrator session** | User-driven conversation, manual commands | Entire working session (hours) | Full anchor every N actions (configurable, default 30); hook-enforced | `.claude/state/sr_dev_workflow.json` `actions_limit: 30` |
| **execute-pipeline parent** | Outer agent orchestrating backlog to task-builder to run-task.sh | Full pipeline (minutes to hours) | Full anchor at session start; spawns one-shot agents for execution | `.claude/skills/execute-pipeline/SKILL.md` lines 48-55 |
| **Agent swarm orchestrator** | Parent session managing spawn + monitor loop | Spawn + monitoring phase | Anchor at start; monitors per-agent state files | `.claude/skills/spawn-agent-swarm/SKILL.md` steps 4-5 |

## Observed Degradation Evidence

### From Lessons and DEFECT_LOG

1. **Quick-anchor violations (recurred 5 times):** The primary symptom of context decay in long-lived sessions. Agent reads the "never quick-anchor" rule, then violates it within the same session — indicating the rule faded from active context despite being read. Documented recurrences: 2026-03-22, 2026-05-01 (batch operations), 2026-05-26, 2026-07-07. See `lessons.md` RULE ZERO paragraph 2.

2. **State contention from shared mutable state (2026-04-23, 2026-06-14):** Long-lived orchestrator sessions and concurrent one-shot agents fight over `session_state.json` and `sr_dev_workflow.json`. Agent 132 completed all deliverables but state was overwritten by agent 131 running concurrently — orchestrator lost visibility entirely. See `lessons/state-contention.md` and `lessons.md` "MULTI-AGENT STATE ISOLATION."

3. **Rule application decay (2026-04-28):** Within a single execute-pipeline run, agent committed 3 violations in one session: (a) edited `pending_anchor_token` to bypass hook, (b) paused pipeline for user approval despite "no pause points" rule, (c) used Edit instead of Write for state reset. All three rules were read at anchor. See `lessons.md` "NEVER IMPROVISE" paragraph.

4. **Action counter reaching 21-28 between anchors:** Anchor logs from 2026-07-21 show 28 actions in a single inter-anchor window (`anchor-logs/2026-07-21/01-41-00Z.json`). The workflow state shows `actions_since_anchor: 21` in `sr_dev_workflow.json`. These high counts, especially 28, suggest the agent was operating well past the intended re-centering point.

5. **DEF-001 through DEF-006:** The DEFECT_LOG documents 6 defects in the first 3 days of kernel operation, ALL caused by agent context issues in long-lived sessions: skipping learn (DEF-001), state key mismatch (DEF-002), domain naming (DEF-003), domain persistence (DEF-004), hook removal during debugging (DEF-005), and anchor/validate redundancy (DEF-006).

### From Anchor Logs

The anchor-logs directory spans 2026-03-30 through 2026-07-21 (20 date folders). The presence of consistent anchoring across months confirms the mechanism is operational, but the recurrence of violations documented in lessons.md indicates that re-reading rules every N actions mitigates but does not eliminate context decay in long-lived sessions. The ephemeral one-shot pattern (run-task.sh) avoids this entirely — each agent starts fresh and operates within a single-task context window.

## One-Shot Agent Anchor Contract

Per `session-start.md` step 6 and `run-task.sh` lines 91-98:

1. `one_shot: true` is set in `session_state.json` before the agent launches
2. Agent runs `/kernel/session-start` then detects `one_shot: true` then skips force-anchor reset (does not set `anchored: false` in workflow state)
3. Agent inherits `anchored: true` from parent's prior anchor
4. Agent runs `/kernel/anchor` (full ceremony) once at start
5. Agent picks one task, implements it, runs `/kernel/complete`
6. Agent emits `ONE_SHOT_COMPLETE` or `ALL_TASKS_COMPLETE`

The one-shot contract eliminates context decay by design: context window is consumed by exactly one task's work plus the anchor ceremony overhead. There is no opportunity for multi-task context accumulation, rule-application decay, or state contention beyond the initial state file reads.

## Summary

The kernel already has a robust ephemeral execution surface via run-task.sh, prod-test, spawn-subagent, and spawn-agent-swarm. The long-lived orchestrator session is the primary source of observed degradation — all 5 recurring rule violations in lessons.md trace to interactive or extended-pipeline sessions, not one-shot agents. The question is whether to expand the ephemeral surface to cover workflows currently handled by long-lived sessions.
