# Gate Contract — 232 Render Runtime

Deliverables in .claude/skills/render/: lib/render_server.py, templates/review-board/{template.md,generate.py}; decision addendum in design payload lavish-adoption.md.

| Gate | Check | Method |
|------|-------|--------|
| RRT-01 | render_server.py: stdlib-only imports; binds 127.0.0.1:0; prints port; GET / serves page; POST /annotate atomic append (write-temp-rename) | run_test (005) |
| RRT-02 | SINGLE-OUTPUT-PATH LAW: AST proves exactly one open-for-write file target (the session's annotations.json + its temp file); zero other filesystem writes; zero reads/writes touching .claude/state outside the passed session dir | run_test (006) — AST ONLY |
| RRT-03 | template.md: data source = review-queue's diff discovery; full action map (accept/iterate/reject/skip/defer) with destructive flags matching design annotation-contract.md exactly | grep + read |
| RRT-04 | generate.py: real unreviewed-items input → self-contained page.html (zero external hosts), action buttons + notes input per card, "Send to session" POSTs the FROZEN schema {target, action, raw_words, at}, session-dir banner | run_test |
| RRT-05 | L3 closed loop, programmatic + honest: page generated from a COPY of real review data, server serves it, POST accept + POST iterate(raw_words) → annotations.json exact-matches schema + raw_words verbatim; a watcher process blocking on the file exits ≤2s after the write. Env problem → L3-BLOCKED report, never fake | run_test (007) |
| RRT-06 | Lavish addendum written into design payload lavish-adoption.md: repo actually read (cite files/URLs), criteria applied, ADOPT or KEEP-SHIM decision + why. Decision only — no engine change | grep addendum |
| RRT-07 | Non-destructive: live review-status.json byte-identical before/after all tests; no stray listeners left (kill own PIDs) | run_code (hash compare + port scan) |

## Test-Script Requirements (lessons #39/#43 — MANDATORY)

AST-based semantics checks only; docstrings excluded by construction; body-scoped walks (`fn.body` per-statement — NEVER `ast.walk(FunctionDef)` for body rules; decorators/annotations false-positive). String-grep semantics checks BANNED. RRT-03/RRT-06 greps are docs-presence checks — allowed.

## Law Reminders

- UI never writes state; server's only output is annotations.json (RRT-02 is the mechanical proof)
- raw_words verbatim — L3 asserts byte equality
- Routing (RND-05) is session behavior — NOT built here
- Tests: temp dirs + copies; the workspace has no feature branch to protect you
