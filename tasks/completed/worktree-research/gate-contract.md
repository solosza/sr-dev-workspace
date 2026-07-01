# Gate Contract — Worktree Research

## Verification Methods

Structural (file_exists, grep), Functional (manual review), Semantic (research quality).

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Project dir created | file_exists | `test -d projects/worktree-research/` | Create dir |
| BUILD-02 | README exists | file_exists | `test -f projects/worktree-research/README.md` | Create file |
| BUILD-03 | EnterWorktree analysis | file_exists | `test -f projects/worktree-research/01-enterworktree-analysis.md` | Create file |
| BUILD-04 | EnterWorktree testing | file_exists | `test -f projects/worktree-research/02-enterworktree-testing.md` | Create file |
| BUILD-05 | State isolation experiment | file_exists | `test -f projects/worktree-research/03-state-isolation-experiment.md` | Create file |
| BUILD-06 | State isolation results | file_exists | `test -f projects/worktree-research/04-state-isolation-results.md` | Create file |
| BUILD-07 | Merge conflict analysis | file_exists | `test -f projects/worktree-research/05-merge-conflict-analysis.md` | Create file |
| BUILD-08 | Merge results | file_exists | `test -f projects/worktree-research/06-merge-results.md` | Create file |
| BUILD-09 | Lifecycle design | file_exists | `test -f projects/worktree-research/07-lifecycle-design.md` | Create file |
| BUILD-10 | Execute-pipeline integration | file_exists | `test -f projects/worktree-research/08-execute-pipeline-changes.md` | Create file |
| BUILD-11 | Run-task.sh compatibility | file_exists | `test -f projects/worktree-research/09-run-task-sh-compatibility.md` | Create file |
| BUILD-12 | Research report | file_exists | `test -f projects/worktree-research/RESEARCH-REPORT.md` | Create file |
| BUILD-13 | Integration design | file_exists | `test -f projects/worktree-research/INTEGRATION-DESIGN.md` | Create file |
| DOC-01 | Research report complete | grep | `grep -q "Recommendations" projects/worktree-research/RESEARCH-REPORT.md` | Expand doc |

## Requirements Coverage

Each gate corresponds to a task deliverable. All tasks must complete for all gates to pass.
