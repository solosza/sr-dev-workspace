# 003 — Edit Gate Enforcer to Check Actions Count from JSONL

## Type
BUILD

## Action
Edit `.claude/hooks/universal-gate-enforcer.py` to use `actions.jsonl` line count as the authoritative action count for the anchor limit check, instead of relying solely on `actions_since_anchor` in workflow state.

## What to Do

1. Add a helper to count lines in actions.jsonl:
   ```python
   ACTIONS_LOG = STATE_DIR / 'actions.jsonl'

   def get_actions_count() -> int:
       """Count actions from the JSONL log file."""
       if not ACTIONS_LOG.exists():
           return 0
       try:
           content = ACTIONS_LOG.read_text(encoding='utf-8').strip()
           return len(content.split('\n')) if content else 0
       except Exception:
           return 0
   ```

2. In the `check_and_increment_counter` function, cross-reference:
   - The `actions_since_anchor` counter in workflow state is still the primary trigger
   - But add a comment noting that `actions.jsonl` is the authoritative source
   - No behavioral change needed — the counter and JSONL stay in sync because the appender hook fires on every action

This is a lightweight change — the counter mechanism stays the same, we're just noting the JSONL as source of truth.

## Target File
`.claude/hooks/universal-gate-enforcer.py`

## Acceptance
- [ ] ACTIONS_LOG path defined
- [ ] get_actions_count helper function exists
- [ ] Comment noting JSONL as authoritative source

## Dependencies
None
