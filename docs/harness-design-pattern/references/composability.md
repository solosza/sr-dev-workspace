# Composability: Calling Primitive Loops from Orchestrators

Primitive loops can be invoked by orchestrator loops, enabling composition and reusability.

## How It Works

**Orchestrator loop can call primitive loop as a step:**

```markdown
# /my-pipeline/run-parallel-tests [count]

## Instructions

1. Initialize test state
2. For each iteration (1 to count):
   a. **Call loop:** spawn-subagent
      Input: "Run test suite iteration [N]"
      Output: agent_id
      Behavior: Non-blocking (doesn't wait)
   b. Log agent_id
3. Return list of all agent_ids to user
```

**Flow:**
```
Orchestrator (Step 2a):
  ↓
Calls primitive loop: spawn-subagent
  ↓
Primitive loop executes steps 1-4
  ↓
Primitive loop returns: agent_id
  ↓
Orchestrator receives agent_id
  ↓
Orchestrator continues immediately (doesn't wait)
  ↓
Orchestrator repeats for next iteration
```

---

## Example: Parallel Agent Spawning

```markdown
# /test-harness/parallel-run [agent-count]

Spawn multiple autonomous test agents in parallel.

## Instructions

1. Parse agent_count from input
2. Validate agent_count >= 1, <= 20
3. Initialize agents_list = []
4. **Loop:** For i = 1 to agent_count:
   a. **Call primitive loop: spawn-subagent**
      Description: "Run comprehensive test suite iteration [i] with verbose logging"
      Receive: agent_id
      Add agent_id to agents_list
      **Do NOT wait for agent to complete**
5. Return agents_list to user
6. Provide user with instructions:
   "Check progress: TaskGet(task_id='[agent_id]')"
```

**Result:**
- User invokes: `/test-harness/parallel-run 10`
- Orchestrator spawns 10 agents in rapid succession
- Each call to spawn-subagent returns immediately
- Orchestrator completes and returns all 10 agent IDs
- User can check progress of any agent anytime
- All 10 agents run in parallel

---

## Primitive Loop Contract

When calling a primitive loop from an orchestrator:

**Expectation:**
```
call_primitive_loop(input) → returns output immediately (non-blocking)
```

**NOT:**
```
call_primitive_loop(input) → waits for completion → returns output (BLOCKING)
```

**Key guarantee:** Primitive loops return control immediately, enabling orchestrator parallelism.

---

## Nested Calling

Primitive loops can call OTHER primitive loops:

```markdown
# /utility/batch-create-backlogs [count]

Creates multiple backlog items using a reusable primitive loop.

## Instructions

1. For each item (1 to count):
   a. **Call primitive loop: spawn-subagent**
      Description: "Create backlog item [i] from template"
      Receive: agent_id
   b. **Call primitive loop: create-backlog** (if it existed)
      Input: backlog_data[i]
      Receive: backlog_id
2. Return list of all IDs
```

---

## Design Constraints

### Do:
- ✅ Call primitive loops from orchestrators
- ✅ Call primitive loops from other primitive loops
- ✅ Spawn multiple instances of same primitive loop
- ✅ Return immediately after calling primitive loop
- ✅ Let background agents run in parallel

### Don't:
- ❌ Wait for primitive loop to complete
- ❌ Orchestrator loops call each other (orchestrate skills instead)
- ❌ Create coupling between orchestrators
- ❌ Block user or parent operation

---

## Real-World Use Case

**Scenario:** Testing a harness before production

```markdown
# /ops/test-all-harnesses

Tests every harness in production in parallel.

## Instructions

1. Load list of harnesses: [reddit-pain, spawn-subagent, ...]
2. Initialize results = []
3. For each harness:
   a. **Call primitive loop: spawn-subagent**
      Description: "Run production test for [harness]"
      Receive: agent_id
      Append to results
4. Return results to user
5. User checks status: TaskGet(task_id='agent_1_id'), etc.
```

**Benefits:**
- All tests run in parallel (10 harnesses tested simultaneously)
- Orchestrator completes immediately
- User can monitor progress via agent IDs
- No blocking, maximum parallelism

---

*Composability enables primitive loops to be building blocks for larger orchestrations.*
