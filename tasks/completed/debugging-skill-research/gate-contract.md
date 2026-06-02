# Gate Contract — Systematic Debugging Skill Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/debugging-skill-research/` | Create dir |
| DOC-02 | skill-summary exists | file_exists | `test -f projects/debugging-skill-research/skill-summary.md` | Write file |
| DOC-03 | Summary covers 4 phases | grep | `grep -qi "phase\|RCA\|root cause\|boundary" projects/debugging-skill-research/skill-summary.md` | Expand doc |
| DOC-04 | kernel-fix-comparison exists | file_exists | `test -f projects/debugging-skill-research/kernel-fix-comparison.md` | Write file |
| DOC-05 | Comparison addresses scope difference | grep | `grep -qi "scope\|application\|kernel\|/kernel/fix" projects/debugging-skill-research/kernel-fix-comparison.md` | Expand doc |
| DOC-06 | research-report exists | file_exists | `test -f projects/debugging-skill-research/research-report.md` | Write file |
| DOC-07 | Report has integration point recommendation | grep | `grep -qi "integration\|/kernel/debug\|/kernel/fix\|@debugger\|recommend" projects/debugging-skill-research/research-report.md` | Expand doc |
| DOC-08 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/debugging-skill-research/research-report.md") -gt 60` | Expand doc |
