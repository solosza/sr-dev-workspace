# Kernel Integration Assessment — Named Agents

**Date:** 2026-06-01
**Dependency:** agents-spec-summary.md (task 002)

---

## Hook Inheritance Finding

### What hooks exist in this workspace

| Hook | Type | Enforcement |
|------|------|-------------|
| `universal-gate-enforcer.py` | PreToolUse | Blocks Write/Edit/Bash if session not started, not anchored, needs_learn, action limit exceeded, protocol hash mismatch |
| `sr_dev-gate-enforcer.py` | PreToolUse | Domain-specific code quality, state validation, bash validation (cd blocking) |
| `actions-log-appender.py` | PostToolUse | Appends every Write/Edit/Bash to actions.jsonl + session_state.json summary |
| `test-failure-detector.py` | PostToolUse | Detects test failures, sets `needs_learn: true` |
| `auto-approve-claude-writes.py` | PreToolUse | Auto-approves .claude/ infrastructure writes |
| `agent-inline-execution-blocker.py` | PreToolUse | Blocks inline task execution (forces run-task.sh) |

### Do named agents inherit parent hooks?

**No — not automatically.** The spec is explicit:

1. **Subagents get a fresh context window.** They do not inherit the parent session's hook configuration.
2. **Hooks can be defined per-agent** via the `hooks` frontmatter field (PreToolUse, PostToolUse, Stop).
3. **Project-level settings.json hooks** (SubagentStart, SubagentStop) fire at the parent level when a subagent starts/stops — but these are parent-side lifecycle hooks, not enforcement hooks running inside the subagent.

**Critical implication:** A named agent spawned via @-mention runs **outside kernel enforcement** unless its YAML frontmatter explicitly wires up the same PreToolUse/PostToolUse hooks. This means:

- The universal-gate-enforcer would NOT block unanchored writes
- The actions-log-appender would NOT track the agent's actions
- The test-failure-detector would NOT catch test failures
- The domain gate-enforcer would NOT validate code quality

### Mitigation: Hook inheritance by configuration

To make named agents kernel-governed, each agent's YAML must include:

```yaml
hooks:
  PreToolUse:
    - command: "python .claude/hooks/universal-gate-enforcer.py"
    - command: "python .claude/hooks/sr_dev-gate-enforcer.py"
  PostToolUse:
    - command: "python .claude/hooks/actions-log-appender.py"
    - command: "python .claude/hooks/test-failure-detector.py"
```

**However**, this creates a state contention problem: the hooks read/write shared state files (`session_state.json`, `sr_dev_workflow.json`). Multiple agents writing to the same state files causes the race condition documented in the `state-contention.md` lesson. The `one_shot` flag in session_state.json partially mitigates this (one-shot agents skip anchor/counter/token/hash gates) but the actions_log_appender still writes to shared files.

**Recommendation:** Named agents should either:
1. Run with `one_shot: true` semantics (skip anchor gates, inherit parent's anchored state), OR
2. Use scoped state files (`session_state_<agent-name>.json`) to avoid contention — requires hook refactor

---

## Candidate Assessment

### @reviewer — Code/Doc Review on Demand

**Purpose:** Review code or documentation for quality, patterns, anti-patterns.

| Attribute | Value | Rationale |
|-----------|-------|-----------|
| **Model** | `sonnet` | Review is pattern-matching, not generation. Sonnet is sufficient and faster. |
| **Tools** | `Read, Glob, Grep` | Read-only. Reviewer should never write files. |
| **disallowedTools** | `Write, Edit, Bash` | Explicitly block mutation. |
| **Placement** | **Project** (`.claude/agents/reviewer.md`) | Review rules are project-specific (protocol patterns, anti-patterns, naming conventions). Different projects have different standards. |
| **Hooks** | None needed | Read-only agent — gate enforcer only checks Write/Edit/Bash. No state mutation possible. |
| **maxTurns** | 20 | Bounded review — prevent runaway exploration. |
| **skills** | Protocol + lessons | Preload `.claude/protocols/sr_dev-protocol.md` and `.claude/lessons/lessons.md` so reviewer knows the rules. |

**Fit assessment:** Strong fit. Read-only, no state contention, no hook inheritance needed. Can be deployed immediately.

### @security — Vulnerability Scanner

**Purpose:** Scan files for OWASP top 10, hardcoded secrets, injection risks.

| Attribute | Value | Rationale |
|-----------|-------|-----------|
| **Model** | `sonnet` | Security scanning is pattern-matching. Sonnet handles this well. |
| **Tools** | `Read, Glob, Grep, Bash` | Needs Bash for running security tools (bandit, semgrep, etc.) but NOT Write/Edit. |
| **disallowedTools** | `Write, Edit` | Must not modify code. Reports findings only. |
| **Placement** | **Global** (`~/.claude/agents/security.md`) | Security rules are universal — OWASP, secrets detection, injection patterns don't change per project. Global placement means it's available in all repos. |
| **Hooks** | PreToolUse only: sr_dev-gate-enforcer (bash validation) | Block `cd` in bash. No Write/Edit hooks needed since those tools are disallowed. |
| **maxTurns** | 30 | Security scans may need more turns for large codebases. |
| **background** | `true` | Security scans can run concurrently without blocking main work. |

**Fit assessment:** Good fit. Minimal state contention (no writes). Bash-only hook needed. Background execution is ideal — run security scan while working on features.

### @pr-writer — PR Description Generator

**Purpose:** Generate PR descriptions from git diff output.

| Attribute | Value | Rationale |
|-----------|-------|-----------|
| **Model** | `haiku` | PR descriptions are summarization — haiku is fast and cheap for this. |
| **Tools** | `Read, Bash, Grep` | Needs Bash for `git diff`, `git log`. Read for file context. |
| **disallowedTools** | `Write, Edit` | Should output text, not write files. PR creation happens via `gh pr create` in main session. |
| **Placement** | **Global** (`~/.claude/agents/pr-writer.md`) | PR description format is consistent across projects. Git conventions don't change per repo. |
| **Hooks** | None | Read-only + Bash for git commands. No state mutation. |
| **maxTurns** | 10 | PR descriptions are quick — bounded to prevent over-analysis. |

**Fit assessment:** Strong fit. Lightweight, stateless, fast. Haiku model keeps costs minimal for a high-frequency operation.

---

## Model Routing Conflict: run-task.sh vs Named Agents

### Current state: run-task.sh routing

`run-task.sh` uses `lib/model-router.sh` + `lib/model-routing-config.json` to select a model per task:
- **Keyword-based:** Task content scanned for haiku/sonnet/opus keywords
- **Criteria-based:** Number of acceptance criteria influences tier
- **Frontmatter override:** `model:` in task frontmatter takes highest priority
- **Retry upgrade:** Failed tasks upgrade tier (haiku -> sonnet -> opus)

### Named agent routing

Named agents use YAML `model` field (or `CLAUDE_CODE_SUBAGENT_MODEL` env var). Resolution order:
1. `CLAUDE_CODE_SUBAGENT_MODEL` env var
2. Per-invocation model parameter (Claude chooses)
3. Agent YAML `model` field
4. Parent session model (inherit)

### Conflict analysis

**These are NOT in conflict — they operate in different contexts:**

| Dimension | run-task.sh | Named Agents |
|-----------|-------------|--------------|
| **When** | Autonomous batch execution via `claude -p` | Interactive delegation via @-mention |
| **Who decides** | model-router.sh (deterministic rules) | YAML config (static per agent) |
| **Override mechanism** | Task frontmatter `model:` | `CLAUDE_CODE_SUBAGENT_MODEL` env var |
| **Retry logic** | Upgrades model on failure | No built-in retry/upgrade |

**They could conflict if:** a named agent is used inside run-task.sh (e.g., a one-shot agent delegates to @reviewer during task execution). In that case:
- run-task.sh selected model X for the one-shot agent
- The one-shot agent delegates to @reviewer with model Y (from YAML)
- This is **not a conflict** — it's intentional specialization. The delegated subagent should use its own model (review doesn't need opus).

**Potential issue:** If `CLAUDE_CODE_SUBAGENT_MODEL` is set globally, it overrides ALL named agent model selections, including those carefully chosen per-agent. This env var should NOT be set in production — let each agent use its YAML-specified model.

### Recommendation

No routing conflict exists. The two systems are complementary:
- **run-task.sh** routes the primary task executor (the `claude -p` session)
- **Named agents** route specialized subtasks (review, security, PR writing)

The only guard needed: do NOT set `CLAUDE_CODE_SUBAGENT_MODEL` in environments that use named agents with intentional model assignments.

---

## Summary

| Finding | Status |
|---------|--------|
| Hook inheritance | NOT automatic — agents are ungovererned by default |
| @reviewer fit | Strong — read-only, no contention, deploy immediately |
| @security fit | Good — background execution, minimal hooks needed |
| @pr-writer fit | Strong — lightweight, stateless, haiku-tier |
| Model routing conflict | None — complementary systems |
| Key risk | State contention if agents run kernel hooks on shared state files |
| Mitigation | Read-only agents avoid the problem entirely; write-capable agents need scoped state |
