# 003 — Build the serve-and-watch launcher

Type: BUILD

## Deliverable
`.claude/skills/render/lib/serve_and_watch.py`

## What it does
The reusable mechanics proven by hand this session, wrapped in one launcher: given an items.json path and a session dir, it (1) runs the leaderboard generator to make page.html, (2) starts render_server.py on 127.0.0.1 as a background process, (3) writes the chosen port to a file, and (4) writes an arm-marker for the annotations watcher. It does the file work; the session opens the browser and answers questions.

## Acceptance Criteria
- [ ] File exists at the deliverable path.
- [ ] Exposes `serve(items_json, session_dir)` that calls `templates/leaderboard/generate.py` to write `session_dir/page.html`.
- [ ] Starts `lib/render_server.py session_dir` as a subprocess and records `PORT=<n>` into `session_dir/port.txt`.
- [ ] Resolves paths relative to the render skill root via `__file__` (never a cwd-relative path — lesson: cwd-relative data paths break under a different cwd).
- [ ] Uses Windows-safe paths for the native python subprocess.
- [ ] No `print()` statements — write status to `session_dir/serve-status.json`, do not print.
- [ ] Server runs detached from the launcher process so the launcher can return (the caller keeps it alive as a main-session background process).

## Verify
`python -c "import ast; ast.parse(open('.claude/skills/render/lib/serve_and_watch.py').read())"` exits 0, and `! grep -nE '(^|[^_])print\(' .claude/skills/render/lib/serve_and_watch.py`.
