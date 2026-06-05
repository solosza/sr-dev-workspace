# Gate Contract — AI Harness Job Search

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/ai-harness-job-search/` | Create dir |
| BUILD-02 | Runs subdir exists | file_exists | `test -d projects/ai-harness-job-search/runs/` | Create dir |
| BUILD-03 | Profile summary exists | file_exists | `test -f projects/ai-harness-job-search/profile-summary.md` | Re-run task 002 |
| BUILD-04 | Profile has match criteria | grep | `grep -q "match" projects/ai-harness-job-search/profile-summary.md` | Update profile |
| BUILD-05 | Anthropic/OpenAI run file exists | file_exists | `test -f projects/ai-harness-job-search/runs/*anthropic-openai.md` | Re-run task 003 |
| BUILD-06 | Google/Meta/xAI run file exists | file_exists | `test -f projects/ai-harness-job-search/runs/*google-meta-xai.md` | Re-run task 004 |
| BUILD-07 | Other companies run file exists | file_exists | `test -f projects/ai-harness-job-search/runs/*other-companies.md` | Re-run task 005 |
| BUILD-08 | Job list markdown exists | file_exists | `test -f projects/ai-harness-job-search/runs/*job-list.md` | Re-run task 006 |
| BUILD-09 | Job list JSON exists | file_exists | `test -f projects/ai-harness-job-search/runs/*job-list.json` | Re-run task 006 |
| BUILD-10 | JSON is valid | run_code | `python -c "import json,glob; [json.load(open(f)) for f in glob.glob('projects/ai-harness-job-search/runs/*job-list.json')]"` exits 0 | Fix JSON |
| BUILD-11 | JSON has required fields | run_code | `python -c "import json,glob; j=json.load(open(glob.glob('projects/ai-harness-job-search/runs/*job-list.json')[0])); assert all('url' in r and 'match_score' in r for r in j)"` exits 0 | Add missing fields |
| BUILD-12 | README updated | file_exists | `test -f projects/ai-harness-job-search/README.md` | Create README |
