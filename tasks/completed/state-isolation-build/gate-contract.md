# Gate Contract — State Isolation Build

| Gate ID | Type | Check | File/Path | Expected |
|---------|------|-------|-----------|----------|
| BUILD-01 | file_exists | actions-log-appender.py modified | .claude/hooks/actions-log-appender.py | Contains `agent_id` routing logic |
| BUILD-02 | grep | Agent log routing function exists | .claude/hooks/actions-log-appender.py | `get_actions_log_path` or `agent_id` in file |
| BUILD-03 | grep | Agent state write guard | .claude/hooks/universal-gate-enforcer.py | `agent_id` check blocks parent state writes |
| BUILD-04 | grep | run-task.sh passes agent_id | run-task.sh | `agent_id` in pre_init_state line |
| BUILD-05 | grep | Anchor handles per-agent cleanup | .claude/commands/kernel/anchor.md | `agent-*-state.json` or `agent-*-actions.jsonl` mentioned |
| TEST-01 | run_code | With agent_id set, actions append to agent-specific log | .claude/hooks/actions-log-appender.py | agent-{id}-actions.jsonl created |
| TEST-02 | run_code | Without agent_id, actions append to shared log | .claude/hooks/actions-log-appender.py | actions.jsonl used (backward compatible) |
