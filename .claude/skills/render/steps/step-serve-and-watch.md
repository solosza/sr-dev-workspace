# Step: Serve and Watch (shared render step)

Parent: [[../SKILL.md]]. The reusable FINAL step any loop calls to turn its result into a live, question-able board. Standalone and modular: a loop can call it alone or in-chain. Verified working end to end (adapter + launcher + server) in the 308 build.

## Sequence
1. **Close any prior render session** (v1: one active session at a time). Kill a prior server pid if one is recorded.
2. **Adapter** — pass the loop's decide/output through [[../adapters/INDEX]] (`to_items`) to produce `items.json` in the session dir. Plain vocab, rank on merit, fit-as-tag, no em dashes are already baked in.
3. **Serve** — call `lib/serve_and_watch.py serve(items.json, session_dir)`. It generates `page.html`, starts `lib/render_server.py` on 127.0.0.1 detached, and returns `{port, pid, url}`.
4. **Open the browser** to `http://127.0.0.1:<port>/`.
5. **Arm the annotations watcher** — a background watcher that blocks until `annotations.json` grows, then wakes the session with the new questions.
6. **Route answers** via [[step-route-annotations]] — answer inline or dispatch deeper.

## Hard rules
- **Localhost only** (127.0.0.1, ephemeral port).
- **Server runs as a MAIN-SESSION background process, never a detach-then-end sub-agent.** A sub-agent that launches the server and ends its turn tears the server down (launcher-death lesson). The launcher detaches the server so it outlives the launcher call; the session keeps it alive.
- **Windows-safe paths** to native python (never MSYS `/d/...`).
- **Watcher writes its result to a file, never `print()`** (sr_dev code-quality gate blocks debug statements in .py).
- **One active session at a time** — close before opening another.
- Server/watcher pids tracked so teardown kills both (no stray listeners).

## Reuse
- `lib/render_server.py` and `templates/leaderboard/generate.py` are used as-is (no rebuild).
- Non-ranked (plan-shaped) loop outputs are out of scope for the leaderboard — see [[../templates/INDEX.md]].
