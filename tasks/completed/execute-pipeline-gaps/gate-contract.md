## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | step-03 plan review flag | grep | `grep -q '"skip_plan_review": false' .claude/skills/execute-pipeline/references/step-03-run-task-builder.md` | Edit flag |
| BUILD-02 | run-task.sh has CURRENT_TASK | grep | `grep -q 'CURRENT_TASK' run-task.sh` | Add variable |
| BUILD-03 | run-task.sh has BACKLOG_PATH | grep | `grep -q 'BACKLOG_PATH' run-task.sh` | Add argument |
| BUILD-04 | run-task.sh has move-to-done | grep | `grep -q 'docs/backlog/done' run-task.sh` | Add move logic |
| BUILD-05 | step-09 has mode docs | grep | `grep -q -i 'standalone' .claude/skills/task-builder/references/step-09-execute.md` | Add docs |
| BUILD-06 | complete.md has gate verify | grep | `grep -q 'gate-contract.md' .claude/commands/kernel/complete.md` | Add step |
| BUILD-07 | step-04 has classify logic | grep | `grep -q -i 'classif' .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` | Add logic |
| BUILD-08 | step-04 has autonomous-cycle | grep | `grep -q 'autonomous-cycle' .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` | Add route |
| BUILD-09 | granularity-reference exists | file_exists | `test -f .claude/skills/task-builder/references/granularity-reference.md` | Write file |
| BUILD-10 | step-05-decompose has wikilink | grep | `grep -q 'granularity-reference' .claude/skills/task-builder/references/step-05-decompose.md` | Add link |
| BUILD-11 | step-06-atomize has wikilink | grep | `grep -q 'granularity-reference' .claude/skills/task-builder/references/step-06-atomize.md` | Add link |
| FUNC-01 | run-task.sh syntax valid | run_code | `bash -n run-task.sh` exits 0 | Fix syntax |
| FUNC-02 | common.sh syntax valid | run_code | `bash -n lib/common.sh` exits 0 | Fix syntax |
| TEST-01 | dispatch has default fallback | grep | `grep -q -i 'default\|fallback\|uncertain' .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` | Add fallback |
