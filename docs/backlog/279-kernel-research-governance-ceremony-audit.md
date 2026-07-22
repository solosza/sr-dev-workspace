# Governance Ceremony Audit — Load-Bearing Gates vs Rubber-Stamp Friction

## Status
Open

## Priority
Medium — the 2026 HITL research is blunt: "the fix is not more gates or fewer gates — it is the right gate in the right place." Some kernel gates are load-bearing; some are ceremony the operator routes around. Ceremony that gets bypassed is the rubber-stamp failure mode in reverse, and it trains the operator to treat gates as obstacles.

## Summary
A 2026 study found plan-approval gates only let humans catch a bad action 9-26% of the time — an approval click is often a rubber stamp, and the real safety comes from matching control to consequence (prevent/sandbox/cap blast-radius for what a human can't catch; reserve approval gates for high-consequence actions a human *can* realistically catch). Audit the kernel's gates against this principle: classify each as load-bearing (keep/strengthen) vs friction (cut/automate), with special attention to the ones the operator already works around.

## Evidence (gates flagged as friction this session)
- **Anchor-token tax:** the every-N-actions anchor ceremony repeatedly blocked legitimate work; background agents flipped `anchored:false` on shared state, forcing re-anchors that were pure overhead (not re-centering). The token-confirm step is enforcement theater when the real work is elsewhere.
- **JIT rule-injector friction:** the injector's Read-blindness / hook-block interactions (category 6, previously excluded) caused STEP-0 blocks that had to be worked around via PowerShell — the gate obstructed the exact action it should have allowed.
- **The pattern:** when a gate blocks a *correct* action, the operator learns to bypass, which erodes the whole hard-enforcement value proposition. That is the failure mode to hunt.

## Requirements
- **Classify every gate** (universal-gate-enforcer + sr_dev-gate-enforcer + the kernel-loop ceremonies: anchor, learn, complete, intent-chain, JIT injector) as: **load-bearing** (prevents a real, un-catchable-by-human failure — keep), **catchable-approval** (high-consequence, human can realistically catch — keep as approval), or **friction** (blocks correct actions / gets routed around — cut, automate, or replace with prevention).
- **Apply the "prevent, don't approve" test:** for each gate, ask — is this preventing an outcome a human can't catch (right), or is it an approval click that's become a rubber stamp (wrong)? Realign accordingly.
- **Anchor-cadence review:** is every-N-actions the right trigger, or does it fire on batches where nothing drifted? Consider drift-based anchoring vs fixed-count.
- **Bypass telemetry:** identify where the operator has historically worked around a gate (the strongest signal a gate is friction, not safety) — from lessons + this session's PowerShell-workaround / anchored-flip incidents.
- **Output:** a keep/cut/automate decision per gate, so governance stays hard where it matters and stops being theater where it doesn't.

## References
- 2026 HITL study (9-26% catch rate; right-gate-right-place; prevent-don't-approve): port.io/blog/human-in-the-loop-for-ai-coding-agents
- Self-improvement anchored to spec+regression-oracle (avoid goodharting): analyticsvidhya.com/blog/2026/06/self-improving-loops
- Kernel gates: `.claude/hooks/universal-gate-enforcer.py`, `.claude/hooks/sr_dev-gate-enforcer.py`, commands/kernel/{anchor,learn,complete}.md, the JIT rule-injector
- This session's friction: anchored-flip re-anchors, JIT-injector STEP-0 blocks (the excluded "category 6")

## Task Builder Input
- **Deliverable:** Research report in `projects/governance-ceremony-audit/` — a per-gate classification (load-bearing / catchable-approval / friction) with keep/cut/automate decisions, applying the prevent-don't-approve principle, plus a bypass-telemetry finding and an anchor-cadence recommendation.
- **Location:** subproject:governance-ceremony-audit
- **Scope:** RESEARCH
- **Constraints:** Do NOT weaken load-bearing gates — the goal is precision, not deregulation. Ground in real bypass history (lessons + this session), not hypotheticals. The hard-enforcement model stays; this removes theater and sharpens placement. No code; produce the decisions for follow-up fix backlogs.
