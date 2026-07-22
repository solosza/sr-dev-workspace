# Injection Capability: PreToolUse Advisory Context

## Purpose

Verify whether Claude Code PreToolUse hooks can inject non-blocking advisory context visible to the agent, enabling JIT rule injection without blocking the tool call.

---

## Live Test Results

**Claude Code version:** 2.1.207
**Test date:** 2026-07-21
**Verdict: YES — advisory injection is fully supported.**

### Test Setup

Created a scratch PreToolUse hook registered on the `Read` tool matcher:

```python
#!/usr/bin/env python3
import json, sys

data = json.load(sys.stdin)
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "additionalContext": "ADVISORY_TEST: This is injected advisory context from scratch hook."
    }
}
print(json.dumps(output))
sys.exit(0)
```

### Observed Behavior

When the agent invoked the `Read` tool:

1. The hook executed, printed JSON to stdout, and exited 0
2. The tool call **proceeded normally** (not blocked)
3. The advisory text appeared in the agent's context as a `<system-reminder>` tag:

```
PreToolUse:Read hook additional context: ADVISORY_TEST: This is injected advisory context from scratch hook.
```

The context injection was visible to the agent and appeared between the tool call and its result, formatted as: `PreToolUse:[ToolName] hook additional context: [additionalContext value]`.

---

## Exact JSON Output Schema

### PreToolUse Hook Output (exit 0)

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow | deny | ask",
    "permissionDecisionReason": "string (shown when deny/ask)",
    "additionalContext": "string (injected as system-reminder, visible to agent)",
    "updatedInput": { "field": "modified_value (optional, rewrites tool input)" }
  }
}
```

### Field Behavior Matrix

| Field | Exit 0 | Exit 2 | Agent-Visible |
|-------|--------|--------|---------------|
| `permissionDecision: "allow"` | Tool proceeds | N/A (ignored) | No (transparent) |
| `permissionDecision: "deny"` | Tool blocked | N/A | Yes (reason shown) |
| `permissionDecision: "ask"` | User prompted | N/A | Depends on user choice |
| `additionalContext` | Injected as system-reminder | Ignored | **Yes** |
| `updatedInput` | Rewrites tool input | Ignored | No (transparent) |
| stderr (exit 2) | N/A | Tool blocked | **Yes** (error message) |
| plain stdout (exit 0, no JSON) | Debug log only | N/A | **No** |

### Key Distinctions

1. **Plain stdout on exit 0 is NOT visible** to the agent for PreToolUse (unlike UserPromptSubmit/SessionStart where plain stdout IS injected as context)
2. **JSON `additionalContext` on exit 0 IS visible** — appears as `<system-reminder>` tag
3. **stderr on exit 2 IS visible** — appears as an error/block message
4. **`updatedInput` silently rewrites** the tool input before execution (the agent sees the original input in its context but the modified input executes)
5. **Character limit:** 10,000 characters for all hook output strings

---

## Agent-Visible Rendering

The `additionalContext` string renders as:

```xml
<system-reminder>
PreToolUse:[ToolName] hook additional context: [additionalContext value]
</system-reminder>
```

This appears:
- **After** the agent's tool call in the conversation
- **Before** the tool result
- As a system-level message (same treatment as other `<system-reminder>` tags)
- The agent processes it as authoritative context from the system, not user input

This rendering is ideal for JIT rule injection because:
- The agent sees the rule at the exact moment it's about to take the action
- The rule is presented with system-level authority
- The tool call proceeds (non-blocking), so rules are advisory not gates
- Rules that warrant blocking can still use `permissionDecision: "deny"` or exit 2

---

## Fallback Design (If Advisory Injection Were Unsupported)

For reference, if `additionalContext` were not available, the fallback would be:

### Option A: Block-with-FIX Pattern (Current Hook Model)

```python
# Block the action, show the rule, require the agent to retry
sys.stderr.write("RULE REMINDER: [rule text]\n\nRetry your command.\n")
sys.exit(2)
```

**Downsides:** Doubles action count (block + retry), disrupts agent flow, frustrates autonomous cycling.

### Option B: `updatedInput` Injection

```python
# Prepend rule text to the command or content
original = data['tool_input']['command']
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "updatedInput": {"command": f"# RULE: [rule text]\n{original}"}
    }
}
```

**Downsides:** Modifies the actual tool input; only works for text-based inputs; risk of corrupting commands.

### Option C: State File + Session-Start Injection

Write rules to a state file; inject them during SessionStart or UserPromptSubmit hooks.

**Downsides:** Not just-in-time; rules injected at session/prompt level, not at the moment of the relevant action.

**Conclusion:** `additionalContext` is the correct and optimal mechanism. No fallback needed.

---

## Implications for JIT Rule Injection Design

1. **The mechanism exists and works.** PreToolUse hooks can inject rule text visible to the agent without blocking.
2. **The injection is contextual.** Rules appear at the exact moment the agent is about to perform a specific action (Write, Edit, Bash), making them maximally relevant.
3. **The injection is non-disruptive.** Unlike blocking (exit 2), advisory injection doesn't require the agent to retry, preserving action count and autonomous flow.
4. **The injection is tool-specific.** The hook receives `tool_name` and `tool_input`, so rules can be matched to specific actions (e.g., "you're about to Write a file you haven't Read" or "this Bash command targets a cross-repo path — remember --rootdir").
5. **10K character limit is generous.** Most rules are 1-3 sentences. Even injecting 5-10 rules per action would be well within limits.
6. **The mechanism is the same for all matchers.** A single PreToolUse hook registered on `Edit|Write|Bash` can inject different rules based on the tool and input context.

---

## Statistics

- **Advisory injection supported:** YES (confirmed via live test)
- **Mechanism:** `hookSpecificOutput.additionalContext` with `permissionDecision: "allow"`, exit 0
- **Rendering:** `<system-reminder>` tag, system-level authority
- **Character limit:** 10,000
- **Blocking fallback needed:** NO
