# Task 002 — Verify PreCompact Hook Capability

## Type
RESEARCH

## Description
Verify PreCompact hook support in the INSTALLED Claude Code version (live check, not docs memory — RULE ZERO): event name, when it fires, payload schema, and critically whether the hook can inject content into the compacted summary or only run side effects (state writes). Also check SessionStart and any compaction-related events. Document exact capabilities with citations from live testing or official docs matched to the installed version.

## Acceptance Criteria
- [ ] File `projects/kernel-precompact-reanchor-research/01-hook-capability.md` exists
- [ ] Covers: installed Claude Code version and supported hook events
- [ ] Covers: PreCompact payload + whether content injection into the summary is possible
- [ ] Covers: whether compaction/PreCompact fires in one-shot (claude -p) agents
- [ ] Minimum 300 words

## Gate
DOC-01, DOC-02

## Dependencies
001
