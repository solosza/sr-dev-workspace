# Gate Contract — Run-Task Zombie Process Fix

## Structural Gates

| Gate | Check | Passed |
|------|-------|--------|
| BUILD-01 | `run-task.sh` uses file-based output capture (not `$()`) | [ ] |
| BUILD-02 | `lib/common.sh` `kill_process_tree` kills entire tree on Windows | [ ] |
| BUILD-03 | Pre-iteration exit guard prevents extra spawns after ALL_TASKS_COMPLETE | [ ] |
| BUILD-04 | Log files namespaced by pipeline run (no cross-pipeline overwrites) | [ ] |
| BUILD-05 | Cleanup trap propagates SIGTERM to child `claude -p` process | [ ] |

## Functional Gates

| Gate | Check | Passed |
|------|-------|--------|
| FUNC-01 | Audit identifies which backlog requirements are already fixed | [ ] |
| FUNC-02 | `bash -n run-task.sh` and `bash -n lib/common.sh` pass (no syntax errors) | [ ] |
| FUNC-03 | Live test completes without zombie processes or empty logs | [ ] |
