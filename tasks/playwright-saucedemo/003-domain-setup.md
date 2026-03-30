# 003 — Domain Setup

## Type
BUILD

## Executor
inline

## Action
Pre-init state (mkdir .claude/state, write session_state.json with session_started=true), then spawn `claude -p` in C:/Users/solos/my_ai_projects/platform-playwright to run domain-setup.

```bash
mkdir -p C:/Users/solos/my_ai_projects/platform-playwright/.claude/state
echo '{"session_started": true}' > C:/Users/solos/my_ai_projects/platform-playwright/.claude/state/session_state.json
claude -p "Run /kernel/domain-setup" --cwd C:/Users/solos/my_ai_projects/platform-playwright
```

## Acceptance Criteria
- Protocol file exists in .claude/protocols/ at C:/Users/solos/my_ai_projects/platform-playwright/
- settings.local.json has hooks configured
