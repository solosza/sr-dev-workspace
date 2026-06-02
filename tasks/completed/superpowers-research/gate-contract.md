# Gate Contract — Superpowers Integration Research

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Project dir exists | file_exists | `test -d projects/superpowers-research/` | Create dir |
| DOC-02 | skills-inventory exists | file_exists | `test -f projects/superpowers-research/skills-inventory.md` | Write file |
| DOC-03 | Inventory lists 20+ skills | grep | `grep -c "##\|^-\s" projects/superpowers-research/skills-inventory.md` | Expand doc |
| DOC-04 | tdd-assessment exists | file_exists | `test -f projects/superpowers-research/tdd-assessment.md` | Write file |
| DOC-05 | TDD covers kernel overlap | grep | `grep -qi "kernel\|test-task\|run-task" projects/superpowers-research/tdd-assessment.md` | Expand doc |
| DOC-06 | worktree-assessment exists | file_exists | `test -f projects/superpowers-research/worktree-assessment.md` | Write file |
| DOC-07 | Worktree covers EnterWorktree | grep | `grep -qi "EnterWorktree\|worktree\|branch" projects/superpowers-research/worktree-assessment.md` | Expand doc |
| DOC-08 | code-review-assessment exists | file_exists | `test -f projects/superpowers-research/code-review-assessment.md` | Write file |
| DOC-09 | research-report exists | file_exists | `test -f projects/superpowers-research/research-report.md` | Write file |
| DOC-10 | Report has recommendation | grep | `grep -qi "ADOPT\|SKIP\|recommend\|integrate" projects/superpowers-research/research-report.md` | Expand doc |
| DOC-11 | Report is substantive | run_code | `test $(wc -l < "D:/my_ai_projects/project_test_repos/sr_dev_workspace/projects/superpowers-research/research-report.md") -gt 80` | Expand doc |
