# Gate Contract — Workflow State Isolation Build

| Gate ID | Type | Check | File/Path | Expected |
|---------|------|-------|-----------|----------|
| BUILD-01 | grep | Gate enforcer routing | .claude/hooks/universal-gate-enforcer.py | get_workflow_state function routes by agent_id |
| BUILD-02 | grep | run-task.sh routing | run-task.sh | AGENT_WORKFLOW variable and routing logic |
| BUILD-03 | grep | complete.md routing | .claude/commands/kernel/complete.md | agent_id routing instructions for per-agent workflow |
| BUILD-04 | grep | Workflow seeding | run-task.sh | seed_agent_workflow function |
| TEST-01 | bash | Isolation verification | Test script | All routing checks pass |
