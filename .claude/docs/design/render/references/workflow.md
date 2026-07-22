# /kernel/render — Workflow Payload

Step specs for the render session lifecycle. Parent: [[../index.md]]

## Step 1 — Resolve

**Purpose:** Validate the request and gather the artifact data the template consumes.

**Procedure:**
1. Parse `template` + optional `artifact` from args; `--close` short-circuits to Step 6.
2. Read `templates/INDEX.md`; unknown template → list registered templates, stop (only HITL in the happy path).
3. Read `.claude/state/render-session.json`; if `status: serving` → report active session, require `--close` first (Critical Rule 6).
4. Gather artifact data per the template's `template.md` (e.g., review-board: diff `docs/backlog/done/` against review-status.json exactly like `/kernel/review-queue` step 1 — same discovery, never a parallel bookkeeping system).

## Step 2 — Generate

**Purpose:** Turn artifact data into a self-contained interactive page.

**Procedure:**
1. Create session dir `.claude/state/render-sessions/[date]-[template]/`.
2. Run the template's `generate.py` with the artifact data → `page.html`.
3. Page requirements (validated by gate): self-contained (no external hosts), annotation JS POSTs to `/annotate` with the annotation schema, a visible "Send to session" submit affordance, and a read-only banner naming the session dir (so the user knows which session they're annotating).

## Step 3 — Serve

**Purpose:** Stand the return path up.

**Procedure:**
1. Start `lib/render_server.py` as a background process: binds `127.0.0.1:0` (ephemeral), serves `page.html`, `POST /annotate` appends atomically to `annotations.json` (write-temp-rename).
2. Record `server_pid`, `port`, paths, `status: serving` in render-session.json.
3. Open `http://127.0.0.1:[port]/` in the default browser.

## Step 4 — Watch

**Purpose:** Arrange the wake-up without polling.

**Procedure:**
1. Spawn a background watcher (Bash, `run_in_background`) that blocks until `annotations.json` exists/changes, then exits — its exit re-invokes the session via the standard task-notification, identical to pipeline completions.
2. Record `watcher_task` in state. Session returns control to the user; they annotate at their own pace.

## Step 5 — Route

**Purpose:** Convert annotations into real state changes — through kernel commands only.

**Procedure:**
1. On wake: read `annotations.json`; validate every entry against the annotation schema (unknown action for the template → report, skip that entry, never guess).
2. For each entry, dispatch per the template's action map. review-board v1:
   - `accept` → review-queue acceptance transition (review-status.json append via the review-queue flow)
   - `iterate` → `/kernel/backlog` invoked with `raw_words` VERBATIM as the argument, parent-linked
   - `reject` → review-queue rejection with `raw_words` as reason
   - `skip` / `defer` → review-queue semantics, no state / deferred marker
3. Destructive or irreversible actions (template-flagged) are re-confirmed in chat before routing — the page click queues them, the session confirms.
4. Log each routing (`target → command → result`) into the session dir; update `routed_count`.

## Step 6 — Re-render / Close

**Purpose:** Continue the loop or end it cleanly.

**Procedure:**
1. After routing: regenerate the page from fresh state (Step 2) and re-serve so the board reflects reality — or, if the queue/artifact is exhausted or `--close` was invoked, tear down.
2. Teardown: kill `server_pid` and watcher, set `status: closed`, keep `annotations.json` + routing log in the session dir (audit trail).
3. Report: rendered/routed/remaining counts, session dir path.

## Resume

`render-session.json` is the single source: on session restart with `status: serving`, verify the server PID is alive (re-serve if not), re-arm the watcher if annotations haven't arrived, or go straight to Step 5 if they have.
