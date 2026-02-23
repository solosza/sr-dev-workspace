# Isagawa Kernel Design v5

**Version:** 5.0
**Date:** 2026-02-18
**Status:** Implementation Current + Planned Enhancements

---

## Change Summary from v4

| Area | v4 | v5 |
|------|----|----|
| Indexing | [THEORY] Modular protocols | **[IMPLEMENTED]** Tiered Index Architecture (was "Three-tier indexing") |
| Activity count | [THEORY] Tunable, default 7 | **[IMPLEMENTED]** `actions_since_anchor`, default 10, auto-incremented |
| Validate command | [TBD] May be redundant | **[RESOLVED]** Deprecated, merged into anchor Part B |
| Fix command | Not documented | **[IMPLEMENTED]** Impact assessment before kernel fixes |
| Skills architecture | Not documented | **[IMPLEMENTED]** SKILL.md + step files pattern |
| `needs_learn` enforcement | Not documented | **[IMPLEMENTED]** Hook-enforced learn-after-fix loop |
| Test failure detector | Not documented | **[IMPLEMENTED]** PostToolUse hook |
| Domain hook purpose | files_since_validate + protected paths | **[IMPLEMENTED]** Code quality enforcement (debug, secrets, etc.) |
| Session state | 5 fields | **Extended** with `context`, `needs_learn`, `completed` |
| Conversation context | Not addressed | **[PLANNED]** Save to session_state.json at anchor/complete |
| Context window scaling | [TBD] | Partially addressed by Tiered Index Architecture |

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
│   ~120 lines. The sequence + auto-counter + learn triggers. │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ invokes
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      COMMANDS                               │
│                    (The Details)                            │
│                                                             │
│   /kernel/session-start   ← Check state, resume             │
│   /kernel/domain-setup    ← Create protocol + hooks          │
│   /kernel/anchor          ← Re-read protocol + check work   │
│   /kernel/learn           ← Update protocol + hooks          │
│   /kernel/fix             ← Impact assessment before fix     │
│   /kernel/complete        ← Final gate                       │
│   /kernel/reset           ← Fresh start (dev tool)           │
│   /kernel/validate        ← DEPRECATED (merged into anchor) │
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
│            - Checks: session_started, needs_learn,          │
│              anchored, actions_since_anchor                  │
│            - Auto-increments action counter                  │
│            - Skips: .claude/* files, safe bash commands     │
│                                                             │
│   Layer 2: Domain Hook (agent-created)                      │
│            - Checks: code quality (debug, secrets,          │
│              wildcards, skipped tests, file size)            │
│                                                             │
│   Layer 3: Test Failure Detector (PostToolUse)              │
│            - Detects: non-zero exit on test commands        │
│            - Sets: needs_learn flag                          │
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

## Tiered Index Architecture

> **Full specification:** [`docs/design/tiered-index-architecture.md`](tiered-index-architecture.md)

Every file is either an **index** (pointer) or a **payload** (content), never both. When any file crosses 200 lines, it splits into a folder with an index and focused sub-files. The pattern is fractal — it applies at every layer and grows organically. No fixed depth.

Previously called "Three-Tier Indexing System" in v5. Renamed and generalized to reflect the fractal, depth-agnostic nature of the pattern.

---

## The Loop (CLAUDE.md)

```
session-start → anchor → WORK ─────────────────→ complete
                   ↑         ↓                       ↑
                   └─ every 10 actions ←─────────────┘
                             ↓
                   failure? → fix → learn (MANDATORY)
```

### Work Loop Details

```
WORK:
  1. Write/Edit/Bash (any action)
  2. Hook AUTO-INCREMENTS counter (agent doesn't need to)
  3. Every 10 actions → hook blocks → /kernel/anchor
  4. Run tests
  5. If test fails → fix → /kernel/learn
  6. Repeat until done
  7. /kernel/complete
```

### Learn Triggers (Enforced by Hook)

Agent MUST invoke `/kernel/learn` after:
- **Test failure** — PostToolUse hook detects non-zero exit, sets `needs_learn: true`
- **Anchor violation** — `/kernel/anchor` Part B finds protocol violation

Hook blocks next Write/Edit/Bash until `/kernel/learn` is invoked.

---

## The Re-Centering Mechanism

**This is the core enforcement pattern.**

```
Agent tries to write → Hook checks state
                            │
                            ▼
                      State valid?
                    ┌─────┴─────┐
                   YES          NO
                    │            │
                    ▼            ▼
                  PASS      BLOCK + FIX
                                 │
                                 ▼
                      "Invoke /kernel/anchor"
                                 │
                                 ▼
                        Agent anchors
                        Reads protocol
                        Updates state
                        Re-centers
                                 │
                                 ▼
                         Retries write → PASS ✓
```

**The hook is the bouncer. The anchor is the re-centering.**

---

## File Structure

```
isagawa-kernel/
├── CLAUDE.md                                 ← The Loop (~120 lines)
├── .claude/
│   ├── commands/
│   │   ├── kernel/                           ← Kernel commands (8 files)
│   │   │   ├── session-start.md
│   │   │   ├── domain-setup.md
│   │   │   ├── anchor.md
│   │   │   ├── validate.md                   ← DEPRECATED
│   │   │   ├── learn.md
│   │   │   ├── fix.md
│   │   │   ├── complete.md
│   │   │   └── reset.md
│   │   └── [domain]-*.md                     ← Domain commands (agent creates)
│   ├── skills/
│   │   └── kernel-domain-setup/              ← Multi-step skill
│   │       ├── SKILL.md                      ← Index/orchestrator
│   │       └── references/                   ← 10 step files
│   │           ├── step-01-prerequisites.md
│   │           ├── step-02-discover.md
│   │           ├── step-03-read.md
│   │           ├── step-04-extract.md
│   │           ├── step-05-enforcement.md
│   │           ├── step-06-workflow.md
│   │           ├── step-07-protocol.md
│   │           ├── step-08-commands.md
│   │           ├── step-09-state.md
│   │           └── step-10-report.md
│   ├── hooks/
│   │   ├── universal-gate-enforcer.py        ← Pre-installed (Layer 1)
│   │   ├── test-failure-detector.py          ← Pre-installed (PostToolUse)
│   │   └── [domain]-gate-enforcer.py         ← Agent-created (Layer 2)
│   ├── protocols/                            ← Domain protocols (agent creates)
│   │   └── [domain]-protocol.md              ← Pure index, no duplication
│   ├── lessons/                              ← Lessons learned (agent creates)
│   │   └── lessons.md
│   ├── state/                                ← AI-controlled state
│   │   ├── session_state.json
│   │   └── [domain]_workflow.json
│   └── settings.local.json                   ← Pre-wired with hooks
└── docs/
    └── design/                               ← Design docs (indexed: 0-, 1-, 2-)
        ├── 0-design-isagawa-kernel.md
        ├── 1-prd-isagawa-kernel.md
        ├── 2-tasks-isagawa-kernel.md
        └── KERNEL_DESIGN_v5.md
```

---

## Two-Layer Hook Architecture

### Layer 1: Universal Hook (Pre-installed)

**File:** `.claude/hooks/universal-gate-enforcer.py`

**What it checks (4 gates):**
1. `session_started` = true (from session_state.json)
2. `needs_learn` = false (must learn after fix before continuing)
3. `anchored` = true (from [domain]_workflow.json)
4. `actions_since_anchor` <= `actions_limit` (auto-incremented)

**What it skips:**
- All files in `.claude/*` (kernel infrastructure)
- Safe bash commands (git status, ls, grep, etc.)

**When it runs:**
- On every `Write`, `Edit`, and `Bash` tool call

**Auto-increment:** Hook increments `actions_since_anchor` on every tracked action. Agent does NOT increment manually.

```python
# Simplified logic
if tool_name not in ('Write', 'Edit', 'Bash'):
    exit(0)

if tool_name == 'Bash' and is_safe_command(command):
    exit(0)

if tool_name in ('Write', 'Edit') and '.claude/' in file_path:
    exit(0)

if not session_state['session_started']:
    smart_block("session not started", "/kernel/session-start")

if session_state.get('needs_learn'):
    smart_block("lesson not recorded", "/kernel/learn")

if not domain_state['anchored']:
    smart_block("not anchored", "/kernel/anchor")

# Auto-increment and check limit
actions_since += 1
if actions_since > actions_limit:
    smart_block("action limit reached", "/kernel/anchor")
```

### Layer 2: Domain Hook (Agent-created)

**File:** `.claude/hooks/[domain]-gate-enforcer.py`

**What it checks (code quality):**
- Debug statements (`console.log`, `print(`, `fmt.Println`, etc.)
- Hardcoded secrets (`password=`, `api_key=`, `token=`)
- Wildcard imports (`import *`, `from x import *`)
- Skipped tests (`.skip`, `@pytest.mark.skip`, `xit(`)
- File size (> 300 lines)

**What it skips:**
- `.claude/`, `node_modules/`, `__pycache__/`, `.git/`
- Test files (`*.test.*`, `test_*`, `*.spec.*`)
- Design docs (`docs/design/`)

**Created by:** `/kernel/domain-setup`

**Requires restart:** Yes (hooks load at startup)

### Layer 3: Test Failure Detector (PostToolUse)

**File:** `.claude/hooks/test-failure-detector.py`

**What it does:**
- Fires after every Bash command
- Detects test commands (pytest, jest, go test, etc.)
- If non-zero exit: sets `needs_learn: true` in session_state.json
- Universal hook then blocks until `/kernel/learn` is invoked

### Hook Chain in settings.local.json

```json
{
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
      "hooks": [
        {"type": "command", "command": "python .claude/hooks/test-failure-detector.py"}
      ]
    }]
  }
}
```

---

## Commands Reference

### /kernel/session-start

**Purpose:** Check state and determine next step.

**Flow:**
- No state → `/kernel/domain-setup`
- State exists with domain → `/kernel/anchor`
- `needs_restart: true` → Clear flag, resume from `resume_after_restart`

**Domain persistence rule:** If domain exists → USE IT (never create new). One project = one domain = one protocol.

**Force anchor on fresh start:** Sets `anchored: false` to ensure hook blocks until anchor invoked.

**Updates:** `session_state.json`

### /kernel/domain-setup

**Purpose:** Create complete enforcement for a new domain.

**Implementation:** Points to skill at `.claude/skills/kernel-domain-setup/SKILL.md` which orchestrates 10 steps.

**Step 0:** Normalize domain name (lowercase, underscores, no special chars).

**Creates:**
- `.claude/protocols/[domain]-protocol.md` (indexed protocol)
- `.claude/lessons/lessons.md` (lessons folder)
- `.claude/state/[domain]_workflow.json` (state)
- `.claude/hooks/[domain]-gate-enforcer.py` (hook)
- `.claude/commands/[domain]-*.md` (domain commands)

**Critical:** Must PRESERVE existing kernel hooks in settings.local.json (append, never overwrite).

**Sets:** `needs_restart: true` (hooks require restart)

### /kernel/anchor

**Purpose:** Re-read protocol and re-center. Unified command combining protocol refresh + work quality check.

**Part A — Refresh Protocol:**
1. Read protocol file
2. Summarize key patterns, anti-patterns
3. Review lessons learned

**Part B — Check Recent Work (if any):**
4. Review files created/modified since last anchor
5. Check against protocol (naming, architecture, anti-patterns, quality gates)
6. If violation: set `needs_learn`, fix, invoke `/kernel/learn`

**Part C — Reset and Proceed:**
7. State current task
8. Update state: `anchored: true`, `actions_since_anchor: 0`

**When to invoke:**
- After `/kernel/session-start` (mandatory)
- Every 10 actions (hook-enforced)
- After any failure
- When context drifts

### /kernel/learn

**Purpose:** Update protocol AND hooks after fixing failure. Clears `needs_learn` block.

**Two-tier learning:**
1. **Soft enforcement:** Add to protocol lessons learned
2. **Hard enforcement:** Add to hooks (if enforceable)

**Updates:**
- Protocol: New lesson, anti-pattern, quality gate
- Hook: New check (if pattern is mechanically detectable)
- State: `needs_learn: false`, `lessons_count: N`

### /kernel/fix

**Purpose:** Mandatory impact assessment before any fix to kernel components.

**Flow:**
1. Log defect in DEFECT_LOG.md
2. Impact assessment: who calls this? what depends on it? what breaks?
3. Present assessment, wait for approval
4. Implement fix
5. Invoke `/kernel/learn`

### /kernel/complete

**Purpose:** Final gate before marking work done.

**Checks:** `protocol_created: true`, `anchored: true`

**Updates:** `complete: true`, `complete_timestamp`

### /kernel/reset

**Purpose:** Reset repo for fresh kernel test (dev tool).

**Removes:** State, protocols, lessons, domain hooks, domain commands.

**Keeps:** Kernel commands, universal hook, test-failure-detector, skills, CLAUDE.md, design docs.

### /kernel/validate (DEPRECATED)

Merged into `/kernel/anchor` Part B. Do not use.

---

## State Files

### session_state.json

```json
{
  "session_started": true,
  "domain": "[domain]",
  "timestamp": "ISO-8601",
  "needs_restart": false,
  "resume_after_restart": null,
  "needs_learn": false,
  "needs_learn_reason": null,
  "context": "Summary of current conversation context",
  "completed": ["list of completed items"],
  "resume_step": null
}
```

**Extended fields (v5):**
- `needs_learn` / `needs_learn_reason` — Set by test-failure-detector or anchor Part B, cleared by `/kernel/learn`
- `context` — Conversation context saved at anchor/complete (key/value, agent-extensible)
- `completed` — Tracking array for multi-step work
- `resume_step` — Used by skills for mid-skill resume after restart

### [domain]_workflow.json

```json
{
  "domain": "[domain]",
  "setup_complete": true,
  "protocol_created": true,
  "commands_created": true,
  "hooks_created": true,
  "anchored": false,
  "anchor_timestamp": null,
  "actions_since_anchor": 0,
  "actions_limit": 10,
  "validated": false,
  "files_checked": [],
  "lesson_recorded": false,
  "lessons_count": 0,
  "last_lesson": null,
  "timestamp": "ISO-8601"
}
```

**Changed fields (v5):**
- `actions_since_anchor` — Replaces `files_since_validate`. Auto-incremented by universal hook.
- `actions_limit` — Configurable (default 10). Was hardcoded 5 in v4.

---

## Learning Cascade

```
FAILURE DETECTED
       │
       ▼
/kernel/fix (impact assessment, defect log)
       │
       ▼
DIAGNOSE (what failed, why, root cause)
       │
       ▼
FIX (implement solution)
       │
       ▼
/kernel/learn
├── SOFT: Add to protocol (knowledge)
│   ├── Lessons learned section
│   ├── New anti-pattern
│   └── New quality gate
│
└── HARD: Add to hooks (prevention)
    ├── New check in domain hook
    └── Block future violations automatically
       │
       ▼
KERNEL SMARTER
- Next /kernel/anchor reads updated protocol
- Next write attempt hits updated hooks
- Same mistake now impossible
```

---

## Planned Enhancements

### [IMPLEMENTED] Conversation Context Save

**Problem:** Multi-turn conversations degrade model performance (Microsoft Research + Salesforce, 2026). Performance drops from 90% (single-turn) to 65% (multi-turn). Unreliability increases 112%. The kernel externalizes protocol knowledge to files but not conversation context — decisions, direction changes, and insights made during chat are lost when context compresses.

**Solution:** Save conversation context as key/value pairs in `session_state.json` at known trigger points. No new files, no new hooks, no new commands — pure agent behavior change via instruction updates.

**Implementation (agent tasks only):**
- `session-start.md` — Step 1: read and report `context` key from session_state.json; Step 5: MERGE into existing state (preserve `context`)
- `anchor.md` — Part A Step 4: restore `context` from session_state.json; Part C Step 8: save current conversation context before resetting counter
- `complete.md` — Step 2: save final conversation context/summary before marking done

**Triggers:**
- At anchor (hook-enforced, reliable)
- At complete (reliable)
- Manual (user-initiated)

**What gets saved:**
- Key decisions made in conversation
- Direction changes and tabled items
- Current thread of discussion
- User preferences and constraints discovered

**Known gap:** Pure chat turns (no tool calls) have no hook trigger. The agent cannot be mechanically forced to save context during chat-only exchanges. Read/Glob/Grep tool calls also don't trigger hooks. This is accepted as a limitation — the anchor and complete triggers cover work phases; pure chat phases remain a gap.

### [PLANNED] JSONL Audit Format

**Current:** No audit command implemented.

**Planned:** JSONL append-only format for incremental logging.

```jsonl
{"timestamp": "...", "event": "session_started", ...}
{"timestamp": "...", "event": "command_invoked", "command": "/kernel/anchor", ...}
```

### [FUTURE] HITL Levels

**Status:** Post-MVP

**Levels:**
- `strict` — Every checkpoint (dev/testing)
- `normal` — Failures + completion only
- `minimal` — Completion only

---

## Session Persistence

### The Problem

Hooks are loaded at Claude Code startup. If agent creates hooks mid-session, they don't take effect until restart.

### The Solution

1. **Pre-installed universal hook** — Always active
2. **State-based resume** — Agent writes state, reads on next session
3. **Restart prompt** — When new hooks created, prompt user to restart
4. **Skill resume** — `resume_step` enables mid-skill restart

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
6. **Tiered Index Architecture**: Every file is index or payload, never both → [`docs/design/tiered-index-architecture.md`](tiered-index-architecture.md)
7. **200-Line Rule**: Split files at threshold, always index
8. **Session Persistence**: State survives restart
9. **Minimal Core**: CLAUDE.md is just the loop, commands hold details
10. **Autonomy**: Report after, don't ask before

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-02-07 | Commands only, never invoked |
| v2 | 2026-02-07 | Smart gates, HITL, learn, audit |
| v3 | 2026-02-08 | Triangle architecture, state schema |
| v4 | 2026-02-10 | Two-layer hooks, re-centering, activity count [THEORY], modular protocols [THEORY] |
| v5 | 2026-02-18 | Tiered Index Architecture [IMPLEMENTED], unified action counter [IMPLEMENTED], validate deprecated, fix command, skills architecture, needs_learn enforcement, test-failure-detector, conversation context [PLANNED] |

---

## Implementation Status

| Component | Status | Notes |
|-----------|--------|-------|
| CLAUDE.md | ✅ Implemented | ~120 lines with auto-counter + learn triggers |
| 8 Kernel Commands | ✅ Implemented | session-start, domain-setup, anchor, learn, fix, complete, reset, validate (deprecated) |
| Universal Hook | ✅ Implemented | 4 gates: session, needs_learn, anchored, action limit + auto-increment |
| Test Failure Detector | ✅ Implemented | PostToolUse, sets needs_learn on test failure |
| Domain Hook Pattern | ✅ Implemented | Code quality: debug, secrets, wildcards, tests, file size |
| State Files | ✅ Implemented | session_state + domain_workflow (extended fields) |
| Learning Cascade | ✅ Implemented | Soft + hard enforcement, needs_learn blocking |
| Tiered Index Architecture | ✅ Implemented | Index/payload split at every layer → [`docs/design/tiered-index-architecture.md`](tiered-index-architecture.md) |
| SKILL.md + Step Files | ✅ Implemented | kernel-domain-setup with 10 steps |
| 200-Line Rule | ✅ Implemented | In step-07-protocol.md |
| Fix Command | ✅ Implemented | Impact assessment + defect logging |
| Conversation Context | ❌ Planned | Save to session_state.json at anchor/complete |
| JSONL Audit | ❌ Not Implemented | Planned |
| HITL Levels | ❌ Not Implemented | Post-MVP |

---

*End of Design*
