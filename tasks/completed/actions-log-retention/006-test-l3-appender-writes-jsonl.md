# 006 — L3: Integration Test — Appender Writes JSONL

## Type
TEST

## Action
Verify end-to-end that the appender hook creates and writes to actions.jsonl correctly.

## What to Check

1. Clear any existing actions.jsonl:
```bash
rm -f "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/actions.jsonl"
```

2. Trigger the hook with a test action:
```bash
echo '{"tool_name":"Bash","tool_input":{"command":"echo hello"}}' | python "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/actions-log-appender.py"
```

3. Verify:
```bash
# INTEG-01: actions.jsonl was created and has content
test -f "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/actions.jsonl"

# INTEG-02: each line is valid JSON
python -c "
import json
with open('D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/actions.jsonl') as f:
    for line in f:
        line = line.strip()
        if line:
            json.loads(line)
            print('PASS: valid JSON line')
"

# INTEG-03: line count is within retention limit
python -c "
with open('D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/actions.jsonl') as f:
    lines = [l for l in f if l.strip()]
    assert len(lines) <= 200, f'Too many lines: {len(lines)}'
    print(f'PASS: {len(lines)} lines (within 200 limit)')
"
```

## Acceptance
- [ ] actions.jsonl created after hook execution
- [ ] All lines are valid JSON
- [ ] Line count within 200-line retention limit

## Dependencies
001
