# Workflow State Field Classification

## Classification: Global vs Per-Agent

Based on the consumer map, each field is classified by whether it belongs to the session (global) or to a specific run-task.sh invocation (per-agent).

| Field | Classification | Rationale |
|-------|---------------|-----------|
| `domain` | Global | Session-level identity, never changes |
| `setup_complete` | Global | One-time flag set during domain-setup |
| `protocol_created` | Global | One-time flag |
| `commands_created` | Global | One-time flag |
| `hooks_created` | Global | One-time flag |
| `validated` | Global | One-time flag |
| `actions_limit` | Global | Configuration, not runtime state |
| `lesson_recorded` | Global | Session-level learning state |
| `lessons_count` | Global | Cumulative counter |
| `last_lesson` | Global | Session-level |
| `last_lesson_timestamp` | Global | Session-level |
| `hooks_updated` | Global | Session-level |
| `anchored` | **Ambiguous** | See analysis below |
| `anchor_timestamp` | **Ambiguous** | See analysis below |
| `actions_since_anchor` | **Ambiguous** | See analysis below |
| `last_anchor_token_confirmed` | **Ambiguous** | See analysis below |
| `cycling` | Per-Agent | Each agent cycles through its own task folder |
| `cycling_complete` | Per-Agent | Per task folder |
| `task_folder` | Per-Agent | Each agent has its own task folder |
| `total_tasks` | Per-Agent | Count is per task folder |
| `current_task` | Per-Agent | Each agent works its own task |
| `completed_tasks` | Per-Agent | Each agent tracks its own completions |
| `skipped_tasks` | Per-Agent | Each agent tracks its own skips |
| `attempts_on_current` | Per-Agent | Retry counter per agent |
| `complete` | Per-Agent | Each agent determines its own completion |
| `complete_timestamp` | Per-Agent | Per agent |
| `timestamp` | Per-Agent | Last write, meaningless when shared |

## Ambiguous Fields — Breakage Analysis

### `anchored` (bool)

**If Global:**
- One agent anchors, sets `anchored: true` — all agents proceed
- Another agent's session-start sets `anchored: false` — all agents blocked
- Cross-agent anchor interference

**If Per-Agent:**
- Each agent manages its own anchor state independently
- One-shot agents already skip anchor gates (one_shot guard in hook)
- No risk if one_shot is set. For non-one-shot agents, per-agent is correct.

**Verdict:** Per-Agent. One-shot agents already skip this gate. For parallel non-one-shot agents, each must anchor independently.

### `actions_since_anchor` (number)

**If Global:**
- All agents increment the same counter — reaches limit N times faster
- Agent A's action triggers anchor requirement for agent B
- Phantom anchor requirements, agents blocked by each other's counter

**If Per-Agent:**
- Each agent has its own counter
- Anchor requirement tied to that agent's actual action count
- One-shot agents already skip the counter increment.

**Verdict:** Per-Agent. One-shot agents skip it. Non-one-shot parallel agents need independent counters.

### `anchor_timestamp` and `last_anchor_token_confirmed`

**If Global:** Last writer wins, no meaningful data
**If Per-Agent:** Each agent tracks its own anchor timing

**Verdict:** Per-Agent.

## Summary

| Scope | Count | Fields |
|-------|-------|--------|
| Global | 12 | domain, setup_complete, protocol_created, commands_created, hooks_created, validated, actions_limit, lesson_recorded, lessons_count, last_lesson, last_lesson_timestamp, hooks_updated |
| Per-Agent | 15 | cycling, cycling_complete, task_folder, total_tasks, current_task, completed_tasks, skipped_tasks, attempts_on_current, complete, complete_timestamp, timestamp, anchored, anchor_timestamp, actions_since_anchor, last_anchor_token_confirmed |

**Key finding:** 15 of 27 fields are per-agent. The file is majority per-agent state being treated as global. This is the root cause of contention.

## One-Shot Guard Interaction

When `one_shot: true` in session_state.json:
- Hook skips Gates 3-5 (anchored check, counter increment)
- Session-start skips setting `anchored: false`
- `anchored` and `actions_since_anchor` are effectively ignored

But `/kernel/complete` still writes to `completed_tasks`, `current_task`, `task_folder` etc. even in one-shot mode. These writes are the primary contention source — the one-shot guard does not protect them.
