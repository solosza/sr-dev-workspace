# Gate Contract

| Gate ID | Task | Method | Check | Expected |
|---------|------|--------|-------|----------|
| BUILD-01 | 001 | file_exists | `.claude/skills/reference-scanner/scanner.py` | exists |
| BUILD-02 | 002 | grep | `grep -l "topic_tags\|interests" .claude/skills/reference-scanner/scanner.py` | match |
| BUILD-03 | 003 | file_exists | `.claude/skills/reference-scanner/state-schema.md` | exists |
| BUILD-04 | 004 | file_exists | `.claude/skills/reference-scanner/SKILL.md` | exists |
| TEST-05 | 005 | run_code | `python -c "from pathlib import Path; assert Path('.claude/skills/reference-scanner/scanner.py').exists()"` | exit 0 |
