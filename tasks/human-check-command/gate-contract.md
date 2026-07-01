# Gate Contract — Human Check Command

| Gate ID | Type | Check | File/Path | Expected |
|---------|------|-------|-----------|----------|
| BUILD-01 | file_exists | Detection engine | .claude/skills/human-check/detect.py | Python script with regex-based AI tell detection |
| BUILD-02 | file_exists | Skill orchestrator | .claude/skills/human-check/SKILL.md | Skill with identity, philosophy, workflow, file index |
| BUILD-03 | file_exists | Command entry point | .claude/commands/kernel/human-check.md | Command with usage, input modes, examples |
| TEST-01 | grep | Detection accuracy | Test output | Em dashes, hedge words, formulaic starters all detected |
