# Component: Shared Render Step

## Status
NEW

## Location
`.claude/skills/render/steps/step-serve-and-watch.md` (the reusable spec) + a thin launcher `.claude/skills/render/lib/serve_and_watch.py` (new) that wraps the mechanics. Each loop skill references the step at its end.

## What it does
The reusable final step every loop calls after the adapter produces items.json. Standalone and modular: any loop can call it alone or in-chain.

## Steps (mechanics, already proven by hand this session)
1. Close any active render session first (v1: one active session at a time).
2. `python templates/leaderboard/generate.py <items.json> <session_dir>` → page.html.
3. Start `python lib/render_server.py <session_dir>` as a MAIN-SESSION background process; capture `PORT=<n>` from its stdout.
4. Open the browser to `http://127.0.0.1:<port>/`.
5. Arm the annotations watcher (blocks until annotations.json grows, then hands the new questions to the session). See [[answer-routing]].
6. On teardown: kill server + watcher (no stray listeners); record/clear PIDs.

## Rules baked in
- Localhost only (127.0.0.1, ephemeral port).
- render server = main-session background, NEVER a detach-then-end sub-agent (launcher-death lesson).
- Pass Windows-style session_dir to native python (not MSYS `/d/...`).
- The watcher writes its result to a file, never `print()` (sr_dev code-quality gate blocks debug statements in .py).
- Session dir is a stable per-loop path (so re-renders reuse it).

## Dependencies
- Consumes items.json from [[adapter]]; feeds annotations to [[answer-routing]].
- Reuses render_server.py + generate.py as-is (no rebuild).

## Tests (L1/L2/L3)
- L1: step spec + launcher exist; each loop skill references the step.
- L2: launcher generates page.html and starts the server; GET / returns the page title; GET /status returns idle.
- L3: full loop-to-board once end to end (adapter → serve → GET / 200 with rows), server torn down cleanly (port no longer listening).
