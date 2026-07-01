# Kernel Regression Testing — Research Report

**Backlog:** 168-kernel-research-regression-testing
**Date:** 2026-06-28
**Status:** Complete

## Executive Summary

The kernel modifies hooks and protocol via `/kernel/learn` but never verifies the change didn't break something. The eval platform (platform-deepeval, 15/16 tests) exists but isn't wired into the learn/anchor cycle. The recommended approach: run structural tests (4 tests, ~5 seconds, zero cost) as a post-learn gate, run full eval suite (16 tests, ~60 seconds, ~$0.10) as a periodic check every 5 pipelines, and distinguish pre-existing failures from change-caused failures using a baseline snapshot.

## Part 1: Current State

### What Ships Without Regression Testing

| Kernel Event | What Changes | Currently Verified? |
|-------------|-------------|-------------------|
| `/kernel/learn` after test failure | Hook logic, lesson entry | No |
| `/kernel/learn` after anchor violation | Protocol, lesson entry | No |
| Manual protocol edit | Protocol file | No |
| CLAUDE.md update | System configuration | No |

### The Eval Platform

| Component | Count | API Cost | Runtime |
|-----------|-------|----------|---------|
| Structural tests | 4 | $0.00 | ~5 seconds |
| GEval tests | 12 | ~$0.10 | ~60 seconds |
| Total | 16 | ~$0.10 | ~65 seconds |

Current invocation:
```bash
python -m pytest "D:/my_ai_projects/project_test_repos/platform-deepeval/tests/" \
  --harness-root "D:/my_ai_projects/isagawa-kernel" \
  --rootdir "D:/my_ai_projects/project_test_repos/platform-deepeval"
```

### The Gap

Changes ship → eval runs later (manually) → if it fails, nobody connects the failure to the change. The eval platform exists but operates independently of the kernel loop.

## Part 2: Integration Point Analysis

### Option A: Inside `/kernel/learn` (Recommended for Structural)

```
/kernel/learn
  1. Record lesson
  2. Modify hook/protocol (if needed)
  3. Run structural regression tests ← NEW
  4. If regression detected → block + warn
  5. Complete
```

**Pros:** Immediate feedback, catches structural breaks before they propagate
**Cons:** Adds ~5 seconds to every learn event
**Verdict:** Use for structural tests only (zero cost, fast)

### Option B: Post-Learn Hook (Not Recommended)

A PostToolUse hook that triggers after `/kernel/learn` completes.

**Pros:** Decoupled from learn logic
**Cons:** Hook architecture doesn't support "run tests after a specific skill completes" — hooks fire on tool use (Bash, Write, Edit), not on skill completion
**Verdict:** Not feasible with current hook architecture

### Option C: Separate Command — `/kernel/eval` (Recommended for Full Suite)

Already exists as a command. Run it:
- After every 5th pipeline (count from metrics.jsonl)
- On demand
- Before major releases/pushes

**Pros:** Full suite with GEval, periodic not per-event, controllable cost
**Cons:** Delayed feedback (regression may ship before detection)
**Verdict:** Use for full suite (GEval + structural)

### Option D: CI/CD Gate (Future)

Run eval suite in GitHub Actions on every push:
```yaml
- name: Regression Test
  run: |
    pip install deepeval
    pytest tests/ --harness-root . -k structural
```

**Pros:** Catches regressions before merge, industry standard
**Cons:** Requires CI/CD infrastructure (not yet set up for kernel)
**Verdict:** Future phase — after metrics (164) and experiments (165) are in place

## Part 3: Smoke Test Subset

### Which Tests Constitute the Regression Gate?

Not all 16 tests are equally valuable for regression detection:

**Smoke tier (run after every learn event):**

| Test | What It Catches | Cost |
|------|----------------|------|
| `test_commands_exist` | Missing/deleted command files | $0.00 |
| `test_claudemd_references` | Broken references in CLAUDE.md | $0.00 |
| `test_hook_files_exist` | Missing hook files | $0.00 |
| `test_lessons_exist` | Lessons file deleted/empty | $0.00 |

Runtime: ~5 seconds. These are the "always on" safety net.

**Full tier (run periodically):**

| Test | What It Catches | Cost |
|------|----------------|------|
| All smoke tests | (as above) | $0.00 |
| `test_command_quality` (6 tests) | Command clarity degradation | ~$0.06 |
| `test_protocol_quality` | Protocol quality decline | ~$0.01 |
| `test_hook_coverage` | Hook enforcement gaps | ~$0.01 |
| `test_lessons_actionability` | Lesson quality decline | ~$0.01 |
| `test_claudemd_completeness` | CLAUDE.md completeness decline | ~$0.01 |

Runtime: ~60 seconds. Total cost: ~$0.10.

### Tiered Strategy

```
After /kernel/learn   → Smoke tests (structural, 4 tests, ~5s, $0)
After 5th pipeline    → Full suite (16 tests, ~60s, ~$0.10)
Before git push       → Full suite
On demand (/kernel/eval) → Full suite
```

## Part 4: Pre-Existing vs Change-Caused Failures

### The Problem

If `test_hook_coverage` was already failing before a learn event, and it's still failing after, the learn event didn't cause the regression. Blaming the change is wrong. But if it was passing before and fails after, the change caused it.

### Solution: Baseline Snapshot

Before each learn event, record the current test state:

```json
{
  "baseline_timestamp": "2026-06-28T19:30:00Z",
  "event": "pre_learn_baseline",
  "tests": {
    "test_commands_exist": "PASS",
    "test_claudemd_references": "PASS",
    "test_hook_files_exist": "PASS",
    "test_lessons_exist": "PASS"
  }
}
```

After learn completes, run the same tests:

```json
{
  "post_timestamp": "2026-06-28T19:31:00Z",
  "event": "post_learn_regression",
  "tests": {
    "test_commands_exist": "PASS",
    "test_claudemd_references": "FAIL",  // ← REGRESSION
    "test_hook_files_exist": "PASS",
    "test_lessons_exist": "PASS"
  },
  "regressions": ["test_claudemd_references"],
  "pre_existing_failures": [],
  "new_passes": []
}
```

### Classification Logic

```python
def classify_results(baseline, current):
    regressions = []      # Was PASS, now FAIL → change caused it
    pre_existing = []     # Was FAIL, still FAIL → not change-related
    improvements = []     # Was FAIL, now PASS → change fixed it

    for test_name in baseline:
        before = baseline[test_name]
        after = current[test_name]
        if before == "PASS" and after == "FAIL":
            regressions.append(test_name)
        elif before == "FAIL" and after == "FAIL":
            pre_existing.append(test_name)
        elif before == "FAIL" and after == "PASS":
            improvements.append(test_name)

    return regressions, pre_existing, improvements
```

### Failure Path

| Classification | Action |
|---------------|--------|
| Regression (was PASS, now FAIL) | **Block** — learn event caused breakage. Fix before continuing. |
| Pre-existing (was FAIL, still FAIL) | **Warn** — log but don't block. The learn event didn't make it worse. |
| Improvement (was FAIL, now PASS) | **Celebrate** — the learn event fixed something. |

## Part 5: Performance Analysis

### Can Regression Tests Run on Every Learn Event?

| Test Type | Runtime | Cost | Every Learn? |
|-----------|---------|------|-------------|
| Structural (4) | ~5s | $0 | Yes |
| GEval (12) | ~60s | ~$0.10 | No (periodic) |

**Learn event frequency:** ~2-3 per session, ~1-2 sessions per day = 2-6 learn events per day.

**Structural tests on every learn:** 2-6 × 5s = 10-30 seconds/day. Negligible.

**GEval on every learn:** 2-6 × $0.10 = $0.20-$0.60/day. Acceptable but unnecessary — GEval tests measure quality trends that change slowly.

**Recommendation:** Structural on every learn. GEval every 5th pipeline (~every other day at current pace).

## Part 6: Integration Architecture

### Data Flow

```
/kernel/learn invoked
       ↓
[1] Record baseline (current structural test results)
       ↓
[2] Execute learn (record lesson, modify files)
       ↓
[3] Run structural regression tests
       ↓
[4] Compare to baseline
       ↓
[5a] No regressions → continue normally
[5b] Regression found → BLOCK
       ↓
     Report which tests regressed
     Agent must fix before proceeding
     Record regression in learn-events.jsonl
       ↓
     Fix applied → re-run tests → if pass, continue
```

### Integration with Other Backlogs

| Backlog | Integration Point |
|---------|------------------|
| 164 (Metrics) | Regression test results feed into metrics.jsonl |
| 165 (Experiments) | Experiment evaluation uses regression test trends |
| 166 (Auto-Eval) | Post-learn structural tests ARE the auto-eval trigger |
| 167 (Rollback) | Regression detection triggers rollback candidate signal |

### Implementation in `/kernel/learn`

Add to learn command, after lesson recording:

```markdown
## Post-Learn Regression Check

After recording the lesson and modifying files:

1. Run structural tests:
   ```bash
   python -m pytest "[platform-deepeval]/tests/" \
     --harness-root "[harness-root]" \
     --rootdir "[platform-deepeval]" \
     -k "structural" --tb=short -q
   ```

2. If any test fails that was passing before:
   - Report the regression
   - Set `needs_fix: true` in session state
   - The agent must fix before continuing

3. If all tests pass (or only pre-existing failures):
   - Continue normally
   - Log results to eval-results.jsonl
```

## Part 7: Implementation Plan

| Phase | Work | Dependency |
|-------|------|-----------|
| 1 | Add baseline snapshot before learn | None |
| 2 | Add structural regression check after learn | Phase 1 |
| 3 | Add regression classification (pre-existing vs change-caused) | Phase 2 |
| 4 | Add results logging to eval-results.jsonl | Phase 3 |
| 5 | Wire periodic full suite trigger (every 5th pipeline) | Phase 4 + metrics (164) |
| 6 | Connect regression signals to rollback candidates | Phase 4 + rollback (167) |
| 7 | Add CI/CD regression gate (GitHub Actions) | Phase 5 |

### Quick Win: Phase 1-2

Phases 1-2 can ship independently with zero dependencies:
- Before learn: run 4 structural tests, record results
- After learn: run same tests, compare
- If regression: block and report

Total overhead: ~10 seconds per learn event. Zero API cost.

## Conclusion

Regression testing for the kernel is straightforward because the eval platform already exists. The missing piece is wiring: run structural tests (4 tests, ~5 seconds, $0) after every learn event with baseline comparison. This catches the most common regression type (broken file references, missing commands) immediately. Full GEval suite runs periodically for quality trend detection. Pre-existing failure classification prevents false blame. The infrastructure connects to all four other self-improvement capabilities (metrics, experiments, auto-eval, rollback) as a shared signal source.

## Sources

- [Complete Guide to LLM & AI Agent Evaluation 2026 (Adaline)](https://www.adaline.ai/blog/complete-guide-llm-ai-agent-evaluation-2026)
- [Regression Testing in CI/CD (Harness)](https://www.harness.io/blog/regression-testing-in-ci-cd-deliver-faster-without-the-fear)
- [LLM Regression Testing (FutureAGI)](https://futureagi.com/glossary/llm-regression-testing/)
- [Building a Regression Test Suite for AI Agents with AgentProctor](https://medium.com/@diegomou92/building-a-regression-test-suite-for-ai-agents-with-agentproctor-and-pytest-1d48bdd23b7a)
- [AI Agent Evaluation Pipeline 2026 Methodology](https://www.digitalapplied.com/blog/ai-agent-evaluation-pipeline-2026-testing-methodology)
- [CI/CD Tools for Testing AI Agents 2026 (Confident AI)](https://www.confident-ai.com/knowledge-base/compare/best-ci-cd-tools-testing-ai-agents-before-production-2026)
