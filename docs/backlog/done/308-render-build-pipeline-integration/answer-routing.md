# Component: Answer Routing

## Status
NEW

## Location
`.claude/skills/render/steps/step-route-annotations.md` (spec) — session-side routing logic (no new server code; render_server.py already collects annotations).

## What it does
When the watcher wakes the session with new annotations from the board, this decides what each one means and acts. The UI stays a capture surface; only the session changes state, only through kernel commands.

## Annotation shape (from render_server.py)
`{ target: <item id>, action: "ask", raw_words: <the question>, ref: <qid>, at: <ISO> }`

## Routing rules
- **action = ask, plain question:** the session answers inline by writing `session-reply.json` = `{status, answers:[{ref, answer}]}` (accumulate all prior answers so re-polls stay filled). The page fills the answer under that row by `ref`.
- **action = ask, "go deeper" intent** (raw_words asks for a full workup, competitors, a plan): re-confirm in chat, then route `/deep-dive <the wedge named by target>`; when it returns, re-render the board (or a new deep-dive board) via [[render-step]].
- **Any next-loop or destructive action:** re-confirm in chat before routing (render Critical Rule 8).
- `raw_words` pass verbatim into any routed kernel command (intent-chain input).

## Loop control
- After answering/routing, re-arm the watcher with the new answered-count so the next question wakes the session. This is the standing loop the session manages across turns.

## Dependencies
- Consumes annotations.json produced by the render-step's server ([[render-step]]).
- May invoke `/deep-dive` (existing loop).

## Tests (L1/L2/L3)
- L1: routing spec exists and each loop's render step points to it.
- L2: given a sample annotations.json with one plain ask, the session produces a schema-valid session-reply.json keyed by ref.
- L3: end to end on the live board: type a question → answer appears inline under the row; type a "go deeper" question → chat re-confirm → /deep-dive invoked for that wedge.
