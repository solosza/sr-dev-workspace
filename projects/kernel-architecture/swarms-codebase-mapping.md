# Isagawa Codebase → Swarm Pattern Mapping

## Current Architecture as a Swarm

### run-task.sh = Swarm Orchestrator
- Spawns one `claude -p` agent per task, sequentially
- Each agent is stateless (one-shot) — born, executes task, dies
- Orchestrator tracks progress via `completed_tasks[]` in workflow state
- Retry logic: 2 consecutive failures → skip task, move to next
- **Swarm analog:** Sequential task dispatch with failure tolerance

### execute-pipeline = Pipeline Controller
- Takes a goal → decomposes into tasks → dispatches to run-task.sh
- Classify-then-route: simple tasks inline, complex tasks via run-task.sh
- Manages pipeline state across steps (parse → task-builder → execute → validate)
- **Swarm analog:** High-level planner that creates work for the swarm

### prod-test = Nested Swarm Spawner
- Outer agent builds a test workspace
- Inner run-task.sh executes test tasks inside that workspace
- Two-layer spawning: parent → test coordinator → test agents
- **Swarm analog:** Specialized sub-swarm for validation

### Gate Contracts = Handoff Protocol
- Each task's output feeds the next task's prerequisites
- Gates define mechanical verification: file_exists, grep, run_code
- Failed gates block progression — the "handoff" only completes when the gate passes
- **Swarm analog:** Typed, verified message passing between agents

### Hook System = Governance Layer
- Every agent (spawned or interactive) governed by the same hooks
- universal-gate-enforcer.py blocks actions when anchor is needed
- test-failure-detector.py forces learning after failures
- actions-log-appender.py tracks all work for audit
- **Swarm analog:** Nothing comparable exists in CrewAI/AutoGen/LangGraph/Swarm

### Skills = Role Specialization
- website-cloner: extraction specialist
- audit-workflow: review/audit specialist
- prod-test: testing specialist
- task-builder: decomposition specialist
- **Swarm analog:** Dedicated-job agents with defined capabilities

## The Delta: Pipeline vs Swarm

| Feature | Isagawa (Current) | Purpose-Built Swarm |
|---------|-------------------|---------------------|
| Execution | Sequential (one agent at a time) | Parallel (multiple agents simultaneously) |
| Agent lifetime | One-shot (born → task → die) | Persistent (live across tasks, accumulate context) |
| Inter-agent comms | File-based (state files on disk) | Direct (message passing, shared memory) |
| Agent identity | Anonymous (each `claude -p` is identical) | Named (researcher, builder, reviewer have distinct prompts) |
| Orchestration | Centralized (run-task.sh controls flow) | Distributed or centralized (varies) |
| Governance | Hook-enforced (mechanical, cannot bypass) | None or voluntary |
| Self-improvement | Lesson recording → protocol update | No equivalent |

## Key Finding

Isagawa is already a **governed sequential swarm**. The components map cleanly:
- run-task.sh = orchestrator
- Skills = agent roles
- Gate contracts = handoff protocols
- Hooks = governance layer
- Lessons = self-improvement loop

What it's NOT (yet):
- Not parallel — agents run one at a time
- Not persistent — agents don't accumulate context across tasks
- Not communicative — agents don't talk to each other, only to files
- Not visual — no dashboard showing swarm activity

The delta is primarily **parallelism** and **persistence**. The governance and self-improvement layers are unique advantages no competitor has.
