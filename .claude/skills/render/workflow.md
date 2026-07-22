# Render — Workflow

Session lifecycle for the render loop. Step specs: `steps/`. Full design: [[references/INDEX.md]].

## Lifecycle

```
resolve → generate → serve → watch ──(user annotates at own pace)──> wake
                                                                       ↓
                     close ←── exhausted/--close ←── re-render ←── route
```

Steps 1-4 run in one invocation and RETURN CONTROL (the session does not wait).
Step 5 runs when the watcher's exit re-invokes the session (task-notification).
Step 6 loops to Step 2 (fresh state) or tears down.

**Reply file:** `<session_dir>/session-reply.json` is written by the session at route time (confirms, dry_run_ack, results) and served read-only by the server via `GET /status`. Schema: → [[references/annotation-contract.md]] § Reply Channel.

## State Schema

**Location:** `.claude/state/render-session.json` (single slot — Critical Rule 6)

```json
{
  "template": "review-board",
  "artifact": "unreviewed-queue",
  "status": "serving | routing | closed",
  "server_pid": 12345,
  "watcher_task": "b1a2c3",
  "port": 8031,
  "session_dir": ".claude/state/render-sessions/2026-07-15-review-board/",
  "annotations_file": ".../annotations.json",
  "routed_count": 0,
  "last_updated": "..."
}
```

## Pre-Generation Checkpoints

Every step file declares its reads before acting (tiered-index Layer 2):
- Step 1 reads `templates/INDEX.md`, `render-session.json`, and the template's `template.md` (data source spec)
- Step 2 reads the template's `generate.py` contract (input shape)
- Step 5 reads `annotations.json` + the template's action map BEFORE any routing

## Resume

On session restart with `status: serving`:
1. Verify `server_pid` alive → re-serve if dead (same session dir)
2. `annotations.json` present → skip to Step 5
3. Else re-arm the watcher (Step 4)

`--close` at any point: kill server + watcher, `status: closed`, keep session dir (annotations + routing log = audit trail).

## Error Handling

| Failure | Response |
|---------|----------|
| Unknown template | List registry, stop (HITL) |
| Active session exists | Report it, require `--close` |
| Port bind failure | Retry ephemeral bind ×3, then report |
| Malformed annotation entry | Report + skip entry, route the rest — never guess an action |
| Routing command fails | Stop routing, report which annotations routed/pending — annotations file is the recovery source |
| Malformed/missing session-reply.json | Page degrades to idle; board never crashes |
| Stray processes on teardown | Kill by recorded PID only — never pattern-kill (user's own processes are sacred) |
