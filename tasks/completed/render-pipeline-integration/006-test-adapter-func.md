# 006 — Test: adapter emits schema-valid items.json (L1/L2)

Type: TEST
Depends: 001

## What it verifies
The adapter turns a realistic sample loop output into a schema-valid items.json with the right recs, tags, and plain vocabulary, and no em dashes.

## Method
Write a test `tasks/render-pipeline-integration/_test/test_adapter.py` that:
- Builds a sample loop_output dict (3 items with names, descs, recs, fits, merit ranks — reuse the engine-as-a-product wedges as sample data).
- Calls `to_items(...)`.
- Asserts: top-level keys present; each item has id/rank/name/desc/rec/tag; rec tones in {c,b,e}; tag tones in {a,b,c}; order follows the merit signal (NOT fit); no `—` and no jargon terms (wedge/assay/GO-IF) in any string.

## Acceptance Criteria
- [ ] `_test/test_adapter.py` exists.
- [ ] Running it exits 0 with all assertions passing.
- [ ] The test writes its result to `_test/adapter-result.json` (no print — code-quality gate).

## Verify
`python tasks/render-pipeline-integration/_test/test_adapter.py` exits 0.
