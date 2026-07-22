# Research: Just-In-Time Rule Injection at the Tool Boundary

## Status
Open

## Priority
High — highest token-efficiency alternative, and it extends the kernel's core thesis (mechanical enforcement at the tool boundary) rather than replacing it.

## Summary
Instead of re-reading the full protocol/spec every N actions, the PreToolUse hook inspects the attempted action and injects ONLY the relevant rule at the moment of use — e.g., a write to `pages/login_page.py` gets the 5-line Layer 2 Page Object rule in the hook output. Zero context bloat; the rule arrives at the exact moment it can be violated. Our gate enforcers already do the blocking half (block + FIX text); research the injection half: proactive per-path/per-layer rule delivery without a block.

## Requirements
- Inventory current hook behavior: which rules are already mechanically enforced (blocks) vs. protocol-only (soft) — the soft set is the JIT candidate list
- Verify injection mechanics in our Claude Code version: can PreToolUse return advisory context (non-blocking `additionalContext`/system message) or is output only visible on block? Test live
- Design rule-routing: file-path/layer pattern → rule snippet lookup (e.g. rules indexed by glob in a JSON map derived from lessons.md quality gates and the 5-layer contract)
- Payload discipline: max snippet size, dedup (don't re-inject the same rule every consecutive write), interaction with actions counter
- Assess coverage limits: JIT handles rule-at-point-of-violation, but NOT drift in task direction or cross-file architecture — quantify what the anchor still must do
- **Verdict: yah or nay** — implement JIT injection alongside (not instead of) hook blocking, and if yah, hook design + rule-map schema + which anchor duties it offloads

## References
- `.claude/hooks/sr_dev-gate-enforcer.py` (rule blocking + FIX messages — the reactive half), `.claude/hooks/universal-gate-enforcer.py`
- `.claude/lessons/lessons.md` quality gates (each is a JIT rule candidate); 5-layer contract references
- Backlogs 237, 238, 240 (sibling context-decay research)
- Context-decay strategy comparison (user-provided analysis, 2026-07-21): exact rule at the exact millisecond

## Task Builder Input
- **Deliverable:** Research report — injection capability verification, rule-map design, coverage analysis vs. anchor, yah/nay verdict
- **Location:** subproject:kernel-jit-rule-injection-research
- **Scope:** RESEARCH
- **Constraints:** Research only. Injection capability must be live-tested in this harness version, not assumed from docs. No hook modifications in this backlog.
