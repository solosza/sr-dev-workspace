# Worktree Prune Report — 289 (task 003)

**Date:** 2026-07-23T08:57Z
**Operator:** kernel agent (automated worktree-prune task)

## Summary

Successfully pruned 37 stale agent-* worktrees. Preserved 4 KEEP worktrees with unmerged/unreviewed branches. Registry cleaned.

## Before / After

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Total worktrees** | 42 | 5 | -37 |
| Main | 1 | 1 | — |
| Agent worktrees | 41 | 4 | -37 |
| KEEP (unmerged) | 4 | 4 | — |
| PRUNE-ELIGIBLE | 37 | 0 | -37 |

## Removed (37 worktrees)

All removed worktrees were finished agent-* runs with branches merged into `main` and no pending review status. Contained only state churn (`.claude/state/*.json`), no real work product lost.

| Agent ID | Branch | Notes |
|----------|--------|-------|
| agent-a046b69c360dd46b5 | worktree-agent-a046b69c360dd46b5 | Merged |
| agent-a04d789342368621a | worktree-agent-a04d789342368621a | Merged |
| agent-a1270b22844053784 | worktree-agent-a1270b22844053784 | Merged |
| agent-a33c1e769f41172be | worktree-agent-a33c1e769f41172be | Merged |
| agent-a3b8610f0611bd1c4 | worktree-agent-a3b8610f0611bd1c4 | Merged |
| agent-a450b3e7865d74886 | worktree-agent-a450b3e7865d74886 | Merged |
| agent-a46e5126609b5c3c5 | worktree-agent-a46e5126609b5c3c5 | Merged |
| agent-a5498709192caea64 | worktree-agent-a5498709192caea64 | Merged |
| agent-a59e7ff6376a0367e | worktree-agent-a59e7ff6376a0367e | Merged |
| agent-a5ba849999644bfde | worktree-agent-a5ba849999644bfde | Merged |
| agent-a5d4b822338de0d18 | worktree-agent-a5d4b822338de0d18 | Merged |
| agent-a6054de8924884b88 | worktree-agent-a6054de8924884b88 | Merged |
| agent-a637756e23866798b | worktree-agent-a637756e23866798b | Merged |
| agent-a6a13404a71cefe54 | worktree-agent-a6a13404a71cefe54 | Merged |
| agent-a71e818a73aa39687 | worktree-agent-a71e818a73aa39687 | Merged |
| agent-a737dbad64fec608f | worktree-agent-a737dbad64fec608f | Merged |
| agent-a7560104f65d9033f | worktree-agent-a7560104f65d9033f | Merged; dirty gitlink tracked (state-churn only) |
| agent-a783cc1172810c3e8 | worktree-agent-a783cc1172810c3e8 | Merged |
| agent-a8f1b888f5ec6fcdd | worktree-agent-a8f1b888f5ec6fcdd | Merged |
| agent-a9e6bb539e4a71866 | worktree-agent-a9e6bb539e4a71866 | Merged |
| agent-aac43fb78d699557b | worktree-agent-aac43fb78d699557b | Merged |
| agent-aaedba1485b80552b | worktree-agent-aaedba1485b80552b | Merged |
| agent-ab9caa448d56178cf | worktree-agent-ab9caa448d56178cf | Merged |
| agent-abfbe941 | worktree-agent-abfbe941 | Merged; dirty gitlink tracked (state-churn only) |
| agent-ac464e98e915cecab | worktree-agent-ac464e98e915cecab | Merged |
| agent-aced922cd7d9c1b5d | worktree-agent-aced922cd7d9c1b5d | Merged |
| agent-ad3b8b55433bfc8ed | worktree-agent-ad3b8b55433bfc8ed | Merged |
| agent-ad4d2dae8f8173535 | worktree-agent-ad4d2dae8f8173535 | Merged |
| agent-ad508742308465fc3 | worktree-agent-ad508742308465fc3 | Merged |
| agent-addb848227d134ba4 | worktree-agent-addb848227d134ba4 | Merged |
| agent-ae01e334316f3ce24 | worktree-agent-ae01e334316f3ce24 | Merged |
| agent-ae3b0db5d9be5a0c6 | worktree-agent-ae3b0db5d9be5a0c6 | Merged |
| agent-ae4d1683201288f55 | worktree-agent-ae4d1683201288f55 | Merged |
| agent-ae6ceeb0701b1579d | worktree-agent-ae6ceeb0701b1579d | Merged |
| agent-aebea906db56e78a7 | worktree-agent-aebea906db56e78a7 | Merged |
| agent-af5c22d031567ad8b | worktree-agent-af5c22d031567ad8b | Merged |
| agent-af89ba412ddacf936 | worktree-agent-af89ba412ddacf936 | Merged |

## Skipped — KEEP (4 worktrees)

All KEEP worktrees have unmerged/unreviewed branches. Preserved to avoid losing in-progress work.

| Agent ID | Branch | Status | Reason |
|----------|--------|--------|--------|
| agent-a1b4a8081df5eb1e8 | worktree-agent-a1b4a8081df5eb1e8 | unmerged | `git branch --no-merged main` identified as unmerged work |
| agent-a73eb60730cced699 | worktree-agent-a73eb60730cced699 | unmerged | `git branch --no-merged main` identified as unmerged work |
| agent-adf30ca91b9dd4ffb | worktree-agent-adf30ca91b9dd4ffb | unmerged | `git branch --no-merged main` identified as unmerged work |
| agent-ada9b04dbe2276d91 | worktree-agent-ada9b04dbe2276d91 | unreviewed/held | Backlog 208 (build/208-qa-build-reference-tests-ui) — orchestrator-marked ENV-BLOCKED (UT-04 click-navigation wedge), merge held pending env fix. Review status: unreviewed. Also tracked as dirty gitlink in parent index (state-churn only). |

## Completion Notes

- `git worktree prune` completed successfully (cleaned dead registry entries).
- All 37 PRUNE-ELIGIBLE worktrees removed with `--force` (all contained state-churn, no data loss).
- 4 KEEP worktrees preserved (unmerged/unreviewed).
- `git worktree list` verification: 5 total (main + 4 KEEP) — **correct state achieved**.
- No uncommitted work in main or KEEP worktrees was affected by this operation.
