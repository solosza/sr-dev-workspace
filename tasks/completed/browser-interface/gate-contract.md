# Gate Contract — BrowserInterface

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` on branch build/203-qa-build-browser-interface

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BRI-01 | Feature branch current | run_code | branch --show-current → build/203-qa-build-browser-interface | Re-run 001 |
| BRI-02 | Interface file exists | file_exists | `framework/interfaces/browser_interface.py` | Re-run 002 |
| BRI-03 | Monolith guard | grep | `grep -ciE "def .*(order|customer|login|orderly)" browser_interface.py` == 0 (no domain vocabulary in method names) | Re-run 002 — strip domain methods |
| BRI-04 | Primitives present | grep | click, send_keys/enter_text, find_element, wait_for each ≥ 1 | Re-run 002 |
| BRI-05 | Imports + instantiates (L1/L2) | run_code | python: import class, instantiate with a stub driver object, call a wrapped method against the stub — exit 0 | Re-run 003 |
| BRI-06 | Live against Orderly (L3) | run_code | headless Chrome + running Orderly: navigate to /login, enter seeded clerk creds via interface primitives, click login, wait for post-login element — exit 0. If Chrome/driver unavailable: report L3-BLOCKED and STOP | Fix or L3-BLOCKED stop |
| BRI-07 | Committed, clean, main untouched | run_code | commit on branch; porcelain empty; main unchanged | Re-run 005 |

## Requirements Coverage
1.1 design doc (copy/adapt) → BRI-02/04; contract L1 rules + monolith guard → BRI-03; L1/L2/L3 completeness → BRI-05/06; branch discipline → BRI-01/07.
