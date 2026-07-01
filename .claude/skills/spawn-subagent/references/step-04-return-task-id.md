# Step 4: Return Task ID (Non-Blocking)

## Purpose

Capture the task ID from the Agent response and return it to the user immediately, without waiting for the background task to complete.

## Capture Task ID

From the Agent tool invocation (Step 3), extract the task ID from the response.

**Agent tool response format:**

```
Async agent launched successfully.
agentId: a7907ce5ecd3f520b
The agent is working in the background. You will be notified automatically when it completes.
```

**Extract the agentId value.** It's typically a string like:
- `a7907ce5ecd3f520b`
- `harness-research-12345`
- `build-adventure-98765`

## Return to User

Format a clear message with the task ID and log file path, then return immediately:

```
Task spawned: [task-id]

You can check progress:
  tail -f /tmp/[task-name]-[timestamp].log

Background agent is running — you can continue working.
```

**Example outputs:**

### Example 1: Simple task

```
Task spawned: a7907ce5ecd3f520b

You can check progress:
  tail -f /tmp/harness-research-1621234567.log

Background agent is running — you can continue working.
```

### Example 2: Long-running task

```
Task spawned: build-adventure-98765

Estimated duration: 2-3 hours

You can check progress:
  tail -f /tmp/build-adventure-1621234567.log

Background agent is running — you can continue working.
```

### Example 3: Multiple agents spawned

```
Agents spawned:

1. Task a7907ce5ecd3f520b (harness research): /tmp/harness-research-1621234567.log
2. Task b1234567890abcdef (execute-pipeline): /tmp/execute-pipeline-128-1621234567.log
3. Task c9876543210fedcba (testing): /tmp/test-all-harnesses-1621234567.log

You can check progress:
  tail -f /tmp/harness-research-1621234567.log
  tail -f /tmp/execute-pipeline-128-1621234567.log
  tail -f /tmp/test-all-harnesses-1621234567.log

All background agents are running in parallel — you can continue working.
```

## Non-Blocking Guarantee

**MANDATORY:** Return control immediately after capturing task ID.

**This MUST happen:**
1. Agent tool is invoked (Step 3)
2. Response received with task ID
3. Message formatted and returned to user
4. **Control returns to user immediately** ← CRITICAL

**This MUST NOT happen:**
- ✗ Wait for agent completion
- ✗ Poll task status
- ✗ Block on output
- ✗ Pause for user confirmation
- ✗ Spin up monitoring thread

## User Experience

After spawn-subagent returns, the user should be able to:

```
> /spawn-subagent Build adventure pack

Task spawned: a7907ce5ecd3f520b

You can check progress:
  tail -f /tmp/build-adventure-1621234567.log

Background agent is running — you can continue working.

> /kernel/backlog Create new backlog item

[Backlog command runs immediately, no waiting]

> tail -f /tmp/build-adventure-1621234567.log

[User checks progress of background agent by reading live log]
[Adventure pack build: 25% complete...]
[Adventure pack build: 50% complete...]
[Adventure pack build: complete! 50 monsters generated.]
```

**Key:** User can invoke new commands immediately after spawn-subagent. No blocking.

## Checking Progress Later

The task ID returned allows the user to reference the background task. Real-time progress is visible via the log file:

```bash
tail -f /tmp/[task-name]-[timestamp].log
```

Real-time output shows what the agent is doing:

```
[INFO] Starting Pulsia marketplace research...
[INFO] Searching for existing harness marketplaces...
[FETCH] claudemarketplaces.com...
[FETCH] aitmpl.com...
[FETCH] agentskills.io...
[INFO] Analysis complete: 8 platforms identified
[INFO] Creating backlog item...
[BACKLOG] Item 130 created: Research harness marketplace platforms
[INFO] Research complete!
```

## Error Handling

**If task ID is missing from response:**

```
ERROR: Failed to spawn background agent

Agent response missing task ID.
Response: [show the actual response]

This is a system issue. Possible fixes:
1. Try again — the Agent tool may be temporarily unavailable
2. Check system logs for errors
3. Contact admin if this persists
```

**If Agent tool itself failed:**

```
ERROR: Background agent spawn failed

Agent tool returned error: [error message]

Possible causes:
1. Agent tool unavailable
2. Invalid bash command format
3. System resource limits

Try again or use sequential execution instead of spawn-subagent.
```

## Implementation Requirements

**Code must:**
- ✓ Invoke Agent tool with run_in_background=True
- ✓ Wrap bash command in prompt
- ✓ Use env -u CLAUDECODE in the bash command
- ✓ Extract task_id from response
- ✓ Format clear message for user
- ✓ Include task_id and log file path in message
- ✓ Return immediately (no waiting)
- ✓ Handle missing task_id gracefully

**Code must NOT:**
- ✗ Wait for agent completion
- ✗ Implement monitoring/polling
- ✗ Block user input
- ✗ Ask for confirmation
- ✗ Modify the Agent response

## Summary

This step completes the spawn-subagent flow:

1. User calls `/spawn-subagent [description]`
2. Description parsed (Step 1)
3. Validated for background safety (Step 2)
4. Agent tool invoked with bash command in prompt (Step 3)
5. Task ID captured and returned to user (Step 4) ← **You are here**
6. **User continues working immediately**
7. Background agent runs to completion
8. User checks progress anytime with `tail -f /tmp/[task].log`

The non-blocking guarantee is met when Step 4 returns.
