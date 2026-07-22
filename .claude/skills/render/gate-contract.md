# Gate Contract — Render

Per-step acceptance criteria. Soft gates (agent-verified) unless marked mechanical.

| Gate | Step | Check | Method |
|------|------|-------|--------|
| RND-01 | 1 | Template in registry; no active session (or --close path taken); artifact data gathered from the template's declared source (never a parallel bookkeeping system) | read registry + state |
| RND-02 | 2 | page.html exists in session dir; self-contained (zero external hosts); posts the standard annotation schema; has "Send to session" affordance + session-dir banner | grep + file check |
| RND-03 | 3 | Server alive on 127.0.0.1 ephemeral port; GET / returns page; state file written with pid/port/paths; `status: serving` | run_code (curl localhost) — contract: contracts/step-03-contract.json |
| RND-04 | 4 | Watcher spawned with task id recorded; session RETURNED CONTROL (no blocking wait) | state check |
| RND-05 | 5 | Every routed annotation validated against schema; unknown actions skipped + reported; raw_words passed VERBATIM to kernel commands; destructive actions re-confirmed in chat; routing log written | contract: contracts/step-05-contract.json |
| RND-06 | 6 | Teardown: server + watcher PIDs dead (kill by recorded PID only), `status: closed`, session dir preserved with annotations + routing log | run_code |

## The Law Gates (apply to every step)

- **UI-never-writes-state:** render_server.py has exactly ONE output path (its session's annotations.json). Any other filesystem write in the server is a build failure.
- **Intent chain:** iterate/reject routing invokes kernel commands with raw_words unedited. The render layer NEVER calls intent.py (that ban is mechanical — the existing gate-enforcer hook already blocks it).
