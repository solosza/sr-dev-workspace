# Gate Contract — Career Role Matching

## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir exists | file_exists | `test -d projects/career-role-matching/` | Create dir |
| BUILD-02 | Profile exists | file_exists | `test -f projects/career-role-matching/profile.json` | Create file |
| BUILD-03 | Raw dir has 10+ files | run_code | `ls projects/career-role-matching/raw/*.json 2>/dev/null \| wc -l` >= 10 | Run missing searches |
| BUILD-04 | Compiled listings exist | file_exists | `test -f projects/career-role-matching/compiled-listings.json` | Compile |
| BUILD-05 | Scored rankings exist | file_exists | `test -f projects/career-role-matching/scored-rankings.json` | Score |
| BUILD-06 | Report exists | file_exists | `test -f projects/career-role-matching/report.md` | Write report |
| FUNC-01 | Profile JSON valid | run_code | `python -c "import json; json.load(open('projects/career-role-matching/profile.json'))"` exits 0 | Fix JSON |
| FUNC-02 | Compiled JSON valid | run_code | `python -c "import json; json.load(open('projects/career-role-matching/compiled-listings.json'))"` exits 0 | Fix JSON |
| FUNC-03 | Scored JSON has entries | run_code | `python -c "import json; d=json.load(open('projects/career-role-matching/scored-rankings.json')); assert len(d)>0"` exits 0 | Fix data |
| FUNC-04 | Required fields present | run_code | Every entry in compiled-listings.json has: url, company, title, tier, match_score | Fix data |
| FUNC-05 | No duplicate URLs | run_code | `python -c "import json; d=json.load(open('projects/career-role-matching/compiled-listings.json')); urls=[x['url'] for x in d]; assert len(urls)==len(set(urls))"` exits 0 | Deduplicate |
