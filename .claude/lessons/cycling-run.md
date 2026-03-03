# Cycling Run Lessons

Issues discovered during first autonomous cycling run (7 specs, 28 tests, ~15 min).

---

## 2026-03-03 First Autonomous Cycling Run — 5 Lessons

### Lesson 1: Learn Self-Enforcement — Hook Is Safety Net, Not Only Trigger
- **Issue:** Agent skipped `/kernel/learn` after test failures when `needs_learn` was not set in state.
- **Root Cause:** Treated `needs_learn: true` as the only trigger. Hook hadn't restarted yet, so it never fired.
- **Fix:** Self-enforce: test failed → fix → `/kernel/learn`. Always. Hook or no hook.

### Lesson 2: Complete Gate Possibly Skipped for Specs 003-005
- **Issue:** No visible `Skill(/kernel:complete)` invocation. Format was printed but skill may not have been invoked.
- **Root Cause:** Agent printed the COMPLETE format without invoking the actual skill.
- **Fix:** Invoke `/kernel/complete` via Skill tool. Printing without invoking is a protocol violation.

### Lesson 3: Stale Session State Between Specs
- **Issue:** `session_state.json` context not updated after spec completion — only during anchor.
- **Root Cause:** `/kernel/complete` updated workflow.json but not session_state.json.
- **Fix:** Dual state update after each spec. Both files MUST be updated.

### Lesson 4: Redundant Spec Created by Domain-Setup
- **Issue:** Step-07 created placeholder `001-setup.md` when `specs/` already had files.
- **Root Cause:** Blanket rule without checking if specs/ was already populated.
- **Fix:** Pre-existing specs check: if `specs/` has `.md` files, skip creation.

### Lesson 5: Uncommitted Domain-Setup Output
- **Issue:** After domain-setup, all generated files left untracked. Dirty state on restart.
- **Root Cause:** No step committed output before requesting restart.
- **Fix:** Commit all domain-setup artifacts before setting `needs_restart`.
