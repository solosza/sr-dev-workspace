# Build lib/render_server.py

## Context
Backlog 232. The transport half of the return path. READ FIRST: .claude/docs/design/render/references/annotation-contract.md (schema + laws) and .claude/skills/render/steps/step-03-serve.md.

## Type
BUILD
## Execution
inline
## Dependencies
- None

## Requirements
- File: `.claude/skills/render/lib/render_server.py`, stdlib ONLY (http.server/socketserver, json, os, sys, tempfile)
- CLI: `python render_server.py <session_dir>` — serves `<session_dir>/page.html` at GET /; binds 127.0.0.1 port 0; prints `PORT=<n>` to stdout (flush) so the caller can capture it
- `POST /annotate`: body = one annotation JSON `{target, action, raw_words, at}`; validate fields present (400 on malformed, file untouched); append to `<session_dir>/annotations.json` (JSON array) ATOMICALLY: write full new array to `<session_dir>/.annotations.tmp`, then os.replace
- THE LAW (RRT-02): the ONLY filesystem writes in the entire file are that tmp file + os.replace target. No logs-to-file, no state files, nothing else. Usage header docstring states this.
- No try/except swallowing: validation errors return 4xx responses; unexpected errors propagate (crash > silent corruption)

## Acceptance Criteria
- [ ] Compiles; usage header documents CLI + the single-output-path law

## Gates Satisfied
- RRT-01 (build half)

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
