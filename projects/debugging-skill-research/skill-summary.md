# Superpowers Systematic Debugging Skill — Summary

**Source:** [obra/superpowers](https://github.com/obra/superpowers) — `skills/systematic-debugging/`

## Core Principle

"ALWAYS find root cause before attempting fixes. Symptom fixes are failure."

## The 4-Phase Methodology

### Phase 1: Root Cause Investigation
- Read error messages and stack traces carefully
- Reproduce issues consistently with documented steps
- Review recent changes via version control
- Add diagnostic logging at each component boundary to identify which layer fails
- Trace data flow backward from symptoms to originating source

### Phase 2: Pattern Analysis
- Locate similar working code in the codebase
- Study reference implementations completely
- List all differences between working and broken implementations
- Understand dependencies and configuration assumptions

### Phase 3: Hypothesis and Testing
- Formulate a specific hypothesis with reasoning
- Test with minimal changes (one variable at a time)
- Accept "I don't understand" rather than guessing
- Form new hypotheses if testing fails

### Phase 4: Implementation
- Create a failing test case first
- Implement a single fix addressing root cause
- Verify fix resolves the issue without breaking other tests
- **Escalation rule:** After 3 failed fixes, stop and question the architecture

## Component Boundary Logging

Multi-component diagnostics through systematic instrumentation at component boundaries. The technique:

1. **Identify boundaries** — Every point where data crosses between components (API calls, function interfaces, service layers, file I/O)
2. **Add diagnostic logging at each boundary** — Log data entering, data exiting, and environment state at each layer
3. **Trace failure location** — When a bug surfaces, the boundary logs reveal exactly which layer introduced the problem
4. **Use `console.error()` in tests** (not logger — may not show) for visibility during test execution
5. **Capture context before dangerous operations** — directories, environment variables, stack traces via `new Error().stack`

This is the practical application of the "trace backward from symptom" principle — boundary logs eliminate guesswork about where data goes wrong.

## Root Cause Analysis (RCA) Application

RCA in this skill follows a 5-step backward trace:

1. **Observe the symptom** — Document where the error manifests
2. **Find immediate cause** — Identify the code directly producing the error
3. **Trace upward** — What called the problematic function?
4. **Continue backward** — Keep asking what preceded each layer
5. **Locate original trigger** — Find where invalid data originated

Key distinction: RCA here means "don't fix where the error appears — fix where the bad data was created." The root cause is always upstream from the symptom.

## Supporting Techniques

### Defense-in-Depth Validation
Validate at EVERY layer data passes through. Four layers:

| Layer | Purpose |
|-------|---------|
| Entry Point | Catches invalid input at API boundaries |
| Business Logic | Ensures data is contextually appropriate |
| Environment Guards | Prevents dangerous operations in wrong context |
| Debug Instrumentation | Captures diagnostics when other layers fail |

Goal: Make the bug structurally impossible, not just caught once.

### Condition-Based Waiting
Replaces arbitrary timing delays (`sleep`, `setTimeout`) with polling for actual conditions:
- Poll every 10ms with configurable timeout (default 5s)
- Throw descriptive error if condition never met
- Resolves test flakiness (60% → 100% pass rate, 40% faster execution)

## Red Flags Requiring Process Reset
- Proposing solutions without investigation
- Attempting multiple simultaneous fixes
- Skipping tests
- Continuing after multiple failed attempts

## Claimed Time Savings
- Systematic debugging: **15-30 minutes**
- Random fix attempts: **2-3 hours**
- First-time fix rate: **95%** (systematic) vs **40%** (guessing)
