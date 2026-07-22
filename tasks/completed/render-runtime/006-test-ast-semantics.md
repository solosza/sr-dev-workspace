# Test: AST Semantics — Single-Output-Path Law + stdlib-only

## Context
Backlog 232. The mechanical proof of "the UI never writes state." Lessons #39/#43 method MANDATORY: ast.parse, docstrings excluded by construction, BODY-SCOPED walks (`fn.body` per statement — never ast.walk(FunctionDef) for body rules).

## Type
TEST
## Execution
inline
## Dependencies
- 001, 003

## Requirements
- Script over render_server.py via `ast` ONLY:
  - imports: every Import/ImportFrom module in the stdlib allowlist (http, socketserver, json, os, sys, tempfile, pathlib, datetime, urllib) — no third-party
  - open-for-write detection: collect ast.Call nodes for open(...,'w'/'wb'/'a'), Path.write_*, tempfile usage, os.replace — assert every write target derives from the session_dir argument and the ONLY logical outputs are the tmp file + os.replace to annotations.json; stdout prints are allowed (PORT=)
  - no string literal or os.path/pathlib expression referencing `.claude/state` outside the passed session dir
- Same script over generate.py: stdlib-only imports; only write target is `<session_dir>/page.html`
- Exit non-zero on real violations → fix CODE → /kernel/learn; script misfire → fix SCRIPT (never weaken)

## Acceptance Criteria
- [ ] Exit 0 with every check genuinely executed

## Gates Satisfied
- RRT-02

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
