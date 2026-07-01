# Gate Contract — Resume Rewrite

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| RESEARCH-01 | Target role language research exists | file_exists | `projects/resume-loops-agent-systems/target-role-language.md` exists | Create research |
| RESEARCH-02 | Current resume analyzed | file_exists | `projects/resume-loops-agent-systems/current-resume-analysis.md` exists | Create analysis |
| BUILD-01 | New resume markdown exists | file_exists | `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.md` updated | Rewrite resume |
| BUILD-02 | PDF generated | file_exists | `D:/my_ai_projects/project_test_repos/job-application-spec/resumes/alain-ignacio-ai-agent-architect.pdf` updated | Generate PDF |
| TEST-01 | Resume has no em dashes | grep | No em dash characters in resume markdown | Fix |
| TEST-02 | Resume mentions loops/agent systems | grep | Contains "loop" and "agent system" | Fix |
