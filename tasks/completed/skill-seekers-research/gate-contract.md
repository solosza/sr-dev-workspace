# Gate Contract — Skill Seekers Pattern Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/skill-seekers-research/` | Create dir |
| DOC-02 | projects-survey exists | file_exists | `test -f projects/skill-seekers-research/projects-survey.md` | Write file |
| DOC-03 | Survey lists existing projects | grep | `grep -qi "hoi-an\|govcon\|business-credit\|ugc\|geo" projects/skill-seekers-research/projects-survey.md` | Expand doc |
| DOC-04 | packaging-pattern-design exists | file_exists | `test -f projects/skill-seekers-research/packaging-pattern-design.md` | Write file |
| DOC-05 | Design covers SKILL.md format | grep | `grep -qi "SKILL.md\|skill.*format\|invocation" projects/skill-seekers-research/packaging-pattern-design.md` | Expand doc |
| DOC-06 | research-report exists | file_exists | `test -f projects/skill-seekers-research/research-report.md` | Write file |
| DOC-07 | Report has recommendation | grep | `grep -qi "recommend\|adopt\|skip\|build" projects/skill-seekers-research/research-report.md` | Expand doc |
| DOC-08 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/skill-seekers-research/research-report.md") -gt 60` | Expand doc |
