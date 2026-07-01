# Gate Contract — /kernel/eval Command Build

## BUILD Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Command entry point exists | file_exists | `test -f .claude/commands/kernel/eval.md` | Create file |
| BUILD-02 | SKILL.md exists | file_exists | `test -f .claude/skills/eval/SKILL.md` | Create file |
| BUILD-03 | workflow.md exists | file_exists | `test -f .claude/skills/eval/workflow.md` | Create file |
| BUILD-04 | Skill gate-contract.md exists | file_exists | `test -f .claude/skills/eval/gate-contract.md` | Create file |
| BUILD-05 | step-01-create-test-repo.md exists | file_exists | `test -f .claude/skills/eval/steps/step-01-create-test-repo.md` | Create file |
| BUILD-06 | step-02-compile-harness.md exists | file_exists | `test -f .claude/skills/eval/steps/step-02-compile-harness.md` | Create file |
| BUILD-07 | step-03-copy-artifact.md exists | file_exists | `test -f .claude/skills/eval/steps/step-03-copy-artifact.md` | Create file |
| BUILD-08 | step-04-component-check.md exists | file_exists | `test -f .claude/skills/eval/steps/step-04-component-check.md` | Create file |
| BUILD-09 | step-05-generate-tests.md exists | file_exists | `test -f .claude/skills/eval/steps/step-05-generate-tests.md` | Create file |
| BUILD-10 | step-06-run-and-score.md exists | file_exists | `test -f .claude/skills/eval/steps/step-06-run-and-score.md` | Create file |
| BUILD-11 | References INDEX.md exists | file_exists | `test -f .claude/skills/eval/references/INDEX.md` | Create file |
| BUILD-12 | kernel-file-list.md exists | file_exists | `test -f .claude/skills/eval/references/step-02/kernel-file-list.md` | Create file |
| BUILD-13 | deepeval-file-list.md exists | file_exists | `test -f .claude/skills/eval/references/step-02/deepeval-file-list.md` | Create file |
| BUILD-14 | dependency-resolution.md exists | file_exists | `test -f .claude/skills/eval/references/step-03/dependency-resolution.md` | Create file |
| BUILD-15 | component-decision-table.md exists | file_exists | `test -f .claude/skills/eval/references/step-04/component-decision-table.md` | Create file |
| BUILD-16 | golden-translation-patterns.md exists | file_exists | `test -f .claude/skills/eval/references/step-05/golden-translation-patterns.md` | Create file |
| BUILD-17 | metric-selection.md exists | file_exists | `test -f .claude/skills/eval/references/step-06/metric-selection.md` | Create file |
| BUILD-18 | report-format.md exists | file_exists | `test -f .claude/skills/eval/references/step-06/report-format.md` | Create file |
| BUILD-19 | step-02-contract.json exists | file_exists | `test -f .claude/skills/eval/contracts/step-02-contract.json` | Create file |
| BUILD-20 | step-03-contract.json exists | file_exists | `test -f .claude/skills/eval/contracts/step-03-contract.json` | Create file |
| BUILD-21 | step-05-contract.json exists | file_exists | `test -f .claude/skills/eval/contracts/step-05-contract.json` | Create file |
| BUILD-22 | step-06-contract.json exists | file_exists | `test -f .claude/skills/eval/contracts/step-06-contract.json` | Create file |

## INTEGRITY Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| INT-01 | SKILL.md references all 6 step files | grep | All step filenames appear in SKILL.md | Add missing references |
| INT-02 | SKILL.md references workflow.md | grep | `grep -q "workflow.md" .claude/skills/eval/SKILL.md` | Add reference |
| INT-03 | SKILL.md references gate-contract.md | grep | `grep -q "gate-contract.md" .claude/skills/eval/SKILL.md` | Add reference |
| INT-04 | Each step file references its dependencies | grep | Step files reference their reference/contract files | Fix references |
| INT-05 | INDEX.md references all reference files | grep | All reference filenames appear in INDEX.md | Add missing references |
| INT-06 | Command entry point references SKILL.md | grep | `grep -q "SKILL.md" .claude/commands/kernel/eval.md` | Add reference |
| INT-07 | No file exceeds 200 lines | wc | `wc -l` on each file is <= 200 | Extract to sub-file |

## FUNCTIONAL Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | All contract JSONs parse as valid JSON | json_parse | `python -c "import json; json.load(open(f))"` for each contract | Fix JSON |
| FUNC-02 | Eval invocation against check-data produces scored report | run_eval | `/kernel/eval check-data D:\my_ai_projects\project_test_repos\hmsa-healthcare-qa` produces score output | Debug and fix |
