# Build /kernel/render Runtime — Server, Review-Board Template, Closed-Loop Tests

## Status
Open

## Priority
High — closes the interaction gap the user called out ("if i type in the ui, its static"); first working template unblocks the 42-item visual review session

## Summary
The /kernel/render command is designed (.claude/docs/design/render/) and scaffolded (.claude/skills/render/), with runtime marked PENDING BUILD. This backlog builds the runtime: the localhost annotations server, the review-board template, the lavish-axi adoption read, and L1/L2/L3 tests that prove the closed annotation loop programmatically (serve → POST → annotations.json → watcher exit).

## Requirements
- `lib/render_server.py` in the render skill: stdlib only; binds 127.0.0.1:0; GET / serves page.html; POST /annotate appends to annotations.json atomically (write-temp-rename); prints bound port to stdout; EXACTLY ONE filesystem write path (its session's annotations.json) — the UI-never-writes-state law, verifiable by AST
- `templates/review-board/template.md`: data source (diff docs/backlog/done/ vs review-status.json — same discovery as /kernel/review-queue) + action map (accept/iterate/reject/skip/defer with destructive flags) per design payload annotation-contract.md
- `templates/review-board/generate.py`: (unreviewed items JSON) → self-contained page.html — cards with action buttons + notes input, "Send to session" submit POSTing the standard annotation schema, session-dir banner; visual reference: the 2026-07-15 mock artifact (scratchpad render-loop-mock.html) — but generated from real data
- Lavish-axi adoption read (RESEARCH task inside this pipeline): read https://github.com/kunchenguid/lavish-axi source/docs; decide per design payload lavish-adoption.md criteria; write decision addendum to that payload — DECISION ONLY, no engine swap in this backlog regardless of outcome
- L1: files exist, import/compile. L2: server unit cycle (start, GET 200, POST valid annotation → file contains it, POST malformed → 4xx + file untouched, atomicity). L3: REAL closed loop programmatically — generate page from real review-status data, serve, POST two annotations (one accept, one iterate with raw_words), assert annotations.json exact content, assert a filesystem watcher process exits on the write; NO faking, report L3-BLOCKED if env prevents
- AST gate on server: single open-for-write target; no imports beyond stdlib; no reads/writes to .claude/state outside its session dir

## References
- .claude/docs/design/render/ (index + 4 payloads — the governing design)
- .claude/skills/render/ (scaffold, gate-contract RND-01..06, contracts step-03/step-05)
- projects/kun-dev-workflow-tools/research-report.md (lavish-axi background, backlog 231)
- Lessons #39/#43 (AST-based test scripts, body-scoped walks), #41 (honest env gating)

## Task Builder Input
- **Deliverable:** Working render runtime: lib/render_server.py + templates/review-board/{template.md,generate.py} inside .claude/skills/render/, lavish-adoption decision addendum, L1/L2/L3 test evidence. Command /kernel/render review-board becomes operational (human demo happens after merge, run by the user).
- **Location:** workspace:.claude/skills/render/
- **Scope:** BUILD
- **Constraints:** Workspace build (no target-repo branch; workspace has no feature-branch flow — tests must be non-destructive to live state: L2/L3 run against a TEMP session dir and a COPY of review-status data, never the real file). Server: stdlib only, localhost only, single-output-path law (AST-gated). Annotation schema is FROZEN per design payload annotation-contract.md — templates conform to it, not vice versa. Test scripts AST-based where checking semantics (lessons #39/#43: docstring-excluded, body-scoped walks). The routing step (RND-05) is SESSION behavior, not runtime code — do not build routing automation in this backlog. Lavish read is decision-only.
