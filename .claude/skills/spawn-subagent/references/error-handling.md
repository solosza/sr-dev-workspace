# Error Handling — Spawn-Subagent

## Overview

This reference documents error cases and recovery strategies for each step of spawn-subagent.

---

## Step 1: Parse Description

### Error 1A: Description empty or missing

**Cause:** User calls `/spawn-subagent` with no arguments or empty string

**Detection:**
```
Description length == 0
```

**Recovery:**
```
ERROR: No task description provided

Usage: /spawn-subagent [task description]

Examples:
  /spawn-subagent Test all harness commands
  /spawn-subagent Build H3 adventure pack with 50 monsters
  /spawn-subagent Refactor backlog 127 to specification

Provide a description and try again.
```

**Action:** Fail immediately. Ask user to provide description.

### Error 1B: Description too short

**Cause:** User provides very short description (< 10 characters)

**Detection:**
```
Description length < 10
```

**Recovery:**
```
ERROR: Description too short (minimum 10 characters)

You provided: "[description]"

Please provide more detail about what the background agent should do.

Example: Instead of "test", use "Test the new harness specification against sample inputs"
```

**Action:** Fail immediately. Ask for more detail.

---

## Step 2: Validate Background-Safe

### Error 2A: Task requires user confirmation

**Cause:** Description contains patterns like "ask me", "confirm", "wait for user"

**Detection:**
```
Pattern match: "ask me" / "confirm" / "wait" / "when I"
```

**Recovery:**

**Option 1 (Warn but proceed):**
```
⚠ Task description sounds interactive: "[excerpt]"

Interpreted as: [background-safe interpretation]

Background agent will make decisions autonomously.

Proceeding...
```

**Option 2 (Fail):**
```
This task requires user confirmation:
  "[excerpt]"

Background agents cannot interact with users. Options:
1. Restructure the task for autonomous execution
2. Run sequentially instead (don't use spawn-subagent)

Example restructure:
  Instead: "Deploy and ask me if it worked"
  Better: "Deploy and log whether tests pass"

Try again with an autonomous task description.
```

**Action:** Warn (soft gate). Proceed unless critical block.

### Error 2B: Task blocks downstream work

**Cause:** Result is needed immediately for next step

**Detection:**
```
Pattern match: "then run" / "after that" / "next step is"
Description includes dependency on result
```

**Recovery:**
```
⚠ This task blocks downstream work

Description: "[excerpt]"

If the next step MUST wait for this result, consider:
1. Run sequentially (don't spawn background)
2. Redesign workflow to allow parallel work

Proceeding with background spawn, but note this may cause issues.
```

**Action:** Warn (soft gate). Proceed but flag.

---

## Step 3: Invoke Bash Tool (Background)

### Error 3A: Bash tool not available

**Cause:** Bash tool unavailable or system issue

**Detection:**
```
Bash tool call fails
Response is error message, not task info
```

**Recovery:**
```
ERROR: Failed to spawn background agent

The Bash tool is unavailable. This may be:
1. Temporary system issue → Try again in a moment
2. Rate limiting → Wait a few seconds and retry
3. Configuration problem → Contact admin

Technical error: [show actual error]
```

**Action:** Fail immediately. Suggest retry or contact admin.

### Error 3B: Command too long

**Cause:** Task description is extremely detailed (> 10,000 characters)

**Detection:**
```
command_length > system_limit
Bash tool returns error
```

**Recovery:**
```
ERROR: Command is too long for Bash tool

Your description: [length] characters (limit: 10000)

Suggestions:
1. Simplify the description
2. Remove examples or detailed explanations
3. Include file paths instead of inline text
4. Point to external reference instead of embedding

Example: Instead of pasting 5KB of code, say:
  "Refactor the harness per the spec at docs/harness-spec.md"
```

**Action:** Fail. Ask user to shorten description.

### Error 3C: Malformed response

**Cause:** Bash tool response doesn't contain task ID

**Detection:**
```
Response missing task_id field
task_id == null or undefined
Response unparseable
```

**Recovery:**
```
ERROR: Bash tool returned unexpected response

Response was: [show raw response]

This may be:
1. A system glitch → Try again
2. A version mismatch → Contact admin

Cannot proceed without task ID.
```

**Action:** Fail. Suggest retry.

---

## Step 4: Return Task ID

### Error 4A: No task ID captured

**Cause:** Step 3 succeeded but task ID couldn't be extracted

**Detection:**
```
Bash response received
task_id extraction fails
No valid ID in response
```

**Recovery:**
```
ERROR: Could not extract task ID from Bash response

Bash response: [show response]

This is a system issue. Suggestions:
1. Try again — may be transient
2. Check system logs
3. Contact admin
```

**Action:** Fail. Provide details for debugging.

---

## Retry Strategy

### When to retry

| Error | Retry? | Max Attempts |
|-------|--------|--------------|
| Empty description | No — ask user | N/A |
| Too short description | No — ask user | N/A |
| Bash tool unavailable | Yes | 3 |
| Command too long | No — ask user | N/A |
| Malformed response | Yes | 2 |
| Task ID missing | Yes | 2 |

### Backoff pattern

If retrying:
```
Attempt 1: Retry immediately
Attempt 2: Wait 1 second, retry
Attempt 3: Wait 2 seconds, retry
After attempt 3: Fail with message
```

---

## User-Facing Error Messages

All errors should:
- ✓ Clearly state the problem
- ✓ Suggest a fix
- ✓ Provide examples when helpful
- ✓ Be non-technical (unless user is debugging)

**Bad example:**
```
TaskID extraction failed: NoneType error at line 42
```

**Good example:**
```
ERROR: Could not extract task ID from Agent response

The Agent tool returned a response, but it didn't include
a task ID we could use to track the background agent.

This usually means:
1. Temporary system issue — try again in a moment
2. Agent tool configuration problem — contact admin

Your description: "[description]"
Agent response: [show what we got back]
```

---

## Recovery Decision Tree

```
Spawn attempt failed

↓
Which step failed?

├─ Step 1 (Parse)
│  └─ Ask user for valid description
│
├─ Step 2 (Validate)
│  └─ Warn but proceed (soft gate)
│     OR ask user to restructure
│
├─ Step 3 (Invoke Bash)
│  ├─ Bash unavailable? → Retry 3x with backoff
│  ├─ Command too long? → Ask user to shorten
│  ├─ Response malformed? → Retry 2x
│  └─ Other error? → Fail with details
│
└─ Step 4 (Return ID)
   ├─ Task ID missing? → Retry 2x
   └─ Extraction error? → Fail with details
```

---

## Implementation Checklist

When implementing error handling:

- ✓ Catch exceptions at each step
- ✓ Provide clear error messages
- ✓ Suggest fixes where possible
- ✓ Don't silently fail
- ✓ Log errors for debugging
- ✓ Implement retry logic where appropriate
- ✓ Never block user on retries
- ✓ Default to user-friendly messages
