# Gate Contract — Eval Platform Learning Loop

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | metrics dir exists | file_exists | `test -d D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/` | Create dir |
| BUILD-02 | harness_metrics.py exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/harness_metrics.py` | Create file |
| BUILD-03 | architecture_notes.py exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/architecture_notes.py` | Create file |
| BUILD-04 | criteria_changelog.md exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/platform-deepeval/framework/metrics/criteria_changelog.md` | Create file |
| BUILD-05 | conftest.py exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/platform-deepeval/tests/conftest.py` | Create file |
| BUILD-06 | test file exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/platform-deepeval/tests/test_eval_kernel_minimal.py` | Create file |
| FUNC-01 | make_geval_metric importable | run_code | `python -c "import sys; sys.path.insert(0,'D:/my_ai_projects/project_test_repos/platform-deepeval/framework'); from metrics.harness_metrics import make_geval_metric"` exits 0 | Fix imports |
| FUNC-02 | get_notes importable | run_code | `python -c "import sys; sys.path.insert(0,'D:/my_ai_projects/project_test_repos/platform-deepeval/framework'); from metrics.architecture_notes import get_notes"` exits 0 | Fix imports |
| FUNC-03 | conftest accepts --harness-root | run_code | `python -m pytest --co --harness-root=D:/my_ai_projects/isagawa-kernel --rootdir=D:/my_ai_projects/project_test_repos/platform-deepeval -q 2>&1` exits 0 | Fix conftest |
| TEST-01 | Full eval suite passes | run_test | `python -m pytest D:/my_ai_projects/project_test_repos/platform-deepeval/tests/test_eval_kernel_minimal.py --harness-root=D:/my_ai_projects/isagawa-kernel --rootdir=D:/my_ai_projects/project_test_repos/platform-deepeval -v` — 17 passed | Fix tests |
