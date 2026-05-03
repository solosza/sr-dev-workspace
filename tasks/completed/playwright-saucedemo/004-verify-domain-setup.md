# 004 — Verify Domain Setup

## Type
TEST

## Executor
inline

## Action
Verify protocol file exists, hooks registered, kernel commands present.

```bash
ls C:/Users/solos/my_ai_projects/platform-playwright/.claude/protocols/*.md
cat C:/Users/solos/my_ai_projects/platform-playwright/.claude/settings.local.json
ls C:/Users/solos/my_ai_projects/platform-playwright/.claude/commands/kernel/
```

## Acceptance Criteria
- `ls .claude/protocols/*.md` shows at least one protocol file
- `cat .claude/settings.local.json` shows hooks configuration
- Kernel commands directory contains expected command files
