# Step 2: Generate

## Purpose
Turn artifact data into a self-contained interactive page.

## Pre-generation Checkpoint
- Read: the template's `generate.py` docstring (input shape contract)

## Procedure
1. Create session dir `.claude/state/render-sessions/[date]-[template]/`.
2. Run `python templates/[template]/generate.py` with the artifact data → `page.html` in the session dir.
3. Verify page requirements (RND-02): self-contained (no external hosts — CSP-proof, offline-proof), annotation JS POSTs the standard schema to `/annotate`, visible "Send to session" affordance, read-only banner naming the session dir.

## Acceptance Criteria
- [ ] RND-02 satisfied: compliant page.html in session dir
