# Gate Contract — Orderly Harness UI Slice

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` on branch build/202-qa-build-harness-ui-slice. App port: 8017.

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| HUI-01 | Feature branch current | run_code | branch --show-current → build/202-qa-build-harness-ui-slice | Re-run 001 |
| HUI-02 | App boots | run_code | uvicorn starts; GET http://127.0.0.1:8017/login returns 200 within 15s; process cleanly stopped | Fix app; re-run 011 |
| HUI-03 | Core pages render | run_code | After demo login: /customers and /orders return 200 with expected page markers | Fix routes/templates |
| HUI-04 | data-testid coverage | run_code | Audit script: every `<a>`, `<button>`, `<input>`, `<select>`, `<form>` in harness templates has data-testid — zero misses | Re-run 012 |
| HUI-05 | Seed deterministic | run_code | Run seed twice on fresh DBs → identical row sets (fixed IDs) | Re-run 013 |
| HUI-06 | No healthcare vocabulary | grep | `grep -riE "hmsa|claim|member|patient|provider|healthcare" harness/` → 0 matches | Purge vocabulary |
| HUI-07 | Committed, clean, main untouched | run_code | Commit on branch; porcelain empty; main log unchanged | Re-run 014 |

## Requirements Coverage
harness-app.md V1 slice → HUI-02/03; data-testid convention → HUI-04; deterministic seed → HUI-05; user constraint (generic commerce) → HUI-06; branch discipline → HUI-01/07.
