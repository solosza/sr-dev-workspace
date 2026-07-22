# Gate Contract — trace.py Utility

Target repo: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` (all checks on branch build/199-qa-build-trace-utility)

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| TRC-01 | Feature branch exists and is current | run_code | `git -C <target> branch --show-current` → `build/199-qa-build-trace-utility` | Re-run task 001 |
| TRC-02 | trace.py exists | file_exists | `framework/resources/utilities/trace.py` present | Re-run task 002 |
| TRC-03 | Renamed decorator, no legacy name | grep | `grep -c "def trace" trace.py` ≥ 1 AND `grep -ci "autologger\|automation_logger" trace.py` == 0 | Task 002: complete the rename |
| TRC-04 | Importable + wraps (L2) | run_code | python: import trace module, decorate a sample fn, call it — exit 0 | Re-run task 003 |
| TRC-05 | START/END output through logging (L3) | run_code | python: decorated call emits `- START` and `- END` lines via logging handler — exit 0 | Re-run task 004 |
| TRC-06 | Committed, clean tree | run_code | `git -C <target> status --porcelain` empty; log shows the 199 commit on the branch | Re-run task 005 |

## Requirements Coverage
Backlog 199: rename → TRC-03; same implementation working → TRC-04/05; branch discipline → TRC-01/06.
