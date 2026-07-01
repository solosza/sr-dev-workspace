# Iteration Tracking: Score Progression Across Passes

## Status
NEW

## Purpose

Track DeepEval scores across iteration passes so progression is visible. Each pass through the backlog → task-builder → cycle → prod-test loop produces scores. Tracking enables: "Pass 1: 0.62 TaskCompletion → Pass 3: 0.91" reporting.

## Score Record Schema

Each prod-test L3 run produces a score record:

```json
{
  "pass_number": 1,
  "timestamp": "2026-06-24T08:00:00Z",
  "command": "check-data",
  "contract_id": "step-03-dates-contract",
  "metrics": {
    "ToolCorrectness": { "score": 0.72, "threshold": 0.7, "pass": true },
    "TaskCompletion": { "score": 0.55, "threshold": 0.7, "pass": false },
    "GEval_SV301": { "score": 0.80, "threshold": 0.8, "pass": true },
    "GEval_SV305": { "score": 0.40, "threshold": 0.8, "pass": false }
  },
  "overall_pass": false,
  "failing_metrics": ["TaskCompletion", "GEval_SV305"],
  "gaps_identified": [
    "Agent did not check clean break rule (SV-305) — metric score 0.40",
    "Agent skipped Step 5 (check constraints) — TaskCompletion 0.55"
  ]
}
```

## Score History File

Location: `eval/results/score-history.json`

```json
{
  "command": "check-data",
  "passes": [
    { "pass_number": 1, "timestamp": "...", "scores": { ... }, "overall_pass": false },
    { "pass_number": 2, "timestamp": "...", "scores": { ... }, "overall_pass": false },
    { "pass_number": 3, "timestamp": "...", "scores": { ... }, "overall_pass": true }
  ],
  "progression": {
    "TaskCompletion": [0.55, 0.78, 0.91],
    "ToolCorrectness": [0.72, 0.85, 0.93],
    "GEval_SV301": [0.80, 0.85, 0.95],
    "GEval_SV305": [0.40, 0.70, 0.88]
  },
  "production_ready": true,
  "production_ready_at_pass": 3
}
```

## Progression Reporting

After each pass, the validation report includes:

```
DEEPEVAL L3 SCORES — check-data (Pass 3)

  Metric              Pass 1  Pass 2  Pass 3  Status
  ToolCorrectness     0.72    0.85    0.93    PASS ✓
  TaskCompletion      0.55    0.78    0.91    PASS ✓
  GEval: SV-301       0.80    0.85    0.95    PASS ✓
  GEval: SV-305       0.40    0.70    0.88    PASS ✓

  Overall: PASS (all metrics >= threshold)
  Production ready at pass 3.
```

## Regression Detection

If any metric score drops between passes, flag it:

```
REGRESSION DETECTED — check-data (Pass 4)

  ToolCorrectness: 0.93 → 0.65 (REGRESSION -0.28)
  Possible cause: Recent edit to step-03-assign-dates.md changed tool usage pattern
```

Regression triggers:
- Score drops > 0.1 from previous pass
- A previously-passing metric fails
- Overall pass reverts to fail

## Integration with /kernel/learn

When L3 scores identify gaps:
1. Gaps feed into `/kernel/learn` as structured findings
2. Learn updates the skill/protocol to address the gap
3. Next cycle's prod-test L3 re-evaluates
4. Score should improve — if not, the fix was insufficient

## Dependencies

- Score history file must persist across prod-test runs (not inside test repo — it gets recreated)
- Location: source repo's `eval/results/` or a dedicated tracking location
- Regression detection runs automatically after each L3 pass
