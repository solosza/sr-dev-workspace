# Gate Contract — Targeted Resume Pair

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Positioning research exists | file_exists | `test -f projects/targeted-resume-pair/00-positioning-research.md` | Create file |
| BUILD-02 | AI Agent resume exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-engineer.md` | Create file |
| BUILD-03 | AI QA resume exists | file_exists | `test -f D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-qa-engineer.md` | Create file |
| BUILD-04 | Agent resume has summary | grep | `grep -q 'SUMMARY' D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-engineer.md` | Add section |
| BUILD-05 | QA resume has summary | grep | `grep -q 'SUMMARY' D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-qa-engineer.md` | Add section |
| BUILD-06 | Agent resume prose-only (no bullets) | run_code | `! grep -q '^\*' D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-engineer.md` | Remove bullets |
| BUILD-07 | QA resume prose-only (no bullets) | run_code | `! grep -q '^\*' D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-qa-engineer.md` | Remove bullets |
