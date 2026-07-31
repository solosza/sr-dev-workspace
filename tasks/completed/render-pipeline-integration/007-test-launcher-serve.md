# 007 — Test: launcher serves the page live (L2)

Type: TEST
Depends: 003

## What it verifies
serve_and_watch generates page.html, starts the server, and GET / returns the page; teardown leaves no listener.

## Method
A test that calls `serve(sample_items_json, tmp_session_dir)`, reads port.txt, does GET / (assert 200 + leaderboard title) and GET /status (assert idle JSON), then kills the server process and asserts the port is no longer listening.

## Acceptance Criteria
- [ ] `_test/test_launcher.py` exists.
- [ ] GET / returns 200 containing the title text.
- [ ] GET /status returns valid JSON with a status field.
- [ ] After teardown, the port is not accepting connections.
- [ ] Result written to `_test/launcher-result.json` (no print).

## Verify
`python tasks/render-pipeline-integration/_test/test_launcher.py` exits 0.

## Notes
Complex task (spawns a server subprocess) — route to run-task.sh or run in the outer session with explicit process cleanup. Windows-safe paths.
