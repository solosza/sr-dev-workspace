# Architectural Gaps — What Needs to Change for Full Swarm Support

## Gap 1: Parallel Task Execution

### Current State
- run-task.sh executes tasks sequentially: one `claude -p` at a time
- No concurrent agent instances
- Background Agent tool can spawn one parallel process, but state contention prevents multiple

### What Would Change
- Parallel run-task.sh: spawn N agents simultaneously, each working on independent tasks
- State partitioning: each agent gets its own state scope (no shared `session_state.json`)
- Merge protocol: after parallel execution, merge results back into shared state
- Dependency-aware scheduling: only parallelize tasks with no dependencies between them

### Effort: HIGH
- Requires state scoping (backlog 040 was a start but didn't solve parallelism)
- Requires rewriting run-task.sh to manage concurrent processes
- Requires merge conflict resolution for state files
- Estimated: 2-3 pipelines of work

### Value: MEDIUM
- Speed improvement for large task sets (8 tasks in 20 min instead of 60)
- Visual appeal (Pattern 2 from viral analysis)
- But: most research/build tasks have dependencies, limiting parallelism in practice

### Necessity: NICE-TO-HAVE
- Sequential execution works for all current use cases
- The speed cost is acceptable for governed execution
- Only becomes necessary for: real-time multi-agent products, parallel content generation at scale

## Gap 2: Agent Identity and Persistence

### Current State
- Every `claude -p` instance is anonymous — same system prompt, no memory of past invocations
- Agent "identity" comes from the task file it reads, not from persistent state
- Lessons are system-wide, not agent-specific

### What Would Change
- Named agents: "The Auditor", "The Builder", "The Researcher" — each with its own system prompt, memory, and specialization
- Persistent memory: agent-specific context that accumulates across invocations
- Specialization fine-tuning: system prompts optimized for each role over time
- Agent registry: track which agents exist, what they've done, how they've performed

### Effort: MEDIUM
- System prompt per agent role: LOW (just different CLAUDE.md files)
- Persistent memory: MEDIUM (need a memory store — file-based or database)
- Agent registry: LOW (JSON file tracking agent metadata)
- Performance tracking: MEDIUM (need metrics collection per agent)

### Value: HIGH
- Enables the "agent team" narrative for marketing
- Persistent memory means agents learn from repeated execution
- Agent-specific optimization improves quality over time

### Necessity: MEDIUM
- Current skill model works but doesn't learn per-role
- Would become necessary for: customer-facing agents, specialized audit agents, agent marketplace

## Gap 3: Inter-Agent Communication

### Current State
- Agents communicate via files: state files, task files, gate contracts
- No direct message passing between agents
- No shared context beyond what's on disk

### What Would Change
- Message queue: agents can send typed messages to other agents
- Shared context: a shared memory space that multiple agents can read/write
- Event system: agents can subscribe to events (task completed, error detected, etc.)
- Handoff protocol: agent A can explicitly transfer work to agent B with context

### Effort: HIGH
- Requires infrastructure: message queue, event bus, shared memory store
- Requires agent lifecycle management (who's alive, who's waiting, who's blocked)
- Requires error handling for failed communications
- Estimated: 2-3 pipelines of work

### Value: MEDIUM
- Enables real-time coordination (auditor spots issue → builder gets notified → tester re-runs)
- Reduces file I/O overhead
- But: file-based communication is simple, reliable, and sufficient for current use cases

### Necessity: NICE-TO-HAVE
- File-based communication works and is auditable
- Only becomes necessary for: real-time multi-agent coordination, high-frequency task handoffs

## Gap 4: Visual Dashboard

### Current State
- Terminal-only: agent output appears as text in the console
- run-task.sh output shows task names and pass/fail
- No visual representation of agent activity, task progress, or swarm state

### What Would Change
- Web dashboard: real-time view of agent activity, task progress, swarm state
- Agent cards: each agent shows its current task, status, and recent history
- Pipeline view: DAG visualization of task dependencies and progress
- Metrics: token usage, time per task, success rates, cost tracking

### Effort: MEDIUM
- Simple web UI: LOW (static HTML + WebSocket for real-time updates)
- Real-time agent streaming: MEDIUM (need event emission from run-task.sh)
- Metrics collection: MEDIUM (extend actions-log-appender)
- Full dashboard app: HIGH (React/Vue app with database backend)

### Value: HIGH
- Essential for demos and marketing (Pattern 2 from viral analysis)
- Useful for debugging multi-agent executions
- Required for any customer-facing product

### Necessity: HIGH for marketing/demos, LOW for core functionality

## Priority Matrix

| Gap | Effort | Value | Necessity | Priority |
|-----|--------|-------|-----------|----------|
| Parallel execution | HIGH | MEDIUM | NICE-TO-HAVE | 4th |
| Agent persistence | MEDIUM | HIGH | MEDIUM | 2nd |
| Inter-agent comms | HIGH | MEDIUM | NICE-TO-HAVE | 3rd |
| Visual dashboard | MEDIUM | HIGH | HIGH (marketing) | 1st |

## Recommended Build Order

1. **Visual dashboard** — highest ROI. A simple web view of the loop running would make demos compelling and is the fastest path to viral content.
2. **Agent persistence** — medium effort, high value. Named agents with memory would enable the "agent team" narrative and improve quality over time.
3. **Inter-agent comms** — defer. File-based communication is sufficient for sequential execution.
4. **Parallel execution** — defer. Only needed when task volume justifies the complexity. State contention is the hard problem and hasn't been fully solved.
