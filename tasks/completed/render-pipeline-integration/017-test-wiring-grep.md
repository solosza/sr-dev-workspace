# 017 — Test: all 7 ranked loops reference the render step (L1)

Type: TEST
Depends: 009,010,011,012,013,014,015

## What it verifies
Every ranked-output loop is wired to the shared render step.

## Method
A test `_test/test_wiring.py` that, for each of assay, competition, deep-dive, expand, small, lateral, source, greps the skill dir for `step-serve-and-watch` and asserts a match; writes the per-loop result to `_test/wiring-result.json`.

## Acceptance Criteria
- [ ] `_test/test_wiring.py` exists.
- [ ] All 7 loops match (exit 0).
- [ ] Result written to `_test/wiring-result.json` (no print).

## Verify
`python tasks/render-pipeline-integration/_test/test_wiring.py` exits 0.
