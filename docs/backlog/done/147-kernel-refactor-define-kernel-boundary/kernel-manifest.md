# Kernel Manifest

## Status
NEW

## What
Create `kernel-manifest.json` in isagawa-kernel root that lists every file that IS the kernel. This is the single source of truth for what gets copied by domain-setup and what gets synced.

## Proposed Manifest Structure

```json
{
  "version": "1.0",
  "description": "Isagawa Kernel — core files manifest",
  "core": {
    "commands": [
      ".claude/commands/kernel/session-start.md",
      ".claude/commands/kernel/anchor.md",
      ".claude/commands/kernel/learn.md",
      ".claude/commands/kernel/complete.md",
      ".claude/commands/kernel/fix.md",
      ".claude/commands/kernel/domain-setup.md",
      ".claude/commands/kernel/reset.md"
    ],
    "hooks": [
      ".claude/hooks/universal-gate-enforcer.py",
      ".claude/hooks/actions-log-appender.py",
      ".claude/hooks/test-failure-detector.py",
      ".claude/hooks/auto-approve-claude-writes.py"
    ],
    "skills": [
      ".claude/skills/kernel-domain-setup/",
      ".claude/skills/autonomous-cycling/"
    ],
    "scripts": [
      "run-task.sh",
      "common.sh"
    ],
    "config": [
      "CLAUDE.md",
      ".claude/settings.local.json"
    ],
    "lessons": [
      ".claude/lessons/lessons.md"
    ]
  }
}
```

## Rules
- If a file is NOT in the manifest, it's NOT kernel
- domain-setup reads this manifest to know what to copy
- Sync script reads this manifest to know what to push to isagawa-kernel
- Extensions can reference kernel files but are not listed in the manifest

## Dependencies
- None — this is the first deliverable
