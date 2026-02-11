# /kernel/domain-setup

Create complete enforcement for a new domain. Invoke when starting work in a new domain.

## Instructions

### Step 0: Normalize Domain Name

**CRITICAL:** Domain name MUST be normalized before use:
- Lowercase
- Replace hyphens with underscores
- Remove special characters

Example: `playwright-automation` → `playwright_automation`

This ensures consistency between:
- `session_state.json` domain field
- `[domain]_workflow.json` filename
- `[domain]-protocol.md` filename
- `[domain]-*.md` command filenames

### Step 1: Create Protocol File

Create `.claude/protocols/[domain]-protocol.md` with:

```markdown
# [Domain] Protocol

## Overview
[What this domain is about]

## Architecture
[Key structural patterns]

## Naming Conventions
[How to name files, classes, methods]

## Patterns
[What to do]

## Anti-Patterns
[What NOT to do]

## Quality Gates
[What to check before proceeding]

## Lessons Learned
[Will be updated by /kernel/learn]
```

### Step 2: Create Domain Commands

Create in `.claude/commands/`:

| File | Purpose |
|------|---------|
| `[domain]-anchor.md` | Re-read protocol (calls /kernel/anchor) |
| `[domain]-learn.md` | Record lesson (calls /kernel/learn) |

Each domain command should reference the kernel command.

**Note:** `/kernel/validate` is deprecated. Anchor Part B handles quality checks.

### Step 3: Create Hooks

Create `.claude/hooks/[domain]-gate-enforcer.py`:

```python
#!/usr/bin/env python3
"""
[Domain] Gate Enforcer - Blocks writes without gate validation.
"""
import json, sys
from pathlib import Path

PROTECTED_PATHS = {
    # 'path/prefix/': 'required_state_key',
}

STATE_FILE = Path('.claude/state/[domain]_workflow.json')

def main():
    try:
        data = json.load(sys.stdin)
    except:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    if tool_name not in ('Write', 'Edit'):
        sys.exit(0)

    file_path = data.get('tool_input', {}).get('file_path', '').replace('\\', '/')

    for prefix, key in PROTECTED_PATHS.items():
        if prefix in file_path:
            if not STATE_FILE.exists():
                print(f"BLOCKED: No state. Invoke /kernel/anchor first.", file=sys.stderr)
                sys.exit(2)
            state = json.loads(STATE_FILE.read_text())
            if not state.get(key):
                print(f"BLOCKED: {key} not set. Invoke required command.", file=sys.stderr)
                sys.exit(2)
    sys.exit(0)

if __name__ == '__main__':
    main()
```

### Step 4: Wire Up Settings

#### 4a: Create `.claude/settings.json`

Create this file with:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "defaultMode": "default"
  }
}
```

#### 4b: Update `.claude/settings.local.json` (PRESERVE KERNEL HOOKS)

**CRITICAL:** Do NOT replace the entire settings file. You MUST preserve ALL kernel hooks:
- `universal-gate-enforcer.py` (PreToolUse)
- `test-failure-detector.py` (PostToolUse)

1. **Read** existing `.claude/settings.local.json`
2. **Append** domain hook to existing PreToolUse hooks array
3. **Never** remove kernel hooks

**Before (kernel hooks only):**
```json
{
  "permissions": {
    "allow": []
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write|Bash",
      "hooks": [{"type": "command", "command": "python .claude/hooks/universal-gate-enforcer.py"}]
    }],
    "PostToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command", "command": "python .claude/hooks/test-failure-detector.py"}]
    }]
  }
}
```

**After (kernel + domain hooks):**
```json
{
  "permissions": {
    "allow": []
  },
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write|Bash",
      "hooks": [
        {"type": "command", "command": "python .claude/hooks/universal-gate-enforcer.py"},
        {"type": "command", "command": "python .claude/hooks/[domain]-gate-enforcer.py"}
      ]
    }],
    "PostToolUse": [{
      "matcher": "Bash",
      "hooks": [{"type": "command", "command": "python .claude/hooks/test-failure-detector.py"}]
    }]
  }
}
```

**WHY kernel hooks must stay:**
- `universal-gate-enforcer.py` - Enforces session-start, anchor, learn, action limits
- `test-failure-detector.py` - Detects test failures, sets needs_learn flag

### Step 5: Create State Directory

Create `.claude/state/` if not exists.

### Step 6: Update State

Update `.claude/state/session_state.json`:
```json
{
  "domain": "[normalized_domain]"
}
```

Create `.claude/state/[normalized_domain]_workflow.json`:
```json
{
  "domain": "[normalized_domain]",
  "setup_complete": true,
  "protocol_created": true,
  "commands_created": true,
  "hooks_created": true,
  "anchored": false,
  "actions_since_anchor": 0,
  "actions_limit": 7,
  "timestamp": "..."
}
```

**Counter Fields:**
- `actions_since_anchor`: Hook auto-increments on Write/Edit/Bash
- `actions_limit`: Configurable limit (default 7) before anchor required

**IMPORTANT:** The domain value in session_state.json MUST match the workflow filename prefix.

### Step 7: Report & Restart Requirement

Hooks are loaded at Claude Code startup. New hooks require restart.

Update `.claude/state/session_state.json`:
```json
{
  "needs_restart": true,
  "resume_after_restart": "anchor"
}
```

Then report:

```
REPORT: Setup Complete - RESTART REQUIRED

Created enforcement for [domain]:

┌───────────────┬───────────────────────────────────────────┐
│     Asset     │                   Path                    │
├───────────────┼───────────────────────────────────────────┤
│ Protocol      │ .claude/protocols/[domain]-protocol.md    │
│ Commands      │ .claude/commands/[domain]-*.md            │
│ Hooks         │ .claude/hooks/[domain]-gate-enforcer.py   │
│ Settings      │ .claude/settings.json (created)           │
│ Settings      │ .claude/settings.local.json (updated)     │
│ State         │ .claude/state/[domain]_workflow.json      │
└───────────────┴───────────────────────────────────────────┘

⚠️  RESTART REQUIRED

Hooks load at startup. Domain hook is NOT active yet.

1. Restart Claude Code now
2. After restart, say "continue"
3. I will resume from /kernel/anchor

Waiting for restart...
```

**STOP. Do not proceed until user restarts and says "continue".**
