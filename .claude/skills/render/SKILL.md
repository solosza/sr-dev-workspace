---
name: render
version: 1.0
status: draft
type: skill
design_doc: .claude/docs/design/render/index.md
design_doc_hash: 441ced92fdafbe76bc82f19e04fdbbb5bf29dc4618707e1b327597fbe6abe915
---

# Render — Skill

## Identity

You are a render layer. You take any agent artifact (review queue, chain status, gate report, research report), generate interactive HTML from a registered template, serve it on a local server with an annotation return path, and — when the user's annotations arrive — route every action through the proper kernel command so the UI changes real state without ever touching it directly.

## Philosophy

1. **The UI is a capture surface, never an actor** — pages collect clicks and raw words into an annotations file; only the session changes state, only through kernel commands. `raw_words` reach `/kernel/backlog` verbatim, so the intent chain survives.
2. **Primitive, not monolith** — render is a capability other commands call. Templates are the extension mechanism: one template = one integration point.
3. **Closed loop over pretty page** — the return path is the product.
4. **Local by design** — server binds 127.0.0.1 only; annotations land on the same disk the session reads.
5. **Reuse the wake-up machinery** — a background watcher exits when annotations arrive, re-invoking the session like pipeline notifications. No polling.
6. **Engine pragmatism** — v1 ships self-contained template HTML + stdlib server shim; lavish-axi adoption is an open decision made after reading the repo. → [[references/INDEX.md]] → lavish-adoption payload.

## Vocabulary

| Term | Meaning |
|------|---------|
| **render session** | One serve-annotate-route cycle over one artifact |
| **template** | Registered artifact renderer: HTML generator + action map (what each action means, which kernel command routes it) |
| **annotation** | One captured user action: `{target, action, raw_words, at}` — raw_words verbatim |
| **annotations file** | `annotations.json`, written only by the local server — the UI's sole output |
| **return path** | page → POST → local server → annotations file → watcher → session |
| **routing** | Session-side translation of annotations into kernel command invocations |
| **watcher** | Background process whose exit (on annotations write) wakes the session |

## Critical Rules

1. **The UI never writes state.** The server writes ONLY the annotations file. No review-status.json, no workflow files, never intent.py. Routing through kernel commands is the session's job.
2. **raw_words verbatim** into routed kernel commands — the hashable intent-chain input.
3. **Localhost only** — 127.0.0.1, ephemeral port recorded in state.
4. **Templates own semantics, the primitive owns transport.** Action meaning lives in the template's action map; the core knows render/serve/watch/route-dispatch.
5. **Never blocks pipelines.** Render sessions are async; an open page stalls nothing.
6. **One active render session at a time** (v1). `--close` before rendering a different template.
7. **Process hygiene.** Server/watcher PIDs in state; teardown kills both; no stray listeners.
8. **Destructive actions re-confirm in chat** before routing (template-flagged).
9. **Response-board convention (this operator).** This user works *through* boards — deliver responses AS a render board, not a text wall ("keep it like this for every response"). Every generated board MUST include (a) **per-card reply controls** — 👍 OK / ⏸ Hold / ↕ Redirect + a per-card note — so they can respond per item, and (b) a **general-comments free-text field at the bottom**, above the send button, for session-wide input. On submit, the general-comments value rides the `__session__` submit annotation's `raw_words`. See memory `render-board-responses`.

## Workflow

> `workflow.md` for session lifecycle, state schema, resume.

| Step | What It Does |
|------|-------------|
| 1. Resolve | Parse template + artifact; registry check; single-session check; gather artifact data |
| 2. Generate | Template's generate.py → self-contained page.html in session dir |
| 3. Serve | Start localhost server, open browser, write state |
| 4. Watch | Spawn background watcher on annotations file; return control to user |
| 5. Route | On wake: validate annotations, route each through its kernel command per action map |
| 6. Re-render / Close | Regenerate from fresh state, or tear down cleanly |

## File Index

| File | Purpose |
|------|---------|
| `SKILL.md` | This file — orchestrator |
| `workflow.md` | Session lifecycle, state schema, resume |
| `gate-contract.md` | Per-step gates |
| `steps/step-01-resolve.md` … `steps/step-06-rerender-close.md` | Step specs |
| `lib/render_server.py` | Localhost annotation server (BUILT + operational) |
| `lib/serve_and_watch.py` | Launcher: generate page + start server detached + record port (BUILT, 308) |
| `adapters/loop_to_leaderboard.py` + `adapters/INDEX.md` | Loop output -> leaderboard items.json, plain-vocab + rank-on-merit baked in (BUILT, 308) |
| `steps/step-serve-and-watch.md` + `steps/step-route-annotations.md` | Shared render step + answer routing (BUILT, 308) |
| `templates/INDEX.md` | Template registry |
| `templates/leaderboard/` | Plain-English ranked list (BUILT). The default for venture-loop ranked output |
| `templates/venture-board/` | Venture-loop board: pipeline stage-columns + funnel + verdict cards (BUILT) |
| `templates/review-board/` | Review-queue board: unreviewed done-backlog cards (BUILT: generate.py + template.md) |
| `references/INDEX.md` | Links to design doc payloads |
| `contracts/step-03-contract.json`, `contracts/step-05-contract.json` | Serve + routing validations |
