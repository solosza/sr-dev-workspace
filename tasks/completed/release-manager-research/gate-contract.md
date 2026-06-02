# Gate Contract — Release Manager Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/release-manager-research/` | Create dir |
| DOC-02 | release-gap-assessment exists | file_exists | `test -f projects/release-manager-research/release-gap-assessment.md` | Write file |
| DOC-03 | Gap covers current push method | grep | `grep -qi "push\|deploy\|pipeline\|git" projects/release-manager-research/release-gap-assessment.md` | Expand doc |
| DOC-04 | kernel-integration-design exists | file_exists | `test -f projects/release-manager-research/kernel-integration-design.md` | Write file |
| DOC-05 | Design covers /kernel/release command | grep | `grep -qi "/kernel/release\|release.*command\|changelog\|tag" projects/release-manager-research/kernel-integration-design.md` | Expand doc |
| DOC-06 | standalone-product-assessment exists | file_exists | `test -f projects/release-manager-research/standalone-product-assessment.md` | Write file |
| DOC-07 | Standalone covers competitive landscape | grep | `grep -qi "Netlify\|Vercel\|GitHub Pages\|competitive\|market" projects/release-manager-research/standalone-product-assessment.md` | Expand doc |
| DOC-08 | research-report exists | file_exists | `test -f projects/release-manager-research/research-report.md` | Write file |
| DOC-09 | Report has recommendation | grep | `grep -qi "recommend\|build\|skip\|integrate" projects/release-manager-research/research-report.md` | Expand doc |
| DOC-10 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/release-manager-research/research-report.md") -gt 80` | Expand doc |
