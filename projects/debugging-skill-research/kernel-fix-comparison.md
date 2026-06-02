# /kernel/fix vs Superpowers Debugging Skill — Comparison

## Scope Comparison

| Dimension | /kernel/fix | Debugging Skill |
|-----------|------------|-----------------|
| **Target** | Kernel infrastructure (hooks, commands, state contracts) | Application code (Python, TypeScript, SQL, configs) |
| **Trigger** | Kernel component is broken or needs change | Test failure, runtime bug, unexpected behavior |
| **Process** | Impact assessment → approval → implement → learn | 4-phase RCA → hypothesis → test → implement |
| **Key concern** | "What else breaks if I change this?" | "Where did the bad data originate?" |
| **Output** | Fix + defect log + lesson + optional hook update | Fix + test + validation layers |
| **Scope guard** | Before ANY fix to hooks/commands/state | Before ANY fix to application code |

## They Do Not Overlap

`/kernel/fix` is a **change management** process — its primary value is the impact assessment (who calls this, what depends on it, what breaks, migration path). It answers: "Is it safe to change this kernel component?"

The debugging skill is a **root cause investigation** process — its primary value is the 4-phase methodology. It answers: "Why is the application code broken and where is the actual cause?"

Different questions, different workflows, different scopes.

## Where They Connect

The kernel loop already has a fix → learn cycle: test fails → `/kernel/fix` → implement → `/kernel/learn`. But `/kernel/fix` assumes you already know WHAT to fix — it gates the HOW (impact assessment before changing kernel code).

The debugging skill fills the gap BEFORE `/kernel/fix`: when a test fails and the agent doesn't yet know where the root cause is. The 4-phase process (investigate → analyze patterns → hypothesize → implement) is the missing upstream step.

## Real Debugging Scenarios

### Python pytest failures (hmsa-healthcare-qa)
- **Current behavior:** Agent sees test failure, reads traceback, attempts fix at symptom location
- **With debugging skill:** Agent would add boundary logging at each layer (config loader → validator → rule engine → reporter), trace backward to find where invalid data entered, then fix at origin
- **Value:** Prevents "fix the assertion" pattern — forces upstream tracing

### TypeScript Playwright failures (platform-playwright)
- **Current behavior:** Agent sees selector timeout, tries different selector or adds wait
- **With debugging skill:** Agent would apply condition-based waiting (no arbitrary sleeps), check component boundaries (test → page object → browser → DOM), trace which boundary failed
- **Value:** Eliminates flaky test whack-a-mole; condition-based waiting alone resolves most Playwright timing issues

### SSH compliance issues
- **Current behavior:** Agent sees compliance check fail, adjusts the check or the config
- **With debugging skill:** Agent would trace data flow through compliance layers (config JSON → Python validator → hook enforcer), identify which layer introduced the discrepancy
- **Value:** Defense-in-depth validation ensures compliance is structurally enforced at every layer, not just at the check point

## Integration Point Recommendation

**Recommended: Create `/kernel/debug` as a new command.**

Rationale:

1. **Not an extension of /kernel/fix** — `/kernel/fix` is scoped to kernel components and centers on impact assessment. Bolting application debugging onto it would overload its purpose and blur the scope boundary.

2. **Not a named agent (@debugger)** — The debugging methodology should be available as a command anyone can invoke, not locked behind agent spawning. Named agents add latency and context loss (per lessons: "NEVER SPAWN AGENTS UNLESS FOR PROD-TEST OR RUN-TASK.SH").

3. **A new command `/kernel/debug`** that:
   - Implements the 4-phase process (investigate → analyze → hypothesize → implement)
   - Adds boundary logging automatically at component interfaces
   - Enforces the "3 failed fixes → question architecture" escalation rule
   - Triggers `/kernel/learn` after resolution (same as `/kernel/fix`)
   - Is invoked when test failures need root cause investigation (before `/kernel/fix` if the fix involves kernel components)

4. **Workflow integration:**
   ```
   test fails → /kernel/debug (find root cause)
                    ↓
              root cause found
                    ↓
              Is it kernel code? → YES → /kernel/fix (impact assessment)
                    ↓ NO
              Fix application code directly
                    ↓
              /kernel/learn (record lesson)
   ```

This preserves `/kernel/fix` for what it does well (kernel change management) while adding the missing upstream investigation step.
