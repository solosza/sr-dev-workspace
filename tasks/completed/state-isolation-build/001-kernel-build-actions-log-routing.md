# Route Actions Log by Agent ID

## Context
When multiple agents run in parallel, they all append to the same `actions.jsonl`. This makes anchor reviews unable to distinguish which agent performed which action. Route writes to per-agent log files when `agent_id` is present in session state.

## Type
BUILD

## Execution
inline

## Dependencies
- None

## Phase Gate
- [ ] `.claude/hooks/actions-log-appender.py` exists and has been read

## Requirements
- Read `.claude/hooks/actions-log-appender.py`
- Add a function `get_actions_log_path(state)` that:
  - Reads `agent_id` from session_state
  - If `agent_id` is set: returns `STATE_DIR / f'agent-{agent_id}-actions.jsonl'`
  - If `agent_id` is not set: returns `STATE_DIR / 'actions.jsonl'` (existing behavior)
- Update `append_jsonl()` to use the routed path instead of hardcoded `ACTIONS_LOG`
- Add `agent_id` field to the JSON record when present
- Backward compatible: no agent_id = existing behavior unchanged

## Acceptance Criteria
- [ ] `get_actions_log_path` function exists in actions-log-appender.py
- [ ] Function reads agent_id from session_state.json
- [ ] When agent_id is set, writes to `agent-{id}-actions.jsonl`
- [ ] When agent_id is not set, writes to `actions.jsonl`

## Gates Satisfied
- BUILD-01, BUILD-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
