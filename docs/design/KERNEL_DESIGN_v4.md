# Isagawa Kernel Design v4

**Version:** 4.0
**Date:** 2026-02-10
**Status:** Implementation + Planned Enhancements

---

## Change Summary from v3

| Area | v3 | v4 |
|------|----|----|
| Hook architecture | Single layer | Two-layer (universal + domain) documented |
| Activity count | 5 files hardcoded | Tunable (default 7), tool-call based |
| Anchor mechanism | "Re-read protocol" | Hook forces anchor (re-centering mechanism) |
| Protocol size | Unlimited | 200-line threshold + modular [THEORY] |
| Audit format | JSON | JSONL append-only [PLANNED] |
| Validate command | Every 5 files | TBD - may be redundant |
| reset.md command | Not documented | Documented |
| Context scaling | Not addressed | TBD |

---

## Overview

The Isagawa Kernel is a universal AI management layer that enables AI agents to self-build, self-improve, and operate safety-first.

**Core Insight:** Agents can create their own enforcement infrastructure — not just soft enforcement (protocols) but hard enforcement (hooks).

**What Isagawa Is:** A kernel (operating system) that runs INSIDE an agent (Claude Code, Cursor, Pi). Not a separate agent — it governs how the host agent works.

---

## Architecture

### The Triangle

```
┌─────────────────────────────────────────────────────────────┐
│                      CLAUDE.md                              │
│                      (The Loop)                             │
│                                                             │
│   First action = /kernel/session-start. Always.            │
│                                                             │
│   ~100 lines. The sequence + file reading boundaries.       │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ invokes
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      COMMANDS                               │
│                    (The Details)                            │
│                                                             │
│   /kernel/session-start   ← Check state, resume             │
│   /kernel/domain-setup    ← Create protocol, hooks          │
│   /kernel/anchor          ← Re-read protocol, re-center     │
│   /kernel/validate        ← Check work against protocol     │
│   /kernel/learn           ← Update protocol + hooks         │
│   /kernel/audit           ← Log session actions             │
│   /kernel/complete        ← Final gate                      │
│   /kernel/reset           ← Fresh start (dev tool)          │
│   /kernel/state-schema    ← Reference for state structure   │
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
│   Commands update. Hooks verify. Can't fake.                │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ checked by
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                 SMART GATES (Two-Layer Hooks)               │
│                    (The Enforcement)                        │
│                                                             │
│   Layer 1: Universal Hook (pre-installed)                   │
│            - Checks: session_started, anchored              │
│            - Skips: .claude/* files                         │
│                                                             │
│   Layer 2: Domain Hook (agent-created)                      │
│            - Checks: files_since_validate (5-file limit)    │
│            - Checks: protected paths                        │
│                                                             │
│   Smart = Block + tell agent HOW to fix                     │
└─────────────────────────────────────────────────────────────┘
```

### Why This Works

| Component | Role | Can Be Skipped? |
|-----------|------|-----------------|
| CLAUDE.md | Map (what to invoke) | Agent might ignore |
| Commands | Work (how to do it) | Agent might skip |
| State | Proof (command was invoked) | Can't fake |
| Smart Gates | Walls + Guide (block + fix) | **Can't bypass** |

Commands update state. Hooks check state. No state = blocked + told how to fix.

---

## The Re-Centering Mechanism

**This is the core enforcement pattern.**

```
┌─────────────────────────────────────────────────────────────┐
│                   HOOK FORCES ANCHOR                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Agent tries to write → Hook checks state                  │
│                              │                              │
│                              ▼                              │
│                        State valid?                         │
│                      ┌─────┴─────┐                          │
│                     YES          NO                         │
│                      │            │                         │
│                      ▼            ▼                         │
│                    PASS      BLOCK + FIX                    │
│                                   │                         │
│                                   ▼                         │
│                        "Invoke /kernel/anchor"              │
│                                   │                         │
│                                   ▼                         │
│                          Agent anchors                      │
│                                   │                         │
│                                   ▼                         │
│                         Reads protocol                      │
│                         Updates state                       │
│                         Re-centers                          │
│                                   │                         │
│                                   ▼                         │
│                           Retries write                     │
│                                   │                         │
│                                   ▼                         │
│                              PASS ✓                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**The hook is the bouncer. The anchor is the re-centering.**

Hook doesn't fix — it blocks and tells agent what command to invoke. Agent invokes command, which updates state and re-centers agent on protocol. Then agent retries.

---

## File Structure

```
isagawa-kernel/
├── CLAUDE.md                           ← The Loop (~100 lines)
├── .claude/
│   ├── commands/
│   │   ├── kernel/                     ← Kernel commands (9 files)
│   │   │   ├── session-start.md
│   │   │   ├── domain-setup.md
│   │   │   ├── anchor.md
│   │   │   ├── validate.md
│   │   │   ├── learn.md
│   │   │   ├── audit.md
│   │   │   ├── complete.md
│   │   │   ├── reset.md                ← Dev tool for fresh starts
│   │   │   └── state-schema.md         ← State file reference
│   │   └── [domain]-*.md               ← Domain commands (agent creates)
│   ├── hooks/
│   │   ├── universal-gate-enforcer.py  ← Pre-installed (Layer 1)
│   │   └── [domain]-gate-enforcer.py   ← Agent-created (Layer 2)
│   ├── protocols/                      ← Domain protocols (agent creates)
│   │   └── [domain]-protocol.md
│   ├── state/                          ← AI-controlled state
│   │   ├── session_state.json
│   │   ├── [domain]_workflow.json
│   │   └── [domain]_audit.json
│   └── settings.local.json             ← Pre-wired with hooks
└── docs/
    └── design/                         ← Design docs (not agent-created)
```

---

## The Loop (CLAUDE.md)

```markdown
# Isagawa Kernel

You are a self-building, self-improving, safety-first agent.

## CRITICAL: First Action Rule

When user says "continue" or starts any session:
1. **IMMEDIATELY** invoke /kernel/session-start
2. Do NOT read other files first
3. Do NOT explore the codebase first

**First action = /kernel/session-start. Always.**

## File Reading Boundaries

**Read ONLY:**
- .claude/commands/kernel/*.md - When command is invoked
- .claude/protocols/[domain]-protocol.md - When /kernel/anchor invokes
- .claude/state/*.json - For state checks

**Do NOT read:**
- SESSION.md, DEFECT_LOG.md, docs/*
- Random .md files outside .claude/

## The Loop

[session-start] → [domain-setup if new] → [anchor] → WORK → [validate] → [complete]

On failure: [anchor] → FIX → [learn] → continue

## Smart Gates

Gates block AND tell you how to fix. No state = blocked + told how to fix.

## Key Principles

- **Self-Build**: Create your own enforcement
- **Self-Improve**: Update protocol + hooks after every failure
- **Safety-First**: Smart gates block + guide, can't be bypassed
- **HITL**: Human checkpoints throughout work
```

---

## Two-Layer Hook Architecture

### Layer 1: Universal Hook (Pre-installed)

**File:** `.claude/hooks/universal-gate-enforcer.py`

**What it checks:**
- `session_started` = true (from session_state.json)
- `anchored` = true (from [domain]_workflow.json)

**What it skips:**
- All files in `.claude/*` (kernel infrastructure)

**When it runs:**
- On every `Write` and `Edit` tool call

```python
# Simplified logic
if tool_name not in ('Write', 'Edit'):
    exit(0)  # Only enforce writes

if file_path in '.claude/':
    exit(0)  # Skip kernel files

if not session_state['session_started']:
    smart_block("session not started", "/kernel/session-start")

if not domain_state['anchored']:
    smart_block("anchor not invoked", "/kernel/anchor")

exit(0)  # Pass
```

### Layer 2: Domain Hook (Agent-created)

**File:** `.claude/hooks/[domain]-gate-enforcer.py`

**What it checks:**
- `files_since_validate` < 5 (5-file limit)
- Protected paths (domain-specific)

**Created by:** `/kernel/domain-setup`

**Requires restart:** Yes (hooks load at startup)

```python
# Simplified logic
if files_since_validate >= 5:
    smart_block("5 files since validate", "/kernel/validate")

for prefix, required_key in PROTECTED_PATHS.items():
    if prefix in file_path and not state[required_key]:
        smart_block(f"{required_key} not set", "/kernel/anchor")

exit(0)  # Pass
```

### Hook Chain in settings.local.json

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {"type": "command", "command": "python .claude/hooks/universal-gate-enforcer.py"},
          {"type": "command", "command": "python .claude/hooks/[domain]-gate-enforcer.py"}
        ]
      }
    ]
  }
}
```

Both hooks run in sequence. First failure blocks.

---

## Commands Reference

### /kernel/session-start

**Purpose:** Check state and determine next step.

**Flow:**
- No state → `/kernel/domain-setup`
- State exists, no domain → `/kernel/domain-setup`
- State exists with domain → `/kernel/anchor`
- `needs_restart: true` → Clear flag, resume from `resume_after_restart`

**Updates:** `session_state.json`

### /kernel/domain-setup

**Purpose:** Create protocol and enforcement for a new domain.

**Creates:**
- `.claude/protocols/[domain]-protocol.md` (protocol)
- `.claude/state/[domain]_workflow.json` (state)
- `.claude/hooks/[domain]-gate-enforcer.py` (hook)
- `.claude/commands/[domain]-*.md` (optional domain commands)

**Sets:** `needs_restart: true` (hooks require restart)

**HITL:** Requires restart before continuing.

### /kernel/anchor

**Purpose:** Re-read protocol and re-center.

**This is the core re-centering mechanism:**
1. Read protocol (ONLY the protocol file)
2. Extract key patterns, anti-patterns, lessons
3. Identify current task
4. Update state: `anchored: true`, `files_since_validate: 0`

**When to invoke:**
- Before ANY code work
- After any failure (before fixing)
- When resuming from restart
- When hook blocks

### /kernel/validate

**Purpose:** Check work against protocol.

**Flow:**
1. Read protocol
2. List files created/modified since last validate
3. Check each file against patterns/anti-patterns
4. Update state: `validated: true`, `files_since_validate: 0`

**When to invoke:**
- Every 5 files (enforced by domain hook)
- Before running tests
- Before completion

**[TBD]:** May be redundant if anchor + 5-file blocking is sufficient.

### /kernel/learn

**Purpose:** Update protocol AND hooks after fixing failure.

**Two-tier learning:**
1. **Soft enforcement:** Add to protocol (knowledge)
2. **Hard enforcement:** Add to hooks (prevention)

**Updates:**
- Protocol: New anti-pattern, quality gate, lesson learned
- Hook: New protected path (if enforceable)
- State: `lesson_recorded: true`, `lessons_count: N`

### /kernel/audit

**Purpose:** Log all session actions.

**Current format:** JSON file at `.claude/state/[domain]_audit.json`

**[PLANNED]:** JSONL append-only format for incremental logging.

### /kernel/complete

**Purpose:** Final gate before marking work done.

**Flow:**
1. Invoke `/kernel/validate` (final check)
2. Invoke `/kernel/audit` (log session)
3. Verify all gates passed
4. Generate completion report
5. HITL checkpoint

### /kernel/reset

**Purpose:** Reset repo for fresh kernel test (dev tool).

**Removes:**
- `.claude/state/*`
- `.claude/protocols/*`
- Domain hooks (keeps universal)
- Domain commands (keeps kernel/*)

**Keeps:**
- `.claude/commands/kernel/*`
- `.claude/hooks/universal-gate-enforcer.py`
- `CLAUDE.md`

### /kernel/state-schema

**Purpose:** Reference for state file structure.

**Not a command** — documentation of state files.

---

## State Files

### session_state.json

```json
{
  "session_started": true,
  "domain": "[domain]",
  "timestamp": "ISO-8601",
  "needs_restart": false,
  "resume_after_restart": null
}
```

### [domain]_workflow.json

```json
{
  "domain": "[domain]",
  "setup_complete": true,
  "protocol_created": true,
  "anchored": false,
  "anchor_timestamp": null,
  "validated": false,
  "validate_timestamp": null,
  "files_since_validate": 0,
  "files_checked": [],
  "lesson_recorded": false,
  "lessons_count": 0,
  "last_lesson": null,
  "hooks_updated": false,
  "audit_complete": false,
  "timestamp": "ISO-8601"
}
```

### [domain]_audit.json

```json
{
  "session_id": "ISO-8601",
  "domain": "[domain]",
  "events": [
    {"timestamp": "...", "type": "command_invoked", "command": "...", "result": "pass"},
    {"timestamp": "...", "type": "file_created", "path": "..."},
    {"timestamp": "...", "type": "gate_blocked", "gate": "...", "reason": "..."},
    {"timestamp": "...", "type": "lesson_learned", "issue": "..."}
  ],
  "summary": {
    "files_created": 0,
    "files_modified": 0,
    "gates_passed": 0,
    "gates_blocked": 0,
    "lessons_learned": 0
  }
}
```

---

## Learning Cascade

```
┌─────────────────────────────────────────────────────────────┐
│                     FAILURE DETECTED                        │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      /kernel/anchor                         │
│                  (re-read protocol)                         │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                        DIAGNOSE                             │
│            (what failed, why, root cause)                   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                          FIX                                │
│               (implement solution)                          │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                      /kernel/learn                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   SOFT ENFORCEMENT (Protocol)                               │
│   ├── Add to "Lessons Learned" section                      │
│   ├── Add new anti-pattern                                  │
│   └── Add new quality gate                                  │
│                                                             │
│   HARD ENFORCEMENT (Hooks)                                  │
│   ├── Add protected path (if enforceable)                   │
│   └── Block future violations automatically                 │
│                                                             │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                    HITL CHECKPOINT                          │
│           "Fixed X, learned Y. Continue?"                   │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     KERNEL SMARTER                          │
│                                                             │
│   Next /kernel/anchor reads updated protocol                │
│   Next write attempt hits updated hooks                     │
│   Same mistake now impossible                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## HITL Checkpoints

| Checkpoint | When | Command |
|------------|------|---------|
| Session Start | After session-start | `/kernel/session-start` |
| Setup Complete | After domain-setup | `/kernel/domain-setup` |
| Anchored | After anchor | `/kernel/anchor` |
| Progress | Every 5 files | `/kernel/validate` |
| After Fix | After learning | `/kernel/learn` |
| Complete | Before done | `/kernel/complete` |

**Rule:** Wait for user approval before proceeding.

---

## Planned Enhancements

### [THEORY] Activity Count Tuning

**Current:** 5 files (hardcoded in domain hooks)

**Planned:** Tunable activity count, default 7

**What counts as activity:**
- `write` = +1
- `edit` = +1
- `bash` = +1
- `read` = 0
- `ls/cat/grep` = 0

**Implementation:** Parameter in domain-setup or protocol.

### [THEORY] Modular Protocols

**Problem:** Large protocols (200+ lines) may exceed context or lose focus.

**Solution:** Index + sub-modules pattern

```
.claude/protocols/
├── qa-protocol.md              ← Index (~50 lines)
│   └── References:
│       - architecture.md
│       - anti-patterns.md
│       - lessons.md
├── qa-architecture.md          ← Sub-module
├── qa-anti-patterns.md         ← Sub-module
└── qa-lessons.md               ← Sub-module
```

**Threshold:** 200 lines before modularization

**Enforcement:** In `/kernel/anchor` (check protocol size, prompt to modularize)

**Not in hook:** Protocol size is knowledge management, not hard gate.

### [PLANNED] JSONL Audit Format

**Current:** JSON file (overwrite on each audit)

**Planned:** JSONL append-only format

```jsonl
{"timestamp": "...", "event": "session_started", ...}
{"timestamp": "...", "event": "command_invoked", "command": "/kernel/anchor", ...}
{"timestamp": "...", "event": "file_created", "path": "...", ...}
```

**Benefits:**
- Append-only (no read-modify-write)
- Streaming compatible
- Full session history

### [TBD] Validate Command Necessity

**Question:** Is `/kernel/validate` redundant?

**Current flow:**
1. Domain hook blocks at 5 files → forces `/kernel/validate`
2. Validate checks work against protocol → resets counter

**Alternative flow:**
1. Domain hook blocks at 5 files → forces `/kernel/anchor`
2. Anchor re-reads protocol → resets counter
3. No separate validate command needed

**Decision:** TBD after more testing.

### [TBD] Context Window Scaling

**Problem:** As protocols grow, they consume more context.

**Potential solutions:**
1. Modular protocols (see above)
2. Summarization on anchor
3. Sliding window of lessons

**Decision:** TBD after protocol growth data.

### [FUTURE] HITL Levels

**Status:** Post-MVP

**Levels:**
- `strict` - Every checkpoint (dev/testing)
- `normal` - Failures + completion only
- `minimal` - Completion only

**Implementation:** Set in protocol, checked by commands.

---

## Session Persistence

### The Problem

Hooks are loaded at Claude Code startup. If agent creates hooks mid-session, they don't take effect until restart.

### The Solution

1. **Pre-installed universal hook** - Always active
2. **State-based resume** - Agent writes state, reads on next session
3. **Restart prompt** - When new hooks created, prompt user to restart

### Flow

```
Session 1:
  /kernel/domain-setup creates domain hook
  Sets needs_restart = true, resume_after_restart = "anchor"
  "Restart Claude Code. Say 'continue' after."

[User restarts]

Session 2:
  /kernel/session-start reads state
  Clears needs_restart
  Resumes from /kernel/anchor
  Domain hook now active
```

---

## Key Principles

1. **Self-Build**: Agent creates its own enforcement (protocol, hooks)
2. **Self-Improve**: Agent updates protocol + hooks after failures
3. **Safety-First**: Smart gates block + guide, can't be bypassed
4. **Hook Forces Anchor**: Hook is the re-centering mechanism
5. **Two-Tier Learning**: Soft (protocol) + Hard (hooks)
6. **HITL**: Human checkpoints throughout work
7. **Session Persistence**: State survives restart
8. **Minimal Core**: CLAUDE.md is just the loop + boundaries

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-07 | Commands only, never invoked |
| v2 | 2026-02-07 | Smart gates, HITL, learn, audit |
| v3 | 2026-02-08 | Triangle architecture, state schema |
| v4 | 2026-02-10 | Two-layer hooks documented, re-centering mechanism, activity count tuning, modular protocols [THEORY], JSONL audit [PLANNED], validate TBD |

---

## Implementation Status

| Component | Status | Notes |
|-----------|--------|-------|
| CLAUDE.md | ✅ Implemented | ~100 lines with boundaries |
| 9 Kernel Commands | ✅ Implemented | All functional |
| Universal Hook | ✅ Implemented | session_started + anchored |
| Domain Hook Pattern | ✅ Implemented | 5-file + protected paths |
| State Files | ✅ Implemented | 3 file types |
| Learning Cascade | ✅ Implemented | Soft + hard enforcement |
| HITL Checkpoints | ✅ Implemented | In all commands |
| Activity Count Tuning | ❌ Not Implemented | Currently hardcoded 5 |
| Modular Protocols | ❌ Not Implemented | Theory only |
| JSONL Audit | ❌ Not Implemented | Currently JSON |
| Validate Necessity | ⚠️ TBD | May be redundant |
| Context Scaling | ❌ Not Designed | Future consideration |
| HITL Levels | ❌ Not Implemented | Post-MVP |

---

*End of Design*
