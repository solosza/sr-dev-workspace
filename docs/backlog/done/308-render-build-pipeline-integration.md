# Render Integration Across the Venture-Loop Pipeline

## Status
Open

## Priority
High — the user works through boards (standing directive); today every loop still ends in a text wall or a hand-wired board. This makes the interactive board the default output surface.

## Summary
Every venture loop (assay, competition, deep-dive, offer, gtm, launch, operate, sharpen, and the reframe trio) should finish by rendering its output as a live leaderboard via the render skill, served on localhost, with a per-item question box that routes back to the session. Today this is four manual steps (hand-author items.json, run generate.py, start the server, arm a watcher). This backlog turns it into a real, reusable pipeline feature: one adapter, one shared render step, and answer-routing.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[308-render-build-pipeline-integration/adapter]] | Convert a loop's decide/output into the leaderboard items.json (plain-vocab, rank-on-merit, rec, fit-as-tag) |
| [[308-render-build-pipeline-integration/render-step]] | Shared, modular final step: generate page.html, serve, open browser, arm watcher |
| [[308-render-build-pipeline-integration/answer-routing]] | Route a board question: answer inline or dispatch into /deep-dive for that wedge |

## Flow

```
loop (assay/competition/…) → decide/output
        → [ADAPTER] output → items.json (plain vocab, rank, rec, fit-tag)
        → [RENDER STEP] generate.py → page.html → render_server.py (127.0.0.1) → open browser → arm watcher
        → user asks on a row
        → [ANSWER ROUTING] annotations.json → session
              → answer inline (session-reply.json) OR route → /deep-dive <wedge>
```

## Requirements
- Reuse the existing `.claude/skills/render` (render_server.py + templates/leaderboard/generate.py already built and verified working this session). Do NOT rebuild them.
- The render step is standalone and modular: any loop can call it alone or in-chain (family rule).
- Honor standing rules everywhere shown: plain vocabulary (no jargon), NO em dashes, lean output.
- Fit-to-you is a displayed tag only, never a ranker (unbiased calibration).
- One active render session at a time (v1 render constraint); the step must close a prior session before opening a new one.
- Localhost only; server/watcher process hygiene (no stray listeners) on teardown.
- Destructive or next-loop actions re-confirm in chat before routing.

## References
- `.claude/skills/render/` (SKILL.md, workflow.md, lib/render_server.py, templates/leaderboard/generate.py + template.md)
- `.claude/skills/assay/steps/step-04-decide.md` (the output that feeds the adapter)
- Memories: `plain-vocabulary`, `loop-output-lean`, `render-board-responses`, `render-board-legend`
- This session's manual run: `projects/assay/runs/2026-07-31-engine-as-a-product.md` (the pattern being productized)

## Task Builder Input
- **Deliverable:** An adapter module + a shared render step wired into each loop skill + answer-routing, replacing the manual four-step hand-wiring.
- **Location:** workspace:.claude/skills/
- **Scope:** BUILD
- **Constraints:** Reuse render_server.py + leaderboard/generate.py as-is. Plain vocab + no em dashes + fit-as-tag are hard rules. sr_dev code-quality gate blocks `print()` in .py (write results to files, not stdout). No `cd` in bash. render server runs as a main-session background process, never a detach-then-end sub-agent (launcher-death). Pass Windows-style paths to native python (not MSYS).
