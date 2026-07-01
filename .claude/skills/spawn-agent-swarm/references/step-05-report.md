# Step 5: Report Final Status

Generate and display final status report when monitoring completes.

## Report Timing

Report is generated when:
- All agents reach status `complete` (normal case)
- Timeout reached (5 minutes)
- Monitoring exits early (no running agents detected)

## Report Structure

```
====================================================================
AGENT SWARM EXECUTION COMPLETE
====================================================================

Execution time: 5m 23s
Agents spawned: 3
Agents completed: 3
Agents failed: 0

RESULTS:
--------

Agent 128: COMPLETE
  Deliverable: Pulsia autonomous AI platform research
  Tasks: 8/8 complete
  Time: 45 minutes
  Backlog: docs/backlog/done/128-market-research-pulsia-autonomous-ai-platform.md

Agent 131: COMPLETE
  Deliverable: Claude Code Harness Distribution Strategy
  Tasks: 7/7 complete
  Time: 52 minutes
  Backlog: docs/backlog/done/131-market-research-claude-code-harness-distribution-strategy.md

Agent 132: COMPLETE
  Deliverable: Claude Harness Marketplace Research
  Tasks: 6/6 complete
  Time: 38 minutes
  Backlog: docs/backlog/done/132-market-research-claude-harness-marketplace-landscape.md

====================================================================
DELIVERABLES
====================================================================

Location: docs/backlog/done/
Archived backlogs: 3
Task folders: projects/[backlog-project-names]

Ready for: Next workflow step, post-processing, or user review
```

## Report Data Sources

Read final manifest and extract:

```json
{
  "total_execution_time": "NOW - first_spawn_time",
  "total_agents": count(manifest.active_agents),
  "completed": count(status=="complete"),
  "failed": count(status=="failed"),
  "results": [
    {
      "backlog": N,
      "status": "complete|failed",
      "deliverable": agent.deliverable,
      "progress": agent.progress,
      "completed_at": agent.completed_at,
      "execution_time": completed_at - spawned_at
    }
  ]
}
```

## Report Variants

### Success Case (All Complete)

```
AGENT SWARM EXECUTION COMPLETE

Execution time: [time]
Agents spawned: [N]
Agents completed: [N]

[detailed results table]
```

### Partial Completion (Some Still Running at Timeout)

```
AGENT SWARM MONITORING TIMEOUT

Execution time: 5m 0s (timeout)
Agents spawned: 3
Agents completed: 2
Agents still running: 1
Agents failed: 0

[results table with running agents marked]

NOTE: Agent 131 is still executing. Check progress with:
  tail -f .claude/state/agent-swarm.json
  tail -f /tmp/execute-pipeline-131-*.log
```

### Failure Case (Agent Failed)

```
AGENT SWARM PARTIAL COMPLETION

Execution time: 3m 45s
Agents spawned: 3
Agents completed: 2
Agents failed: 1

[results table]

FAILED AGENTS:
  Agent 129: No progress updates after 30 seconds (error_code: timeout)
  Recommendation: Check state file and fix, then respawn

How to fix:
1. Read the agent's error log
2. Fix the underlying issue
3. Run: /spawn-agent-swarm 129
```

## Print to Console

Output should be printed to user console (not silent). Example:

```python
print()
print("=" * 70)
print("AGENT SWARM EXECUTION COMPLETE")
print("=" * 70)
print()
print(f"Execution time: {execution_time}")
print(f"Agents spawned: {total_agents}")
print(f"Agents completed: {completed_count}")
print()

for agent in results:
    print(f"Agent {agent.backlog}: {agent.status.upper()}")
    print(f"  Deliverable: {agent.deliverable}")
    print(f"  Time: {agent.execution_time}")
print()
```

## Next Steps

After reporting:
1. **User can proceed** — results are available for next workflow step
2. **Manual check** — user can inspect deliverables in `docs/backlog/done/`
3. **Respawn if needed** — if any agent failed, user can respawn just that agent
4. **Manifest preserved** — `agent-swarm.json` kept for audit trail

## Return Value

Return agent swarm execution status:

```python
{
  "status": "success|timeout|partial",
  "total_agents": N,
  "completed": M,
  "failed": K,
  "execution_time_seconds": T,
  "agent_results": [...]
}
```
