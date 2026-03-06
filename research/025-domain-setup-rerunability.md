# Domain-Setup Rerunability Audit

## Step-by-Step Analysis

| Step | Action | Existing State Check? | Merge or Overwrite? | Issue? |
|------|--------|-----------------------|---------------------|--------|
| 1 — Prerequisites | Check MCP, dependencies | Yes (MCP config) | Overwrite MCP, merge settings | No |
| 2 — Discover | Scan repo structure | N/A (read-only) | N/A | No |
| 3 — Read Reference | Identify pattern files | N/A (read-only) | N/A | No |
| 4 — Extract Patterns | Analyze code patterns | N/A (read-only) | N/A | No |
| 5 — Enforcement | Review hook architecture | N/A (read-only) | N/A | No |
| 6 — Workflow | Read workflow skills | N/A (read-only) | N/A | No |
| 7 — Roadmap | Create/check tasks/ | **Yes** — checks existing .md files | **Preserves existing** | No (good pattern) |
| 8 — Build Protocol | Create protocol + lessons | **No** — no existing check | **Creates new** | **YES** |
| 9 — Wrap Commands | Create command wrappers | **No** — no existing check | **Creates new** | **YES** |
| 10 — Update State | State + settings | Yes (settings) | Merge settings, overwrite state | No |
| 11 — Report | Final report + stop | N/A (read-only) | N/A | No |

## Conflict Points

| File | First Run (kernel spec) | Second Run (domain spec) | Conflict? | Fix |
|------|------------------------|--------------------------|-----------|-----|
| `CLAUDE.md` | Kernel creates it | Domain spec doesn't touch it | No | N/A — kernel-spec handles via _reference/, domain-setup doesn't |
| `.claude/protocols/[domain]-protocol.md` | Doesn't exist yet (kernel uses _reference/) | Domain-setup creates `[domain]-protocol.md` | **No** — different files (kernel installs files, domain-setup creates protocol) | Safe as-is |
| `.claude/commands/kernel/*.md` | Kernel installs 8 commands | Domain spec wraps non-kernel commands | No — different namespaces | Safe as-is |
| `.claude/commands/[domain]-*.md` | Don't exist yet | Step 9 creates wrappers | **YES if re-run** — no check for existing wrappers | Add existence check |
| `.claude/hooks/*.py` | Kernel installs 2 hooks | Domain spec doesn't add hooks (hooks are kernel-level) | No | Safe as-is |
| `.claude/settings.local.json` | Kernel installs with hook registrations | Step 10 merges (explicit MERGE rule) | No — merge is safe | Safe as-is |
| `.claude/state/session_state.json` | Kernel initializes | Step 10 overwrites | **Partial** — overwrites existing context | Add merge logic |
| `.claude/state/[domain]_workflow.json` | Domain-specific, new file per domain | One domain per project rule | No | Safe as-is |
| `.claude/lessons/lessons.md` | Kernel spec seeds lessons | Step 8 creates empty lessons.md | **YES** — overwrites seeded lessons | Add existence check |
| `tasks/` | May have existing tasks | Step 7 preserves existing (good) | No | Safe as-is |

## Critical Issues (Ranked by Severity)

### 1. Step 8 overwrites lessons.md (HIGH)

**Problem:** Step 8 creates `.claude/lessons/lessons.md` with an empty template. If the kernel spec already seeded lessons (as task 023 built), Step 8 would overwrite them with an empty file.

**Fix:** Add existence check in Step 8:
```
If .claude/lessons/lessons.md already exists:
  → SKIP creation (preserve seeded lessons)
  → Append new topic entries if domain spec adds new lesson categories
If missing:
  → Create with empty template
```

### 2. Step 8 doesn't check for existing protocol (MEDIUM)

**Problem:** Step 8 creates `.claude/protocols/[domain]-protocol.md` without checking if one already exists. Re-running domain-setup for the same domain would overwrite the protocol.

**Impact:** Low in practice — the "one project = one domain" rule means you'd only run domain-setup once per domain. But the kernel spec installs files before domain-setup runs, and domain-setup creates the protocol. These are separate steps that don't conflict.

**Fix:** Add existence check in Step 8:
```
If .claude/protocols/[domain]-protocol.md already exists:
  → WARN user: "Protocol already exists. Overwrite? Merge? Skip?"
  → Default: SKIP (preserve existing protocol)
```

### 3. Step 9 doesn't check for existing command wrappers (MEDIUM)

**Problem:** Step 9 creates command wrappers without checking if they already exist. Re-running domain-setup would create duplicate wrappers.

**Fix:** Add existence check in Step 9:
```
If .claude/commands/[domain]-*.md already exists:
  → SKIP (preserve existing wrappers)
  → Report: "Wrapper already exists, skipping"
```

### 4. Step 10 overwrites session_state.json context (LOW)

**Problem:** Step 10 overwrites `session_state.json` without preserving the `context` key. If there's prior context from a kernel installation, it gets lost.

**Fix:** Add merge logic in Step 10:
```
If .claude/state/session_state.json already exists:
  → Read existing file
  → Preserve 'context' key
  → Merge new keys into existing state
  → Write merged result
```

## Required Changes

### Changes to canonical kernel (`isagawa-co/isagawa-kernel`)

1. **step-08-protocol.md** — Add existence checks for protocol and lessons.md
2. **step-09-commands.md** — Add existence check for command wrappers
3. **step-10-state.md** — Add merge logic for session_state.json (preserve context key)

### Changes required: 3 files, all in `.claude/skills/kernel-domain-setup/references/`

## Proposed Fix Strategy

### Per-File Merge Rules

| File Type | Strategy | Reason |
|-----------|----------|--------|
| Protocol | Check-then-create | One protocol per domain, never overwrite |
| Lessons index | Check-then-append | Seeded lessons must survive domain-setup re-runs |
| Lesson payloads | Never touch existing | Domain-setup creates index entries, not payload files |
| Command wrappers | Check-then-create | One wrapper per command, never duplicate |
| Session state | Merge (preserve context) | Context survives across domain-setup runs |
| Workflow state | Overwrite (idempotent) | Each run produces correct state |
| Settings | Merge (existing rule) | Already implemented correctly in Step 10 |
| Tasks directory | Preserve (existing rule) | Already implemented correctly in Step 7 |

### Detection: "Kernel Already Built, Adding Domain Spec"

Domain-setup can detect this via:
```python
# Check for kernel markers
kernel_exists = os.path.exists('.claude/commands/kernel/anchor.md')
lessons_seeded = os.path.exists('.claude/lessons/lessons.md')
protocol_exists = any(glob('.claude/protocols/*-protocol.md'))

if kernel_exists:
    mode = 'layered_install'  # Adding domain on top of kernel
else:
    mode = 'fresh_install'    # First-time setup
```

### Implementation Approach

**Feature branch** on `isagawa-co/isagawa-kernel`:
- Branch: `feature/domain-setup-rerunability`
- Modify: step-08, step-09, step-10
- Test: Run domain-setup twice in cognitive-agent — verify no data loss
- PR to main

## Summary

Domain-setup is **mostly rerunnable** already. Steps 2-7 and 10-11 are safe. The three issues are all in Steps 8-10 and involve missing existence checks before file creation. The fixes are straightforward — add `if exists: skip/merge` guards to three step files.

The good patterns (Step 7's task preservation, Step 10's settings merge) should be extended to all file-creating steps.
