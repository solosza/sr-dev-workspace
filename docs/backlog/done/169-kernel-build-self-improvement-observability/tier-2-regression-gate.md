# Tier 2: Post-Learn Regression Gate

## Status
NEW

## Location
`D:\my_ai_projects\project_test_repos\platform-deepeval`

## What It Does
Wires platform-deepeval's structural tests into the kernel's post-learn cycle as a regression gate. After every `/kernel/learn` event, structural tests (4 tests, ~5 seconds, $0 cost) run automatically. If a test that was passing now fails, the change caused a regression.

## Components

### Baseline Snapshot (before learn)
Before `/kernel/learn` modifies files, capture current structural test state:
```json
{"timestamp":"...","event":"pre_learn_baseline","tests":{"test_commands_exist":"PASS","test_claudemd_references":"PASS",...}}
```
Written to `.claude/state/eval-results.jsonl`.

### Post-Learn Regression Check
After learn completes, run structural tests again and compare to baseline:
```bash
python -m pytest "[platform-deepeval]/tests/" \
  --harness-root "[harness-root]" \
  --rootdir "[platform-deepeval]" \
  -k "structural" --tb=short -q
```

### Regression Classification
```
Was PASS, now FAIL → REGRESSION (block, must fix)
Was FAIL, still FAIL → PRE-EXISTING (warn, don't block)
Was FAIL, now PASS → IMPROVEMENT (celebrate)
```

## Changes to learn.md
Add two steps to `/kernel/learn`:
1. **Before modifying files:** Run baseline snapshot (structural tests, record results)
2. **After modifying files:** Run structural tests again, compare to baseline, report

## Changes to platform-deepeval
- Add `eval-results.jsonl` schema documentation
- Potentially add a `--baseline` flag to conftest.py for snapshot mode
- Ensure structural tests are tagged/filterable with `-k structural`

## Dependencies
- Tier 1 (emission hooks) — not strictly required but should ship together
- Existing platform-deepeval structural tests must be passing

## Constraints
- Only structural tests run on every learn (zero API cost)
- GEval tests run periodically (every 5th pipeline) via /kernel/eval command (Tier 3)
- Regression check must not add >10 seconds to learn event
- Must handle case where platform-deepeval is not installed (skip gracefully)

## Acceptance Criteria
- Structural tests run automatically after every /kernel/learn
- Baseline comparison correctly identifies regressions vs pre-existing failures
- Results logged to eval-results.jsonl
- Learn event is not blocked when platform-deepeval is unavailable (graceful skip)
