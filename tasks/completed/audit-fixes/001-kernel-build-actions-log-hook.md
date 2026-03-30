# Build Actions Log Appender Hook

## Context
Audit gap #1: actions_log in session_state.json is never populated mechanically. The anchor Part B review depends on it but always sees an empty array. The agent is told to self-append (soft enforcement) but forgets after context compaction. A PostToolUse hook solves this — every Edit, Write, and non-safe Bash gets logged automatically.

## Dependencies
- None

## Requirements
- Create `.claude/hooks/actions-log-appender.py` as a PostToolUse hook
- Hook reads tool_name and tool_input from stdin JSON
- For Write/Edit: log `"[tool_name]: [file_path] — [brief description]"`
- For Bash: log `"Bash: [first 80 chars of command]"`
- Skip .claude/ Write/Edit paths (infrastructure, same logic as gate-enforcer)
- Append entry to `actions_log` array in session_state.json (read → append → write)
- Handle missing/malformed state gracefully (don't crash)
- Wire hook in `.claude/settings.local.json` as PostToolUse on `Edit|Write|Bash`
- Keep existing PostToolUse hooks (test-failure-detector on Bash)

## Acceptance Criteria
- [ ] `.claude/hooks/actions-log-appender.py` exists (verify: `test -f`)
- [ ] Hook has docstring explaining purpose (verify: `grep -q 'actions_log' .claude/hooks/actions-log-appender.py`)
- [ ] Hook skips .claude/ paths for Write/Edit (verify: `grep -q '.claude/' .claude/hooks/actions-log-appender.py`)
- [ ] Hook appends to actions_log array (verify: `grep -q 'actions_log' .claude/hooks/actions-log-appender.py`)
- [ ] settings.local.json has PostToolUse entry for actions-log-appender on Edit|Write|Bash (verify: `grep -q 'actions-log-appender' .claude/settings.local.json`)
- [ ] Existing test-failure-detector PostToolUse entry preserved (verify: `grep -q 'test-failure-detector' .claude/settings.local.json`)
- [ ] Functional test: run a Bash command, then read session_state.json — actions_log should have at least one entry

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
