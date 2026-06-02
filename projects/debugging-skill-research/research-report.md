# Systematic Debugging Skill — Research Report

**Date:** 2026-06-01
**Source:** [obra/superpowers](https://github.com/obra/superpowers) — `skills/systematic-debugging/`
**Recommendation:** ADOPT — as `/kernel/debug` command

---

## 1. Skill Methodology

The Superpowers systematic debugging skill is a 4-phase root cause investigation process:

| Phase | Name | What It Does |
|-------|------|-------------|
| 1 | Root Cause Investigation | Read errors, reproduce, add boundary logging, trace backward from symptom |
| 2 | Pattern Analysis | Find working code, compare to broken code, list differences |
| 3 | Hypothesis & Testing | Formulate specific hypothesis, test one variable at a time, accept uncertainty |
| 4 | Implementation | Write failing test first, implement single fix, verify no regressions |

**Core principle:** "ALWAYS find root cause before attempting fixes. Symptom fixes are failure."

**Escalation rule:** After 3 failed fixes, stop and question the architecture.

**Supporting techniques:**
- **Component boundary logging** — Instrument every boundary where data crosses components; logs reveal which layer introduced the problem
- **Defense-in-depth validation** — Validate at every layer (entry, business logic, environment, instrumentation) to make bugs structurally impossible
- **Condition-based waiting** — Replace arbitrary sleeps with polling for actual conditions; eliminates test flakiness

**Claimed results:** 15-30 min systematic vs 2-3 hours guessing; 95% first-time fix rate vs 40%.

## 2. Scope Comparison: /kernel/fix vs Debugging Skill

| Aspect | /kernel/fix | Debugging Skill |
|--------|------------|-----------------|
| Scope | Kernel infrastructure only | Application code (any language) |
| Purpose | Change management — "is it safe to modify?" | Root cause investigation — "why is it broken?" |
| Process | Impact assessment → approval → implement → learn | 4-phase RCA → hypothesis → test → implement |
| Assumption | You already know WHAT to fix | You don't yet know WHERE the root cause is |

**Key finding:** They do not overlap. `/kernel/fix` gates kernel changes with impact assessment. The debugging skill investigates application failures to find root causes. They address different stages of the fix workflow — the debugging skill is upstream of `/kernel/fix`.

## 3. Scenario Analysis

### Python pytest failures (hmsa-healthcare-qa)
- **Without skill:** Agent reads traceback, fixes at symptom location (assertion, return value)
- **With skill:** Agent traces through component boundaries (config → validator → rule engine → reporter), finds where invalid data originated
- **Impact:** Prevents "fix the assertion" pattern; produces durable fixes at the source

### TypeScript Playwright failures (platform-playwright)
- **Without skill:** Agent adjusts selectors, adds arbitrary waits
- **With skill:** Agent applies condition-based waiting (eliminates timing issues), traces component boundaries (test → page object → browser → DOM)
- **Impact:** Condition-based waiting alone resolves most Playwright flakiness; boundary tracing finds real cause instead of selector whack-a-mole

### SSH compliance platform
- **Without skill:** Agent adjusts the failing compliance check or config value
- **With skill:** Agent traces data flow through compliance layers (config JSON → Python validator → hook enforcer), identifies which layer has the discrepancy
- **Impact:** Defense-in-depth ensures compliance is structurally enforced at every layer, not single-point checked

**Verdict:** The skill would meaningfully change debugging behavior in all three scenarios. The strongest value is in Playwright (condition-based waiting) and compliance (defense-in-depth).

## 4. Integration Point Recommendation

**Recommended: Create `/kernel/debug` as a new kernel command.**

### Why not extend /kernel/fix?
`/kernel/fix` is scoped to kernel components. Its value is the impact assessment (callers, dependencies, breakage, migration). Adding application debugging would overload its purpose and blur the kernel/application boundary.

### Why not a named agent (@debugger)?
Per lessons: "NEVER SPAWN AGENTS UNLESS FOR PROD-TEST OR RUN-TASK.SH." A named agent adds latency, loses context, and locks the methodology behind agent spawning. A command is directly invocable.

### Why /kernel/debug?
- Directly invocable from the kernel loop
- Fits the existing pattern: `/kernel/fix` for kernel changes, `/kernel/debug` for application investigation
- Triggers `/kernel/learn` after resolution (same post-fix cycle)
- Can be mechanically enforced: hook detects test failure → suggests `/kernel/debug`

## 5. Design Sketch: /kernel/debug

```
Usage: /kernel/debug [description of the failure]

Step 1: Understand the Failure
  - Read error output, stack traces, test results
  - Reproduce consistently

Step 2: Boundary Analysis
  - Identify component boundaries in the failing code path
  - Add diagnostic logging at each boundary
  - Run again to capture boundary data

Step 3: Root Cause Trace
  - Trace backward from symptom through boundary logs
  - Identify where invalid data originated
  - Find the root cause (not the symptom)

Step 4: Pattern Analysis
  - Find similar working code in the codebase
  - List differences between working and broken
  - Form specific hypothesis

Step 5: Hypothesis Test
  - Test with minimal change (one variable)
  - If fails: form new hypothesis (max 3 attempts)
  - If 3 failures: escalate — question the architecture

Step 6: Implement Fix
  - Write failing test first
  - Implement single fix at root cause
  - Verify no regressions
  - If fix touches kernel code → invoke /kernel/fix for impact assessment

Step 7: /kernel/learn
  - Record what the root cause was
  - Record how boundary logging revealed it
  - Add defense-in-depth validation if applicable
```

**Workflow integration:**
```
test fails → /kernel/debug (find root cause)
                  ↓
            root cause found
                  ↓
            kernel code? → YES → /kernel/fix (impact assessment)
                  ↓ NO
            fix application code
                  ↓
            /kernel/learn
```

**Hook integration:**
- `test-failure-detector.py` already sets `needs_learn: true` on test failure
- Extend to suggest `/kernel/debug` in the block message when root cause is unknown
- The 3-attempt escalation rule maps to `attempts_on_current` (already in workflow state)

## 6. Overall Recommendation

**ADOPT.**

The systematic debugging skill fills a genuine gap in the kernel loop. Currently, when a test fails, the agent jumps straight to fixing (often at the symptom location). The 4-phase methodology forces upstream investigation before any fix attempt. The supporting techniques (boundary logging, defense-in-depth, condition-based waiting) are immediately applicable to existing platform work.

The integration as `/kernel/debug` preserves the existing `/kernel/fix` scope while adding the missing investigation step. The hook infrastructure already supports it (test-failure-detector exists, `attempts_on_current` tracks retries).

**Next step:** Create backlog item for `/kernel/debug` command implementation.
