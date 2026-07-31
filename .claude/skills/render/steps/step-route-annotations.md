# Step: Route Annotations

Parent: [[../SKILL.md]]. When the watcher wakes the session with new board annotations, decide what each means and act. The UI stays a capture surface; only the session changes state, only through kernel commands.

## Annotation shape (from render_server.py)
`{ target: <item id>, action: "ask", raw_words: <the question>, ref: <qid>, at: <ISO> }`

## Routing rules
- **Plain `ask`** — the session answers inline by writing `session-reply.json` = `{status, answers:[{ref, answer}]}`. Accumulate ALL prior answers in the array so re-polls stay filled. The page fills the answer under that row by `ref`.
- **"Go deeper" ask** (raw_words asks for a full workup, the competitors, a plan): re-confirm in chat, then route `/deep-dive <the wedge named by target>`. `raw_words` pass verbatim into the routed command (intent-chain input). When it returns, re-render via [[step-serve-and-watch]].
- **Destructive or next-loop actions**: re-confirm in chat before routing (render Critical Rule 8).

## Loop control
- After answering/routing, **re-arm the watcher** with the new answered-count so the next question wakes the session. This is the standing loop the session manages across turns.
- The watcher exit (annotations.json grew) is the wake signal — no polling.

## Notes
- `session-reply.json` is served by render_server.py at `GET /status`; the page polls it and fills answers by `ref`.
- This step never writes review-status / workflow / intent files — routing goes through kernel commands only.
