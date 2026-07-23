# Canonical Kernel — Graft Base Runner Hardening onto Minimal

## Status
COMPLETE (2026-07-23) — canonical built + validated live at Layer 1; commit `e36c18a` on `canonical-fixdelta-graft`, pushed to `isagawa-co/isagawa-kernel-canonical`. Layer-2 clean-install proof is [[286-kernel-test-prodtest-canonical-kernel]].

### Completion evidence
- **common.sh:** clean-superset graft — `verify_completion_write` (270 RH-01), `check_stall` (270 RH-02), `resolve_workflow_file` + agent-routed `skip_current_task` (271/244), utf-8-sig defensive reads.
- **run-task.sh WIRED (not just present):** `skip_current_task "$AGENT_ID"` (271 — fixes the empty-arg WI-02 parent-write bug) · `verify_completion_write` after task_done on BOTH fresh + resume paths (270) · heartbeat stamped each iteration → `agent-{id}-heartbeat` (262) · 272 router demoted to OPTIONAL layer (guarded `source` + `command -v route_model/upgrade_model`; base runs on `DEFAULT_MODEL=claude-opus-4-8`). This also FIXED a latent break: the layer-strip had left `run-task.sh` sourcing the now-missing `lib/model-router.sh` — the canonical runner could not start until this graft.
- **Validated live:** 270 RH-05 PASS, 271 WI-03 PASS, `bash -n` OK, runtime source-smoke OK (all hardening fns defined, router gracefully absent). Orchestrator re-ran gates live (lesson #39).
- 244 per-agent routing was ALREADY wired in minimal's runner (per-agent workflow seed, routed PRECHECK/current-task) — confirmed, not re-added.

## Priority
High — 30 kernel installs on the machine, only `sr_dev_workspace` has the hardening; the minimal base is the right distributable shape but has none of it. Establish ONE lean canonical (minimal + base hardening) that every harness includes going forward. First of the 3-backlog kernel-consolidation chain.

## Scope decisions (2026-07-23, owner)
- **Minimal stays minimal** = base RUNNER hardening only. It is the common base ALL harnesses include going forward, so it must be lean.
- **IN (base hardening):** 270 (completion write-verify + stall detection + commit-on-complete) · 262 (heartbeat; empty-retry already in minimal) · 271 (routed `skip_current_task`) · **244 per-agent routing (`KERNEL_AGENT_ID`)** — owner: concurrency IS base · 280 (block-to-completion spawn skill)
- **OUT → optional layers (NOT in minimal):** 276 observability · 273 gate-integrity · 272 model-router. These are opt-in layers distributed separately (carve out later).
- **Sync/update mechanism: DEFERRED** — how harnesses track the canonical is a workspace/factory concern, not sorted now.

## Progress
- ✅ Safety feature branch `canonical-fixdelta-graft` on `kernel-minimal` + private backup `isagawa-co/isagawa-kernel-canonical` (both branches pushed).
- ✅ Repo consolidation started: `isagawa-kernel-a`/`-b` ARCHIVED; `isagawa-kernel` kept as reference; `isagawa-kernel-canonical` = canonical going forward.
- ✅ Over-ported layers (272/273/276) STRIPPED off the canonical (`e0a238b`) — 280 skill + 270/271 tests retained. Canonical is now lean.

## Remaining requirements (the base-hardening graft)
- **Graft `lib/common.sh`:** port the 244 per-agent state routing (`KERNEL_AGENT_ID` → `agent-{id}-workflow.json` resolution) + `verify_completion_write` (270) + `check_stall` (270) + the 271-fixed `skip_current_task` (routes off agent_id). Minimal's `common.sh` has NONE of these — port the routing infra + the helpers together (they're intertwined: 271 depends on 244).
- **Graft `run-task.sh`:** wire the hardening into minimal's 473-line runner — state pre-init routes by `KERNEL_AGENT_ID` (244); call `verify_completion_write` after task completion (270); write + check the HEARTBEAT each loop (262); `check_stall` on stale heartbeat (270); commit-on-complete (270); fresh-base worktree note (271). Reconcile against minimal's structure (different from the 661-line workspace runner).
- **WIRING, not just presence (avoid the false-complete trap):** the runner must actually CALL the hardening — functions present-but-unwired is a false completion (the exact class 270/273 exist to catch). The run-task.sh graft is what makes the hardening live; its proof is 286's integration prod-test.
- **Proof:** the 2 base tests pass live on the canonical — 270 RH-05 (`verify_completion_write` re-persists) + 271 WI-03/04 (routed isolation) — orchestrator re-runs live (lesson #39). Full runtime proof is 286.
- **Clean-room:** no client/workspace paths hardcoded; generic distributable kernel.

## References
- Canonical (work here): `D:\my_ai_projects\project_test_repos\kernel-minimal` branch `canonical-fixdelta-graft` (remote `isagawa-co/isagawa-kernel-canonical`)
- Fix source: `sr_dev_workspace` `run-task.sh` @661 + `lib/common.sh` @405 (has 244 routing + `verify_completion_write`/`check_stall`/`skip_current_task`)
- Base gaps confirmed: minimal has 0 `KERNEL_AGENT_ID`, 0 heartbeat, HAS empty-retry
- Next in chain: [[286-kernel-test-prodtest-canonical-kernel]], [[287-kernel-build-publish-canonical-deprecate-sprawl]]

## Task Builder Input
- **Deliverable:** The lean canonical kernel = minimal base + grafted base runner hardening (244 routing + 270 + 271 + 262 heartbeat + 280 skill), WIRED into `run-task.sh`, with 270 RH-05 + 271 WI-03/04 passing live. No 272/273/276.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\kernel-minimal (branch `canonical-fixdelta-graft`)
- **Scope:** BUILD
- **Constraints:** Base runner hardening ONLY (272/273/276 are optional layers, out). 244 per-agent routing IS base. Port + wire — presence-without-wiring is a false complete. Orchestrator re-runs the 2 base tests live before done. STRICTLY SEQUENTIAL (gates 286/287). Delicate cross-base graft — do it carefully, not rushed.
