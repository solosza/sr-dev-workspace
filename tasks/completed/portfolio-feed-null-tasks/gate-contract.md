# Gate Contract — Portfolio Feed Null Tasks Fix

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | attest.py uses `or 0` for total_tasks | grep | `workflow.get("total_tasks") or 0` found in `D:/my_ai_projects/project_test_repos/sr_dev_workspace/lib/attestation/attest.py` | Re-apply fix |
| BUILD-02 | generate-feed.py null-safe task_count | grep | Null guard pattern found in `D:/my_ai_projects/isagawa-co.github.io/generate-feed.py` | Re-apply fix |
| BUILD-03 | feed.html null-safe renderEntry | grep | Null guard for task_count found in `D:/my_ai_projects/isagawa-co.github.io/feed.html` | Re-apply fix |
| BUILD-04 | feed-data.json has no null task_count | run_code | `python -c "import json; d=json.load(open('D:/my_ai_projects/isagawa-co.github.io/feed-data.json')); assert all(e['task_count'] is not None for e in d), 'null found'"` exits 0 | Re-run generator |
| TEST-01 | Playwright: no "null tasks" visible in feed | run_test | Playwright MCP browses feed.html, scrapes all entry text, asserts none contain "null tasks" | Re-investigate and fix |

## Requirements Coverage
- BUILD-01 → 001 acceptance criteria
- BUILD-02 → 002 acceptance criteria
- BUILD-03 → 003 acceptance criteria
- BUILD-04 → 004 acceptance criteria
- TEST-01 → 005 acceptance criteria
