# Report Format — Step 6 Reference

Defines the scored report output format for `/kernel/eval`.

---

## Report Header

```
EVAL COMPLETE: [target]                     # artifact mode
EVAL COMPLETE: [repo-name] (harness)        # harness mode
Source: [original_source]                    # harness mode only
```

Where `[target]` is the artifact name (artifact mode) or repo directory name (harness mode). `[original_source]` shows the original URL or path.

---

## Score Table

```
  Metric              Score   Threshold  Status
  ToolCorrectness     0.85    0.70       PASS
  TaskCompletion      0.78    0.70       PASS
  GEval: SV-301       0.92    0.80       PASS
  GEval: SV-305       0.65    0.80       FAIL
```

Columns:
| Column | Description |
|--------|-------------|
| Metric | DeepEval metric name (ToolCorrectness, Faithfulness, GEval: [rule]) |
| Score | Float 0.0–1.0 |
| Threshold | Minimum passing score from metric config |
| Status | `PASS` if Score >= Threshold, `FAIL` otherwise |

---

## Summary Line

```
  Overall: PASS (all metrics above threshold)
  Overall: FAIL (N metric(s) below threshold)
```

---

## Gaps Section

Listed only when Overall = FAIL:

```
  Gaps:
    - SV-305 (clean break rule) — agent did not verify adjacent ranges
    - TaskCompletion — agent skipped final verification step
```

Each gap includes:
- Metric or rule identifier
- Short description of the failure
- Triage recommendation (what the artifact should do differently)

---

## New Components Section

```
  New components created: N (component_name.py, ...)
  New components created: 0
```

Lists components created during Step 4 (Dynamic Component Check) that did not exist in `_reference/` prior to this run. Count of 0 means all components already existed.

---

## Score History Entry Format

Each eval run appends an entry to `eval/results/score-history.json` in the source repo:

```json
{
  "timestamp": "2026-06-24T20:00:00Z",
  "target": "check-data",
  "metrics": [
    {
      "name": "ToolCorrectness",
      "score": 0.85,
      "threshold": 0.70,
      "status": "PASS"
    },
    {
      "name": "GEval: SV-305",
      "score": 0.65,
      "threshold": 0.80,
      "status": "FAIL"
    }
  ],
  "overall_status": "FAIL",
  "new_components_count": 1
}
```

The file is a JSON array. Each run appends one entry. History enables regression detection across runs.

---

## Regression Warning

When a metric's score drops > 0.1 compared to the previous run of the same target:

```
  REGRESSION WARNING:
    ToolCorrectness: 0.85 → 0.72 (previous: 0.85, current: 0.72, delta: -0.13)
```

Regression warnings appear after the Gaps section. Multiple regressions produce multiple lines. A regression does not change the PASS/FAIL status — it is an advisory signal.

Detection logic:
1. Load `score-history.json`
2. Find the most recent prior entry with matching `target`
3. Compare each metric by name
4. If `previous_score - current_score > 0.1`, emit warning

---

## Complete Examples

### Artifact Mode Example

Based on `check-data` eval against `hmsa-healthcare-qa`:

```
EVAL COMPLETE: check-data

  Metric              Score   Threshold  Status
  ToolCorrectness     0.85    0.70       PASS
  TaskCompletion      0.78    0.70       PASS
  GEval: SV-301       0.92    0.80       PASS
  GEval: SV-305       0.65    0.80       FAIL

  Overall: FAIL (1 metric below threshold)

  Gaps:
    - SV-305 (clean break rule) — agent did not verify adjacent ranges

  New components created: 1 (agent_kernel_metrics.py)
  Score history: eval/results/score-history.json
```

### Harness Mode Example

Based on eval of `kernel-minimal` harness:

```
EVAL COMPLETE: kernel-minimal (harness)
Source: D:\my_ai_projects\project_test_repos\kernel-minimal

  Dimension                    Score   Threshold  Status
  CLAUDE.md Coherence          0.88    0.80       PASS
  Loop Integrity               0.92    0.80       PASS
  Hook Coverage                0.85    0.80       PASS
  Command: session-start       0.78    0.70       PASS
  Command: anchor              0.82    0.70       PASS
  Command: learn               0.75    0.70       PASS
  Command: complete            0.74    0.70       PASS
  Command: fix                 0.71    0.70       PASS
  Command: domain-setup        0.80    0.70       PASS
  Skill: kernel-domain-setup   0.70    0.70       PASS
  Skill: autonomous-cycling    0.72    0.70       PASS
  Manifest Integrity           1.00    1.00       PASS
  Settings Wiring              1.00    1.00       PASS
  Reference Resolution         0.95    1.00       FAIL

  Overall: FAIL (1 dimension below threshold)

  Gaps:
    - Reference Resolution — 2 wikilinks unresolved in domain-setup step files

  New components created: 2 (harness_metrics.py, run_harness_eval.py)
  Score history: eval/results/score-history.json
```
