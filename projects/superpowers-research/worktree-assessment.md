# Worktree Skill Assessment

**Skill:** using-git-worktrees (Superpowers)
**Assessed against:** Kernel git workflow + Claude Code's native EnterWorktree tool

---

## What the Superpowers Worktree Skill Does

### Core Mechanics
1. **Step 0: Detect existing isolation** — checks if already in a linked worktree (compares `GIT_DIR` vs `GIT_COMMON`). If already isolated, skips creation.
2. **Step 1a: Prefer native tools** — if platform has native worktree support (like `EnterWorktree`), use it instead of raw git commands.
3. **Step 1b: Git worktree fallback** — creates worktree in `.worktrees/` (or configured dir), ensures it's in `.gitignore`, creates new branch.
4. **Step 3: Project setup** — auto-detects package manager (npm, cargo, pip, poetry, go) and installs dependencies.
5. **Step 4: Verify clean baseline** — runs tests in the new worktree before starting work.

### Key Principles
- Never create worktree if already in one
- Prefer native tools over git fallback
- Verify directory is gitignored before creating
- Always verify clean test baseline before proceeding

---

## Claude Code's Native EnterWorktree Tool

### What It Does
- Creates a git worktree inside `.claude/worktrees/` with a new branch based on HEAD
- Switches the session's working directory to the new worktree
- On session exit, prompts user to keep or remove the worktree
- Supports VCS-agnostic isolation via hooks (WorktreeCreate/WorktreeRemove)

### Limitations
- Only activates when user explicitly says "worktree"
- No automatic dependency installation
- No test baseline verification
- No detection of existing isolation
- Simple — creates and switches, nothing more

### Comparison

| Aspect | Superpowers Skill | EnterWorktree Tool |
|--------|------------------|-------------------|
| Isolation detection | Yes (Step 0) | No |
| Native tool preference | Yes (Step 1a) | N/A — IS the native tool |
| Directory management | `.worktrees/` with gitignore check | `.claude/worktrees/` (auto) |
| Branch creation | Yes, named branch | Yes, auto-named branch |
| Dependency install | Yes, auto-detect | No |
| Test baseline | Yes, runs tests first | No |
| Cleanup | Manual (finishing-a-development-branch skill) | Prompted on session exit |
| Activation | Protocol-driven (always for new work) | User must say "worktree" |

---

## Interaction with Kernel Git Workflow

### Current Kernel Pattern
- **Workspace repo (sr_dev_workspace):** all work on `main`, no branches
- **Kernel repo (isagawa-kernel):** feature branches per pipeline, golden master pattern
- **QA platform:** feature branches, PRs to main
- No worktree usage anywhere

### What Worktrees Would Change
1. **Pipeline isolation** — each execute-pipeline run could work in its own worktree, preventing branch pollution on main
2. **Parallel safety** — concurrent agents (current state contention problem!) could each have their own worktree with separate working directory
3. **Rollback** — failed work is contained in a worktree that can be deleted without touching main

### What Worktrees Would NOT Fix
- **State file contention** — `.claude/state/` files are in the main repo, not per-worktree. Worktrees share the same `.git` directory but have separate working trees. State files would still conflict unless moved outside the repo.
- **Hook paths** — hooks resolve relative to cwd. If cwd moves to a worktree, hook paths need to be absolute (already a lesson: NEVER USE cd).

---

## Problem Analysis

**Question:** What problem does it solve that branch-per-pipeline doesn't?

**Answer:** Branch-per-pipeline already provides logical isolation but NOT working directory isolation. With branches:
- You switch branches in place — uncommitted changes can conflict
- Only one branch active at a time per working directory
- Switching back loses working state

With worktrees:
- Each branch has its own physical directory
- Multiple branches can be active simultaneously
- No checkout conflicts, no stash needed
- Clean separation of concerns

**However**, the kernel's biggest isolation problem is state file contention from concurrent agents, which worktrees alone don't solve (state files are repo-level).

---

## Recommendation: ADOPT (with caveats)

### Why ADOPT
1. **EnterWorktree already exists** — zero implementation cost, Claude Code has native support
2. **Pipeline isolation** — execute-pipeline could `EnterWorktree` before starting, keeping main clean
3. **Parallel agent safety** — worktrees give each agent a separate working directory
4. **The Superpowers skill's Step 0 detection** is smart — avoid creating worktrees when already in one

### Caveats
1. **State contention unsolved** — worktrees don't fix `.claude/state/` file races. Need per-worktree state or file locking (separate concern).
2. **Hook path impact** — all hook paths must be absolute (already a kernel rule, but becomes critical with worktrees)
3. **Cleanup discipline** — worktrees accumulate if not cleaned up. Need explicit cleanup in `/kernel/complete`.
4. **EnterWorktree is simple enough** — the full Superpowers skill adds dependency install and test baseline, but the kernel's own domain-setup already handles project setup. Don't need the full Superpowers skill — just use EnterWorktree directly.

### Integration Path
1. Add worktree protocol to execute-pipeline: `EnterWorktree` at pipeline start, cleanup at pipeline end
2. Add absolute-path verification to hook enforcement (already exists in lessons, formalize in protocol)
3. Do NOT adopt the full Superpowers worktree skill — it's over-engineered for our use case
4. Use EnterWorktree directly as a single tool call, wrap with kernel conventions (cleanup in `/kernel/complete`)
5. Future: investigate per-worktree state directories to solve the contention problem
