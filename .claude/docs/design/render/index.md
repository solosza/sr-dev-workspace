---
name: render
type: design-document
version: 1.0
date_created: 2026-07-15
status: draft
purpose: Visual interactive layer — render any agent artifact as annotatable HTML served locally, with a closed annotation return path routed through kernel commands
interview_note: Requirements settled in live discussion 2026-07-14/15 (lavish-axi port thread) — user directive "go ahead and design and build it through my commands, we can iterate after". Discussion decisions stand in for the section-by-section interview.
---

# /kernel/render — Design Index

<!-- INDEX file — points to payloads. Do not duplicate payload content here. -->

## Position in System

```
agent: render(artifact, template)           ← callable by session or any command
        ↓
template generates HTML → local server (localhost only) serves page + POST endpoint
        ↓
user clicks/types IN THE PAGE  ──POST──>  annotations.json   (raw words, never state)
        ↓                                        │
background watcher exits on file write ──> session re-invoked (task-notification)
        ↓
session ROUTES each annotation through kernel commands
(accept → review-queue transition · iterate notes → /kernel/backlog · etc.)
        ↓
state changed → optional re-render (same loop) or close
```

The closed-loop counterpart to claude.ai artifacts (which are one-way by sandbox
CSP). This is the lavish-axi pattern ported to the kernel: local server return
path + notification machinery the workspace already uses for pipelines.

v2 adds the reverse channel (the full circle — lavish does this with SSE, we do
it with a polled file): the session writes `session-reply.json`; the page polls
`GET /status` and updates in place — inline confirms for destructive actions,
live routing results on cards, dry-run acknowledgments. Schema + law amendment:
[[references/annotation-contract.md]] Reply Channel section.

## Skill Identity

You are a render layer. You take any agent artifact (review queue, chain status, gate report, research report), generate interactive HTML from a registered template, serve it on a local server with an annotation return path, and — when the user's annotations arrive — route every action through the proper kernel command so the UI changes real state without ever touching it directly.

## Philosophy

1. **The UI is a capture surface, never an actor** — pages collect the user's clicks and raw words into an annotations file; only the session changes state, only through kernel commands. The intent chain survives because `raw_words` reach `/kernel/backlog` verbatim.
2. **Primitive, not monolith** — render is a capability other commands call. Templates are the extension mechanism: one template = one integration point; new commands add templates without touching the core.
3. **Closed loop over pretty page** — the return path is the product. A rendering layer without the annotations → routing path is just a report generator (we already have artifacts for that).
4. **Local by design** — server binds localhost only; page works where the session runs; annotations land on the same disk the session reads.
5. **Reuse the wake-up machinery** — a background watcher process exits when annotations arrive, re-invoking the session exactly like pipeline completion notifications. No polling, no new infrastructure.
6. **Engine pragmatism** — lavish-axi (MIT, own-adjacent IP per backlog 231) is the target engine where its blocks fit; v1 ships self-contained template HTML + a stdlib server shim so the loop is proven before taking the dependency. The adoption decision is a build-pipeline task, made after reading the actual repo (RULE ZERO).

## Vocabulary

| Term | Meaning |
|------|---------|
| **render session** | One serve-annotate-route cycle over one artifact — server up, page open, annotations pending |
| **template** | A registered artifact-type renderer: HTML generator + action semantics (what each UI action means and which kernel command routes it) |
| **template registry** | `templates/` directory in the skill — one subfolder per template; the integration surface for other commands |
| **annotation** | One user action captured by the page: `{target, action, raw_words, at}` — raw_words are the user's verbatim text |
| **annotations file** | `annotations.json` written by the local server on submit — append-only within a session, the ONLY output of the UI |
| **return path** | page → POST → local server → annotations file → watcher → session — the closed loop |
| **routing** | Session-side translation of annotations into kernel command invocations — never a direct state write |
| **watcher** | Background process that exits when the annotations file appears/changes, waking the session via task-notification |

## Input

```
/kernel/render [template] [artifact]        → start a render session
/kernel/render review-board                 → first template: review queue (artifact = discovered unreviewed items)
/kernel/render --close                      → tear down active session (server + watcher)
```

| Argument | Purpose | Example |
|----------|---------|---------|
| `template` | Registered template name | `review-board` |
| `artifact` | Optional artifact ref the template consumes (defaults per template) | a report path, a backlog number list |
| `--close` | Stop server/watcher, keep annotations file | |

## Critical Rules

1. **The UI never writes state.** No review-status.json, no workflow files, no intent.py — the server writes ONLY the annotations file. Routing through kernel commands is the session's job. (Extends the intent-chain law: background/UI contexts never create intent entries.)
2. **raw_words verbatim.** Whatever the user typed in the page reaches the routed kernel command unedited — it is the hashable input for the intent chain.
3. **Localhost only.** Server binds 127.0.0.1, ephemeral port recorded in state; no external exposure, no auth complexity.
4. **Templates own semantics, the primitive owns transport.** The core knows render/serve/watch/route-dispatch; what "accept" MEANS on a review card lives in the template's action map.
5. **Never blocks pipelines.** Render sessions are async like review-queue; a page left open must not stall any autonomous flow.
6. **One active render session at a time** (v1) — state file is a single slot; `--close` before re-render of a different template.
7. **Process hygiene.** Server and watcher PIDs recorded in state; `--close` and session exit kill them; no stray listeners (the 206 stray-uvicorn lesson applies).

## Workflow Summary

| Step | Responsibility | Output | HITL |
|------|---------------|--------|------|
| 1. Resolve | Parse template + artifact; check no active session | Resolved template + artifact data | Only if template unknown |
| 2. Generate | Template renders artifact → self-contained HTML with annotation JS | HTML file in session dir | No |
| 3. Serve | Start localhost server (page + POST endpoint), open browser, write state | Running server, page open | No |
| 4. Watch | Spawn background watcher on annotations file; session returns to user | Watcher task id | No — user annotates at their pace |
| 5. Route | On wake: read annotations, route EACH through its kernel command per template action map | State transitions + routing log | Per template (destructive actions re-confirmed) |
| 6. Re-render / Close | Regenerate page with new state, or tear down on --close/completion | Updated page or clean exit | Optional |

Step details: [[references/workflow.md]]

## State Persistence Schema

**Location:** `.claude/state/render-session.json`

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
  "routed_count": 3,
  "last_updated": "..."
}
```

**Annotation schema** (the contract every template's JS must emit):

```json
[
  { "target": "231", "action": "accept", "raw_words": null, "at": "2026-07-15T09:00:00Z" },
  { "target": "197", "action": "iterate", "raw_words": "go deeper on gnhf kernel compat", "at": "..." }
]
```

## Complete File Structure

```
.claude/commands/kernel/render.md            ← command entry point
.claude/skills/render/
├── SKILL.md                                 ← identity, philosophy, step table
├── workflow.md                              ← session lifecycle, state, resume
├── gate-contract.md                         ← per-step gates
├── steps/
│   ├── step-01-resolve.md
│   ├── step-02-generate.md
│   ├── step-03-serve.md
│   ├── step-04-watch.md
│   ├── step-05-route.md
│   └── step-06-rerender-close.md
├── lib/
│   └── render_server.py                     ← stdlib localhost server: GET page, POST /annotate → annotations.json (atomic append)
├── templates/
│   ├── INDEX.md                             ← template registry
│   └── review-board/
│       ├── template.md                      ← action map: accept/iterate/reject/skip/defer → kernel command routing
│       └── generate.py                      ← artifact → HTML (self-contained, annotation JS posts to /annotate)
├── references/
│   └── INDEX.md                             ← routing table → this design doc's payloads
└── contracts/
    ├── step-03-contract.json                ← server up + state written validation
    └── step-05-contract.json                ← annotations schema + routing-through-commands validation
```

## Design Documents

| Payload | Content |
|---------|---------|
| [[references/workflow.md]] | Step specs (purpose + procedure per step), session lifecycle, wake/route mechanics, re-render loop |
| [[references/annotation-contract.md]] | Annotation schema, raw_words/intent-chain law, per-action routing table for review-board, destructive-action re-confirm rule |
| [[references/template-registry.md]] | Template anatomy (template.md + generate.py), registration, how other commands add templates, planned templates (chain-status, gate-report, research-report) |
| [[references/lavish-adoption.md]] | Open decision: v1 shim vs lavish-axi engine — evaluation criteria, what the build pipeline must read in the lavish repo before deciding |
