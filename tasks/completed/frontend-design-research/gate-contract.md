# Gate Contract — Frontend Design Skill Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/frontend-design-research/` | Create dir |
| DOC-02 | skill-summary exists | file_exists | `test -f projects/frontend-design-research/skill-summary.md` | Write file |
| DOC-03 | Summary covers aesthetic selection | grep | `grep -qi "aesthetic\|brutalism\|minimalism\|style" projects/frontend-design-research/skill-summary.md` | Expand doc |
| DOC-04 | isagawa-fit-assessment exists | file_exists | `test -f projects/frontend-design-research/isagawa-fit-assessment.md` | Write file |
| DOC-05 | Assessment covers existing patterns | grep | `grep -qi "pill-nav\|flow card\|isagawa\|dark\|monospace" projects/frontend-design-research/isagawa-fit-assessment.md` | Expand doc |
| DOC-06 | research-report exists | file_exists | `test -f projects/frontend-design-research/research-report.md` | Write file |
| DOC-07 | Report has recommendation | grep | `grep -qi "ADOPT\|ADAPT\|SKIP\|recommend" projects/frontend-design-research/research-report.md` | Expand doc |
| DOC-08 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/frontend-design-research/research-report.md") -gt 60` | Expand doc |
