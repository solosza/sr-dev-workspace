# 001 — Edit Actions-Log Appender to Write JSONL File

## Type
BUILD

## Action
Edit `.claude/hooks/actions-log-appender.py` to append actions to `.claude/state/actions.jsonl` instead of modifying the `actions_log` array in session_state.json.

## What to Do

1. Replace the current `write_state()` approach with direct JSONL file append:
   - Define `ACTIONS_LOG = STATE_DIR / 'actions.jsonl'`
   - Instead of reading session_state.json, modifying the array, and writing back, append a single JSON line to actions.jsonl

2. Each line in actions.jsonl is a JSON object:
   ```json
   {"timestamp": "2026-04-23T00:30:00Z", "tool": "Bash", "entry": "Bash: ls -la", "session": "current"}
   ```

3. Add retention enforcement — if actions.jsonl exceeds 200 lines, truncate to the last 200 lines (keep newest):
   ```python
   def enforce_retention(log_file: Path, max_lines: int = 200):
       if not log_file.exists():
           return
       lines = log_file.read_text(encoding='utf-8').strip().split('\n')
       if len(lines) > max_lines:
           log_file.write_text('\n'.join(lines[-max_lines:]) + '\n', encoding='utf-8')
   ```

4. Still write a lightweight summary to session_state.json `actions_log` array (last 10 entries only) for backward compatibility with existing anchor reads. But the authoritative log is now actions.jsonl.

## Target File
`.claude/hooks/actions-log-appender.py`

## Acceptance
- [ ] ACTIONS_LOG path defined pointing to actions.jsonl
- [ ] Each action appends one JSON line to actions.jsonl
- [ ] Retention enforcement function exists (200-line cap)
- [ ] Backward-compatible summary still written to session_state.json

## Dependencies
None
