# Worktree Inventory — 289 (task 001)

**Generated:** 2026-07-23T08:46Z
**Source:** `git worktree list` (41 agent-* worktrees + 1 main) cross-referenced against `.claude/state/review-status.json` and `git branch --no-merged main`.

## Method

1. `git worktree list` → 41 `agent-*` worktrees under `.claude/worktrees/`, each on its own `worktree-agent-<id>` branch.
2. `git branch --no-merged main` → identifies branches with commits not yet in `main` (real unmerged work).
3. Searched `review-status.json` for any `agent-<id>` references → only one hit: the `"208"` entry, which is a special (non-`reviewed`-map) key carrying `status: "unreviewed"`, `merge_status: "held_env_blocked"`, and `orchestrator_worktree_branch: "worktree-agent-ada9b04dbe2276d91"`. That worktree's branch tip happens to be a git-ancestor of `main` (no unique commits), but the review-status entry explicitly marks it pending/held, so it's treated as KEEP regardless of the git-merge technicality.
4. Cross-checked `git status --porcelain` on the parent repo: 3 worktrees (`agent-a7560104f65d9033f`, `agent-abfbe941`, `agent-ada9b04dbe2276d91`) are tracked as **dirty gitlinks** in the parent index (`M .claude/worktrees/agent-*`), not plain untracked dirs like the other 38 (`??`). Their internal `git status` shows only routine kernel state-file churn (`.claude/state/actions.jsonl`, `session_state.json`, `sr_dev_workflow.json`, plus stray anchor-log dirs in one case) — no real code/doc work product. Flagged for task 002: removing these needs `git rm --cached` (or equivalent) for the gitlink entry in addition to `git worktree remove`, since the parent repo's index tracks them.

## KEEP (4) — pending review / unmerged, do not prune

| Worktree | Branch | Commit | Reason |
|---|---|---|---|
| `agent-a1b4a8081df5eb1e8` | `worktree-agent-a1b4a8081df5eb1e8` | f15ca98 | Unmerged into `main` (`git branch --no-merged`) |
| `agent-a73eb60730cced699` | `worktree-agent-a73eb60730cced699` | 21cec6f | Unmerged into `main` (`git branch --no-merged`) |
| `agent-adf30ca91b9dd4ffb` | `worktree-agent-adf30ca91b9dd4ffb` | 7430d34 | Unmerged into `main` (`git branch --no-merged`) |
| `agent-ada9b04dbe2276d91` | `worktree-agent-ada9b04dbe2276d91` | 7466bb7 | Explicitly flagged in `review-status.json` under key `"208"`: `status: unreviewed`, `merge_status: held_env_blocked` (backlog 208 UI live-gate paused per lesson #42, ENV-BLOCKED). Also a dirty tracked gitlink in the parent repo — extra reason to leave untouched pending review. |

## PRUNE-ELIGIBLE (37) — finished agent-* runs, branch merged into main, no review-status reference

| Worktree | Branch | Commit | Note |
|---|---|---|---|
| `agent-a046b69c360dd46b5` | `worktree-agent-a046b69c360dd46b5` | 4efd22e | |
| `agent-a04d789342368621a` | `worktree-agent-a04d789342368621a` | bee40ec | |
| `agent-a1270b22844053784` | `worktree-agent-a1270b22844053784` | 40c810f | |
| `agent-a33c1e769f41172be` | `worktree-agent-a33c1e769f41172be` | 43b7c6b | |
| `agent-a3b8610f0611bd1c4` | `worktree-agent-a3b8610f0611bd1c4` | 4b1d734 | |
| `agent-a450b3e7865d74886` | `worktree-agent-a450b3e7865d74886` | ca01e31 | |
| `agent-a46e5126609b5c3c5` | `worktree-agent-a46e5126609b5c3c5` | 65845ed | |
| `agent-a5498709192caea64` | `worktree-agent-a5498709192caea64` | e170c19 | |
| `agent-a59e7ff6376a0367e` | `worktree-agent-a59e7ff6376a0367e` | 370e35f | |
| `agent-a5ba849999644bfde` | `worktree-agent-a5ba849999644bfde` | 0990140 | |
| `agent-a5d4b822338de0d18` | `worktree-agent-a5d4b822338de0d18` | bea49e5 | |
| `agent-a6054de8924884b88` | `worktree-agent-a6054de8924884b88` | 9d826e0 | |
| `agent-a637756e23866798b` | `worktree-agent-a637756e23866798b` | ebd4839 | |
| `agent-a6a13404a71cefe54` | `worktree-agent-a6a13404a71cefe54` | 38accab | |
| `agent-a71e818a73aa39687` | `worktree-agent-a71e818a73aa39687` | b397a20 | |
| `agent-a737dbad64fec608f` | `worktree-agent-a737dbad64fec608f` | 863f562 | |
| `agent-a7560104f65d9033f` | `worktree-agent-a7560104f65d9033f` | a5c8f5b | Dirty tracked gitlink in parent index — needs `git rm --cached` on removal (state-churn only, no real work lost) |
| `agent-a783cc1172810c3e8` | `worktree-agent-a783cc1172810c3e8` | 27d625f | |
| `agent-a8f1b888f5ec6fcdd` | `worktree-agent-a8f1b888f5ec6fcdd` | 652fe8a | |
| `agent-a9e6bb539e4a71866` | `worktree-agent-a9e6bb539e4a71866` | 370e35f | |
| `agent-aac43fb78d699557b` | `worktree-agent-aac43fb78d699557b` | 69cda61 | |
| `agent-aaedba1485b80552b` | `worktree-agent-aaedba1485b80552b` | 770f163 | |
| `agent-ab9caa448d56178cf` | `worktree-agent-ab9caa448d56178cf` | 571c1ef | |
| `agent-abfbe941` | `worktree-agent-abfbe941` | 7466bb7 | Dirty tracked gitlink in parent index — needs `git rm --cached` on removal (state-churn only, no real work lost) |
| `agent-ac464e98e915cecab` | `worktree-agent-ac464e98e915cecab` | 26ab982 | |
| `agent-aced922cd7d9c1b5d` | `worktree-agent-aced922cd7d9c1b5d` | 370e35f | |
| `agent-ad3b8b55433bfc8ed` | `worktree-agent-ad3b8b55433bfc8ed` | 3e8fa1a | |
| `agent-ad4d2dae8f8173535` | `worktree-agent-ad4d2dae8f8173535` | 69e6372 | |
| `agent-ad508742308465fc3` | `worktree-agent-ad508742308465fc3` | affb513 | |
| `agent-addb848227d134ba4` | `worktree-agent-addb848227d134ba4` | 1e7a39a | |
| `agent-ae01e334316f3ce24` | `worktree-agent-ae01e334316f3ce24` | 53a3153 | |
| `agent-ae3b0db5d9be5a0c6` | `worktree-agent-ae3b0db5d9be5a0c6` | c26d623 | |
| `agent-ae4d1683201288f55` | `worktree-agent-ae4d1683201288f55` | a3837b9 | |
| `agent-ae6ceeb0701b1579d` | `worktree-agent-ae6ceeb0701b1579d` | 30aa7bf | |
| `agent-aebea906db56e78a7` | `worktree-agent-aebea906db56e78a7` | 733fda0 | |
| `agent-af5c22d031567ad8b` | `worktree-agent-af5c22d031567ad8b` | 8a8c9ee | |
| `agent-af89ba412ddacf936` | `worktree-agent-af89ba412ddacf936` | 7466bb7 | |

## Summary

- Total worktrees (excl. main): 41
- KEEP: 4
- PRUNE-ELIGIBLE: 37
- No worktrees removed in this task — inventory only, per acceptance criteria.
