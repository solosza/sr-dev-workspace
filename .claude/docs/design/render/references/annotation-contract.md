# Annotation Contract

Parent: [[../index.md]]. The one boundary that keeps the UI safe inside the kernel's law.

## Schema

`annotations.json` — a JSON array, append-only within a session, written ONLY by `render_server.py` (atomic write-temp-rename):

```json
{ "target": "231", "action": "iterate", "raw_words": "go deeper on gnhf kernel compat", "at": "2026-07-15T09:00:00Z" }
```

| Field | Rules |
|-------|-------|
| `target` | Template-defined identifier (backlog number, gate id, report section). String. |
| `action` | Must be in the template's action map. Unknown → session reports + skips, never guesses. |
| `raw_words` | The user's verbatim typed text, or null. NEVER edited, summarized, or "improved" — this is the intent-chain input. |
| `at` | ISO timestamp, client-side. |

## Laws

1. **UI writes annotations, session writes state.** The server process has no code path to any `.claude/state/*` file except `annotations.json` in its own session dir. Mechanically enforceable (server has one output path).
2. **raw_words verbatim into kernel commands.** `iterate` routes as `/kernel/backlog` with raw_words as the argument — the same guarantee as the user typing it in chat.
3. **Destructive actions re-confirm.** Template.md flags actions as `destructive: true` (e.g., reject discards work) → the session lists them in chat and confirms before routing. Clicks queue; the session commits.
4. **Audit trail persists.** annotations.json + routing log outlive the session (kept in session dir) — every state change traceable to a click + words.

## Reply Channel (v2 — the full circle)

The reverse direction, closing the loop lavish closes with SSE — ours is a polled file, matching the file-based transport:

```
me → session-reply.json (I write it) → GET /status (server READS + serves it) → page polls ~2s → cards update
```

`session-reply.json` schema (written ONLY by the session, never the server, never the page):

```json
{
  "status": "processing | idle | closed",
  "dry_run_ack": ["145"],
  "confirms": [ { "target": "145", "action": "reject", "question": "Reject discards completed work — confirm?" } ],
  "results":  [ { "target": "197", "outcome": "accepted" },
                { "target": "188", "outcome": "backlog #233 created" } ],
  "at": "ISO"
}
```

**Law amendment (v2):** the server gains exactly ONE read-and-serve path (`GET /status` → session-reply.json). Its write surface is UNCHANGED — annotations.json only; the AST gate now asserts: writes == {tmp, annotations.json}, served reads == {page.html, session-reply.json}. Confirm answers travel back as ordinary annotations (`action: "confirm"` / `"cancel"` with the original target) — one schema, no second channel.

**Dry-run toggle:** page-level switch; annotations carry `"test": true`; the session acknowledges in the reply file (`dry_run_ack`) and NEVER routes them. Solves the write-test-noise-into-the-intent-chain problem surfaced 2026-07-15 (held annotations on #145/#146).

## review-board Action Map (v1)

| action | destructive | routes to |
|--------|------------|-----------|
| accept | no | review-queue accept transition |
| iterate | no | `/kernel/backlog` (raw_words verbatim, parent-linked) |
| reject | yes | review-queue reject with raw_words reason |
| skip | no | no state change |
| defer | no | review-queue defer marker |
