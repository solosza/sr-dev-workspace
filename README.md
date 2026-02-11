# Isagawa Kernel

**Self-building, self-improving, safety-first AI agent framework.**

> **Dogfood Workspace**: This is the sr_dev kernel's own development environment — the kernel builds and improves itself here.

## Core Philosophy

- **AI Builds**: Agent creates its own protocols, hooks, and commands
- **AI Improves**: Every failure triggers learning; updates both protocol and hooks
- **Safety First**: Smart gates block and tell HOW to fix — can't be bypassed

## The Loop

```
session-start → anchor → WORK → complete
                   ↑         ↓
                   └── every N actions
                             ↓
                   failure? → fix → learn
```

## Components

| Component | Purpose |
|-----------|---------|
| `CLAUDE.md` | Entry point — first action rules |
| `.claude/protocols/` | Domain-specific rules and patterns |
| `.claude/hooks/` | Smart gate enforcers (hard blocks) |
| `.claude/commands/kernel/` | Workflow commands |
| `.claude/state/` | Runtime state (gitignored) |

## Commands

| Command | Purpose |
|---------|---------|
| `/kernel/session-start` | Check state, resume if needed |
| `/kernel/anchor` | Re-read protocol, check work, reset counter |
| `/kernel/learn` | Record lesson after failure/fix |
| `/kernel/fix` | Impact assessment before any fix |
| `/kernel/complete` | Final gate before done |

## Quick Start

1. Open Claude Code in this directory
2. Give any task or say "continue"
3. Agent invokes `/kernel/session-start` automatically
4. Work proceeds with automatic safety gates

## How Safety Gates Work

```
Agent writes code
    ↓
Hook increments counter
    ↓
At limit → BLOCKED
    ↓
"Invoke /kernel/anchor to continue"
    ↓
Agent re-centers on protocol
    ↓
Counter resets, work continues
```

## License

MIT
