# Factory Runner Empty-Output Hardening — Port 262/270 Empty-Retry to run-spec-factory.sh

## Status
COMPLETE (2026-07-23) — ported directly (not via pipeline; editing the runner via a pipeline is circular). `domain-spec-factory` commit `778d8d3`, pushed.

### Root cause (audited)
`run_step_claude` passed the raw `claude -p` JSON **text** to `extract_session_id`/`extract_result`, which do `test -f "$1"` (expect a **file path**) → always empty → `check_step_completion("")` → **always `no_signal`**. So the runner could never see `STEP_COMPLETE`; it fell to resume, then failed (killed platform-hybrid at step 7). Compounding it: `update_factory_state` and the agent both wrote `current_step`, so state drifted (`current_step=12` while only 2 steps ran).

### As-built fixes
1. **Root:** extract from `$logfile`, not raw text.
2. **Completion-truth (270):** a step counts complete only if it signaled done **AND** `check_step_output` confirms its declared artifact exists — false-complete blocked + retried.
3. **Empty-retry (262):** empty output → backoff + retry fresh (MAX_EMPTY_RETRIES) before resume.
4. **No-session-id fallback:** re-run the step **fresh** instead of "cannot resume → stop".
5. **Drift-repair:** the runner owns `current_step` and recomputes it as the max actually-`_complete` step; agent prompt no longer writes it.
6. **Step-11 schema fix:** gate parse reads the true gate array (`result`, count == total) — a summary `failed:0` can lie (platform-hybrid: 15/31 pass, failed:0).

### Proof
`domain-spec-factory/tests/test_281_completion_truth.sh` → **9/9** (syntax, wiring, drift 12→3, step-11 correctly rejects platform-hybrid 15/31, accepts pci-dss 26/26). `bash -n` clean. `.pre281.bak` saved.

## Priority
High — the meta-factory's runner has the same empty-output fragility that repeatedly broke `run-task.sh`, and it just killed a live platform-hybrid build at step 7. The factory is the tool that builds every platform; its runner must be as hardened as `run-task.sh` now is.

## Summary
`domain-spec-factory`'s `run-spec-factory.sh` fails a step when its `claude -p` invocation returns empty/unparseable output: `run_step_claude()` can't extract a session id or completion signal, its 2 resume attempts also capture nothing, and the step "fails" — stopping the whole build. This is the exact empty-output/session-capture class that backlog 262 (empty-retry) and 270 (completion write-verify, stall detection, `lib/common.sh` helpers) fixed for `run-task.sh`. Port that hardening to the factory runner so a transient empty response is retried without consuming the step, and completion is verified from authoritative output rather than the captured stdout alone.

## Evidence (this session)
- platform-hybrid build, step 7 (Write workflow.md): `-> No completion signal. Attempting resume... -> No session ID captured, cannot resume. -> Step 7 failed after 2 resume attempts. Stopping.` (run `bign3cbd4`, exit 1) — a single empty `claude -p` response with no session id took down the run.
- The identical failure mode is what `run-task.sh` hit repeatedly (lessons #49, ledger) before 262/270 hardened it.

## Requirements
- **Port empty-retry (262):** when a step's `claude -p` returns empty output at/near timeout, retry the step once without consuming the failure budget (the EMPTY-RETRY pattern), rather than treating empty as a hard fail.
- **Robust session-id / completion capture:** determine completion from authoritative evidence (the step's output artifact existing + non-empty, the factory state file advancing) rather than solely parsing stdout for a session id — mirror 270's `verify_completion_write` philosophy (banner/stdout can lie; check the artifact).
- **Session-resume without an id:** when no session id is captured, fall back to re-running the step fresh (skip-logic already supports this) instead of "cannot resume → stop."
- **Reuse, don't reinvent:** the factory has its own `lib/common.sh`; port the relevant 270 helpers (`verify_completion_write`-style artifact confirmation, empty-output handling) rather than writing new logic. Keep parity with `run-task.sh` so both runners behave the same.
- **Regression test:** simulate an empty `claude -p` response for a step and assert the runner retries + recovers rather than failing the build.

## References
- `domain-spec-factory/run-spec-factory.sh` (`run_step_claude()` — the empty-output failure point; `check_step_output()` skip logic), `domain-spec-factory/lib/common.sh`
- `run-task.sh` + `lib/common.sh` on sr_dev main (the 262/270 hardening to port: EMPTY-RETRY, `verify_completion_write`, `check_stall`) — merged this session (commit 71c6798)
- `docs/backlog/262-kernel-fix-runtask-hardening.md`, `270-kernel-fix-runner-hardening-v2.md` (the source patterns)

## Task Builder Input
- **Deliverable:** Hardened `run-spec-factory.sh` (+ factory `lib/common.sh`) in `domain-spec-factory` with empty-retry, artifact-based completion verification, and fresh-re-run fallback when no session id is captured — parity with the now-hardened `run-task.sh` — plus a regression test simulating an empty step response.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\domain-spec-factory
- **Scope:** BUILD
- **Constraints:** MUST run AFTER the current platform-hybrid factory build (`a798b603`) completes — this edits the very runner that build is executing; running concurrently would corrupt it. Best executed via the FACTORY's own kernel loop (it is a self-governing kernel repo) once the build is done. Port, don't reinvent — keep parity with `run-task.sh`.
