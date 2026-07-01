# Workflow State Consumer Map

## Target File

`.claude/state/[domain]_workflow.json` (e.g., `sr_dev_workflow.json`)

## Current Schema

| Field | Type | Purpose |
|-------|------|---------|
| `domain` | string | Domain identifier |
| `setup_complete` | bool | Domain setup finished |
| `protocol_created` | bool | Protocol file exists |
| `commands_created` | bool | Commands directory populated |
| `hooks_created` | bool | Hooks registered |
| `anchor_timestamp` | string | Last anchor ISO timestamp |
| `actions_since_anchor` | number | Counter incremented by hook |
| `attempts_on_current` | number | Retry counter for current task |
| `cycling` | bool | Whether in cycling mode |
| `cycling_complete` | bool | All tasks done in cycling |
| `actions_limit` | number | Threshold before anchor required |
| `validated` | bool | Domain validation passed |
| `lesson_recorded` | bool | Last lesson was recorded |
| `lessons_count` | number | Total lesson count |
| `last_lesson` | string | Last lesson description |
| `last_lesson_timestamp` | string | Last lesson ISO timestamp |
| `hooks_updated` | bool | Hooks changed during last learn |
| `timestamp` | string | Last state write timestamp |
| `complete` | bool | Workflow finished |
| `complete_timestamp` | string | Completion ISO timestamp |
| `task_folder` | string | Active task directory path |
| `total_tasks` | number | Count of all tasks |
| `current_task` | string/null | Task currently being worked on |
| `anchored` | bool | Protocol anchor is active |
| `last_anchor_token_confirmed` | string | Last confirmed anchor token |
| `completed_tasks` | array | List of completed task filenames |
| `skipped_tasks` | array | List of skipped task filenames |

## Consumer Map

### Hooks (Runtime — Mechanical Enforcement)

| Consumer | File | Trigger | Fields Read | Fields Written | When |
|----------|------|---------|-------------|----------------|------|
| Universal Gate Enforcer | `.claude/hooks/universal-gate-enforcer.py` | PreToolUse (Write/Edit/Bash) | `anchored`, `actions_since_anchor`, `actions_limit` | `actions_since_anchor` (increment) | Every gated action |
| SR Dev Gate Enforcer | `.claude/hooks/sr_dev-gate-enforcer.py` | PreToolUse | (none — does not read workflow state) | (none) | Every gated action |
| Actions Log Appender | `.claude/hooks/actions-log-appender.py` | PostToolUse | (none — writes to actions.jsonl, not workflow state) | (none) | Every action |

**Key detail:** The universal gate enforcer is the ONLY hook that reads/writes workflow state. It reads `anchored` (Gate 3), `actions_since_anchor` + `actions_limit` (Gate 4), and writes `actions_since_anchor` (auto-increment). For one-shot agents (`one_shot: true` in session_state.json), Gates 3-5 and the counter are skipped entirely.

### Commands (Agent-Invoked)

| Consumer | File | Fields Read | Fields Written | When |
|----------|------|-------------|----------------|------|
| `/kernel/session-start` | `.claude/commands/kernel/session-start.md` | All fields (existence check), `anchored` | `anchored` (set false on fresh start, skip if one_shot) | Session start |
| `/kernel/anchor` | `.claude/commands/kernel/anchor.md` | `actions_since_anchor` (for review count) | `anchored` (true), `anchor_timestamp`, `actions_since_anchor` (reset to 0) | Every 10 actions, session start |
| `/kernel/complete` | `.claude/commands/kernel/complete.md` | `protocol_created`, `anchored`, `one_shot` (from session_state), `cycling`, `completed_tasks`, `skipped_tasks`, `current_task`, `task_folder`, `total_tasks` | `completed_tasks` (append), `current_task` (null or next), `attempts_on_current` (0), `complete` (conditional), `complete_timestamp`, `cycling` (false when done), `cycling_complete` (true when done) | Task completion |
| `/kernel/learn` | `.claude/commands/kernel/learn.md` | (reads for merge) | `lesson_recorded` (true), `lessons_count` (N), `last_lesson`, `last_lesson_timestamp`, `hooks_updated` | After failure fix |
| `/kernel/fix` | `.claude/commands/kernel/fix.md` | `cycling` (check cycling mode for auto-proceed) | (none — fix doesn't write workflow state) | Before fixing |
| `/kernel/autonomous-cycle` | `.claude/commands/kernel/autonomous-cycle.md` | `protocol_created`, `anchored`, `completed_tasks`, `skipped_tasks` | `cycling` (true), `task_folder`, `total_tasks`, `current_task`, `attempts_on_current` (0) | User-invoked cycling start |
| `/kernel/domain-setup` | `.claude/skills/kernel-domain-setup/references/step-10-state.md` | (none — creates fresh) | `domain`, `setup_complete`, `protocol_created`, `anchored` (false), `actions_since_anchor` (0), `actions_limit` (10), `timestamp` | Initial domain creation |

### Scripts (External — Shell-Level)

| Consumer | File | Fields Read | Fields Written | When |
|----------|------|-------------|----------------|------|
| run-task.sh (pre-check) | `run-task.sh` lines 251-268 | `total_tasks`, `completed_tasks`, `skipped_tasks` | (none — read-only check) | Before each iteration (i > 1) |
| run-task.sh (print_state) | `lib/common.sh` lines 94-113 | `anchored`, `completed_tasks`, `skipped_tasks`, `current_task` | (none — read-only display) | Before/after each iteration |
| run-task.sh (skip_current_task) | `lib/common.sh` lines 165-191 | `current_task`, `skipped_tasks` | `skipped_tasks` (append), `current_task` (null), `attempts_on_current` (0) | On task failure after retries |
| run-task.sh (identify task) | `run-task.sh` lines 293-304 | `current_task` | (none — read-only) | Before each iteration |

### Skills (Referenced in Docs)

| Consumer | File | Fields Read | Fields Written | When |
|----------|------|-------------|----------------|------|
| Autonomous Cycling Workflow | `.claude/skills/autonomous-cycling/workflow.md` | `cycling`, `current_task`, `completed_tasks`, `skipped_tasks`, `total_tasks`, `attempts_on_current` | (fields written via /kernel/complete and /kernel/autonomous-cycle) | During cycling |
| Execute Pipeline (validate) | `.claude/skills/execute-pipeline/references/step-05-validate-report.md` | `completed_tasks`, `skipped_tasks` (read for validation) | (none — read-only) | Pipeline validation |
| Spawn Agent Swarm | `.claude/skills/spawn-agent-swarm/` | (explicitly avoids reading workflow state) | (none) | Multi-agent spawn |

## Concurrency Profile

| Writer | Concurrent? | Contention Risk |
|--------|-------------|-----------------|
| Universal Gate Enforcer (hook) | Yes — runs on every agent's action | HIGH — multiple agents increment `actions_since_anchor` simultaneously |
| `/kernel/complete` (command) | Yes — one-shot agents complete independently | HIGH — agents append to `completed_tasks` array; last writer wins |
| `skip_current_task` (run-task.sh) | No — run-task.sh is sequential | LOW |
| `/kernel/anchor` (command) | Yes — if multiple agents anchor | MEDIUM — resets `actions_since_anchor` to 0 while others increment |
| `/kernel/session-start` (command) | Yes — if multiple agents start | MEDIUM — sets `anchored: false` |

## Summary

- **Total unique consumers:** 12 (3 hooks, 7 commands, 2 scripts)
- **Write consumers:** 7 (1 hook, 4 commands, 2 script functions)
- **Read-only consumers:** 5 (2 hooks, 1 command, 2 script functions)
- **Highest contention fields:** `actions_since_anchor` (hook writes on every action), `completed_tasks` (every /kernel/complete appends), `anchored` (anchor + session-start toggle)
- **One-shot guard:** When `one_shot: true` in session_state.json, the hook skips Gates 3-5 and counter increment, and `/kernel/session-start` skips setting `anchored: false`. This reduces but does not eliminate contention on `completed_tasks`.
