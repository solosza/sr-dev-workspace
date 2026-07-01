# Kernel Automatic Evaluation — Research Report

**Backlog:** 166-kernel-research-automatic-evaluation
**Date:** 2026-06-28
**Status:** Complete

## Executive Summary

The kernel has an eval platform (platform-deepeval, 15/16 tests passing) that measures harness quality, but it runs manually. Closing the loop means: eval triggers automatically → results are interpreted programmatically → failures feed back into `/kernel/learn`. The recommended approach is a tiered auto-eval system: structural tests run after every learn event (zero cost), GEval tests run after every 5th pipeline (LLM cost), and full regression runs on demand. Safety boundaries follow the industry standard: low-risk changes auto-apply, medium-risk generate notifications, high-risk require human approval.

## Part 1: Current State

### What Exists

| Component | Status | Location |
|-----------|--------|----------|
| platform-deepeval | 15/16 tests passing | `D:/my_ai_projects/project_test_repos/platform-deepeval/` |
| Structural tests (4) | No API key needed | `test_eval_kernel_minimal.py` — file existence, CLAUDE.md references |
| GEval tests (12) | Requires OPENAI_API_KEY | `test_eval_kernel_minimal.py` — LLM-as-judge quality assessment |
| `--harness-root` flag | Cross-harness testing | `conftest.py` — parameterizes target harness path |
| Validation report | JSON output | `tests/validation-report.json` |

### The Gap

```
Current: Manual run → human reads results → manual protocol change
Needed:  Auto-trigger → programmatic interpretation → auto-learn or human review
```

The eval platform evaluates harness quality. It does NOT evaluate pipeline outcomes. These are complementary:
- **Harness quality** = "Is the kernel well-constructed?" (platform-deepeval)
- **Pipeline outcomes** = "Is the kernel producing good results?" (metrics.jsonl from backlog 164)

Both need to feed into the closed loop.

## Part 2: Trigger Design

### When to Run Evals

| Trigger | What Runs | Cost | Latency |
|---------|----------|------|---------|
| After `/kernel/learn` (every time) | Structural tests only (4 tests) | Zero | ~5 seconds |
| After every 5th pipeline | Full eval suite (16 tests) | ~$0.10 (OpenAI) | ~60 seconds |
| On demand (`/kernel/eval`) | Full eval suite | ~$0.10 | ~60 seconds |
| After experiment window closes | Experiment evaluator | Zero | ~2 seconds |

### Why Not Full Suite on Every Learn?

- GEval tests cost ~$0.10 per run (12 OpenAI API calls)
- At 2-3 learn events per session, 2-3 sessions per day = $0.60-$0.90/day
- Not prohibitive, but unnecessary — structural tests catch the most common failures (missing files, broken references)
- GEval tests catch quality degradation, which changes slowly over multiple learn events

### Trigger Implementation

```python
# In /kernel/learn, after recording the lesson:
def post_learn_eval():
    # Always run structural tests (zero cost, fast)
    result = run_structural_tests(harness_root)
    if result.failures > 0:
        signal_regression(result)

    # Check pipeline count for full eval
    pipeline_count = count_pipelines_since_last_full_eval()
    if pipeline_count >= 5:
        result = run_full_eval(harness_root)
        record_eval_result(result)
```

## Part 3: Programmatic Result Interpretation

### Structural Test Results

Pass/fail binary. Any structural failure = regression. These test:
- Command files exist (anchor.md, session-start.md, etc.)
- CLAUDE.md references valid files
- Hook files exist and are referenced in settings
- Lesson file exists and is non-empty

### GEval Test Results

Score 0.0-1.0 per test, threshold 0.80. Interpretation:

| Score Range | Interpretation | Action |
|------------|---------------|--------|
| ≥ 0.80 | Pass | None |
| 0.70-0.79 | Borderline | Log warning, don't auto-act |
| < 0.70 | Fail | Signal regression |

### Trend Detection

Compare current eval scores to running average of last 5 evals:

```python
def detect_trend(current_scores, historical_scores):
    avg = mean(historical_scores[-5:])
    delta = mean(current_scores) - avg
    if delta < -0.10:  # 10% decline
        return "DEGRADING"
    elif delta > 0.05:  # 5% improvement
        return "IMPROVING"
    return "STABLE"
```

## Part 4: Feedback Loop — Eval → Learn

### Closed Loop Architecture

```
/kernel/learn → modifies hook/protocol
       ↓
post_learn_eval() → runs structural tests
       ↓
result → PASS: continue
       → FAIL: signal regression
              ↓
       auto-create backlog item: "Fix regression in [test_name]"
              ↓
       OR: invoke /kernel/learn with regression context
              ↓
       record lesson: "Change X broke test Y"
```

### Feedback Categories

| Eval Output | Feedback Action | Automation Level |
|-------------|----------------|-----------------|
| Structural test failure | Auto-create backlog | Fully automatic |
| GEval score decline (>10%) | Generate warning + backlog | Semi-automatic (human reviews backlog) |
| GEval score decline (>20%) | Block pipeline, require review | Human-gated |
| Recurring lesson detected | Generate experiment proposal | Semi-automatic |
| Experiment verdict: DEGRADED | Trigger rollback signal | Semi-automatic (backlog 167) |

## Part 5: Safety Boundaries

### Risk Tiers (Industry Standard)

Following the Galileo/W&B/OpenAI guardrails framework:

| Risk Level | Kernel Equivalent | Auto-Apply? |
|-----------|-------------------|-------------|
| **Low** | Add lesson entry, update lesson index | Yes — append-only, no code change |
| **Medium** | Modify hook logic, add new gate | Notify — create backlog, human approves |
| **High** | Modify protocol, change CLAUDE.md, remove hook | Block — require explicit human approval |

### What SHOULD Auto-Apply

- Lesson recording (append-only, always safe)
- Structural test execution (read-only evaluation)
- Metric emission (append to metrics.jsonl)
- Experiment status updates (data recording)

### What SHOULD NOT Auto-Apply

- Hook modifications (could break enforcement)
- Protocol changes (could alter agent behavior unpredictably)
- CLAUDE.md changes (system-level configuration)
- Rollback of prior changes (could cascade — see backlog 167)

### Infrastructure-Level vs Prompt-Level Guardrails

The kernel already has this right: hooks are infrastructure-level controls (Python scripts in PreToolUse/PostToolUse), not prompt-level instructions. Per the research: "If boundaries only exist as instructions in an AI system prompt, a crafted input can override them, while infrastructure-level controls can't be prompted away."

Auto-eval should follow the same pattern: safety boundaries enforced in the evaluator script, not in the agent's prompt.

## Part 6: Pattern Detection — Recurring Lessons

### The Problem

Lessons.md shows recurring violations. Example: "NEVER USE cd" has been violated 4+ times despite being in RULE ZERO. The current system records the lesson each time but doesn't detect the pattern.

### Detection Logic

```python
def detect_recurring_lessons(lessons_file, window=30):
    lessons = parse_lessons(lessons_file)
    # Group by topic/rule
    by_topic = group_by(lessons, key="topic")
    recurring = {t: entries for t, entries in by_topic.items()
                 if len(entries) >= 3}
    return recurring
    # → {"cd_usage": [entry1, entry2, entry3, entry4]}
```

### Response to Recurring Patterns

If a lesson has been recorded 3+ times:
1. Generate an experiment proposal: "The lesson '{topic}' isn't working. Hypothesis: need mechanical enforcement (hook), not just a written rule."
2. Create a backlog item for the mechanical fix
3. This is the transition from Level 4 (self-modifying) to Level 5 (self-improving): the system detects that its own fixes aren't working and proposes structural changes.

## Part 7: Integration with Existing Platform

### platform-deepeval Integration

The eval platform already supports `--harness-root` for cross-harness testing. Auto-eval invocation:

```bash
# From sr_dev_workspace (or any harness):
python -m pytest "D:/my_ai_projects/project_test_repos/platform-deepeval/tests/" \
  --harness-root "D:/my_ai_projects/isagawa-kernel" \
  --rootdir "D:/my_ai_projects/project_test_repos/platform-deepeval" \
  -k "structural"  # or remove -k for full suite
```

### Eval Results Storage

Append to `.claude/state/eval-results.jsonl`:

```json
{
  "timestamp": "2026-06-28T19:30:00Z",
  "trigger": "post_learn",
  "harness": "isagawa-kernel",
  "tests_total": 16,
  "tests_passed": 15,
  "tests_failed": 1,
  "tests_skipped": 0,
  "structural_passed": 4,
  "geval_passed": 11,
  "geval_failed": 1,
  "avg_geval_score": 0.87,
  "failed_tests": ["test_hook_coverage"],
  "trend": "STABLE"
}
```

## Part 8: Implementation Plan

| Phase | Work | Dependency |
|-------|------|-----------|
| 1 | Add structural test runner to `/kernel/learn` | None |
| 2 | Create `eval-results.jsonl` and recording | Phase 1 |
| 3 | Add trend detection (compare to last 5 evals) | Phase 2 |
| 4 | Add recurring lesson detection | None |
| 5 | Wire GEval to periodic trigger (every 5th pipeline) | Phase 2 + OPENAI_API_KEY |
| 6 | Connect to experiment tracking (backlog 165) | Phase 3 + backlog 165 |
| 7 | Connect to rollback mechanism (backlog 167) | Phase 3 + backlog 167 |

## Conclusion

The kernel has the eval platform — it just needs the wiring. Structural tests (zero cost) can run after every learn event. GEval tests (~$0.10) run periodically. Results feed back through backlog creation (auto) and learn invocation (semi-auto). Safety boundaries follow industry standard: low-risk auto-applies, high-risk requires human approval. The infrastructure-level enforcement pattern the kernel already uses for hooks is the right model for eval guardrails.

## Sources

- [Self-Improving AI Agents: The 2026 Guide](https://o-mega.ai/articles/self-improving-ai-agents-the-2026-guide)
- [AI Agent Self-Correction Feedback Loops](https://www.claudio-novaglio.com/en/blog/ai-automation/ai-agent-self-correction-feedback-loop)
- [The Kitchen Loop: User-Spec-Driven Development](https://arxiv.org/pdf/2603.25697)
- [Galileo AI Agent Guardrails Framework](https://galileo.ai/blog/ai-agent-guardrails-framework)
- [W&B Guardrails for AI Agents](https://wandb.ai/site/articles/guardrails-for-ai-agents/)
- [Agentic AI Guardrails for Safe Scaling](https://aembit.io/blog/agentic-ai-guardrails-for-safe-scaling/)
