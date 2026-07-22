# Gate Contract — retry.py Utility

Target: `D:/my_ai_projects/project_test_repos/hmsa-qa-platform` on branch build/200-qa-build-retry-utility

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| RTY-01 | Feature branch current | run_code | `git -C <target> branch --show-current` → build/200-qa-build-retry-utility | Re-run 001 |
| RTY-02 | retry.py exists | file_exists | `framework/resources/utilities/retry.py` | Re-run 002 |
| RTY-03 | Canonical signature | grep | `grep -c "def retry_operation" retry.py` ≥ 1 | Re-run 002 |
| RTY-04 | Transient retry works (L2/L3) | run_code | python: op fails twice (ConnectionError) then succeeds → returns value, called exactly 3 times — exit 0 | Re-run 003 |
| RTY-05 | Exhaustion re-raises; undeclared not caught | run_code | python: raises last error after max_attempts; a non-declared exception type propagates on FIRST call — exit 0 | Re-run 004 |
| RTY-06 | Committed, clean, main untouched | run_code | commit on branch; `status --porcelain` empty; main log unchanged | Re-run 005 |

## Requirements Coverage
Backlog 200: canonical implementation → RTY-02/03; behavior verified → RTY-04/05; branch discipline → RTY-01/06.
