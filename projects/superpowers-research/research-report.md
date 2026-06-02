# Superpowers Integration Research Report

**Date:** 2026-06-01
**Framework:** github.com/obra/superpowers (Jesse Vincent / Prime Radiant)
**Assessed for:** Isagawa Kernel integration

---

## 1. Framework Overview

Superpowers is a composable software development methodology for AI coding agents. It provides 14 skills organized across testing, debugging, collaboration, git workflow, and meta categories. Skills are markdown-based protocol files that instruct the agent on structured workflows — similar to kernel references but focused on development practices rather than infrastructure governance.

The framework supports multiple platforms (Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot) via platform-specific plugin directories. Skills activate automatically when loaded.

**Architecture:** Each skill is a directory under `skills/` containing `SKILL.md` (main instructions) and optional reference files (e.g., `testing-anti-patterns.md`). This mirrors the kernel's skill structure (SKILL.md + references/).

---

## 2. Skills Inventory Summary

| # | Skill | Category | Kernel Status |
|---|-------|----------|---------------|
| 1 | test-driven-development | Testing | **GAP** — no TDD enforcement |
| 2 | verification-before-completion | Testing | Covered — `/kernel/complete` |
| 3 | systematic-debugging | Debugging | Partial — `/kernel/fix` + `/kernel/learn` |
| 4 | brainstorming | Planning | Not covered |
| 5 | writing-plans | Planning | Covered — task-builder |
| 6 | executing-plans | Execution | Covered — execute-pipeline |
| 7 | subagent-driven-development | Execution | Partial — run-task.sh |
| 8 | using-git-worktrees | Git | **GAP** — no isolation |
| 9 | finishing-a-development-branch | Git | Not covered |
| 10 | requesting-code-review | Review | **GAP** — no review dispatch |
| 11 | receiving-code-review | Review | **GAP** — no feedback triage |
| 12 | dispatching-parallel-agents | Parallel | Partial — sequential only |
| 13 | writing-skills | Meta | Partial |
| 14 | using-superpowers | Meta | N/A |

**Summary:** 5 covered, 4 genuine gaps, 5 marginal/partial.

→ Full inventory: `skills-inventory.md`

---

## 3. TDD Skill Assessment

**What it does:** Enforces strict RED-GREEN-REFACTOR with an "iron law" — no production code without a failing test first. Includes verification checklist, anti-pattern reference, and restart triggers when TDD is violated.

**Kernel comparison:** Kernel has L1/L2/L3 test levels and gate contracts that verify tests exist and pass. But it doesn't enforce test-first ordering — BUILD tasks write code, TEST tasks validate afterward. No RED phase exists.

**Recommendation: CONDITIONAL ADOPT** — for code-heavy projects (QA platform, RT automation) as a domain-specific protocol reference. Skip for kernel infrastructure and research work where deliverables are markdown/config. Adapt the RED-GREEN cycle to work within atomicity constraints.

→ Full assessment: `tdd-assessment.md`

---

## 4. Worktree Skill Assessment

**What it does:** Creates isolated git worktrees for development. Detects existing isolation first, prefers native tools (EnterWorktree), falls back to git commands. Includes dependency install and test baseline verification.

**Kernel comparison:** Kernel has zero isolation mechanism. All work happens in-place. Claude Code's `EnterWorktree` tool exists but is unused. The Superpowers skill explicitly prefers native tools like EnterWorktree over raw git commands.

**Recommendation: ADOPT** — use EnterWorktree directly (the full Superpowers skill is over-engineered for our use case). Wire into execute-pipeline for pipeline isolation. Does NOT solve `.claude/state/` file contention (separate concern).

→ Full assessment: `worktree-assessment.md`

---

## 5. Code Review Skill Assessment

**What it does:** Two complementary skills. Requesting: dispatches reviewer subagent with git SHAs and requirements. Receiving: structures feedback handling with VERIFY-before-implement pattern and Critical/Important/Minor triage.

**Kernel comparison:** Anchor Part B reviews inter-anchor work but is self-review by the same agent. Gate contracts provide structural checks only. No fresh-perspective review exists.

**Comparison to @reviewer (backlog 115):** Complementary. Superpowers provides the PROCESS (when/how to review). @reviewer provides the MECHANISM (configured agent). The process should use the mechanism.

**Recommendation: ADOPT** — implement via @reviewer named agent. Add review template with SHA scope and feedback triage. Wire as optional step at execute-pipeline end.

→ Full assessment: `code-review-assessment.md`

---

## 6. Other Notable Skills

**systematic-debugging** — 4-phase root cause analysis. Kernel's `/kernel/fix` + `/kernel/learn` partially covers this. Could inform a future `/kernel/debug` command but low priority since the existing failure loop works.

**subagent-driven-development** — Two-stage review (spec compliance, then code quality) per task. Interesting concept but conflicts with kernel's atomicity rule and NEVER SPAWN AGENTS lesson. The two-stage review idea could inform the @reviewer template.

**brainstorming** — Socratic design exploration before coding. Could be valuable as a pre-task-builder phase but low priority — the user typically provides clear direction.

**dispatching-parallel-agents** — Parallel task execution. Kernel is deliberately sequential to avoid state contention. Skip.

**writing-skills** — Meta-skill for creating new skills. Kernel already has skill structure conventions but no explicit meta-skill. Low priority.

---

## 7. Top Skills to Integrate (Ranked)

| Rank | Skill | Value | Effort | Net Priority |
|------|-------|-------|--------|-------------|
| **#1** | Code review (via @reviewer) | High — catches issues anchor misses | Low — @reviewer spec exists | **High** |
| **#2** | Worktrees (via EnterWorktree) | High — pipeline isolation | Low — native tool exists | **High** |
| **#3** | TDD (domain-specific) | Medium — code projects only | Medium — needs adaptation | **Medium** |

---

## 8. Integration Plan

### #1: Code Review via @reviewer

| Item | Detail |
|------|--------|
| Location | `.claude/agents/reviewer.md` (project-level) |
| Trigger | On-demand `/kernel/review`, optional at pipeline end |
| Changes | New command, review template in `.claude/references/`, @reviewer YAML |
| Model | Sonnet (pattern-matching, not generation) |
| Tools | Read, Glob, Grep only (Write/Edit/Bash blocked) |
| Backlog | 115 already covers @reviewer creation |

### #2: Worktrees via EnterWorktree

| Item | Detail |
|------|--------|
| Location | Protocol reference `.claude/references/worktree-workflow.md` |
| Trigger | Execute-pipeline start (create), `/kernel/complete` (cleanup) |
| Changes | Pipeline step 0 creates worktree, complete cleans up |
| Caveat | Does not solve state file contention |
| Backlog | New item needed |

### #3: TDD (Domain-Specific)

| Item | Detail |
|------|--------|
| Location | `.claude/references/tdd-discipline.md` in target domain repo |
| Trigger | Domain-setup adds to protocol when repo has testable code |
| Changes | BUILD tasks producing code follow RED-GREEN-REFACTOR |
| Caveat | Not for kernel itself, only application repos |
| Backlog | New item needed |

---

## 9. Conflicts Table

| Superpowers Skill | Kernel Mechanism | Conflict | Resolution |
|-------------------|-----------------|----------|------------|
| verification-before-completion | `/kernel/complete` | Duplicate | Skip — kernel gate is hook-enforced |
| writing-plans | task-builder | Duplicate | Skip |
| executing-plans | execute-pipeline | Duplicate | Skip |
| subagent-driven-development | run-task.sh | Partial | Take review idea, skip workflow |
| dispatching-parallel-agents | Sequential pipeline | Philosophy | Skip — deliberate choice |

No hard conflicts. All overlaps resolve cleanly by keeping kernel mechanisms.

---

## 10. Overall Recommendation

### ADOPT 3 skills (selectively):

1. **Code review process** (requesting + receiving) — implemented via @reviewer named agent. Highest value, lowest effort. Backlog 115 covers the mechanism.

2. **Worktree isolation** — via native EnterWorktree tool. Addresses pipeline isolation and parallel agent safety. Needs new backlog item.

3. **TDD discipline** — as domain-specific reference for code projects only. Not for kernel infrastructure. Needs new backlog item.

### SKIP the other 11 skills:
- 5 already covered by kernel mechanisms
- 5 marginal value (partial coverage or nice-to-have)
- 1 meta-documentation only

### Key Principle

Do NOT adopt Superpowers wholesale. Cherry-pick the 3 skills that fill genuine kernel gaps, adapt them to kernel conventions (hooks, gate contracts, atomic tasks), and implement using existing infrastructure. The kernel's enforcement model (hooks + protocol + lessons) is stronger than Superpowers' protocol-only approach — keep the kernel's enforcement, add Superpowers' development practices where they fill real gaps.
