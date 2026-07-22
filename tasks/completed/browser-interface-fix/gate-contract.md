# Gate Contract — BrowserInterface Contract Fix

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform`, EXISTING branch build/203-qa-build-browser-interface

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FIX-01 | No swallowed exceptions | run_code | python regex over except blocks: count without `raise` == 0 | Re-run 001 |
| FIX-02 | No screenshot machinery | grep | `grep -c "_take_screenshot\|save_screenshot" browser_interface.py` == 0 | Re-run 002 |
| FIX-03 | L2 stub + L3 live still green | run_code | stub delegation test exits 0 AND committed test_l3_browser_interface.py exits 0 (live Orderly + headless Chrome) | Fix regressions |
| FIX-04 | Committed on the SAME branch, clean, main untouched | run_code | new commit on build/203-...; porcelain empty; main unchanged | Re-run 004 |

## Requirements Coverage
Contract error rule 1 → FIX-01; Browser addendum rule 5 (screenshots = conftest) → FIX-02; no regressions → FIX-03.
