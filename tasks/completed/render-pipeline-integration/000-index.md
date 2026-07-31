# Tasks: Render Integration Across the Venture-Loop Pipeline

Backlog: [[../../docs/backlog/308-render-build-pipeline-integration]]
Scope: BUILD (worktree OFF — repo bgIsolation=none; edits .claude/skills, must land in-place)

## Phases

```
Phase 1: Core machinery (001-008)
   ↓  adapter + launcher + specs, tested L1/L2/L3
Phase 2: Wire ranked-output loops + doc plan-shaped loops (009-017)
```

## Tasks

| # | Task | Type | Deliverable | Depends |
|---|------|------|-------------|---------|
| 001 | [[001-build-adapter-module]] | BUILD | `render/adapters/loop_to_leaderboard.py` | - |
| 002 | [[002-build-adapter-index]] | BUILD | `render/adapters/INDEX.md` | 001 |
| 003 | [[003-build-serve-watch-launcher]] | BUILD | `render/lib/serve_and_watch.py` | - |
| 004 | [[004-build-render-step-spec]] | BUILD | `render/steps/step-serve-and-watch.md` | 003 |
| 005 | [[005-build-answer-routing-spec]] | BUILD | `render/steps/step-route-annotations.md` | - |
| 006 | [[006-test-adapter-func]] | TEST | adapter emits schema-valid items.json | 001 |
| 007 | [[007-test-launcher-serve]] | TEST | launcher serves page.html live | 003 |
| 008 | [[008-test-render-e2e]] | TEST | full adapter→serve→rows→teardown | 001,003 |
| 009 | [[009-build-wire-assay]] | BUILD | assay SKILL final render step | 004 |
| 010 | [[010-build-wire-competition]] | BUILD | competition SKILL final render step | 004 |
| 011 | [[011-build-wire-deep-dive]] | BUILD | deep-dive SKILL final render step | 004 |
| 012 | [[012-build-wire-expand]] | BUILD | expand SKILL final render step | 004 |
| 013 | [[013-build-wire-small]] | BUILD | small SKILL final render step | 004 |
| 014 | [[014-build-wire-lateral]] | BUILD | lateral SKILL final render step | 004 |
| 015 | [[015-build-wire-source]] | BUILD | source SKILL final render step | 004 |
| 016 | [[016-build-doc-plan-loops]] | BUILD | render templates INDEX note for plan-shaped loops | 004 |
| 017 | [[017-test-wiring-grep]] | TEST | all 7 ranked loops reference the render step | 009-015 |

## Notes
- Ranked-output loops wired: assay, competition, deep-dive, expand, small, lateral, source (leaderboard fits).
- Plan-shaped loops (offer, gtm, launch, operate) NOT wired — documented as needing a future board template (016).
- Reuse render_server.py + templates/leaderboard/generate.py as-is (no rebuild).
