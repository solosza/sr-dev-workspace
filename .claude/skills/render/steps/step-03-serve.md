# Step 3: Serve

## Purpose
Stand the return path up.

## Pre-generation Checkpoint
- Read: `lib/render_server.py` usage header (args: session_dir, page path)

## Procedure
1. Start `lib/render_server.py` as a background process: binds `127.0.0.1:0` (ephemeral), serves page.html at `/`, `POST /annotate` appends atomically (write-temp-rename) to `annotations.json` in the session dir. The server's ONLY filesystem write is that file.
2. Capture the bound port from server stdout; record `server_pid`, `port`, paths, `status: serving` in render-session.json.
3. Open `http://127.0.0.1:[port]/` in the default browser (`start` on Windows).
4. Verify: GET / returns 200 with the page (curl localhost).

## Acceptance Criteria
- [ ] RND-03 satisfied (contracts/step-03-contract.json): server alive, page served, state written
