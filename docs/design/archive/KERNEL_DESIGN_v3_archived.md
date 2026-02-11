# Isagawa Kernel Design v3 (Minimal)

**Version:** 3.0
**Date:** 2026-02-07
**Status:** Validated POC

---

## Executive Summary

The Isagawa Kernel is the **AI Management Layer** — a minimal system that governs how AI agents execute work through self-built enforcement.

**Three Principles:**
- **Self-Build** — Agent creates its own protocol, commands, hooks
- **Self-Improve** — Failures become lessons, lessons become enforcement
- **Safety-First** — Hook blocks until state is correct, can't be bypassed

**Three Components:**
- `CLAUDE.md` — The brain (loop instructions)
- `commands/` — The interface (slash commands)
- `hooks/` — The enforcement (gate enforcer)

---

## The Core Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                         THE LOOP                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│    ┌──────────────┐                                              │
│    │ USER PROMPT  │                                              │
│    └──────┬───────┘                                              │
│           │                                                      │
│           ▼                                                      │
│    ┌──────────────┐                                              │
│    │session-start │ ◄─── First action. ALWAYS.                   │
│    └──────┬───────┘                                              │
│           │                                                      │
│           ▼                                                      │
│    ┌──────────────┐      ┌──────────────┐                        │
│    │ State exists?│──NO─►│ domain-setup │                        │
│    └──────┬───────┘      └──────┬───────┘                        │
│           │YES                  │                                │
│           │◄────────────────────┘                                │
│           ▼                                                      │
│    ┌──────────────┐                                              │
│    │    anchor    │ ◄─── Re-read protocol. Center.               │
│    └──────┬───────┘                                              │
│           │                                                      │
│           ▼                                                      │
│    ╔══════════════╗                                              │
│    ║     WORK     ║ ◄─── Actual domain work                      │
│    ╚══════╤═══════╝                                              │
│           │                                                      │
│           ▼                                                      │
│    ┌──────────────┐      ┌──────────────┐                        │
│    │   Failure?   │──YES─►│    anchor   │                        │
│    └──────┬───────┘      └──────┬───────┘                        │
│           │NO                   │                                │
│           │                     ▼                                │
│           │              ┌──────────────┐                        │
│           │              │     FIX      │                        │
│           │              └──────┬───────┘                        │
│           │                     │                                │
│           │                     ▼                                │
│           │              ┌──────────────┐                        │
│           │              │    learn     │ ◄─── Update protocol   │
│           │              └──────┬───────┘                        │
│           │                     │                                │
│           │◄────────────────────┘ (back to WORK)                 │
│           │                                                      │
│           ▼                                                      │
│    ┌──────────────┐                                              │
│    │   complete   │ ◄─── Final gate                              │
│    └──────────────┘                                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Simplified:**
```
session-start → anchor → WORK → complete
                   ↓
         failure? → anchor → fix → learn → WORK
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     ISAGAWA KERNEL                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐            │
│  │  CLAUDE.md  │   │  commands/  │   │   hooks/    │            │
│  │   (Brain)   │   │ (Interface) │   │(Enforcement)│            │
│  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘            │
│         │                 │                 │                    │
│         │    Instructs    │    Invokes      │    Blocks          │
│         ▼                 ▼                 ▼                    │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                        AGENT                             │    │
│  └─────────────────────────────────────────────────────────┘    │
│         │                 │                 ▲                    │
│         │    Creates      │    Updates      │    Checks          │
│         ▼                 ▼                 │                    │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐            │
│  │  protocols/ │   │   state/    │   │  PreToolUse │            │
│  │   (Rules)   │   │  (Memory)   │   │   (Gate)    │            │
│  └─────────────┘   └─────────────┘   └─────────────┘            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. CLAUDE.md (The Brain)

The kernel instructions. Teaches the agent the loop.

```markdown
# Isagawa Kernel (Minimal)

You are a self-building, self-improving, safety-first agent.

## CRITICAL: First Action Rule

When user gives any task or says "continue":
1. **IMMEDIATELY** invoke `/kernel/session-start`
2. Do NOT read files first
3. Do NOT explore the codebase first
4. Do NOT run any commands first

**First action = /kernel/session-start. Always.**
```

**Key insight:** The First Action Rule forces the loop to start. Without it, agents wander.

---

### 2. Commands (The Interface)

```
.claude/commands/kernel/
├── session-start.md   ← Check state, resume or setup
├── domain-setup.md    ← Create protocol, commands, hooks
├── anchor.md          ← Re-read protocol before work
├── learn.md           ← Update protocol + hooks after fix
└── complete.md        ← Final gate before done
```

**Command flow:**

| Command | Input State | Output State | Next |
|---------|-------------|--------------|------|
| session-start | none | `session_started: true` | domain-setup or anchor |
| domain-setup | session_started | `protocol_created: true` | anchor |
| anchor | protocol_created | `anchored: true` | WORK |
| learn | after fix | `lesson_recorded: true` | WORK |
| complete | anchored | `complete: true` | DONE |

---

### 3. Hooks (The Enforcement)

```python
# universal-gate-enforcer.py

# Fires on every Write/Edit
# Checks state
# Blocks if missing
# Tells agent how to fix

if not session_state.get('session_started'):
    smart_block(
        missing="Session not started",
        fix_command="/kernel/session-start",
        fix_description="This initializes the session"
    )

if not domain_state.get('anchored'):
    smart_block(
        missing="Protocol not anchored",
        fix_command="/kernel/anchor",
        fix_description="This reads protocol and updates state"
    )
```

**Smart Gate Pattern:**

```
┌─────────────────────────────────────────┐
│             SMART GATE                   │
├─────────────────────────────────────────┤
│                                          │
│  BLOCKED: Protocol not anchored.         │
│                                          │
│  FIX:                                    │
│  1. Invoke /kernel/anchor                │
│  2. This reads protocol and updates state│
│  3. Then retry your write                │
│                                          │
│  Command: /kernel/anchor                 │
│                                          │
└─────────────────────────────────────────┘
```

Gates don't just block. They tell you how to fix.

---

## State Management

```
.claude/state/
├── session_state.json       ← Session-level state
└── {domain}_workflow.json   ← Domain-level state
```

**Session state:**
```json
{
  "session_started": true,
  "domain": "playwright",
  "timestamp": "2026-02-07T00:00:00Z"
}
```

**Domain state:**
```json
{
  "protocol_created": true,
  "anchored": true,
  "anchor_timestamp": "2026-02-07T00:01:00Z",
  "complete": false
}
```

**State flow:**

```
session_started ──► protocol_created ──► anchored ──► complete
      │                    │                 │            │
      ▼                    ▼                 ▼            ▼
  Can setup           Can anchor         Can write     Can finish
```

---

## Self-Build

When agent enters a new domain, it creates its own enforcement:

```
┌─────────────────────────────────────────────────────────────────┐
│                      DOMAIN-SETUP                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  INPUT: Domain description ("Playwright test automation")       │
│                                                                  │
│  CREATES:                                                        │
│                                                                  │
│  1. Protocol                                                     │
│     └── docs/protocols/{domain}-protocol.md                      │
│         - Architecture patterns                                  │
│         - Naming conventions                                     │
│         - Anti-patterns                                          │
│         - Quality gates                                          │
│         - Lessons learned (empty)                                │
│                                                                  │
│  2. Domain Commands                                              │
│     └── .claude/commands/{domain}-*.md                           │
│         - {domain}-anchor.md                                     │
│         - {domain}-validate.md                                   │
│         - {domain}-learn.md                                      │
│                                                                  │
│  3. Domain Hook                                                  │
│     └── .claude/hooks/{domain}-gate-enforcer.py                  │
│         - Domain-specific enforcement                            │
│         - Added to settings.local.json                           │
│                                                                  │
│  4. State                                                        │
│     └── .claude/state/{domain}_workflow.json                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Agent builds its own jail.** Then operates within it.

---

## Self-Improve

When a failure occurs, the agent must learn:

```
┌─────────────────────────────────────────────────────────────────┐
│                        /kernel/learn                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. IDENTIFY                                                     │
│     - What failed?                                               │
│     - Root cause?                                                │
│     - How was it fixed?                                          │
│                                                                  │
│  2. UPDATE PROTOCOL (Soft Enforcement)                           │
│     - Add to "Lessons Learned" section                           │
│     - Add new anti-pattern                                       │
│     - Add new quality gate                                       │
│                                                                  │
│  3. UPDATE HOOK (Hard Enforcement)                               │
│     - If failure is enforceable, add to hook                     │
│     - Same mistake becomes impossible                            │
│                                                                  │
│  4. CREATE COMMAND (If Recurring)                                │
│     - Pattern that needs checking → new command                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Learning cascade:**

```
Failure
   │
   ▼
Protocol updated (soft) ──► Agent remembers next anchor
   │
   ▼
Hook updated (hard) ──► Agent physically can't repeat mistake
```

---

## Safety-First

The hook is the safety layer:

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAFETY ENFORCEMENT                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│                      Agent wants to Write                        │
│                             │                                    │
│                             ▼                                    │
│                    ┌─────────────────┐                           │
│                    │   Hook Fires    │                           │
│                    │  (PreToolUse)   │                           │
│                    └────────┬────────┘                           │
│                             │                                    │
│              ┌──────────────┼──────────────┐                     │
│              │              │              │                     │
│              ▼              ▼              ▼                     │
│        ┌──────────┐   ┌──────────┐   ┌──────────┐               │
│        │ Session  │   │ Anchored │   │ Domain   │               │
│        │ Started? │   │    ?     │   │ Gates?   │               │
│        └────┬─────┘   └────┬─────┘   └────┬─────┘               │
│             │              │              │                      │
│        YES/NO         YES/NO         YES/NO                      │
│             │              │              │                      │
│             └──────────────┴──────────────┘                      │
│                             │                                    │
│              ┌──────────────┴──────────────┐                     │
│              │                             │                     │
│              ▼                             ▼                     │
│        ┌──────────┐                  ┌──────────┐               │
│        │  ALLOW   │                  │  BLOCK   │               │
│        │ exit(0)  │                  │ exit(2)  │               │
│        └──────────┘                  └──────────┘               │
│                                            │                     │
│                                            ▼                     │
│                                    ┌──────────────┐             │
│                                    │  Smart Fix   │             │
│                                    │  Message     │             │
│                                    └──────────────┘             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**The agent cannot bypass the hook.** It's mechanical, not instructional.

---

## POC Results

**Test run:** 2026-02-07

| Metric | Result |
|--------|--------|
| First Action Rule | ✓ Invoked session-start immediately |
| Domain Setup | ✓ Created protocol, commands, hooks |
| Anchor | ✓ Read protocol, updated state |
| Hook Block | ✓ Caught state mismatch |
| Self-Correction | ✓ Agent debugged and fixed state |
| Protocol Following | ✓ Caught locator-in-test violation |
| Complete Gate | ✓ Invoked at end |
| Tests | ✓ 2/2 passing |

**Self-built artifacts:**
- `docs/protocols/playwright-protocol.md`
- `.claude/commands/playwright-*.md` (3 commands)
- `.claude/hooks/playwright-gate-enforcer.py`
- `.claude/state/playwright_workflow.json`
- Full Playwright test framework (6 files)

---

## Known Defects

| ID | Issue | Severity | Status |
|----|-------|----------|--------|
| DEF-001 | Agent skips /kernel/learn after self-fix | Medium | OPEN |
| DEF-002 | State key mismatch (anchored vs protocol_anchored) | Medium | OPEN |
| DEF-003 | Domain naming mismatch | Low | OPEN |

See `DEFECT_LOG.md` for details.

---

## File Structure

```
isagawa-kernel/
├── CLAUDE.md                          ← Kernel brain
├── .claude/
│   ├── commands/
│   │   └── kernel/
│   │       ├── session-start.md       ← Entry point
│   │       ├── domain-setup.md        ← Self-build
│   │       ├── anchor.md              ← Re-center
│   │       ├── learn.md               ← Self-improve
│   │       └── complete.md            ← Final gate
│   ├── hooks/
│   │   └── universal-gate-enforcer.py ← Safety layer
│   ├── state/                         ← Runtime state
│   └── settings.local.json            ← Hook config
├── docs/
│   └── protocols/                     ← Self-built protocols
└── DEFECT_LOG.md                      ← Known issues
```

---

## Distribution

**As Claude Code Plugin:**

```
isagawa-kernel/
├── .claude-plugin/
│   └── plugin.json          ← Plugin manifest
├── skills/
│   └── kernel/
│       └── SKILL.md         ← Kernel instructions
├── commands/                ← Slash commands
├── hooks/
│   └── hooks.json           ← Hook config
└── agents/
    └── kernel-agent.md      ← Agent definition
```

**Install:**
```
/plugin marketplace add isagawa/kernel
```

---

## Business Model

```
┌─────────────────────────────────────────────────────────────────┐
│                     REVENUE MODEL                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  KERNEL (Free)                                                   │
│  └── Gets adoption                                               │
│      └── Users create domain packs                               │
│          └── Ecosystem grows                                     │
│                                                                  │
│  COMMUNITY PACKS (Free)                                          │
│  └── Anyone can create                                           │
│      └── Grows ecosystem                                         │
│          └── More users                                          │
│                                                                  │
│  CERTIFIED PACKS (Paid)                                          │
│  └── Battle-tested by Isagawa                                    │
│      └── QA Pack, DevOps Pack, Compliance Pack                   │
│          └── Enterprise customers pay for trust                  │
│                                                                  │
│  DEPLOYMENTS (Premium)                                           │
│  └── Isagawa configures kernel for enterprise                    │
│      └── Custom domain packs                                     │
│          └── Training and support                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Summary

**Isagawa Kernel = AI Management Layer**

| Thesis | Implementation |
|--------|----------------|
| "Don't trust the AI" | Hook mechanically blocks |
| "External audit" | Protocol documents patterns |
| "Compliance" | State tracks process |
| "Self-governing" | Agent builds own enforcement |
| "Continuous improvement" | Learn updates protocol + hooks |

**Three words. Three files. One loop.**

```
Self-build. Self-improve. Safety-first.
```

---

*Document version: 3.0 (Minimal)*
*Validated: 2026-02-07*
*Status: POC Complete*
