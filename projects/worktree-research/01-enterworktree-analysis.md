# EnterWorktree Behavior Analysis

**Date:** 2026-07-07
**Source:** Claude Code tool documentation + Agent tool `isolation` parameter

---

## EnterWorktree Tool

### Behavior

- Creates a new git worktree inside `.claude/worktrees/` with a new branch based on HEAD
- Optional `name` parameter for naming the worktree (random name if omitted)
- Switches the session's working directory to the new worktree
- On session exit, user is prompted to keep or remove the worktree

### Constraints

- Must be in a git repository (or have WorktreeCreate/WorktreeRemove hooks configured)
- Must not already be in a worktree
- Tool documentation says: use ONLY when user explicitly asks for worktree

### Branch Handling

- Creates a new branch from HEAD automatically
- Branch name derived from worktree name
- Standard git worktree behavior: shared `.git` directory, separate working trees

### Cleanup

- Session-exit prompt: keep or remove
- If removed, git worktree is pruned and working directory cleaned up
- If kept, worktree persists with its branch for later use

---

## Agent Tool `isolation: "worktree"` Parameter

### Behavior

- When `isolation: "worktree"` is set on an Agent tool call, the agent runs in a temporary git worktree
- Worktree is automatically cleaned up if the agent makes no changes
- If changes are made, the worktree path and branch name are returned in the result
- This is the preferred integration point for automated pipeline use

### Key Properties

| Property | Value |
|----------|-------|
| Worktree creation | Automatic, handled by Agent tool |
| Branch creation | Automatic, new branch from HEAD |
| Cleanup (no changes) | Automatic removal |
| Cleanup (with changes) | Preserved, path + branch returned |
| State isolation | Separate working directory = separate `.claude/state/` files |
| Nested worktree support | Not supported (can't enter worktree from worktree) |

### Pipeline Integration Implications

1. **No manual worktree management needed** — Agent tool handles lifecycle
2. **Branch name is returned** — enables merge gate workflow
3. **Auto-cleanup on no changes** — no orphaned worktrees from failed/empty runs
4. **Changes preserved** — successful builds stay in worktree branch until merged

---

## Comparison: EnterWorktree vs Agent `isolation: "worktree"`

| Aspect | EnterWorktree Tool | Agent isolation |
|--------|-------------------|----------------|
| Use case | Interactive session | Automated pipeline |
| Cleanup | User-prompted | Automatic |
| Branch return | No (stays in session) | Yes (in result) |
| Pipeline fit | Poor (interactive) | Excellent (automated) |
| State isolation | Yes (separate workdir) | Yes (separate workdir) |

**Recommendation:** Use `Agent(isolation: "worktree")` for execute-pipeline integration. EnterWorktree is designed for interactive use and doesn't fit the automated pipeline pattern.

---

## Git Worktree Fundamentals

- Worktrees share the `.git` directory (object store, refs)
- Each worktree has its own working tree and index
- Each worktree is on its own branch (branches can't be shared between worktrees)
- `.claude/` directory contents in each worktree are independent copies
- Untracked files (like `.claude/state/` contents) are NOT shared — each worktree starts with only tracked files
