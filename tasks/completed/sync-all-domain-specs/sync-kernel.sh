#!/usr/bin/env bash
# sync-kernel.sh — Sync kernel infrastructure from isagawa-kernel master to a target repo.
# Usage: bash sync-kernel.sh <target-repo-path>
#
# Copies: kernel commands, skills, hooks, infrastructure
# Preserves: domain commands, domain skills, protocols, state files

set -euo pipefail

TARGET="${1:?Usage: bash sync-kernel.sh <target-repo-path>}"
MASTER="D:/my_ai_projects/isagawa-kernel"

if [ ! -d "$TARGET/.claude" ]; then
  echo "ERROR: $TARGET/.claude not found"
  exit 1
fi

NAME=$(basename "$TARGET")
echo "=== Syncing kernel to: $NAME ==="

# --- 1. Kernel Commands (15 files) ---
mkdir -p "$TARGET/.claude/commands/kernel/"
cp "$MASTER/.claude/commands/kernel/"*.md "$TARGET/.claude/commands/kernel/"
CMD_COUNT=$(ls "$TARGET/.claude/commands/kernel/"*.md | wc -l)
echo "  Commands: $CMD_COUNT copied to .claude/commands/kernel/"

# --- 2. Kernel Skills (7 folders) ---
for skill in audit-workflow autonomous-cycling execute-pipeline kernel-domain-setup prod-test task-builder website-cloner; do
  rm -rf "$TARGET/.claude/skills/$skill/"
  cp -r "$MASTER/.claude/skills/$skill/" "$TARGET/.claude/skills/$skill/"
done
echo "  Skills: 7 kernel skill folders synced"

# --- 3. Kernel Hooks (6 files) ---
for hook in actions-log-appender.py agent-inline-execution-blocker.py auto-approve-claude-writes.py domain-gate-enforcer.template.py test-failure-detector.py universal-gate-enforcer.py; do
  cp "$MASTER/.claude/hooks/$hook" "$TARGET/.claude/hooks/$hook"
done
HOOK_COUNT=$(ls "$TARGET/.claude/hooks/"*.py | wc -l)
echo "  Hooks: 6 kernel hooks copied (total hooks: $HOOK_COUNT)"

# --- 4. Infrastructure ---
# run-task.sh and run-task-batch.sh
cp "$MASTER/run-task.sh" "$TARGET/run-task.sh"
cp "$MASTER/run-task-batch.sh" "$TARGET/run-task-batch.sh"

# lib/
mkdir -p "$TARGET/lib/attestation/"
cp "$MASTER/lib/common.sh" "$TARGET/lib/common.sh"
cp "$MASTER/lib/attestation/"*.py "$TARGET/lib/attestation/"

# lessons index only
mkdir -p "$TARGET/.claude/lessons/"
cp "$MASTER/.claude/lessons/lessons.md" "$TARGET/.claude/lessons/lessons.md"
echo "  Infrastructure: run-task.sh, lib/, lessons/lessons.md copied"

# --- 5. Merge settings.local.json ---
SETTINGS="$TARGET/.claude/settings.local.json"
if [ -f "$SETTINGS" ]; then
  # Use Python to merge hook registrations into existing settings
  python -c "
import json, sys

with open('$SETTINGS', 'r') as f:
    settings = json.load(f)

# Standard kernel hook registrations
kernel_hooks = {
    'PreToolUse': [
        {
            'matcher': 'Edit|Write|Bash',
            'hooks': [{'type': 'command', 'command': 'python .claude/hooks/universal-gate-enforcer.py'}]
        },
        {
            'matcher': 'Agent',
            'hooks': [{'type': 'command', 'command': 'python .claude/hooks/agent-inline-execution-blocker.py'}]
        },
        {
            'matcher': 'Write|Edit',
            'hooks': [{'type': 'command', 'command': 'python .claude/hooks/auto-approve-claude-writes.py'}]
        }
    ],
    'PostToolUse': [
        {
            'matcher': 'Bash',
            'hooks': [{'type': 'command', 'command': 'python .claude/hooks/test-failure-detector.py'}]
        },
        {
            'matcher': 'Edit|Write|Bash',
            'hooks': [{'type': 'command', 'command': 'python .claude/hooks/actions-log-appender.py'}]
        }
    ]
}

settings['hooks'] = kernel_hooks
settings.setdefault('enableAllProjectMcpServers', True)

with open('$SETTINGS', 'w') as f:
    json.dump(settings, f, indent=2)
    f.write('\n')
print('  Settings: merged kernel hooks into existing settings.local.json')
"
else
  # Create new settings with kernel hooks
  python -c "
import json

settings = {
    'permissions': {
        'deny': [
            'Bash(rm -rf *)',
            'Bash(git push --force *)',
            'Bash(git reset --hard *)'
        ],
        'allow': [
            'Read', 'Write', 'Edit', 'Glob', 'Grep',
            'Bash(git *)', 'Bash(ls *)', 'Bash(cat *)',
            'Bash(find *)', 'Bash(grep *)', 'Bash(pwd)',
            'Bash(echo *)', 'Bash(mkdir *)', 'Bash(cp *)'
        ]
    },
    'enableAllProjectMcpServers': True,
    'hooks': {
        'PreToolUse': [
            {
                'matcher': 'Edit|Write|Bash',
                'hooks': [{'type': 'command', 'command': 'python .claude/hooks/universal-gate-enforcer.py'}]
            },
            {
                'matcher': 'Agent',
                'hooks': [{'type': 'command', 'command': 'python .claude/hooks/agent-inline-execution-blocker.py'}]
            },
            {
                'matcher': 'Write|Edit',
                'hooks': [{'type': 'command', 'command': 'python .claude/hooks/auto-approve-claude-writes.py'}]
            }
        ],
        'PostToolUse': [
            {
                'matcher': 'Bash',
                'hooks': [{'type': 'command', 'command': 'python .claude/hooks/test-failure-detector.py'}]
            },
            {
                'matcher': 'Edit|Write|Bash',
                'hooks': [{'type': 'command', 'command': 'python .claude/hooks/actions-log-appender.py'}]
            }
        ]
    }
}

with open('$SETTINGS', 'w') as f:
    json.dump(settings, f, indent=2)
    f.write('\n')
print('  Settings: created new settings.local.json with kernel hooks')
"
fi

echo "=== DONE: $NAME synced ==="
