# Gate Contract — D&D Game Loop Integration

## Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Loop template dir exists | file_exists | `test -d .claude/skills/loop-template/` | Create dir |
| BUILD-02 | Loop template SKILL.md exists | file_exists | `test -f .claude/skills/loop-template/SKILL.md` | Write file |
| BUILD-03 | Loop template has 4 contract templates | file_exists | `ls .claude/skills/loop-template/contracts/*.json | wc -l` >= 4 | Write files |
| BUILD-04 | Loop template has gate template | file_exists | `test -f .claude/skills/loop-template/gate-contract-template.md` | Write file |
| BUILD-05 | Loop template has test fixture template | file_exists | `test -f .claude/skills/loop-template/_test/fixtures/scenario-template.json` | Write file |
| BUILD-06 | No .py files in campaign/ | run_code | `! find campaign/ -name "*.py" | grep .` | Remove files |
| BUILD-07 | No .py files in challenge/ | run_code | `! find challenge/ -name "*.py" | grep .` | Remove files |
| BUILD-08 | No .py files in rest/ | run_code | `! find rest/ -name "*.py" | grep .` | Remove files |
| BUILD-09 | No .py files in atomic-ops/ | run_code | `! find atomic-ops/ -name "*.py" | grep .` | Remove files |
| BUILD-10 | All 11 loops have input contract | file_exists | Each loop has `contracts/[name]-input.json` | Write file |
| BUILD-11 | All 11 loops have output contract | file_exists | Each loop has `contracts/[name]-output.json` | Write file |
| BUILD-12 | All 11 loops have rules contract | file_exists | Each loop has `contracts/[name]-rules.json` | Write file |
| BUILD-13 | All 11 loops have integration contract | file_exists | Each loop has `contracts/[name]-integration.json` | Write file |
| BUILD-14 | All 11 loops have gate-contract.md | file_exists | Each loop has `gate-contract.md` | Write file |
| BUILD-15 | All 11 loops have _test/fixtures/ | file_exists | Each loop has `_test/fixtures/` with at least one fixture | Create dir+file |
| BUILD-16 | All 11 loops have DDD SKILL.md | grep | Each SKILL.md contains "DECLARE" "DETERMINE" "DESCRIBE" | Update SKILL.md |
| BUILD-17 | Integration test specs exist | file_exists | 3 integration test files in game repo | Write files |
| FUNC-01 | All contracts valid JSON | run_code | `python -c "import json, glob; [json.load(open(f)) for f in glob.glob('**/*-*.json', recursive=True)]"` | Fix JSON |
| TEST-01 | Loop template complete | run_code | All 8 template files exist with non-zero content | Fix template |
| TEST-02 | No Python in loops | run_code | Zero .py files in the 11 loop dirs | Remove files |
| TEST-03 | All tiers complete | run_code | All 11 loops pass BUILD-10 through BUILD-16 | Fix loops |
| TEST-04 | Structural audit | run_code | Every loop dir matches generalized pattern | Fix structure |

## Requirements Coverage
Every gate maps to task acceptance criteria. All 11 loops (campaign, orchestration-loop, combat, social, challenge, travel, rest, item-use, ability-saves, environmental-hazards, downtime-activities) must satisfy BUILD-10 through BUILD-16.
