# 005 — L3 Integration Verification: one_shot Bypass Works

## Type
TEST

## Action
Simulate the exact contention scenario and verify the fix works.

## Test Script

```python
import json
import subprocess
import sys

STATE_DIR = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state"
SESSION_FILE = f"{STATE_DIR}/session_state.json"
WORKFLOW_FILE = f"{STATE_DIR}/sr_dev_workflow.json"
HOOK = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/universal-gate-enforcer.py"

# Save original state
with open(SESSION_FILE) as f:
    orig_session = json.load(f)
with open(WORKFLOW_FILE) as f:
    orig_workflow = json.load(f)

def write_state(session_overrides, workflow_overrides):
    s = {**orig_session, **session_overrides}
    w = {**orig_workflow, **workflow_overrides}
    with open(SESSION_FILE, 'w') as f:
        json.dump(s, f, indent=2)
    with open(WORKFLOW_FILE, 'w') as f:
        json.dump(w, f, indent=2)

def run_hook(tool_json):
    result = subprocess.run(
        [sys.executable, HOOK],
        input=json.dumps(tool_json),
        capture_output=True, text=True
    )
    return result.returncode, result.stderr

passed = 0
failed = 0

# Test 1: one_shot=true, anchored=false → should NOT block (exit 0)
write_state({"one_shot": True, "session_started": True, "needs_learn": False}, {"anchored": False})
code, err = run_hook({"tool_name": "Bash", "tool_input": {"command": "echo test"}})
if code == 0:
    print("PASS: one_shot=true, anchored=false → allowed")
    passed += 1
else:
    print(f"FAIL: one_shot=true, anchored=false → blocked (exit {code}): {err}")
    failed += 1

# Test 2: one_shot=false, anchored=false → should block (exit 2)
write_state({"one_shot": False, "session_started": True, "needs_learn": False}, {"anchored": False})
code, err = run_hook({"tool_name": "Bash", "tool_input": {"command": "echo test"}})
if code == 2:
    print("PASS: one_shot=false, anchored=false → blocked")
    passed += 1
else:
    print(f"FAIL: one_shot=false, anchored=false → exit {code} (expected 2)")
    failed += 1

# Test 3: one_shot=true → counter should NOT increment
write_state({"one_shot": True, "session_started": True, "needs_learn": False}, {"anchored": True, "actions_since_anchor": 0})
run_hook({"tool_name": "Bash", "tool_input": {"command": "echo test"}})
with open(WORKFLOW_FILE) as f:
    w = json.load(f)
if w.get("actions_since_anchor", 0) == 0:
    print("PASS: one_shot=true → counter not incremented")
    passed += 1
else:
    print(f"FAIL: one_shot=true → counter incremented to {w.get('actions_since_anchor')}")
    failed += 1

# Restore original state
with open(SESSION_FILE, 'w') as f:
    json.dump(orig_session, f, indent=2)
with open(WORKFLOW_FILE, 'w') as f:
    json.dump(orig_workflow, f, indent=2)

print(f"\nResults: {passed}/3 passed, {failed} failed")
if failed > 0:
    sys.exit(1)
```

## Pass Criteria
- Test 1: one_shot agent with anchored=false is NOT blocked
- Test 2: normal agent with anchored=false IS blocked
- Test 3: one_shot agent does not increment counter
- Original state restored after tests

## Dependencies
001, 002
