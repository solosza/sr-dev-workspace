# Step 2: Validate Background-Safe

## Purpose

Not all tasks are suitable for background execution. This step validates that the task can run autonomously without requiring:
- User confirmation mid-execution
- Interactive feedback loops
- Immediate result access
- Blocking downstream work

## Decision Tree

```
Is the task:

1. Multi-step execution?
   YES → Suitable for background ✓
   NO → Ask: Does it need user confirmation?
        YES → NOT suitable ✗
        NO → Ask: Will result be needed immediately?
             YES → NOT suitable ✗
             NO → Suitable for background ✓

2. Long-running (>30 seconds)?
   YES → Suitable for background ✓
   NO → Still fine, just short duration

3. Generates large output (logs, files)?
   YES → Suitable for background ✓
        (User can check results later)
   NO → Still fine

4. Requires user input mid-execution?
   YES → NOT suitable ✗
        (Spawn a subagent that handles all decisions autonomously)
   NO → Suitable for background ✓

5. Blocks downstream work?
   YES → NOT suitable ✗
        (Restructure task so parallel work is possible)
   NO → Suitable for background ✓
```

## Good Candidates

**Multi-hour builds:**
- Build adventure pack with 50 monsters
- Generate 100 test scenarios
- Run full test suite (selenium, e2e, production)
- Refactor large codebase

**Parallel research:**
- Spawn 2+ agents to explore different approaches
- Run simultaneous analyses
- Fetch data from multiple sources

**Batch processing:**
- Process 1000 records
- Run pipeline across 10 repos
- Execute 50+ tasks sequentially

**Long-running validations:**
- Production test suite
- Comprehensive harness test
- Load testing or scaling tests

## Anti-Patterns (NOT Background-Safe)

**❌ Requires user confirmation:**
```
"Deploy to production" — needs user approval
"Create GitHub repo" — needs user to choose name
"Run migration" — needs user to verify before commit
```

**❌ Blocking downstream work:**
```
Task A spawns; Task B can't start until A completes
Result of background task is needed immediately for next step
```

**❌ Interactive feedback loops:**
```
"Run tests and ask me if you want to retry"
"Analyze results and ask which approach to take"
```

**❌ Requires user monitoring:**
```
"Build while I'm busy and ping me if it fails"
(Acceptable: "Build and log results; I'll check later")
```

## Validation Rules

| Condition | Result | Action |
|-----------|--------|--------|
| Contains "ask", "confirm", "wait for", "when I" | ❌ | Reject — spawn only autonomous agents |
| Contains "immediately after" or "next step is" | ❌ | Reject — task blocks downstream |
| Clearly needs result for next action | ❌ | Reject — do sequential instead |
| Multi-step, no user input needed | ✅ | Approve — background safe |
| "Build X", "test Y", "refactor Z" | ✅ | Approve — typical background work |
| Explicitly says "background" or "parallel" | ✅ | Approve — user intends background execution |

## Examples

### Example 1: Good — Multi-hour build

**Description:**
```
Build H3 adventure pack with 50 monsters and test all encounters
```

**Analysis:**
- Multi-step ✓
- No user confirmation needed ✓
- Not blocking downstream ✓
- Long-running ✓

**Decision:** ✅ **BACKGROUND-SAFE**

### Example 2: Good — Parallel research

**Description:**
```
Analyze 3 competitor websites and document their architecture
```

**Analysis:**
- Can run independently ✓
- Result not needed immediately ✓
- User can work on other things ✓
- No user input needed ✓

**Decision:** ✅ **BACKGROUND-SAFE**

### Example 3: NOT suitable — Blocking downstream

**Description:**
```
Test the harness and if it passes, deploy to production
```

**Analysis:**
- Requires decision (if passes → deploy) ❌
- Downstream action depends on result ❌
- Implicit user approval needed ❌

**Decision:** ❌ **NOT BACKGROUND-SAFE**

**Fix:** Split into two tasks:
1. (Background) Test the harness and log results
2. (Manual) User reviews results, manually deploys if approved

### Example 4: NOT suitable — User confirmation needed

**Description:**
```
Refactor the API and ask me to review before merging
```

**Analysis:**
- Requires user confirmation ❌
- Blocks merge decision ❌

**Decision:** ❌ **NOT BACKGROUND-SAFE**

**Fix:** Spawn agent to refactor and create PR; user reviews PR manually.

### Example 5: Ambiguous — Warn but proceed

**Description:**
```
Run the new harness and tell me if it works
```

**Analysis:**
- Could mean: "Run and log results" (✓ background-safe)
- Could mean: "Run and wait for me to check" (❌ interactive)
- Ambiguous language ⚠️

**Decision:** ✅ **PROCEED WITH WARNING**

**Action:** Warn user but don't block. Background agent will run harness and log results. User can check later.

## Output

```json
{
  "description": "[parsed description]",
  "is_background_safe": true | false,
  "reason": "[explanation]",
  "warnings": ["[list of warnings if any]"],
  "recommendation": "[what to do]"
}
```

## Error Handling

**If NOT background-safe:**

Suggest restructuring:
```
This task requires user confirmation: "[excerpt]"

Suggested fix:
1. Spawn agent to do [autonomously doable part]
2. User reviews results
3. User makes decision
4. Next action proceeds from there

Or: Run sequentially instead of background (don't use spawn-subagent)
```

**If ambiguous but likely safe:**

Warn but proceed:
```
⚠ Task description is ambiguous: "[excerpt]"

Interpreted as: [background-safe interpretation]
If you meant something else, the background agent will do its best.

Proceeding with background spawn.
```

## Implementation Note

This is a **soft gate** — validation doesn't block, just warns. The Agent tool itself is the hard gate (it will fail if the task can't actually run).

**Do:**
- ✓ Validate against patterns
- ✓ Warn on ambiguity
- ✓ Proceed if mostly safe
- ✓ Let Agent tool fail if truly unsuitable

**Don't:**
- ✗ Block on subjective judgment calls
- ✗ Second-guess the user
- ✗ Reject because "might" need input
- ✗ Assume task will fail
