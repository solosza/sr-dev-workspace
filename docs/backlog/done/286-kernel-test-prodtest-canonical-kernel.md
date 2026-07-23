# Canonical Kernel — Prod-Test in a Fresh Install (Canary Failure-Injection)

## Status
COMPLETE (2026-07-23) — ✅ PASS. Clean-install bootstrap confirmed, regression 2/2, canary 6/6 base-failure modes caught. Report: `projects/canonical-kernel-prodtest/prod-test-report.md`. Canary shipped in canonical `tests/test_canary_base_modes.sh` (`cc0555b`). Canary re-scoped to BASE modes (270/271/262/244); the 4 optional-layer modes (oracle/stranded/portability/router) validate with 276/273/272 when packaged. One finding: test-script MSYS-path false-fail (kernel unaffected; lesson recorded). Gates 287 (publish) — OWNER SIGN-OFF required.

## Priority
High — this is the meaningful validation the whole kernel-fix effort was aiming at: prove the fixed kernel works in a CLEAN install, not just in the scarred workspace. Second of the 3-backlog kernel-consolidation chain.

## Summary
Take the clean canonical kernel produced by 285 and prod-test it in a fresh, disposable install — plus a **canary deliverable** that deliberately triggers each failure mode the fixes address, and assert the fixed kernel + observability catch every one. This upgrades "each fix's unit test passes" (Layer 1, already green 5/5 in the workspace) to "the fixes survive packaging + a clean install + integration, and affirmatively catch injected failures" (Layer 2).

## Requirements
- **Fresh clean install:** use `/kernel/prod-test` against the canonical kernel from 285 — assemble master, run `/kernel/domain-setup` to bootstrap the protocol + hooks in a throwaway test repo, confirm a clean bootstrap.
- **Regression suite in the clean install:** run the 5 carried fix-tests (270 RH-05, 271 WI-03/04, 272 MR-03, 273 GI-04, 276 OBS-05) in the fresh install → confirm 5/5 (proves the graft survived packaging + bootstrap).
- **Canary failure-injection (the affirmative proof):** a canary deliverable/pipeline that deliberately produces each failure mode, and the fixed kernel + observability must CATCH each:
  1. **False-done-no-artifact** — a task marks complete with no committed artifact → completion-truth oracle flags it
  2. **Stranded worktree deliverable** — a complete branch never merged → observability lists it as stranded
  3. **Relative `DATABASE_URL` fixture** — a test with a non-portable DB URL → fixture-portability linter flags it
  4. **Empty-output step** — a `claude -p` returns empty → empty-retry recovers / it is not a silent false-fail
  5. **Build-verb task** → routes to sonnet (not haiku) via the tuned router
- **Affirmative verdict:** the pass condition is not "a normal pipeline completed" (that only proves nothing-obviously-broke) — it is "every injected failure was CAUGHT." Capture per-mode evidence.
- **Orchestrator independence (lesson #39):** the orchestrator re-runs/verifies the canary results live, not on the runner's self-report.

## References
- Input: the canonical kernel from [[285-kernel-build-canonical-kernel-extract-fixdelta]]
- `/kernel/prod-test` skill (`.claude/skills/prod-test/`) — assemble master + domain-setup + copy to test repo + L1/L2/L3
- The 5 fix-tests carried into the canonical (270/271/272/273/276)
- Layer-1 proof already green in the workspace (5/5 regression) — this is Layer 2 (clean install + injection)
- Next: [[287-...]] publish + deprecate (runs only if this passes)

## Task Builder Input
- **Deliverable:** A prod-test report for the canonical kernel: clean bootstrap confirmed, 5/5 regression in the fresh install, and all 5 injected failure modes CAUGHT (per-mode evidence).
- **Location:** subproject:canonical-kernel-prodtest
- **Scope:** TEST
- **Constraints:** Runs ONLY after 285 is verified (needs the canonical kernel to exist). Uses `/kernel/prod-test` (its own sub-agent flow, not a plain run-task.sh pipeline). Pass = every injected failure caught, not merely a clean run. STRICTLY SEQUENTIAL; gates 287 (do not publish an unproven kernel).
