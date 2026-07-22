# Step 1: Resolve

## Purpose
Validate the request and gather the artifact data the template consumes.

## Pre-generation Checkpoint
- Read: `templates/INDEX.md` (registry)
- Read: `.claude/state/render-session.json` (single-session check)
- Read: the template's `template.md` (artifact data source + action map)

## Procedure
1. Parse `template` + optional `artifact`; `--close` → jump to step-06.
2. Unknown template → list registered templates, stop (HITL).
3. Active session (`status: serving`) → report it, require `--close` first.
4. Gather artifact data per the template's declared source. review-board: diff `docs/backlog/done/` against `review-status.json` — the SAME discovery `/kernel/review-queue` step 1 uses.

## Acceptance Criteria
- [ ] RND-01 satisfied: registry hit, single-session honored, artifact data in hand
