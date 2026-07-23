# Canonical Kernel — Prod-Test Report (Backlog 286)

**Date:** 2026-07-23
**Subject:** `isagawa-co/isagawa-kernel-canonical` @ `cc0555b` (branch `canonical-fixdelta-graft`)
**Verdict:** ✅ **PASS** — clean-install bootstrap confirmed, regression green, every injected base-failure caught.
**Layer:** 2 (clean install + integration + affirmative failure-injection). Layer 1 (per-fix unit tests) was already green in 285.

---

## Method

Cloned the **committed** canonical into a fresh disposable install (`git clone -b canonical-fixdelta-graft`) — a clean checkout, not the scarred build workspace — then bootstrapped, ran the carried regression suite, and ran an affirmative canary that deliberately injects each base failure mode and asserts the hardening **catches** it. Orchestrator (me) ran and verified every result live (lesson #39); no runner self-report was trusted.

## Scope reconciliation (important)

286's original backlog listed 5 canary modes, but 4 of them target the **optional layers** we deliberately kept **out** of the minimal base:

| Original mode | Needs | In base? |
|---|---|---|
| Completion-truth oracle (false-done-no-artifact) | 276 observability | ❌ optional layer |
| Stranded worktree deliverable | 276 observability | ❌ optional layer |
| Relative `DATABASE_URL` fixture linter | 273 gate-integrity | ❌ optional layer |
| Build-verb → sonnet router | 272 model-router | ❌ optional layer |
| Empty-output step recovery | base empty-retry | ✅ base |

So the canary was **re-scoped to the base hardening's real failure modes** (270 + 271 + 262 + 244). The four optional-layer modes are validated when those layers are packaged and prod-tested separately — not against a base-only kernel.

---

## Results

### 1. Clean-install bootstrap ✅
- Cloned committed canonical → structure intact: `CLAUDE.md`, `run-task.sh`, `lib/common.sh`, 7 kernel commands, `domain-setup` command present.
- `lib/model-router.sh` correctly **absent** (optional 272 layer) — and the runner still loads: `bash -n` OK, `source lib/common.sh` clean, all hardening fns defined (`verify_completion_write`, `check_stall`, `skip_current_task`). Confirms the graft fixed the latent "runner sourced a missing file" break.

### 2. Regression suite (fresh install) ✅ 2/2
- `test_l2_completion_persistence.sh` (270 RH-05) — **PASS**
- `test_wi03_routed_state_isolation.sh` (271 WI-03) — **PASS**

### 3. Canary — affirmative failure-injection ✅ 6/6 caught
| Mode | Injection | Caught by |
|---|---|---|
| CANARY-1 (270 RH-01) | task done but missing from `completed_tasks` | `verify_completion_write` re-persisted it |
| CANARY-2 (271 WI-02) | routed agent skip | wrote agent file; **parent workflow byte-identical** |
| CANARY-3 (262/270 RH-02) | stale heartbeat + work remaining | `check_stall` flagged + marked workflow `stalled` |
| CANARY-3neg | fresh heartbeat | healthy — **no false stall** (negative control) |
| CANARY-4 (base) | empty/eof `claude -p` output | classified `no_signal` — never silent-done; runner backs off + retries |
| CANARY-5 (244) | two concurrent agents skip | each touched only its own workflow — no cross-agent clobber |

The canary now ships in the canonical (`tests/test_canary_base_modes.sh`).

---

## Findings

- **F-1 (test-script defect, kernel unaffected):** the canary false-failed 4/6 on first run — native Windows `python` read raw `/d/...` MSYS sandbox paths as `\d\...`. Kernel code was compliant (regression green); fixed with `cygpath -m` at the sandbox root. Lesson recorded (MR-03 recurrence 2); flagged a reusable `win_path()` test-support helper as a future optional-layer improvement. No kernel change.

## Gate for 287 (publish)
Layer-2 validation is complete and green. **287 (publish canonical as single source of truth + deprecate the ~30 stale copies) is OWNER-SIGN-OFF GATED** — it creates/re-points/archives *published* repos and must not run autonomously. Ready for owner go.
