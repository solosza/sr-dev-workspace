# Isagawa Kernel Design v2

**Version:** 2.0
**Date:** 2026-02-07
**Status:** Draft

---

## Overview

The Isagawa Kernel is a universal AI management layer that teaches AI agents to self-build, self-improve, and operate safety-first.

**Core Insight:** Agents can create their own enforcement infrastructure - not just soft enforcement (commands) but hard enforcement (hooks).

---

## Architecture

### The Triangle

```
┌─────────────────────────────────────────────────────────────┐
│                      CLAUDE.md                              │
│                      (The Loop)                             │
│                                                             │
│   "invoke /kernel/anchor" → "invoke /kernel/validate" → ... │
│                                                             │
│   ~50 lines. Just the sequence. Points to commands.         │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ invokes
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      COMMANDS                               │
│                    (The Details)                            │
│                                                             │
│   /kernel/session-start.md   ← Check state, resume          │
│   /kernel/domain-setup.md    ← Create protocol, hooks       │
│   /kernel/anchor.md          ← Re-read protocol             │
│   /kernel/validate.md        ← Check work (smart gate)      │
│   /kernel/learn.md           ← Update protocol + hooks      │
│   /kernel/audit.md           ← Log session actions          │
│   /kernel/complete.md        ← Final gate                   │
│                                                             │
│   Each command updates STATE when invoked.                  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ updates
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                        STATE                                │
│                   (Proof of Work)                           │
│                                                             │
│   .claude/state/session_state.json                          │
│   .claude/state/[domain]_workflow.json                      │
│   .claude/state/[domain]_audit.json                         │
│                                                             │
│   Extensible metadata per domain.                           │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ checked by
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    SMART GATES (Hooks)                      │
│                    (The Enforcement)                        │
│                                                             │
│   PreToolUse: Check state, BLOCK + provide fix data         │
│   PostToolUse: Audit all actions                            │
│                                                             │
│   Smart = Don't just block, tell agent HOW to fix.          │
└─────────────────────────────────────────────────────────────┘
```

### Why This Works

| Component | Role | Can Be Skipped? |
|-----------|------|-----------------|
| CLAUDE.md | Map (what to invoke) | Agent might ignore |
| Commands | Work (how to do it) | Agent might skip |
| State | Proof (command was invoked) | Can't fake |
| Smart Gates | Walls + Guide (block + fix data) | **Can't bypass** |

Commands update state. Gates check state. No state = blocked + told how to fix.

---

## File Structure

```
isagawa-kernel/
├── CLAUDE.md                           ← The Loop (~50 lines)
├── .claude/
│   ├── commands/
│   │   └── kernel/                     ← Kernel commands
│   │       ├── session-start.md
│   │       ├── domain-setup.md
│   │       ├── anchor.md
│   │       ├── validate.md
│   │       ├── learn.md
│   │       ├── audit.md
│   │       ├── complete.md
│   │       └── state-schema.md
│   ├── hooks/
│   │   └── universal-gate-enforcer.py  ← Pre-installed smart gate
│   ├── state/                          ← AI-controlled state
│   │   ├── session_state.json
│   │   ├── [domain]_workflow.json
│   │   └── [domain]_audit.json
│   └── settings.local.json             ← Pre-wired with hooks
└── docs/
    └── protocols/                      ← Domain protocols (agent creates)
```

---

## The Loop

CLAUDE.md contains only the loop:

```markdown
# Isagawa Kernel

You are a self-building, self-improving, safety-first agent.

## The Loop

1. `/kernel/session-start` ← Always first (check state, resume)
2. `/kernel/domain-setup` ← If new domain (create enforcement)
3. `/kernel/anchor` ← Before any work (re-read protocol)
4. WORK
   - `/kernel/validate` every 5 files (smart gate)
   - Report progress
5. ON FAILURE:
   - `/kernel/anchor` → FIX → `/kernel/learn`
   - Report progress
6. `/kernel/audit` ← Log what was done
7. `/kernel/complete` ← Before saying done (final gate + HITL)

Commands contain the details. Smart gates ensure you can't skip.
```

That's it. ~50 lines. The rest lives in commands.

---

## Autonomy Mode

This kernel operates in pure autonomy mode. No approval checkpoints - work proceeds automatically.

### Reporting

Instead of asking for approval, this kernel:
- Reports what was created after setup
- Reports progress periodically
- Reports what was learned after fixes
- Reports completion with audit summary

### Format

```
REPORT: [what was done]

[Details]

Proceeding with next step.
```

---

## Smart Gates

### What Makes Gates "Smart"

Traditional gates just block:
```
BLOCKED: Gate not passed.
```

Smart gates block AND provide fix data:
```
BLOCKED: anchor not invoked.

TO FIX:
1. Invoke /kernel/anchor
2. This will read protocol and update state
3. Then retry your write

STATE NEEDED: {"anchored": true}
```

### Smart Gate Pattern

```python
def check_gate(required_state_key):
    if state_missing(required_state_key):
        return {
            "status": "blocked",
            "missing": required_state_key,
            "fix": f"Invoke /kernel/{required_state_key} first",
            "command": f"/kernel/{required_state_key}",
            "state_needed": {required_state_key: True}
        }
    return {"status": "pass"}
```

### Gate Response to Agent

When blocked, hook outputs:
```
BLOCKED: [what's missing]

FIX:
1. [exact command to invoke]
2. [what it will do]
3. [then retry]

Command: /kernel/[command]
```

Agent reads this, invokes command, retries. Loop closes.

---

## Validate

### Purpose

Check work against protocol. Catch issues before they accumulate.

### When

- Every 5 files created/modified
- Before tests
- Before completion

### What It Checks

```markdown
## /kernel/validate

1. Read protocol: `docs/protocols/[domain]-protocol.md`

2. List files created/modified since last validate

3. Check each file:
   - Correct location per protocol?
   - Correct naming per protocol?
   - Follows patterns per protocol?
   - No anti-patterns per protocol?
   - Avoids lessons learned issues?

4. Update state:
   ```json
   {
     "validated": true,
     "files_checked": ["file1.ts", "file2.ts"],
     "issues_found": 0,
     "timestamp": "..."
   }
   ```

5. Report:
   - PASS: "Validated N files. All pass."
   - FAIL: "Issues found: [list]. Fixing before proceeding."

6. If FAIL: Fix issues, then re-validate
```

### Smart Gate Integration

After validate updates state, hooks allow next batch of writes.
If validate not invoked after 5 files → hook blocks → tells agent to validate.

---

## Learn

### Purpose

Update protocol AND hooks after fixing any failure. Make the same mistake impossible.

### When

- After fixing any test failure
- After fixing any error
- After discovering an anti-pattern

### What It Does

```markdown
## /kernel/learn

1. Identify what failed:
   - Error message
   - Root cause
   - How it was fixed

2. Update protocol (`docs/protocols/[domain]-protocol.md`):
   ```markdown
   ## Lessons Learned

   ### [Date] [Issue Name]
   - **Issue:** What happened
   - **Root Cause:** Why it happened
   - **Fix:** How it was resolved
   - **Anti-Pattern Added:** What to avoid
   - **Quality Gate Added:** What to check
   ```

3. Update hooks if enforceable:
   ```python
   # If this can be automatically prevented, add to hook
   PROTECTED_PATHS['new/path/'] = 'new_state_key'
   ```

4. Update state:
   ```json
   {
     "lesson_recorded": true,
     "lessons_count": N,
     "last_lesson": "Selector specificity",
     "hooks_updated": true
   }
   ```

5. Report:
   - What was added to protocol
   - What was added to hooks (if any)
   - New commands created (if recurring pattern)
```

### The Learning Loop

```
FAILURE
    ↓
/kernel/anchor (re-read protocol)
    ↓
DIAGNOSE (what failed, why)
    ↓
FIX (implement solution)
    ↓
/kernel/learn
├── Update protocol (knowledge)
├── Update hooks (enforcement)
└── Update state (proof)
    ↓
REPORT progress ("Fixed X, learned Y. Continue?")
    ↓
CONTINUE
```

---

## Audit

### Purpose

Log all session actions for traceability and debugging.

### What Gets Logged

```json
{
  "session_id": "2026-02-07T14:30:00Z",
  "domain": "qa",
  "events": [
    {
      "timestamp": "...",
      "type": "command_invoked",
      "command": "/kernel/anchor",
      "result": "pass"
    },
    {
      "timestamp": "...",
      "type": "file_created",
      "path": "tests/login.spec.ts"
    },
    {
      "timestamp": "...",
      "type": "gate_blocked",
      "gate": "validate",
      "reason": "5 files since last validate"
    },
    {
      "timestamp": "...",
      "type": "lesson_learned",
      "issue": "Selector specificity",
      "protocol_updated": true,
      "hooks_updated": true
    }
  ]
}
```

### Two Audit Mechanisms

1. **Command-based** (`/kernel/audit`):
   - Agent invokes to log summary
   - Updates state with audit complete

2. **Hook-based** (automatic):
   - PostToolUse hook logs every action
   - No agent invocation needed
   - Complete audit trail

### Audit State

```json
{
  "audit_complete": true,
  "files_created": 12,
  "files_modified": 3,
  "gates_passed": 5,
  "gates_blocked": 2,
  "lessons_learned": 1,
  "hitl_checkpoints": 4
}
```

---

## State Schema

### Core Fields (Required)

```json
{
  "domain": "qa",
  "task": "Build QA framework for ParaBank",
  "current_step": "work",
  "gates_passed": ["protocol", "commands", "hooks", "anchor"],
  "needs_restart": false,
  "resume_after_restart": null,
  "last_updated": "2026-02-07T14:30:00Z"
}
```

### Gate State (Updated by Commands)

```json
{
  "anchored": true,
  "anchor_timestamp": "...",

  "validated": true,
  "files_since_validate": 0,
  "last_validate_timestamp": "...",

  "lesson_recorded": false,
  "lessons_count": 0,

  "audit_complete": false
}
```

### Metadata (Domain-Specific, Extensible)

```json
{
  "domain": "qa",
  "metadata": {
    "target_url": "https://parabank.parasoft.com",
    "framework": "playwright",
    "language": "typescript",
    "pages_created": ["LoginPage", "AccountsPage"],
    "tests_created": ["test_login.spec.ts"],
    "selectors_validated": true,
    "lessons_learned": 2
  }
}
```

Agent defines what metadata matters for each domain.

---

## Session Persistence

### The Problem

Hooks are loaded at Claude Code startup. If agent creates hooks mid-session, they don't take effect until restart.

### The Solution

1. **Pre-installed universal hook** - Ships with kernel, always active
2. **State-based resume** - Agent writes state, reads on next session
3. **Restart prompt** - When new hooks created, prompt user to restart

### Flow

```
Session 1:
  Agent creates domain-specific hooks
  Agent writes state: needs_restart = true
  Agent: "Restart Claude Code to activate hooks. Say 'continue' after."

[User restarts]

Session 2:
  Universal hook is active (pre-installed)
  Domain hooks are now active (just created)
  Agent reads state: needs_restart was true
  Agent resumes from resume_after_restart step
```

---

## Enforcement Layers

### Layer 1: Protocol (Knowledge)

```
docs/protocols/[domain]-protocol.md
```

- Domain rules, patterns, anti-patterns
- Quality gates
- Lessons learned (updated by /kernel/learn)

### Layer 2: Commands (Soft Enforcement)

```
.claude/commands/kernel/*.md
.claude/commands/[domain]-*.md
```

- Kernel commands: session-start, domain-setup, anchor, validate, learn, audit, complete
- Domain commands: Agent creates per domain
- Commands update state when invoked

### Layer 3: Smart Gates / Hooks (Hard Enforcement)

```
.claude/hooks/universal-gate-enforcer.py
.claude/hooks/[domain]-gate-enforcer.py
.claude/settings.local.json
```

- PreToolUse: Block + provide fix data
- Automatic - runs on every tool call
- Smart - tells agent how to fix, not just "blocked"

---

## Autonomous Workflow

No approval checkpoints. Work proceeds automatically.

| Step | Action | Report |
|------|--------|--------|
| Setup | Create enforcement | "Created protocol, commands, hooks. Proceeding." |
| Work | Build solution | Progress reports every 5 files |
| Failure | Fix + learn | "Fixed X, learned Y. Continuing." |
| Complete | Final audit | "Done. Audit: N files, M lessons."  |

Safety comes from smart gates (can't bypass) and self-learning (mistakes become enforcement).

---

## Self-Learning Loop

```
FAILURE DETECTED
      ↓
/kernel/anchor (re-read protocol)
      ↓
DIAGNOSE (identify root cause)
      ↓
FIX (implement solution)
      ↓
/kernel/learn
├── Update protocol with lesson
├── Update hooks if enforceable
├── Create new command if recurring
└── Update state
      ↓
REPORT progress ("Fixed X, learned Y. Continue?")
      ↓
CONTINUE
```

The kernel evolves:
- Lessons become protocol entries
- Protocol entries become gate checks
- Gate checks become hook enforcement

---

## Key Principles

1. **Self-Build**: Agent creates its own enforcement (protocol, commands, hooks)
2. **Self-Improve**: Agent updates protocol + hooks after failures
3. **Safety-First**: Smart gates block + guide, can't be bypassed
4. **Autonomy**: Report after, don't ask before
5. **Validate**: Check work against protocol every 5 files
6. **Learn**: Every failure updates protocol AND hooks
7. **Audit**: Log everything for traceability
8. **Extensible State**: Domain-specific metadata
9. **Session Persistence**: State survives restart
10. **Minimal Core**: CLAUDE.md is just the loop

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-07 | Commands only, never invoked |
| v2 | 2026-02-07 | Strict instructions, still soft |
| v3 | 2026-02-07 | HITL + self-learning |
| v4 | 2026-02-07 | Self-built hooks |
| v2 Design | 2026-02-07 | Modular architecture, smart gates, HITL, validate, learn, audit |

---

## Next Steps

1. Implement modular CLAUDE.md (~50 lines)
2. Create /kernel/* command files
3. Create universal-gate-enforcer.py (pre-installed, smart)
4. Test session persistence flow
5. Test with QA domain prompt
