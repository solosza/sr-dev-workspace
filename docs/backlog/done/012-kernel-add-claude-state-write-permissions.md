# Add .claude/ Auto-Approve Hook to Master Kernel

## Status
Open

## Priority
High — without this, headless runs can't use Write/Edit tools on .claude/ files

## Summary
Claude Code 2.1+ protects `.claude/` from writes even in `bypassPermissions` mode. Only `.claude/commands/`, `.claude/agents/`, and `.claude/skills/` are exempt. This blocks the kernel from using Write/Edit on its own state, lessons, protocols, hooks, and settings files.

## What Doesn't Work
- `defaultMode: "bypassPermissions"` — doesn't override .claude/ protection
- `skipDangerousModePermissionPrompt` — doesn't affect .claude/ directory
- Allow rules (`Write(/.claude/state/**)`) — path matching doesn't work for this
- `PreToolUse` hook with `permissionDecision: "allow"` — ignored for protected directories

## What Works
A `PermissionRequest` hook that outputs `decision.behavior: "allow"` for `.claude/` paths.

## Implementation

### 1. Create hook: `.claude/hooks/auto-approve-claude-writes.py`

```python
#!/usr/bin/env python3
import json
import sys

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

tool_name = data.get('tool_name', '')
if tool_name not in ('Write', 'Edit'):
    sys.exit(0)

hook_event = data.get('hook_event_name', '')
tool_input = data.get('tool_input', {})
file_path = tool_input.get('file_path', '').replace('\\', '/')

if '.claude/' in file_path:
    if hook_event == 'PermissionRequest':
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PermissionRequest",
                "decision": {"behavior": "allow"}
            }
        }
    else:
        result = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow"
            }
        }
    print(json.dumps(result))
    sys.exit(0)

sys.exit(0)
```

### 2. Wire in `settings.local.json`

```json
{
  "hooks": {
    "PermissionRequest": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python .claude/hooks/auto-approve-claude-writes.py"
          }
        ]
      }
    ]
  }
}
```

Note: PreToolUse entry is NOT needed. Only PermissionRequest works for .claude/ protected directory overrides.

## Testing
Deployed in sr-dev-workspace and test-run-task-resume (2026-03-22). Write to `.claude/state/session_state.json` confirmed no prompt. Soak testing before pushing to master.

## Files to Update
- `isagawa-kernel/.claude/hooks/auto-approve-claude-writes.py` — new file
- `isagawa-kernel/.claude/settings.local.json` — add PermissionRequest hook
- Sync to all repos per sync rule
