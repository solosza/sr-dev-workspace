# State Isolation Design

**Date:** 2026-07-07
**Status:** Confirmed — worktrees provide working-directory isolation

---

## State Isolation Analysis

### How `.claude/state/` Works in Worktrees

Git worktrees share the `.git` directory but have **separate working directories**. Since `.claude/state/` files live in the working directory (not in `.git/`), each worktree gets its own copy of state files.

### Isolation Matrix

| State File | In Main | In Worktree | Isolated? | Notes |
|-----------|---------|-------------|-----------|-------|
| `session_state.json` | Main session | Worktree session | Yes | Each agent writes its own |
| `[domain]_workflow.json` | Main workflow | Worktree workflow | Yes | Separate progress tracking |
| `agent-*-workflow.json` | Per-agent state | Per-agent state | Yes | Already per-agent by design |
| `actions.jsonl` | Main actions | Worktree actions | Yes | Separate action logs |
| `anchor-logs/` | Main anchors | Worktree anchors | Yes | Separate anchor history |

### Key Finding: State Seeding Required

When a worktree is created, untracked files are NOT copied. If `.claude/state/` files are in `.gitignore`, the worktree starts with an empty state directory.

**Workaround:** run-task.sh already handles this via `pre_init_state` — it seeds `session_state.json` before each `claude -p` invocation. The one-shot agent pattern (session-start → anchor → work → complete) naturally handles fresh state.

### Edge Cases

| Scenario | Impact | Mitigation |
|----------|--------|------------|
| Protocol/lessons untracked | Agent can't anchor | Tracked in git → present in worktree |
| Hooks untracked | Hooks don't fire | `.claude/hooks/` tracked in git → present |
| Settings file untracked | No hook registration | `.claude/settings.local.json` tracked → present |
| CLAUDE.md missing | No instructions | Tracked in git → present |

### Conclusion

**State isolation is confirmed.** Worktrees provide natural working-directory isolation. The existing one-shot agent pattern (run-task.sh + `pre_init_state`) handles state seeding. No workaround needed — the design works as-is.

The only requirement: `.claude/protocols/`, `.claude/hooks/`, `.claude/commands/`, `.claude/skills/`, `.claude/lessons/`, `.claude/settings.local.json`, and `CLAUDE.md` must be tracked in git (not gitignored). These are infrastructure files that agents need, and git worktrees only copy tracked files.

---

## State Flow: Worktree Pipeline

```
Main branch (HEAD)
    │
    ├── Agent spawns in worktree (isolation: "worktree")
    │       │
    │       ├── Fresh .claude/state/ (seeded by pre_init_state)
    │       ├── Full .claude/protocols/ (tracked, copied)
    │       ├── Full .claude/hooks/ (tracked, copied)
    │       ├── Full .claude/skills/ (tracked, copied)
    │       │
    │       ├── Agent works: edits code, creates files
    │       ├── State changes stay in worktree
    │       ├── Git commits on feature branch
    │       │
    │       └── Agent completes → returns branch name
    │
    ├── Merge gate: review → accept → git merge feature-branch
    │
    └── Main updated with agent's work
```

No state contention. No shared mutable files. Each agent is fully isolated.
