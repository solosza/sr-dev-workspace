# Canonical Kernel — Extract Fix-Delta + Build Clean Distributable Kernel

## Status
Open

## Priority
High — 30 kernel installs exist on the machine and only `sr_dev_workspace` has tonight's fixes; the *published* canonical (`isagawa-kernel-a/b`) is 5 months stale with none of them. There is currently NO clean, distributable kernel that has the fixes. Every downstream (factory, platforms, prod-test) depends on there being one. First of the 3-backlog kernel-consolidation chain.

## Summary
Produce ONE clean, distributable canonical kernel = the `kernel-minimal` base (June, 7 commands, 473-line `run-task.sh`, clean shape — the right *distributable* form) grafted with the bounded fix-delta developed in `sr_dev_workspace` tonight (270/271/272/273/276/280). The workspace kernel has the fixes but is a bloated dev environment (661-line `run-task.sh`, 25 commands, 21 skills, project cruft) — NOT distributable. Extract exactly the fixes, nothing else, onto the clean base, and carry the fixes' own regression tests so the canonical ships with proof.

## Requirements
- **Diff first (the fix-delta is bounded and known):** diff the workspace `run-task.sh` + `lib/` + the `spawn-subagent` skill against the `kernel-minimal` base to isolate EXACTLY the fix-delta:
  - `run-task.sh` hardening (270: completion write-verify + stall detection + commit-on-complete; 262 heartbeat/empty-retry/task-resolution if not already in minimal; 271 fresh-base + routed-state containment)
  - `lib/common.sh` helpers `verify_completion_write` + `check_stall` + the `skip_current_task` parent-write fix (270/271)
  - `lib/observability.py` (276) + `lib/kernel_status.py` (276)
  - `lib/gate_integrity.py` (273)
  - `lib/model-router.sh` + `lib/model-routing-config.json` re-weighting (272) — with the current model IDs (opus-4-8/sonnet-5/haiku-4.5)
  - the `spawn-subagent` skill block-to-completion change (280) + the launcher-death lesson
  - the relevant hooks (whatever the fixes depend on)
- **Graft onto the clean minimal base — NOT the workspace:** start from `kernel-minimal` (the distributable shape), apply the delta. Do NOT carry the workspace's 25 commands / 21 skills / project-specific state, backlogs, or projects. Minimal-core + fixes only.
- **Ship with proof:** carry the fixes' regression tests into the canonical (270 RH-05, 271 WI-03/04, 272 MR-03, 273 GI-04, 276 OBS-05) so `286`'s prod-test can run them in a clean install.
- **Verify the graft is coherent:** the fixes were written against the 661-line `run-task.sh`; grafting onto the 473-line minimal base needs reconciliation (line offsets, function presence, sourcing). The regression suite must pass 5/5 on the canonical before this backlog is done — orchestrator re-runs live (lesson #39).
- **Clean-room / no leakage:** no client/project identifiers, no workspace paths hardcoded, no `sr_dev`-specific protocol. A generic distributable kernel.

## References
- Base: `D:\my_ai_projects\project_test_repos\kernel-minimal` (June, clean shape, 7 cmds, 1 lib/py)
- Fix source: `D:\my_ai_projects\project_test_repos\sr_dev_workspace` (`run-task.sh` @661, `lib/{common.sh,observability.py,kernel_status.py,gate_integrity.py,model-router.sh,model-routing-config.json}`, `.claude/skills/spawn-subagent/`)
- Stale published canonical to supersede: `isagawa-kernel-a` (Feb, v3), `isagawa-kernel-b` (Feb) — consolidated in `287`
- The fixes: backlogs 270/271/272/273/276/280 (all in `docs/backlog/done/`)
- Next in chain: [[286-...]] prod-test the canonical, [[287-...]] publish + deprecate sprawl

## Task Builder Input
- **Deliverable:** A clean canonical kernel repo (`kernel-minimal` base + the extracted 270/271/272/273/276/280 fix-delta + their regression tests), with the regression suite passing 5/5 live.
- **Location:** new-repo:D:\my_ai_projects\isagawa-kernel-canonical
- **Scope:** BUILD
- **Constraints:** Graft onto the MINIMAL base, not the workspace — minimal-core + fixes only, no workspace cruft. The fix-delta is bounded (270/271/272/273/276/280); do not re-derive the fixes, port them. Orchestrator re-runs the 5-test regression suite live before done. STRICTLY SEQUENTIAL — 286 (prod-test) and 287 (publish) run only after this is verified. This is the machine's single-source-of-truth reset.
