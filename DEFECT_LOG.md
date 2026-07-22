# Isagawa Kernel - Defect Log

## DEF-001: Agent skips /kernel/learn after self-fix

**Date:** 2026-02-07
**Severity:** Medium
**Status:** RESOLVED

### What Happened
Agent hit hook block (state mismatch: `protocol_anchored` vs `anchored`). Agent debugged, found issue, fixed state. But did NOT invoke `/kernel/learn` to record the lesson.

### Expected Behavior
After any fix, agent should invoke `/kernel/learn` to:
1. Update protocol with lesson
2. Update hooks if enforceable
3. Prevent same mistake in future

### Actual Behavior
Agent fixed and moved on. No lesson recorded. Same mistake can recur.

### Root Cause
`/kernel/learn` invocation is soft instruction only. Nothing enforces it after a fix.

### Impact
- Self-improvement loop broken
- Lessons not captured
- Mistakes can repeat

### Proposed Fix Options
1. **Stronger CLAUDE.md language** — "ALWAYS invoke /kernel/learn after ANY fix"
2. **Hook enforcement** — Track `fix_count` vs `learn_count` in state, block next write if mismatch
3. **Command chaining** — Anchor command auto-invokes learn if `last_action: "fix"`

### Resolution
**RESOLVED 2026-02-07** — Implemented Option 2 with enhancements:

1. **Hook enforcement via `needs_learn` flag:**
   - PreToolUse hook detects direct state edits → sets `needs_learn: true`
   - PostToolUse hook detects test failures → sets `needs_learn: true`
   - Next Write/Edit blocked until `/kernel/learn` invoked

2. **Added `/kernel/validate` command:**
   - Self-check against protocol every 5 files
   - Catches violations hook can't detect
   - Violations trigger `/kernel/learn`

3. **Updated CLAUDE.md:**
   - Documents learn triggers
   - Shows updated loop with validate

Files modified:
- `.claude/hooks/universal-gate-enforcer.py` — Added needs_learn detection and blocking
- `.claude/hooks/test-failure-detector.py` — New PostToolUse hook for test failures
- `.claude/commands/kernel/validate.md` — New command
- `.claude/commands/kernel/learn.md` — Clears needs_learn flag
- `.claude/settings.local.json` — Added PostToolUse hook config
- `CLAUDE.md` — Updated loop documentation

---

## DEF-002: State key mismatch - anchored vs protocol_anchored

**Date:** 2026-02-07
**Severity:** Medium
**Status:** RESOLVED

### What Happened
Anchor command set `protocol_anchored: true` in state. Universal gate enforcer checks for `anchored: true`. Mismatch caused hook to block writes even after anchoring.

### Expected Behavior
Anchor command should set the same key the hook checks.

### Actual Behavior
- Anchor sets: `protocol_anchored: true`
- Hook checks: `anchored: true`
- Result: BLOCKED despite being anchored

### Root Cause
No contract between anchor command and universal gate enforcer on state key names.

### Impact
- Agent blocked unexpectedly
- Agent had to debug and manually fix state
- Friction in first run

### Proposed Fix Options
1. **Standardize key name** — Anchor command uses `anchored` (match hook)
2. **Hook flexibility** — Hook checks both `anchored` OR `protocol_anchored`
3. **State schema enforcement** — Document required keys in state-schema.md

### Resolution
**RESOLVED 2026-02-07** — anchor.md already uses `anchored: true`. The mismatch occurred because agent didn't follow the command exactly. With DEF-001 fix, if agent manually edits state, `needs_learn` triggers and lesson is captured.

---

## DEF-003: Domain naming mismatch between session and workflow

**Date:** 2026-02-07
**Severity:** Low
**Status:** RESOLVED

### What Happened
Session state set `domain: "playwright-automation"`. Workflow file created as `playwright_workflow.json`. Hook looks for `{domain}_workflow.json` → looked for `playwright-automation_workflow.json` → didn't find it.

### Expected Behavior
Domain name should be consistent across:
- session_state.json `domain` field
- `{domain}_workflow.json` filename
- Protocol filename

### Actual Behavior
- Session: `playwright-automation`
- Workflow file: `playwright_workflow.json`
- Hook lookup failed

### Root Cause
No validation that domain-setup creates workflow file matching session domain name.

### Impact
- State lookup failed
- Agent had to manually align domain names
- Could cause silent failures if not caught

### Proposed Fix Options
1. **Domain normalization** — domain-setup normalizes name (remove hyphens, lowercase)
2. **Session-workflow sync** — domain-setup reads session domain, uses exact name
3. **Validation gate** — Hook validates domain name matches before checking state

### Resolution
**RESOLVED 2026-02-07** — Implemented Option 1:

Added "Step 0: Normalize Domain Name" to `/kernel/domain-setup`:
- Lowercase
- Replace hyphens with underscores
- Remove special characters
- Explicit instruction that session_state.json domain MUST match workflow filename prefix

Files modified:
- `.claude/commands/kernel/domain-setup.md` — Added Step 0 and explicit sync instructions

---

## DEF-004: Agent creates new domain instead of extending existing

**Date:** 2026-02-07
**Severity:** Medium
**Status:** RESOLVED

### What Happened
Agent was asked to add API testing support to existing project. Instead of extending the "playwright" domain, agent tried to create a new "api" domain via `/kernel/domain-setup`.

### Expected Behavior
Agent should recognize that API testing is part of the same project and extend the existing domain's protocol to cover new capabilities.

### Actual Behavior
- Agent saw "API testing" ≠ "playwright"
- Concluded new domain needed
- Invoked `/kernel/domain-setup` for new domain
- Would have created separate protocol, hooks, state

### Root Cause
`/kernel/session-start` has no logic for:
1. "Same project, different capability" detection
2. Domain extension vs domain creation decision
3. Single domain per project rule

### Impact
- Protocol fragmentation (multiple protocols per project)
- State fragmentation (multiple workflow files)
- Lessons not shared across "domains" in same project
- Unnecessary complexity

### Proposed Fix Options
1. **Generic domain name** — Rename "playwright" to "qa" or "automation" (covers UI + API)
2. **Domain extension logic** — session-start checks if new work is related to existing domain
3. **Single domain per project** — One domain per project, period. Protocol grows to cover capabilities.

### Resolution
**RESOLVED 2026-02-07** — Implemented Option 3:

Added "Domain persistence rule (CRITICAL)" to `/kernel/session-start`:
- If domain exists → USE IT (never create new)
- One project = one domain = one protocol
- New capabilities extend existing protocol via `/kernel/learn`
- Only `/kernel/domain-setup` if NO domain exists

Also added `/kernel/fix` command for mandatory impact assessment before any kernel fixes.

Files modified:
- `.claude/commands/kernel/session-start.md` — Added domain persistence rule
- `.claude/commands/kernel/fix.md` — New command for impact assessment
- `CLAUDE.md` — Updated commands list

---

## DEF-005: PostToolUse hook removed during debugging

**Date:** 2026-02-08
**Severity:** Medium
**Status:** RESOLVED

### What Happened
Test failure enforcement not working. Agent ran tests, tests failed, but no `needs_learn` block fired. Agent voluntarily invoked `/kernel/fix` but wasn't enforced.

### Expected Behavior
PostToolUse hook detects test failure → sets `needs_learn: true` → blocks next write until `/kernel/learn` invoked.

### Actual Behavior
- `test-failure-detector.py` deleted from working directory
- `PostToolUse` section removed from `settings.local.json`
- No enforcement on test failure

### Root Cause
During "circular trap" debugging in previous session, these were removed to work around issues. Never restored.

Committed HEAD has correct config:
- `test-failure-detector.py` exists
- `PostToolUse` hook configured for Bash matcher

### Impact
- Test failure enforcement broken
- Agent can continue after test failures without learning
- Self-improvement loop not enforced

### Proposed Fix
Restore from HEAD:
```bash
git checkout HEAD -- .claude/hooks/test-failure-detector.py .claude/settings.local.json
```

Or re-add PostToolUse config to current settings.local.json.

### Resolution
**RESOLVED 2026-02-10** — Recreated test-failure-detector.py and added PostToolUse hook to settings.local.json.

Files modified:
- `.claude/hooks/test-failure-detector.py` — Created with test command detection
- `.claude/settings.local.json` — Added PostToolUse section for Bash matcher

---

## DEF-006: Anchor and Validate redundancy

**Date:** 2026-02-08
**Severity:** Low
**Status:** RESOLVED

### What Happened
5-file enforcement triggers `/kernel/validate`. But anchor already re-centers on protocol. If agent re-anchors and reviews recent work, validate is redundant.

### Expected Behavior
Single re-centering action that includes reviewing recent files.

### Actual Behavior
- Anchor = refresh rules (before work)
- Validate = check work (after work)
- Two separate commands for related purpose

### Root Cause
Design assumed anchor and validate serve distinct purposes. But re-anchoring naturally includes noticing drift in recent work.

### Impact
- Extra command when one would suffice
- Confusing distinction between anchor and validate
- 5-file checkpoint could be simpler

### Proposed Fix
Enhance anchor to include "review recent files":
```
ANCHOR (enhanced):
1. Re-read protocol
2. Review files since last anchor (if any)
3. Check: Do recent files match protocol?
4. If violations: fix → learn
5. State current task
6. Reset counter
```

Then:
- 5-file limit triggers anchor (not validate)
- Validate reserved for final gate before complete
- Simpler loop

### Resolution
**RESOLVED 2026-02-10** — Implemented proposed fix with full deprecation:

1. Enhanced anchor.md with Part A (protocol refresh) + Part B (check recent work) + Part C (reset)
2. Deprecated validate.md entirely (not even "before complete" - anchor + complete is enough)
3. Updated domain-setup.md to remove validate from domain commands
4. Updated CLAUDE.md commands list and learn triggers

Files modified:
- `.claude/commands/kernel/anchor.md` — Added Part B (work quality check)
- `.claude/commands/kernel/validate.md` — Marked DEPRECATED
- `.claude/commands/kernel/domain-setup.md` — Removed validate from Step 2
- `CLAUDE.md` — Updated commands list and learn triggers

---

## DEF-010: Domain-setup overwrites universal gate enforcer

**Date:** 2026-02-10
**Severity:** High
**Status:** RESOLVED

### What Happened
During `/kernel/domain-setup`, agent created new settings.local.json that only included the domain-specific hook (playwright-gate-enforcer.py), removing the pre-installed universal-gate-enforcer.py from the hook chain.

### Expected Behavior
Domain-setup should ADD the domain hook to settings, not REPLACE all hooks. Universal gate enforcer must always remain in the chain.

### Actual Behavior
- Before: settings had universal-gate-enforcer.py
- After domain-setup: settings only has playwright-gate-enforcer.py
- Universal gate enforcer still exists but is not triggered

### Root Cause
`/kernel/domain-setup` command writes entire settings.local.json instead of merging with existing hooks.

### Impact
- Session-start enforcement lost
- Anchor enforcement lost (from universal hook)
- Learn enforcement lost
- Only domain-specific rules enforced
- Core kernel protections bypassed

### Proposed Fix
1. domain-setup should READ existing settings first
2. APPEND domain hook to existing hooks array
3. Never overwrite universal-gate-enforcer.py

### Resolution
**FIX APPLIED 2026-02-10** — Updated `/kernel/domain-setup` Step 4:
- Added "PRESERVE UNIVERSAL HOOK" warning
- Explicit before/after JSON showing hook array append
- Explanation of why universal hook is critical

Also updated Step 6 to use unified counter fields (`actions_since_anchor`, `actions_limit`).

**VERIFIED 2026-02-10** — Fresh kernel test confirmed universal hook preserved and blocking works.

---

## DEF-011: Hook syntax error - backslash escaping quote

**Date:** 2026-02-10
**Severity:** Critical
**Status:** RESOLVED

### What Happened
Universal gate enforcer hook had a Python syntax error on line 101. The backslash in `.replace('\', '/')` was escaping the quote instead of being a literal backslash character. Python couldn't parse the file, so the hook never ran.

### Expected Behavior
Hook should run on every Write/Edit/Bash and increment action counter.

### Actual Behavior
- Hook failed to parse (SyntaxError: unterminated string literal)
- `actions_since_anchor` stayed at 0 after 7+ writes
- No re-centering block fired

### Root Cause
Line 101 had:
```python
file_path = tool_input.get('file_path', '').replace('\', '/')
```

Should be:
```python
file_path = tool_input.get('file_path', '').replace('\\', '/')
```

### Impact
- All hook enforcement completely broken
- Counter never incremented
- Re-centering never triggered
- Session-start/anchor/learn gates never checked

### Resolution
**FIX APPLIED 2026-02-10** — Changed `'\', '/'` to `'\\', '/'` on line 101.

Verified with `python -m py_compile` - syntax now OK.

**VERIFIED 2026-02-10** — Fresh kernel test confirmed:
- Hook runs successfully
- Counter increments (0→6)
- Block fires at action 6
- Agent re-anchors and continues

---

## DEF-012: Task-builder atomize step allows action bundling

**Date:** 2026-03-23
**Severity:** High
**Status:** OPEN

### What Happened
User asked 3 times to decompose tasks to maximum granularity (one action per task). Agent repeatedly bundled 3-10 actions into single tasks. E2E test (task 043) had 6+ distinct actions in one task file. Validation tasks (037-040) similarly bundled.

### Expected Behavior
Each task file contains exactly ONE action: one file write, one test run, one config change, one copy operation. No bundling.

### Actual Behavior
- Agent grouped "related" actions into single tasks
- E2E test had: create workspace + install kernel + 3 run-task iterations + verify results = 6+ actions
- Agent applied subjective "merge if <3 criteria" rule to justify bundling
- User had to correct 3 times

### Root Cause
1. step-04-atomize.md has conflicting rules: "one action per task" vs "merge if <3 subtasks"
2. The merge rule gives the agent permission to bundle, overriding the atomicity rule
3. No explicit "NEVER bundle multiple file writes/commands into one task" directive
4. Agent optimizes for fewer tasks (feels more efficient) rather than following granularity instruction

### Impact
- Tasks not executable in one-shot mode (too many actions per iteration)
- Violations of DRY principle — user repeats same instruction 3 times
- Erodes user trust in agent's ability to follow instructions

### Proposed Fix
1. Remove "merge if <3" rule from step-04-atomize.md — it contradicts atomicity
2. Add explicit "NEVER bundle" rule to atomize step
3. Add lesson to lessons.md
4. Re-decompose coarse tasks (037-043) into truly atomic ones

### Resolution
**RESOLVED 2026-03-23** — Root cause fixed in task-builder skill:

1. **step-04-atomize.md** — Removed "merge if <3" rule. Replaced with "NEVER merge" + "One task = one action. No exceptions." Added explicit anti-bundling rules in Rules section.
2. **step-03-decompose.md** — Removed "too small → merge" and "3-10 tasks, not 40" cap. Replaced with "small is GOOD" and "task count driven by work, not arbitrary cap."
3. **Lesson recorded** — via /kernel/learn (see lessons.md)

Files modified:
- `.claude/skills/task-builder/references/step-04-atomize.md` — Removed merge rule, added granularity rule
- `.claude/skills/task-builder/references/step-03-decompose.md` — Removed merge rule, removed task cap

Still needed: re-decompose coarse tasks (037-043) into truly atomic ones.

---

## DEF-014: Dual import roots in hmsa-qa-platform _reference package

**Date:** 2026-07-20
**Severity:** Medium
**Status:** OPEN

### What Happened
Importing `_reference.tasks` (as the 213 pytest suite does) crashes with `ModuleNotFoundError: No module named 'components'` when only `framework/` is on sys.path. Discovered during orchestrator validation of 213's skipped gate 004 (lesson 46).

### Expected Behavior
The whole `_reference` package imports cleanly from a single root (`framework/` on sys.path), matching the platform-wide import convention (`from _reference...`, `from interfaces...`, `from resources...`).

### Actual Behavior
`framework/_reference/pages/orders_page.py` (merged in 205) imports `from components.grid_component` / `from components.modal_component` — a style rooted at `framework/_reference/`. One import of the tasks package triggers both styles via the `__init__` chain, so no single path root satisfies it. Masked until 213 because 212's live gate loaded modules via importlib, bypassing the package `__init__`.

### Root Cause
205 shipped pages with `_reference`-relative imports; every gate passed because nothing imported the package through its real path. Grep confirms only these 2 lines deviate from the framework-root convention repo-wide.

### Proposed Fix
Change the 2 imports in orders_page.py to `from _reference.components...` (unify on framework-root style — the majority convention, used by 17 other import statements).

### Resolution
**RESOLVED 2026-07-21** — 2-line fix on `fix/orders-page-import-root` (de05953), merged to main (8a23917) after user approval of the impact assessment.

Verification (orchestrator, live):
1. Full `_reference` package tree (tasks, roles, pages, api_objects, components) imports cleanly with `PYTHONPATH=framework` only
2. 213 API suite (pulled verbatim from build/213) run against fresh-seeded Orderly on 8018 with SINGLE-root PYTHONPATH: exit 0, 1 passed, residue clean

Follow-on: 229 conftest bootstrap needs only `framework/` on sys.path (lesson 46's dual-root requirement collapses). Lesson updated via /kernel/learn.

---

## DEF-013: Production testing requirement missing from step-04-atomize

**Date:** 2026-03-23
**Severity:** High
**Status:** RESOLVED

### What Happened
Level 3 production tests were never planned during task decomposition. The 3-tier testing requirement (Level 1/2/3) only appears in step-06-execute.md and production-testing.md — but test tasks are planned in step 4-5. By step 6 the task list is finalized.

### Expected Behavior
Step 4 should require verifying every deliverable has Level 1, 2, AND 3 tests before moving to step 5.

### Actual Behavior
Agent created tasks with only Level 1 (file_exists) and some Level 2 (run_code). No Level 3 production tests. User caught the gap manually.

### Root Cause
production-testing.md is referenced only in step-06 (execute). Step-04 (atomize) — where test tasks are planned — has no mention of testing hierarchy or production testing.

### Resolution
**RESOLVED 2026-03-23** — Added "Testing Completeness Check (MANDATORY)" section to step-04-atomize.md:

1. References production-testing.md via wikilink (was only in step-06)
2. Documents 3-tier hierarchy (L1/L2/L3) inline
3. Mandatory checklist: for each deliverable, verify L1/L2/L3 test tasks exist
4. Explicit "simulate is NOT Level 3" rule
5. Common L3 gaps list to watch for
6. Updated Output section to include "testing completeness verified"

Files modified:
- `.claude/skills/task-builder/references/step-04-atomize.md` — Added testing completeness section

---

## Template

```markdown
## DEF-XXX: Brief description

**Date:** YYYY-MM-DD
**Severity:** Critical | High | Medium | Low
**Status:** OPEN | IN_PROGRESS | RESOLVED

### What Happened
[Description]

### Expected Behavior
[What should have happened]

### Actual Behavior
[What actually happened]

### Root Cause
[Why it happened]

### Impact
[Consequences]

### Proposed Fix Options
[Solutions]

### Resolution
[How it was fixed, or TBD]
```
