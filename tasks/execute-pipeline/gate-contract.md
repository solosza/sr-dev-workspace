# Gate Contract — Execute Pipeline

## Verification Methods
→ [[references/verification-methods.md]]

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | step-07 has flag check | grep | `grep -q 'skip_plan_review' .claude/skills/task-builder/references/step-07-plan-review.md` | Add flag check |
| BUILD-02 | step-09 has flag check | grep | `grep -q 'no_execute' .claude/skills/task-builder/references/step-09-execute.md` | Add flag check |
| BUILD-03 | Skill directory exists | file_exists | `test -d .claude/skills/execute-pipeline/references` | Create dirs |
| BUILD-04 | SKILL.md exists | file_exists | `test -f .claude/skills/execute-pipeline/SKILL.md` | Write file |
| BUILD-05 | step-01-parse-input.md exists | file_exists | `test -f .claude/skills/execute-pipeline/references/step-01-parse-input.md` | Write file |
| BUILD-06 | step-02-create-backlog.md exists | file_exists | `test -f .claude/skills/execute-pipeline/references/step-02-create-backlog.md` | Write file |
| BUILD-07 | step-03-run-task-builder.md exists | file_exists | `test -f .claude/skills/execute-pipeline/references/step-03-run-task-builder.md` | Write file |
| BUILD-08 | step-04-execute-tasks.md exists | file_exists | `test -f .claude/skills/execute-pipeline/references/step-04-execute-tasks.md` | Write file |
| BUILD-09 | step-05-validate-report.md exists | file_exists | `test -f .claude/skills/execute-pipeline/references/step-05-validate-report.md` | Write file |
| BUILD-10 | Command file exists | file_exists | `test -f .claude/commands/kernel/execute-pipeline.md` | Write file |
| BUILD-11 | CLAUDE.md lists execute-pipeline | grep | `grep -q 'execute-pipeline' CLAUDE.md` | Add entry |
| BUILD-12 | Protocol lists execute-pipeline | grep | `grep -q 'execute-pipeline' .claude/protocols/sr_dev-protocol.md` | Add entry |
| FUNC-01 | step-07 skip works | run_code | Set flag in state, verify step-07 text contains skip logic | Fix flag check |
| FUNC-02 | step-09 stop works | run_code | Set flag in state, verify step-09 text contains stop logic | Fix flag check |
| TEST-01 | All 10 deliverable files exist | run_code | Glob count matches 10 | Fix missing files |
| TEST-02 | E2E pipeline executes backlog 031 | run_test | run-task.sh completes against execute-pipeline tasks | Fix pipeline |
