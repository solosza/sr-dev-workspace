# Gate Contract — Target Repo Git Baseline

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| GIT-01 | Repo initialized | run_code | `git -C "D:/my_ai_projects/project_test_repos/hmsa-qa-platform" rev-parse --is-inside-work-tree` exits 0 | Re-run task 001 |
| GIT-02 | .gitignore present + Python entries | grep | `grep -c "__pycache__" .gitignore` ≥ 1 in target repo | Re-run task 002 |
| GIT-03 | README stub present | grep | `grep -ci "hmsa qa platform" README.md` ≥ 1 in target repo | Re-run task 003 |
| GIT-04 | Baseline commit on main | run_code | `git -C <target> log --oneline` exits 0 with ≥ 1 line; current branch is main | Re-run task 004 |

## Requirements Coverage
Backlog 198 requirements: git init → GIT-01; .gitignore → GIT-02; README stub → GIT-03; main baseline → GIT-04.
