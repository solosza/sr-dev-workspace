# 004 — Build the shared render step spec

Type: BUILD
Depends: 003

## Deliverable
`.claude/skills/render/steps/step-serve-and-watch.md`

## What it does
The reusable final-step spec every loop references. Prescribes the sequence: adapter → generate → serve → open browser → arm watcher → route answers. Standalone and modular (any loop calls it alone or in-chain).

## Acceptance Criteria
- [ ] File exists at the deliverable path.
- [ ] Lists the ordered steps: (1) close prior render session, (2) adapter to items.json, (3) serve_and_watch, (4) open browser to `http://127.0.0.1:<port>/`, (5) arm annotations watcher, (6) route via `[[step-route-annotations]]`.
- [ ] States the hard rules: localhost only, server as MAIN-SESSION background (never a detach-then-end sub-agent — launcher-death), Windows-safe paths, watcher writes to file not print, one active session at a time.
- [ ] Is an index/spec (pointers + step list), not code.
- [ ] Links `[[../adapters/INDEX]]`, `[[../lib/serve_and_watch]]` (conceptually), and `[[step-route-annotations]]`.

## Verify
`test -f .claude/skills/render/steps/step-serve-and-watch.md` and `grep -q 'launcher-death\|main-session\|main session' .claude/skills/render/steps/step-serve-and-watch.md`.
