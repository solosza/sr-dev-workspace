# Research: PreCompact Hook Re-Anchoring (Event-Driven Instead of N-Action Timer)

## Status
Open

## Priority
High — directly addresses the re-anchoring paradox (appending full spec text to a saturated window accelerates compaction) and is harness-native if supported.

## Summary
Instead of firing the anchor blindly every N actions, hook the runtime's context-compaction event: when Claude Code compresses history, a PreCompact hook ensures protocol contracts, gate states, and active task are explicitly re-injected into the compressed state, and/or forces `anchored: false` so the next action triggers a full re-anchor. Re-anchoring then happens exactly when context is actually being lost. Research whether this can replace or should complement the N-action counter.

## Requirements
- Verify PreCompact hook support in our installed Claude Code version: event name, payload, whether it can inject content into the compacted summary or only run side effects (state writes)
- Determine what our current compaction already preserves (session_state.json `context` key is our manual re-injection path — how does it perform post-compaction today?)
- Design: PreCompact fires → set `anchored: false` + write structured anchor payload → next tool call hook-blocks → full `/kernel/anchor` runs on fresh context. Validate against existing gate-enforcer flow
- Failure modes: does compaction fire in one-shot (`claude -p`) agents? What happens if PreCompact never fires in a short session (answer: N-action timer as fallback)?
- Recommend hybrid policy: event-driven primary + N-action fallback (raise N?) vs. pure timer vs. pure event — with token-cost estimates for each
- **Verdict: yah or nay** — implement PreCompact re-anchoring in the kernel loop, and if yah, hook spec + settings.json wiring + state fields

## References
- `.claude/commands/kernel/anchor.md`, `.claude/hooks/universal-gate-enforcer.py`, `.claude/hooks/sr_dev-gate-enforcer.py`
- Claude Code hooks docs (PreCompact/SessionStart events) — verify against installed version, not memory (RULE ZERO)
- Backlogs 237, 239, 240 (sibling context-decay research)
- Context-decay strategy comparison (user-provided analysis, 2026-07-21): re-anchor only when context is actually being lost

## Task Builder Input
- **Deliverable:** Research report — harness capability verification, hook design, hybrid policy recommendation, yah/nay verdict
- **Location:** subproject:kernel-precompact-reanchor-research
- **Scope:** RESEARCH
- **Constraints:** Research only — no hook changes in this backlog. Hook capability claims must be verified against the installed Claude Code version (live test, not docs memory).
