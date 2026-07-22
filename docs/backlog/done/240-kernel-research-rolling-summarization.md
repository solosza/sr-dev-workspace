# Research: Rolling Summarization / Structured State Pinning

## Status
Open

## Priority
Medium — partially implemented already (anchor Step 10 writes structured `context` JSON; harness compaction summarizes history); research is about closing the gap deliberately vs. leaving it implicit.

## Summary
Industry pattern: periodically summarize older turns into structural JSON (`Completed: [...]`, `Current file state: [...]`) while pinning system rules at the top, so conversational filler (failed attempts, terminal output) drops out but architectural constraints survive. The kernel already does a manual version of this — the anchor saves a structured `context` object into session_state.json and archives the actions log. Research whether a deliberate rolling-summarization layer adds value over (a) what the anchor already saves and (b) what harness-native compaction already does.

## Requirements
- Audit current state fidelity: after a real compaction event, what survives from (1) session_state `context`, (2) workflow JSON, (3) harness summary — and what is lost (verify with a live long session, not assumption)
- Compare against the pattern's promise: is there recoverable signal we currently drop (e.g., failed-attempt history that prevents retrying dead ends — DEFECT_LOG partially covers this)
- Design candidate: anchor Step 10 extended to a rolling structured ledger (completed/failed/decisions schema) vs. new periodic summarizer — cost and complexity of each
- Overlap analysis with backlogs 237-239: if PreCompact re-anchoring (238) ships, does rolling summarization become redundant? Rank the four strategies as a portfolio
- **Verdict: yah or nay** — add explicit rolling summarization to the kernel loop, and if yah, schema + trigger point (anchor step vs. hook)

## References
- `.claude/commands/kernel/anchor.md` Step 10 (structured context save) and Step 11 (actions log archive)
- `.claude/state/session_state.json` `context` key; `DEFECT_LOG.md` pattern in hmsa-qa-platform
- Backlogs 237, 238, 239 (sibling context-decay research — this backlog owns the portfolio ranking)
- Context-decay strategy comparison (user-provided analysis, 2026-07-21): keep constraints, drop filler

## Task Builder Input
- **Deliverable:** Research report — compaction-survival audit, gap analysis, portfolio ranking of all four strategies, yah/nay verdict
- **Location:** subproject:kernel-rolling-summarization-research
- **Scope:** RESEARCH
- **Constraints:** Research only. Compaction-survival claims must come from a live observed compaction, not assumption. Portfolio ranking must reconcile with 237-239 findings if available.
