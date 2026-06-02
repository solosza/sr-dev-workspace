# Gate Contract — Skill Security Auditor Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/skill-security-research/` | Create dir |
| DOC-02 | audit-surface-analysis exists | file_exists | `test -f projects/skill-security-research/audit-surface-analysis.md` | Write file |
| DOC-03 | Surface covers skill formats | grep | `grep -qi "SKILL.md\|YAML\|frontmatter\|agent" projects/skill-security-research/audit-surface-analysis.md` | Expand doc |
| DOC-04 | static-analysis-design exists | file_exists | `test -f projects/skill-security-research/static-analysis-design.md` | Write file |
| DOC-05 | Design covers destructive patterns | grep | `grep -qi "destructive\|rm -rf\|force.push\|credential" projects/skill-security-research/static-analysis-design.md` | Expand doc |
| DOC-06 | research-report exists | file_exists | `test -f projects/skill-security-research/research-report.md` | Write file |
| DOC-07 | Report has recommendation | grep | `grep -qi "recommend\|build\|skip\|audit" projects/skill-security-research/research-report.md` | Expand doc |
| DOC-08 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/skill-security-research/research-report.md") -gt 60` | Expand doc |
