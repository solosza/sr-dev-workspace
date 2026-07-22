# Rule Inventory: Hard-Enforced vs Soft (Protocol-Only) Rules

## Purpose

Inventory of all kernel rules, categorized by enforcement mechanism. Soft rules are candidates for JIT (Just-In-Time) injection at the PreToolUse boundary.

---

## Hard-Enforced Rules (Hook-Blocked)

These rules are mechanically enforced by hooks. Violations are blocked before the action executes.

### Universal Gate Enforcer (`universal-gate-enforcer.py`)

| # | Rule | Gate | Mechanism | Line(s) |
|---|------|------|-----------|---------|
| H1 | Session must be started before any non-safe action | Gate 1 | Checks `session_started` in session_state.json; blocks Write/Edit/Bash if false | 219-224 |
| H2 | Lessons must be recorded after failures before continuing | Gate 2 | Checks `needs_learn` flag; blocks until `/kernel/learn` clears it | 227-233 |
| H3 | Protocol must be anchored before non-safe actions | Gate 3 | Checks `anchored` in workflow state; blocks if false (skipped for one-shot agents) | 236-245 |
| H4 | Action counter limit triggers re-anchor | Gate 4 | Counts actions via JSONL; blocks at limit, generates token; resets on anchor | 125-165, 266-267 |
| H5 | Anchor token must be confirmed (anti-quick-anchor) | Gate 5 | Blocks if `pending_anchor_token` exists but `anchor_token_confirmed` is false | 248-255 |
| H6 | Protocol hash verified at entry (removed from execution path) | Gate 6 (removed) | Was: hash check per action. Now: entry-only validation at session-start | 257-263 |

Counter logic: All Bash increments; Write/Edit to `.claude/` paths skip entirely; Write/Edit to project files increment. Safe Bash (ls, cat, grep, git status, etc.) skips gate checks but still increments.

### Domain Gate Enforcer (`sr_dev-gate-enforcer.py`)

| # | Rule | Mechanism | Line(s) |
|---|------|-----------|---------|
| H7 | No `cd` in Bash commands | Delegates to `bash_validation.check_cd()` — regex detects standalone `cd` outside quotes | 70-72 (enforcer), bash_validation.py:12-48 |
| H8 | No direct `intent.py record` calls | String match blocks `intent.py record` unless prefixed with `KERNEL_BACKLOG_INTENT=1` marker | 49-68 |
| H9 | Anchor ceremony completeness on Write/Edit | Delegates to `state_validation.check()` — verifies all 7 ceremony fields populated | 33-36 (enforcer), state_validation.py:10-71 |

### Code Quality Validator (`code_quality.py`, called by domain enforcer on Write/Edit)

| # | Rule | Detection | Line(s) |
|---|------|-----------|---------|
| H10 | No debug statements (print, console.log, debugger, etc.) | Regex per file extension, line-by-line | code_quality.py:18-50, 89-100 |
| H11 | No hardcoded secrets (password, api_key, token, etc.) | Regex patterns, language-agnostic | code_quality.py:53-61, 103-113 |
| H12 | No wildcard imports (`from X import *`) | Regex per file extension | code_quality.py:64-68, 116-128 |
| H13 | No skipped tests (.skip, @pytest.mark.skip, xit, etc.) | Regex in test files only | code_quality.py:71-78, 130-144 |
| H14 | File size ≤ 300 lines | Line count check | code_quality.py:81, 148-152 |

Note: HTML files are exempt from code quality checks (line 41 of domain enforcer).

### PostToolUse Hooks

| # | Rule | Mechanism | File |
|---|------|-----------|------|
| H15 | Test failure triggers learn obligation | Detects pytest/jest/etc. with non-zero exit or failure patterns in output; sets `needs_learn: true` | test-failure-detector.py |
| H16 | Action logging (append-only ledger) | Appends every Write/Edit/Bash to actions.jsonl; per-agent routing when agent_id set | actions-log-appender.py |

---

## Soft Rules (Protocol-Only / Lessons-Only)

These rules exist only as written instructions in the protocol, lessons, or skill files. The agent must self-enforce them. They are candidates for JIT injection.

### From RULE ZERO (lessons.md)

| # | Rule | Source | JIT Candidacy | Rationale |
|---|------|--------|---------------|-----------|
| S1 | Never assume, always verify — read files before acting | RULE ZERO | **HIGH** | Could inject "verify before write" reminder at PreToolUse for Write/Edit targeting files the agent hasn't Read in the current session |
| S2 | Never quick-anchor | RULE ZERO | LOW | Already mechanically enforced via Gate 5 (anchor token). Residual risk is ceremony shortcuts, which are caught by state_validation.py (H9) |
| S3 | Always use wikilink tiered indexing (>50 lines → extract) | RULE ZERO | **MEDIUM** | Could check content length at Write time and inject "consider extracting" for SKILL.md/workflow.md files exceeding threshold |
| S4 | Never improvise, never skip steps — follow commands exactly | RULE ZERO | LOW | Too abstract for mechanical injection. This is a meta-rule about following other rules |
| S5 | Never stop cycling, never skip HUMAN REQUIRED tasks | RULE ZERO | LOW | Cycling-specific; would require tracking cycling state at PreToolUse, high complexity |
| S6 | Always use kernel commands for kernel operations | RULE ZERO | **MEDIUM** | Could detect writes to `docs/backlog/` without `/kernel/backlog` invocation context |
| S7 | Use background agent + `env -u CLAUDECODE` for run-task.sh | RULE ZERO | LOW | Only relevant during pipeline execution; narrow trigger surface |
| S8 | Execute-pipeline with multiple backlogs: strictly sequential | RULE ZERO | LOW | Pipeline orchestration logic, not a per-action check |
| S9 | Never bundle actions into one task | RULE ZERO | LOW | Task decomposition happens during planning, not at tool-use time |
| S10 | Backlog report says "execute-pipeline" not "task-builder" | RULE ZERO | LOW | Output formatting rule; trivial and narrow |

### From Lessons (Quality Gates & Anti-Patterns)

| # | Rule | Source | JIT Candidacy | Rationale |
|---|------|--------|---------------|-----------|
| S11 | Always verify L1/L2/L3 testing completeness during atomization | Lesson (testing-completeness.md) | LOW | Planning-phase rule, not a per-action gate |
| S12 | Never spawn agents unless for prod-test or run-task.sh | Lesson (RULE ZERO) | **HIGH** | Could intercept Agent tool calls and inject a reminder about the restriction |
| S13 | No `cd` in Bash commands | Lesson (RULE ZERO) | ALREADY HARD (H7) | Mechanized after repeated violations |
| S14 | Cross-repo pytest needs `--rootdir=<target>` | Lesson (cross-repo-pytest.md) | **MEDIUM** | Could detect `pytest` commands targeting paths outside cwd and inject rootdir reminder |
| S15 | Protocol validation at entry, not execution | Lesson (multi-agent-orchestration.md) | ALREADY IMPLEMENTED | Gate 6 was removed from execution path |
| S16 | Per-agent state isolation for multi-agent work | Lesson (multi-agent-orchestration.md) | LOW | Architecture pattern, not a per-action check |
| S17 | Semantics gate scripts must be AST-based, not string-grep | Lesson (#39, #43, #44) | **MEDIUM** | Could detect `pytest` or `python` commands in `tasks/` that import `re` without `ast` and inject warning |
| S18 | Vocab lexicon check on design docs feeding pipelines | Lesson (#45) | **MEDIUM** | Could inject vocab-check reminder when writing to files matching certain domain patterns |
| S19 | Verify import roots (PYTHONPATH) before running pytest | Lesson (#46) | **MEDIUM** | Could detect `pytest` commands and inject PYTHONPATH reminder if not set |
| S20 | Don't prefix imports with `framework.` inside framework code | Lesson (platform-deepeval) | LOW | Narrow domain rule; code_quality.py could handle with pattern but very project-specific |
| S21 | When blocked by hook, report to user — don't modify system state | Lesson (#42, RULE ZERO) | LOW | Meta-rule about obstacle response behavior |
| S22 | Healthcare vocab ban list (hmsa, claim, patient, member, etc.) | Lesson (#45) | **MEDIUM** | Could be added to code_quality.py as a domain-specific content check |

---

## JIT Candidacy Summary

### Tier 1 — High Candidacy (clear trigger, high value, low complexity)

| Rule | Injection Point | Trigger | Injected Content |
|------|----------------|---------|-----------------|
| S1 (verify before acting) | PreToolUse: Write/Edit | Target file not in session's Read history | "RULE ZERO: You haven't Read this file yet. Verify before writing." |
| S12 (no unnecessary agents) | PreToolUse: Agent | Any Agent tool call | "RULE: Only spawn agents for prod-test or run-task.sh. Can you do this work yourself?" |

### Tier 2 — Medium Candidacy (clear trigger but more complex to implement)

| Rule | Injection Point | Trigger | Injected Content |
|------|----------------|---------|-----------------|
| S3 (wikilink tiering) | PreToolUse: Write | Content >50 lines targeting SKILL.md/workflow.md/step files | "RULE: Files >50 lines of detail should extract subtopics to reference files." |
| S6 (use kernel commands) | PreToolUse: Write | Path matches `docs/backlog/*.md` without kernel command context | "RULE: Use /kernel/backlog for backlog creation, not direct writes." |
| S14 (cross-repo pytest rootdir) | PreToolUse: Bash | `pytest` + path outside workspace root | "RULE: Pass --rootdir=<target-repo> when running pytest on external repos." |
| S17 (AST-based semantics) | PreToolUse: Write | Writing test scripts that use `re.search` without `ast` imports | "RULE: Semantics checks must be AST-based, not string-grep." |
| S18/S22 (vocab check) | PreToolUse: Write | Content contains banned vocab terms | "RULE: Clean-room vocab violation detected. Check lexicon." |
| S19 (PYTHONPATH for pytest) | PreToolUse: Bash | `pytest` command without explicit PYTHONPATH | "RULE: Verify PYTHONPATH includes required roots before running pytest." |

### Tier 3 — Low Candidacy (abstract, narrow, or already enforced)

S2, S4, S5, S7, S8, S9, S10, S11, S16, S20, S21 — these are either too abstract for mechanical injection, too narrow in trigger surface, or already handled by existing hooks.

---

## Statistics

- **Hard-enforced rules:** 16 (H1–H16)
- **Soft rules inventoried:** 22 (S1–S22)
- **High JIT candidacy:** 2 (S1, S12)
- **Medium JIT candidacy:** 6 (S3, S6, S14, S17, S18/S22, S19)
- **Low/Already enforced:** 14
