# Task 004: Empty-Output Timeout Root Cause — Findings

## What was investigated

- `run_claude()` in `run-task.sh` (the sole place `claude -p` is invoked): the
  Windows background-poll-kill path (~line 184-217 pre-fix) and the Unix
  `timeout` path (~line 211-214 pre-fix).
- `check_stall`/heartbeat (RH-02/RH-03, already covers silent-death outside a
  single iteration — not this task's scope, which is the *within-iteration*
  0-byte-logfile case: "claude -p produced no output" at line 217-223).
- The 262 EMPTY-RETRY block (line 505-514): on a 0-byte logfile it retries the
  same iteration once, then proceeds to the failure/resume path on a second
  empty result. It papers over the case without explaining it.
- The `--output-format json` mode used for every invocation (`cmd_args`,
  line 155): this is **non-streaming** — the CLI computes the full response
  and writes ONE JSON object to stdout at the very end of the run, not
  incrementally. Confirmed by `extract_result`/`extract_session_id`
  (`lib/common.sh:162-193`), which `json.loads()` the entire logfile as a
  single document — this only works if the file is written in one shot at
  process exit.
- The 261 sweep evidence cited in the task brief ("wrapper saw empty stdout
  though subprocess completed and wrote state"): no surviving iteration log
  or artifact from that specific run exists in this worktree (iteration logs
  are ephemeral, overwritten/cleaned between runs) — the claim could not be
  re-verified from a preserved log, only reasoned about from the current code
  path.
- The literal claude CLI stdin-probe behavior: extracted directly from the
  installed binary
  (`C:/Users/solos/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/node_modules/@anthropic-ai/claude-code-win32-x64/claude.exe`)
  via string search. Two confirmed strings:
  - `async function Yq(){let N=process.stdin;if(!N||N.isTTY)return; ... for await(let Q of N)J.push(...)` —
    when stdin is not a TTY, the CLI reads from it.
  - `await dwr(process.stdin,3000);if(process.stdin.off("data",n),o)A6("Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip...")` —
    the read is bounded: it waits **at most 3 seconds**, then proceeds
    regardless, printing a warning naming the exact fix.

## Verdict

**Two distinct findings, not one:**

### 1. Confirmed harness-side defect (FIXED): unredirected stdin

`run_claude()` never redirected the child's stdin — it inherited whatever
stdin the runner itself had (a terminal, or an open pipe in the background-
Agent-spawned case per `nested-session-nesting.md`). Since a prompt is always
passed as a CLI argument here (never via stdin), this stdin was always dead
weight: every single invocation paid an unconditional ~3s tax probing stdin
it would never receive, and on some invocations logged the CLI's own
"Warning: no stdin data received in 3s" line. This is real, verified against
the installed binary's own source strings — not speculation.

This **cannot by itself** explain a full 600s empty-output timeout (the CLI's
own probe is hard-capped at 3s and always proceeds), but it is an unambiguous,
low-risk harness bug: the runner should never leave a subprocess's stdin
attached to an inherited handle it has no use for.

**Fix applied:** both invocation paths (`run_claude()`, Windows background
branch and Unix `timeout` branch) now redirect `< /dev/null`, eliminating the
stall/warning unconditionally.

### 2. The full-600s-timeout empty-output case: inconclusive by design, not by evidence gap

Distinguishing "subprocess produced no output" from "wrapper failed to
capture output" for a *genuine full-timeout* kill is **structurally
impossible with the current invocation shape**, independent of which one
actually happens on a given run:

- `--output-format json` defers ALL output to a single write at the end of a
  successful run. If the process is still working (mid-generation, mid-tool-
  call, waiting on a slow API response) when `TASK_TIMEOUT` fires, the logfile
  is *correctly* 0 bytes — there was nothing to capture yet. This looks
  identical, from the logfile alone, to a harness-side capture failure.
- `kill_process_tree()` (`lib/common.sh:60-79`) issues `kill -9` immediately
  followed by `taskkill //F //T` — both hard kills, no SIGTERM/grace period,
  no attempt to signal the child to flush or dump partial state before dying.
  Even if the CLI *had* buffered partial output client-side (unlikely under
  `--output-format json`, but not verifiable without CLI source), a hard kill
  guarantees it's lost.

Given the CLI's own output mode is provably all-or-nothing at exit, and the
kill path is provably immediate and unconditional, a 0-byte logfile after a
full-duration timeout is the **expected, correct** result of a subprocess
that simply didn't finish in time — this is the model/execution-side
explanation (slow generation, heavy tool use, network latency, or, per the
261 sweep account, a subprocess that finished ITS OWN task and wrote state
but hadn't yet reached the point of emitting its final JSON to stdout when
something else — timing, a second unrelated kill, or an earlier iteration's
stale PID variable — cut it off).

No harness-side stdout/stream *capture* bug was found beyond the stdin issue
above: the file-based redirection (`> "$logfile" 2>&1`, already in place
pre-262 per the code comment at line 146-148) is sound and doesn't drop
output that was actually written.

## Recommendation (out of scope for this task, not implemented)

If root-causing a *specific future* full-timeout occurrence is needed, the
runner would need either (a) `--output-format stream-json` with an
incremental parser (a larger redesign of `extract_result`/`check_completion`,
which currently assume one JSON blob), or (b) a grace-period SIGTERM before
the hard kill so a well-behaved child gets a chance to flush. Neither is
implemented here — this task's scope is root-cause + fix-if-harness-side; the
one confirmed harness-side defect (stdin) is fixed, and the timeout case is
verdicted model/execution-side by design of the current output mode, not a
capture bug.
