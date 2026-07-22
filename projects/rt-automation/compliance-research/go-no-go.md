# Consolidated GO / NO-GO: Therapy Compliance Automation (RT)

**Task:** 004 (RC-04) | **Synthesizes:** `domain-and-compliance.md` (001), `isagawa-feasibility.md` (002), `market-and-switching.md` (003)

---

## Verdict: GO — narrow scope, conditional on four named preconditions

Build the deterministic-layer + audit-ledger + human-gated-judgment-layer compliance harness for RT Medicare Part B eligibility/charting/billing, targeted first at the cousin's own single-facility/independent SNF. Do **not** build or pitch it as a general "AI-native governed billing platform" — that framing lost its differentiation on 2026-06-02 when PointClickCare shipped Advisor Suite natively inside the EMR this project would target (003 §4.2). The defensible version of this system is narrower: an RT-specific clinical-judgment wedge, sold on liability/audit-defensibility to an owner who already fears being CMS's next SNF audit target, not a speed/automation pitch.

---

## Why GO — the case that survives the harder look

**Feasibility (002) holds up architecturally.** The det-vs-judgment split (001 §6) maps cleanly onto Isagawa's existing 3-layer pattern plus one addition — a judgment layer that is *structurally incapable* of auto-billing (002 §1). The audit-ledger requirement isn't new engineering; it's this workspace's own attestation/decision-ledger mechanism pointed at a new domain (002 §5, and literally demonstrated by this session's own `context.ledger`). That's a real, not aspirational, fit.

**The buyer case is real for the segment that matters first.** The cousin's likely SNF — independent, single-facility — sits in the fast-decision segment where the administrator is often the owner (003 §3). That collapses the sales cycle this business would otherwise need to survive (multi-facility/CFO-gated deals are a later, harder motion, not the pilot target).

**The value case is real at the system level**, even with two numbers unverified. Documentation failures, not medical-necessity failures, drove 79.1% of 2023 CMS improper payments; MA-plan SNF denial rates run 35-56%; FCA recoveries hit $6.8B in FY2025 (003 §2.1-2.2). The unsourced numbers (SNF-RT-specific clawback precedent, per-claim labor-correction cost) are pitch-deck gaps, not go/no-go blockers — they were never load-bearing for the architecture or the buyer case, only for a "here's your exact dollar ROI" slide.

## Why this isn't a clean, unconditional GO

**Liability is the make-or-break, and it's worse than task 002 assumed.** The FCA can attach to the vendor directly, independent of the human countersign, if the judgment-layer's rubric itself is designed (even unintentionally) to nudge toward billable verdicts (003 §5.1). The never-auto-bill gate (002's core safety design) mitigates clinician and facility exposure — it does **not** mitigate this vendor-side exposure. That makes rubric-design legal review a precondition to writing the first judgment prompt, not a launch-week item.

**PCC's own posture raises the credibility floor.** Advisor Suite ships with PCC's existing BAA/SOC2/HITRUST attestations already in place (003 §4.2). A third-party wedge has to clear that bar, not just "have a BAA" — an owner comparing options will weigh an EMR-native, already-attested product against an outside vendor asking for a new BAA and new PHI access.

**The human-in-the-loop / assist-not-auto-bill / BAA posture is the explicit gating condition for this GO** — not a design nicety layered on top of a separately-justified system. Every part of the case above (feasibility's architecture, the market's liability-aversion buyer lever, the FCA analysis) only holds together *because* the system never auto-bills and never touches PHI without a signed BAA. If either constraint is loosened for speed, the GO reasoning collapses with it.

---

## The four gating preconditions (from 002 §7, reaffirmed after 003's findings) — none satisfied yet, all must be before Phase 2 build starts

1. A named LLM provider confirmed **in writing** to sign a BAA covering the judgment-layer PHI flow.
2. The cousin's target SNF's PCC instance confirmed to expose FHIR/developer API read access — if denied, MVP scope shrinks to CSV-export-assisted charting, never falls back to Playwright against live PHI-bearing sessions (002 §3, §7; this workspace's own Playwright stack has an open, unresolved click-delivery regression on multi-document navigation flows of exactly this shape).
3. An informal judgment-accuracy baseline (cousin-labeled charting examples run through a draft rubric) showing the LLM's verdicts agree with the RT's own judgment often enough that human review is a countersign, not a redo.
4. The audit-ledger export format reviewed against what an actual CMS audit response requires, not just what the kernel already produces internally.

## Top 3 de-risking actions (do these before/alongside business-plan build, not after)

1. **Legal review of the judgment-layer rubric design for FCA "cause" exposure** (003 §5.1) — this is now the single highest-severity, least-mitigated risk in the whole system and was not on task 002's radar. Get this reviewed before a single rubric prompt is written against real PHI.
2. **Confirm the RT-specific differentiation survives contact with PCC's roadmap** — talk to the cousin about how PCC's Billing Advisor actually behaves in practice (pre-submission review framing may already overlap with this system's human-in-the-loop pitch; 003 §4.2 flags this as unconfirmed from the press release alone).
3. **Start the PCC API / BAA relationship conversations now** — both are business/relationship-lead-time items outside engineering's control (002 §6), and both gate the pilot regardless of how fast the deterministic layer + audit ledger can be built.

---

## Next Step

**Immediate:** open a business-plan **build backlog** scoped to `docs/backlog/269-domain-research-therapy-compliance-automation/business-plan.md`'s existing structure (problem/solution/proof/ROI/pricing/GTM/risk posture, per that sub-doc) — that stub is explicitly gated on a GO verdict, which this document now provides. The business plan itself must carry forward the narrowed differentiation (RT-specific wedge, not general AI-native billing) and lead with liability/audit-defensibility, not automation speed, per the buyer analysis in `market-and-switching.md` §3.

The harness build itself (a separate BUILD backlog, per the 269 backlog's own scope note) should not start until precondition 1 (BAA) and precondition 3 (accuracy baseline) are at least in progress — those are the two items most likely to force a design change if they come back negative.
