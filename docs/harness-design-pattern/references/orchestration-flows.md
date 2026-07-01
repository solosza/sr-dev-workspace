# Orchestration Flows

How agents execute harness specifications.

## Primitive Loop Execution

**Example: /spawn-subagent "Build H3 adventure pack with 50 monsters"**

```
Agent invokes: /spawn-subagent "Build H3 adventure pack with 50 monsters"

1. Agent reads: .claude/protocols/sr_dev-protocol.md
2. Agent reads: .claude/commands/spawn-subagent.md
3. Agent reads: .claude/skills/spawn-subagent/SKILL.md
4. Agent executes Step 1: Read step-01-parse-description.md
   - Input gate: Check task_description length > 10 ✓
   - Action: Parse and extract task description
   - Output gate: Verify parsed_description ✓
5. Agent executes Step 2: Read step-02-validate-background-safe.md
   - Input gate: Check parsed_description ✓
   - Action: Run decision tree (multi-step? user input? blocking?)
   - Output gate: Verify is_background_safe ✓
6. Agent executes Step 3: Read step-03-invoke-agent.md
   - Input gate: Check is_background_safe ✓
   - Action: Invoke Agent(run_in_background=true, prompt="env -u CLAUDECODE ...")
   - Output gate: Capture agent_id ✓
7. Agent executes Step 4: Read step-04-return-task-id.md
   - Input gate: Check agent_id ✓
   - Action: Return task ID immediately to user
   - Output gate: Verify user can continue working ✓

Task spawned: a7907ce5ecd3f520b
Background agent is running — you can continue working.

[Control returns to user IMMEDIATELY]
[Background agent runs in parallel]
```

---

## Orchestrator Loop Execution

**Example: /reddit-pain/analyze r/entrepreneur**

```
Agent invokes: /reddit-pain/analyze r/entrepreneur

1. Agent reads: .claude/protocols/reddit-pain-analyzer-protocol.md
2. Agent reads: .claude/commands/reddit-pain/analyze.md
3. Agent executes Step 1-3: Validation & initialization
4. Agent executes Step 4: "Call skill: reddit-data-pipeline"
   → Agent loads: .claude/skills/reddit-data-pipeline/SKILL.md
   → Agent executes steps 1-3 of reddit-data-pipeline
   → Output: text_content, posts_count, tokens
   → State file updated
5. Agent executes Step 5: "Call skill: ai-analysis-engine"
   → Agent validates input gate (tokens >= 500)
   → Agent loads: .claude/skills/ai-analysis-engine/SKILL.md
   → Agent executes steps 1-3 of ai-analysis-engine
   → Output: pain_points, startup_ideas, scored_ideas
   → State file updated
6. Agent executes Step 6: "Call skill: results-processor"
   → Agent validates input gate (analysis_complete)
   → Agent loads: .claude/skills/results-processor/SKILL.md
   → Agent executes steps 1-3 of results-processor
   → Output: results.json, results.md
   → State file updated
7. Agent executes Step 7: "Return results.json + results.md"
   → Deliver final deliverables to user

Analysis complete!
results.json + results.md ready
```

---

## Calling Primitive Loops from Orchestrators

**Example: Orchestrator loop spawning background test agents**

```
# /my-pipeline/run-tests [test-count]

## Step 1-3: Initialize...

## Step 4: Spawn background test agents
FOR each test iteration [1 to test-count]:
  4a. Call loop: spawn-subagent
      Input: "Run test suite iteration [N] with performance metrics"
      Receive: agent_id
      Log: agent_id → agents_list
  4b. Continue to next iteration (do NOT wait for agent)

## Step 5: Return agent ID list
Return: [agent_1_id, agent_2_id, ..., agent_N_id]
```

**Flow:**
```
Orchestrator calls spawn-subagent (primitive loop)
  ↓
spawn-subagent returns agent_id immediately
  ↓
Orchestrator continues (doesn't wait)
  ↓
Orchestrator loops N times, spawning N background agents in parallel
  ↓
Orchestrator returns list of agent IDs to user
  ↓
[User checks progress of agents later with TaskGet(agent_id)]
```

---

## Non-Blocking Guarantee

Primitive loops MUST return control immediately:

```
User action: /spawn-subagent [task]
  ↓
Agent processes steps 1-4
  ↓
At Step 4: Return task ID immediately (non-blocking)
  ↓
User CAN CONTINUE WORKING immediately
  ↓
[Background agent runs in parallel]
```

**Violation example:**
```
❌ Agent waits for background task to complete
❌ Agent polls task status
❌ Agent blocks user from next action
```

**Correct pattern:**
```
✅ Agent returns task ID
✅ User continues working
✅ Agent runs in background
✅ User checks progress later if desired
```

---

## Error Recovery

When a step fails:

```
Step execution hits error
  ↓
Consult error-handling.md
  ↓
If recoverable: Retry (with backoff if needed)
  ↓
If max retries exceeded: Fail gracefully
  ↓
Update state with failure reason
  ↓
Report to user with suggestions
```

---

*All orchestration flows follow the same pattern: read → validate → execute → validate → persist → continue.*
