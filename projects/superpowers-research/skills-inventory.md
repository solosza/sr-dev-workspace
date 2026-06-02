# Superpowers Skills Inventory

**Source:** github.com/obra/superpowers (Jesse Vincent / Prime Radiant)
**Skills count:** 14
**Assessed against:** Isagawa Kernel mechanisms

---

## Complete Skills List

### Testing & Quality

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 1 | **test-driven-development** | Enforces RED-GREEN-REFACTOR cycle with iron law: no production code without a failing test first. Includes verification checklist, anti-patterns reference, and restart triggers. | Partial — kernel has L1/L2/L3 testing levels and gate contracts, but no TDD cycle enforcement | **YES — genuine gap** |
| 2 | **verification-before-completion** | Confirms fixes are actually resolved before marking tasks complete. Evidence-based verification. | Strong overlap — `/kernel/complete` gate already verifies deliverables, reads files, checks gate contracts | No |

### Debugging

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 3 | **systematic-debugging** | 4-phase root cause analysis with tracing and defense techniques. Structured approach to isolating bugs. | Partial — `/kernel/fix` does impact assessment, `/kernel/learn` records lessons, but no structured debugging phases | Marginal |

### Planning & Execution

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 4 | **brainstorming** | Socratic design refinement through questioning and exploration before coding. | No overlap — kernel jumps straight to task decomposition | Marginal |
| 5 | **writing-plans** | Creates detailed implementation plans with bite-sized tasks (2-5 min each). | Strong overlap — task-builder skill decomposes goals into atomic tasks with gate contracts | No |
| 6 | **executing-plans** | Manages batch execution with human checkpoints throughout. | Strong overlap — execute-pipeline + autonomous-cycling + run-task.sh | No |
| 7 | **subagent-driven-development** | Coordinates fast iteration with two-stage review (spec compliance, then code quality). Fresh subagent per task. | Partial — kernel uses one-shot agents via run-task.sh but lacks the two-stage review loop (spec then quality) | Marginal |

### Git & Branching

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 8 | **using-git-worktrees** | Establishes isolated workspaces on separate branches. Detects existing isolation, prefers native tools, falls back to git worktree. | No overlap — kernel has no worktree mechanism; all work happens in-place | **YES — genuine gap** |
| 9 | **finishing-a-development-branch** | Handles merge/PR decisions and worktree cleanup after feature work. | No overlap — kernel has no branch lifecycle management | Marginal (paired with worktrees) |

### Code Review

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 10 | **requesting-code-review** | Dispatches reviewer subagent with git SHAs, plan/requirements context. Pre-review checklist. | Partial — kernel has `/kernel/anchor` Part B (review inter-anchor work) but no dedicated code review dispatch | **YES — genuine gap** |
| 11 | **receiving-code-review** | Manages feedback incorporation — Critical (fix now), Important (fix before proceed), Minor (document for later). | No overlap — kernel has no feedback triage mechanism | Paired with #10 |

### Parallel Work

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 12 | **dispatching-parallel-agents** | Enables concurrent subagent workflows for parallel work on independent tasks. | Partial — kernel spawns one-shot agents sequentially via run-task.sh, not in parallel | Marginal |

### Meta / Infrastructure

| # | Skill | Description | Kernel Overlap | Gap? |
|---|-------|-------------|----------------|------|
| 13 | **writing-skills** | Guides creation of new skills following best practices and structure conventions. | Partial — kernel has skill structure (SKILL.md + references/) but no meta-skill for writing new skills | Marginal |
| 14 | **using-superpowers** | Introduces the skills system itself — how to activate and use skills. | N/A — meta-documentation | No |

---

## Overlap Summary

### Strong Kernel Overlaps (5 skills — already covered)
- **verification-before-completion** → `/kernel/complete` gate
- **writing-plans** → task-builder skill
- **executing-plans** → execute-pipeline + autonomous-cycling
- **using-superpowers** → meta only, not actionable
- **subagent-driven-development** → partially covered by run-task.sh pattern

### Genuine Gaps (3 skills — kernel lacks these)
1. **test-driven-development** — Kernel enforces testing exists (L1/L2/L3) but doesn't enforce the RED-GREEN-REFACTOR cycle or "no code without failing test first" discipline
2. **using-git-worktrees** — Kernel has zero isolation mechanism; all work happens in-place on the current branch, risking main branch pollution
3. **requesting-code-review** + **receiving-code-review** — Kernel anchor Part B reviews work but doesn't dispatch a dedicated reviewer agent with structured feedback triage

### Marginal Gaps (5 skills — nice-to-have)
- **systematic-debugging** — `/kernel/fix` + `/kernel/learn` cover some ground
- **brainstorming** — Design exploration before decomposition
- **finishing-a-development-branch** — Branch lifecycle (paired with worktrees)
- **dispatching-parallel-agents** — Parallel execution (kernel is sequential)
- **writing-skills** — Meta-skill for skill creation

---

## Adoption Priority

| Priority | Skill | Reason |
|----------|-------|--------|
| **P1** | test-driven-development | Biggest quality gap — kernel enforces tests exist but not TDD discipline |
| **P2** | using-git-worktrees | Isolation prevents branch pollution; Claude Code has native `EnterWorktree` tool |
| **P3** | requesting-code-review | Structured review dispatch would catch issues anchor Part B misses |
