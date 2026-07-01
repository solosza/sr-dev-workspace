# Step 1: Parse Task Description

## Input

User provides a task description via the skill arguments:
```
/spawn-subagent [description]
```

**Example inputs:**
```
Build H3 adventure pack with 50 monsters
Test all selenium harness commands
Refactor backlog 127 to harness specification
Run 2-hour scaling tests
Fix CSS bugs in attestation.html and QA platforms
```

## Parsing Rules

### Extract the description

1. Take the entire argument string as the task description
2. Strip leading/trailing whitespace
3. Preserve capitalization, punctuation, technical terms

**Example:**
```
Input: "  Build H3 adventure pack with 50 monsters  "
Output: "Build H3 adventure pack with 50 monsters"
```

### Validate non-empty

Check that description length > 10 characters.

**If empty or too short:**
```
Error: Description too short (minimum 10 characters)
User provided: "[input]"
Fix: Provide a more detailed description of what the background agent should do
```

### Detect description quality issues

Look for red flags that suggest the task might not be background-safe. Don't block on these — just note them.

**Quality checks:**
| Pattern | Issue | Action |
|---------|-------|--------|
| "what is" / "how to" | Looks like a question | Note: suggest rephrasing as task (e.g., "investigate" instead) |
| "check if" / "do you think" | Requires evaluation/opinion | Note: background agent will use own judgment |
| "tell me" / "show me" | Might expect interactive output | Note: agent will log results, not provide interactive feedback |
| "(waiting)" / "pause" | Explicitly blocking | WARN: This defeats background execution |

**Example warning:**
```
⚠ Description looks interactive: "Tell me if the build passes"
  Suggested: "Build the project and report whether it passes"
  Proceeding anyway — background agent will log results.
```

## Output

A clean task description ready for the Agent tool:

```json
{
  "description": "Build H3 adventure pack with 50 monsters",
  "is_valid": true,
  "quality_issues": [],
  "estimated_duration": "multi-hour" // optional guess based on keywords
}
```

## Examples

### Example 1: Good description

**Input:**
```
/spawn-subagent Test all selenium harness commands end-to-end
```

**Parsed:**
```
{
  "description": "Test all selenium harness commands end-to-end",
  "is_valid": true,
  "quality_issues": [],
  "estimated_duration": "multi-hour"
}
```

### Example 2: Description with minor quality flag

**Input:**
```
/spawn-subagent Check if the new harness spec parses correctly
```

**Parsed:**
```
{
  "description": "Check if the new harness spec parses correctly",
  "is_valid": true,
  "quality_issues": ["Interactive-sounding: 'Check if'"],
  "estimated_duration": "short"
}
```

**Note:** Agent proceeds anyway. The background agent will run the check and log results.

### Example 3: Too short

**Input:**
```
/spawn-subagent test
```

**Error:**
```
Description too short (minimum 10 characters)
User provided: "test"
Fix: Provide a more detailed description of what the background agent should do

Example: "Test the new harness specification against sample inputs"
```

## Error Handling

**If description is empty/missing:**
- Fail immediately
- Ask user to provide a description
- Example: `/spawn-subagent Refactor backlog 127 to pure specification`

**If description is too short (<10 chars):**
- Fail immediately with same message as above

**If quality issues detected (but valid):**
- Proceed with warning
- Agent will handle it (background agent has judgment)

## Implementation Note

This step is pure validation — no tool invocations, no side effects. Just parse and check.

**Do:**
- ✓ Parse the string
- ✓ Check length and content
- ✓ Report quality issues as warnings
- ✓ Return cleaned description

**Don't:**
- ✗ Invoke Agent tool yet
- ✗ Block on warnings
- ✗ Modify the description
- ✗ Pre-judge whether task will succeed
