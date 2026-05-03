# Gate Contract — Website Cloner

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Research report exists | file_exists | `test -f .claude/skills/website-cloner/research/repo-analysis.md` | Create file |
| BUILD-02 | Gap analysis exists | file_exists | `test -f .claude/skills/website-cloner/research/gap-analysis.md` | Create file |
| BUILD-03 | Decision report exists | file_exists | `test -f .claude/skills/website-cloner/research/decision.md` | Create file |
| BUILD-04 | SKILL.md exists | file_exists | `test -f .claude/skills/website-cloner/SKILL.md` | Create file |
| BUILD-05 | Clone command exists | file_exists | `test -f .claude/commands/clone.md` | Create file |
| FUNC-01 | Skill references extraction | grep | `grep -q "extract" .claude/skills/website-cloner/SKILL.md` | Fix content |
| TEST-01 | Clone command test | manual | Run `/clone` against a simple public site and verify output | Fix skill |
