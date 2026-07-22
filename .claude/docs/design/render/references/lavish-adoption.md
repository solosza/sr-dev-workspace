# Lavish-axi Adoption — Open Decision

Parent: [[../index.md]]. Status: OPEN — decided inside the build pipeline, not here (RULE ZERO: nobody has read the lavish repo yet; backlog 231's research is README-level).

## The Two Paths

| | v1 shim (default) | lavish-axi engine |
|---|---|---|
| Renderer | Our generate.py per template (self-contained HTML, like the 2026-07-15 mock artifact) | lavish blocks (tables, diffs, diagrams) |
| Server | `lib/render_server.py` (stdlib, ~80 lines, one output path) | lavish's own local server |
| Annotation format | Our schema, ours to keep stable | Whatever lavish emits — needs adapter or replaces our schema |
| Dependency | None | npm + lavish (MIT, active, ~1.8k★ per backlog 231) |

## Decision Procedure (a build-pipeline task)

1. READ the actual repo: server mechanics, annotation/feedback format, extensibility of blocks, skill packaging (`npx skills add kunchenguid/lavish-axi`).
2. Adopt lavish IF: its server exposes annotations as a readable local file/endpoint we can watch, AND its annotation payload carries user free-text verbatim (raw_words law), AND templates can inject our action buttons. Else: keep the shim, revisit when template count makes lavish's block library worth an adapter.
3. Either way the annotation CONTRACT (schema + laws) is ours and stable — engine choice changes transport internals only.

## Why not decide now

The loop's value is proven by the shim at near-zero dependency cost; betting the design on unread internals violates RULE ZERO and lesson #38's spirit (proven source ≠ proven fit).

## Decision Addendum (2026-07-15, backlog 232)

**Decision: KEEP-SHIM**

### Sources Read

- `github.com/kunchenguid/lavish-axi` README.md (full — server mechanics, CLI, env config, skill packaging)
- `src/server.js` — HTTP routes: `GET /api/poll`, `POST /api/:key/prompts`, `GET /events/:key` SSE, `POST /api/:key/end`, whiteboard persistence
- `src/session-store.js` — file-based JSON persistence (`writeFile` with `JSON.stringify`), session schema: `{key, file, url, status, prompts[], chat[], layout_warnings[], dom_snapshot, pending_prompts, updated_at}`
- `src/cli.js` — poll command returns `{session, prompts[], layout_warnings[], next_step}` to stdout; prompts passed through without normalization (`prompts: response.prompts || []`)

### Criterion 1: Local file/endpoint watchable?

**PARTIAL.** Lavish exposes `GET /api/poll` (long-polling HTTP) and `GET /events/:key` (SSE). Session state persists to disk at `LAVISH_AXI_STATE_DIR` (~/.lavish-axi/) via `session-store.js`. However, our contract requires filesystem-level watching — `render_server.py` does atomic append (write-temp-rename) to `annotations.json`, and a watcher process blocks on file changes (RRT-05 gate: watcher exits ≤2s after write). Lavish's feedback delivery is HTTP-based (poll or SSE), not file-event-based. Adapting requires replacing our fs.watch watcher with an HTTP poll client — a transport-layer rewrite, not a drop-in.

### Criterion 2: Free-text verbatim preserved?

**YES.** `cli.js` confirms prompts are returned as-is — `prompts: response.prompts || []` with no transformation. User text survives the round-trip. However, the payload format differs: lavish returns `{session, prompts[], layout_warnings[], next_step}` while our frozen schema is `{target, action, raw_words, at}`. An adapter layer would map between formats. The raw_words law is satisfiable but not native.

### Criterion 3: Action buttons injectable?

**PARTIAL.** `data-lavish-action` marks custom clickable elements; `window.lavish.queuePrompt()` sends structured data. But lavish wraps artifacts in its own browser chrome (conversation panel, annotation preview pills, Mermaid whiteboard editing). Our `generate.py` produces self-contained HTML where the page IS the interface — buttons POST directly to `render_server.py`'s `/annotate` endpoint. Under lavish, the artifact becomes a child frame inside lavish's chrome, and feedback routes through lavish's poll system instead of our direct POST. Our action semantics (accept/iterate/reject/skip/defer with destructive flags and raw_words) are structured review decisions; lavish's model is free-form annotation + chat. Injecting our button taxonomy is technically possible but fights the chrome UI's interaction model.

### Why KEEP-SHIM

1. **Dependency cost vs. value:** Our shim is ~80 lines stdlib Python, zero dependencies. Lavish adds npm + Node.js + pnpm runtime. At template count = 1 (review-board), the block library doesn't pay for the adapter.
2. **Architectural mismatch:** Lavish is an annotation/editing tool for HTML artifacts (annotate elements, edit Mermaid diagrams, chat). Our review-board is a structured decision interface (action buttons with frozen schema). Different interaction paradigms.
3. **Transport mismatch:** Our file-based atomic append + fs.watch is simpler and more deterministic than HTTP long-poll for the single-output-path law (RRT-02). No network layer to debug.
4. **Chrome wrapping:** Lavish wraps artifacts in its own browser chrome. Our design wants the artifact to be the full self-contained page — no wrapper frame.

### Revisit Trigger

When template count exceeds ~5, making lavish's block library (tables, diffs, diagrams, Mermaid whiteboard) worth the adapter cost. At that point, re-evaluate whether the adapter overhead (format mapping + transport rewrite) is justified by lavish's rendering capabilities. File a new backlog at that time.
