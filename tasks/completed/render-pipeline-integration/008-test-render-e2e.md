# 008 — Test: end-to-end adapter → serve → rows → teardown (L3)

Type: TEST
Depends: 001,003

## What it verifies
The whole chain works as one: sample loop output → adapter → items.json → serve_and_watch → page.html served with the right rows visible → clean teardown. This is the real scenario the pipeline will run.

## Method
A test that: builds sample loop output, runs `to_items`, writes items.json, calls `serve`, GET / and assert all sample item names appear as rows and each shows its recommendation badge, then tears down.

## Acceptance Criteria
- [ ] `_test/test_e2e.py` exists.
- [ ] Every sample item name appears in the served HTML.
- [ ] Each rec label (Build / Test first / Don't build) appears where expected.
- [ ] No em dash in the served HTML body content produced by the adapter.
- [ ] Teardown leaves no listener; result written to `_test/e2e-result.json` (no print).

## Verify
`python tasks/render-pipeline-integration/_test/test_e2e.py` exits 0.

## Notes
Complex (spawns server) — same handling as 007.
