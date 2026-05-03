# 005 — L3: Full Anchor Cycle Integration Test

## Type
TEST

## Action
Run a complete anchor cycle and verify the protocol hash is computed, stored, and verified correctly.

## What to Check

1. Compute expected hash:
```bash
python -c "import hashlib; print(hashlib.sha256(open('D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/protocols/sr_dev-protocol.md','rb').read()).hexdigest())"
```

2. After the next `/kernel/anchor` runs, verify:
```bash
# INTEG-01: protocol_hash field exists in session_state.json
grep -q "protocol_hash" "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/session_state.json"

# INTEG-02: stored hash matches expected
python -c "
import json, hashlib
state = json.load(open('D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/session_state.json'))
expected = hashlib.sha256(open('D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/protocols/sr_dev-protocol.md','rb').read()).hexdigest()
stored = state.get('protocol_hash','')
assert stored == expected, f'Hash mismatch: {stored} != {expected}'
print('PASS: protocol hash matches')
"

# INTEG-03: Hook allows action when hash is valid (exit 0)
echo '{"tool_name":"Bash","tool_input":{"command":"echo test"}}' | python "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/universal-gate-enforcer.py"
```

## Acceptance
- [ ] protocol_hash field exists in session_state.json after anchor
- [ ] Stored hash matches SHA-256 of current protocol file
- [ ] Hook allows actions when hash is valid

## Dependencies
001, 002
