# Step 6: Run and Score

Execute the deepeval test suite generated in Step 5, produce a scored report, update score history, and detect regressions.

## Input

| Field | Source | Example |
|-------|--------|---------|
| `mode` | Output of Step 0 | `artifact` or `harness` |
| `target` | Output of Step 0 | `check-data` or `null` (harness mode) |
| `test-repo` | Output of Step 1 | `D:\...\evals\eval-check-data` |
| `source_path` | Output of Step 0 | `D:\...\hmsa-healthcare-qa` |
| `original_source` | Output of Step 0 | Original URL or path (for reporting) |
| Test suite | Output of Step 5 | `tests/test_eval_<target>.py` or `tests/test_eval_harness.py` |

## Pre-Run Checkpoint

Before executing, read these references:
> `references/step-06/metric-selection.md`
> `references/step-06/report-format.md`

Confirm:
1. Test files exist in `<test-repo>/tests/`
2. `conftest.py` is present with fixtures
3. `framework/metrics/` contains required metric modules
4. Step 5 verification passed (all G5.x checks)

## What to Do

### 1. Execute Test Suite

Run deepeval against the generated tests (use `--rootdir`, never `cd`):

```bash
deepeval test run "<test-repo>/tests/" --verbose --rootdir "<test-repo>"
```

Capture:
- stdout (test results, metric scores)
- stderr (errors, warnings)
- Exit code (0 = all pass, non-zero = failures)

### 2. Parse Scores

Extract per-metric scores from deepeval output:
- Metric name
- Score (0.0 to 1.0)
- Threshold (from test configuration)
- Status: `PASS` if score >= threshold, `FAIL` otherwise

### 3. Determine Overall Result

- **PASS**: All metrics meet or exceed their thresholds
- **FAIL**: Any metric falls below its threshold
- Count passing and failing metrics separately

### 4. Generate Triage for Failures

For each failing metric:
- Identify which test cases contributed to the low score
- Map back to the contract rule or artifact behavior being tested
- Recommend specific investigation areas

## What to Produce

### Scored Report

Write `<test-repo>/eval-report.md` in table format:

### Artifact Mode Report

```
EVAL COMPLETE: <target>

  Metric              Score   Threshold  Status
  ToolCorrectness     0.85    0.70       PASS
  TaskCompletion      0.78    0.70       PASS
  GEval: SV-301       0.92    0.80       PASS
  GEval: SV-305       0.65    0.80       FAIL

  Overall: FAIL (1 metric below threshold)
  Gaps: SV-305 (clean break rule) — agent did not verify adjacent ranges

  New components created: <count> (<names>)
  Score history: eval/results/score-history.json
```

### Harness Mode Report

```
EVAL COMPLETE: <repo-name> (harness)
Source: <original_source>

  Dimension                    Score   Threshold  Status
  CLAUDE.md Coherence          0.88    0.80       PASS
  Loop Integrity               0.92    0.80       PASS
  Hook Coverage                0.85    0.80       PASS
  Command: session-start       0.78    0.70       PASS
  Command: anchor              0.82    0.70       PASS
  Command: complete            0.74    0.70       PASS
  Skill: kernel-domain-setup   0.70    0.70       PASS
  Manifest Integrity           1.00    1.00       PASS
  Settings Wiring              1.00    1.00       PASS
  Reference Resolution         0.95    1.00       FAIL

  Overall: FAIL (1 dimension below threshold)
  Gaps: Reference Resolution — 2 wikilinks unresolved in skill step files

  New components created: <count> (<names>)
  Score history: eval/results/score-history.json
```

### Score History

Write or update score history JSON:

**Where to write:**

| Source Type | Score History Location |
|------------|----------------------|
| Local path (original repo) | `<source_path>/eval/results/score-history.json` |
| GitHub clone (disposable) | `<test-repo>/eval/results/score-history.json` (clone is disposable, so keep in test repo) |

In harness mode, `target` is the repo name. In artifact mode, `target` is the artifact name.

```json
{
  "target": "<target or repo-name>",
  "source": "<original_source>",
  "mode": "artifact|harness",
  "history": [
    {
      "timestamp": "2026-06-24T14:00:00Z",
      "overall": "PASS|FAIL",
      "metrics": {
        "ToolCorrectness": 0.85,
        "TaskCompletion": 0.78
      },
      "failing_count": 0,
      "new_components": []
    }
  ]
}
```

Rules:
- Append to `history` array — never overwrite previous entries
- For local source repos: score history lives in the SOURCE repo (persists across eval runs)
- For GitHub clones: score history lives in the test repo (clone is disposable)
- Create `eval/results/` directory if it doesn't exist

### Regression Detection

Compare current scores against the last entry in `score-history.json`:

| Condition | Action |
|-----------|--------|
| Score drop > 0.1 on any metric | Flag as `REGRESSION` in report |
| Score drop <= 0.1 | Normal variance — no flag |
| No previous entry | Skip regression check (first run) |
| New metric (no prior score) | Skip comparison for that metric |

Add regression section to report when detected:

```
REGRESSION DETECTED:
  ToolCorrectness: 0.85 → 0.72 (drop: 0.13)
  Investigate: recent changes to tool selection logic
```

## Verification

| ID | Check | Method | Pass |
|----|-------|--------|------|
| G6.1 | Report file exists | `test -f <test-repo>/eval-report.md` | File present |
| G6.2 | All metrics scored | Report contains numeric scores for every metric | No blanks |
| G6.3 | Score history valid | `python -c "import json; json.load(open('eval/results/score-history.json'))"` | Valid JSON |
| G6.4 | Regression checked | Report contains regression section or "No regressions" | Present |

## Error Handling

| Failure | Action |
|---------|--------|
| `deepeval` not installed | Run `pip install deepeval`, retry once |
| Test execution crashes | Capture stderr, check for missing dependencies, retry once |
| No scores in output | Check deepeval version, verify test format matches deepeval API |
| Score history write fails | Check directory permissions, create `eval/results/` if missing |
| Still failing after retry | Set `failed` state with `resume_step: 6`. Invoke `/kernel/learn`. |

## Output

- `<test-repo>/eval-report.md` — scored report with table, gaps, and triage
- Score history JSON — location depends on source type (see Score History section)
- State transition: `generating_tests` → `scoring` → complete
- Contract: → `contracts/step-06-contract.json`
