# Research: Therapy Compliance Automation on Isagawa — Feasibility + Go/No-Go + Business Plan

## Status
Open

## Priority
High — active revenue venture; facility administrators are asking for a business plan to push to owners; PTs are on the ground validating the pain (manual compliance, recurring human error). Connects to the existing `projects/rt-automation/` work.

## Summary
Decide **yay or nay** on building an AI-native compliance solution — Medicare Part B eligibility + charting/billing compliance checks — for therapy-technician workflows in skilled-nursing / facility settings, built on Isagawa. Then produce a business plan facility owners can act on. The pitch: the incumbent does charting, billing, AND compliance checks **manually**, human errors are frequent and corrected by hand; an Isagawa-governed harness would run the eligibility/compliance logic deterministically + AI-assisted, flagging edge cases for review instead of mis-billing.

**USER CONFIRMED 2026-07-22: this is Respiratory Therapy (RT), not PT — the source doc and the existing rt-automation project are correct.** (Original note kept for record.) **Resolution (Task 001):** the user's message says "physical therapy (PT) technicians," but the attached source doc is **Medicare Part B eligibility for Respiratory Therapy (RT)** (nebulizer, spirometry, CPAP/BiPAP, pulse oximetry), which also matches the existing `projects/rt-automation/` venture. Confirm the actual therapy discipline (RT vs PT vs both) before scoping — the compliance rules and CPT sets differ.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[269-domain-research-therapy-compliance-automation/domain-and-compliance]] | The Medicare Part B eligibility logic (from the source doc) + manual workflow + human-error modes the software must catch |
| [[269-domain-research-therapy-compliance-automation/isagawa-feasibility]] | Can Isagawa build the compliance harness? 3-layer pattern, rt-automation precedent, technical yay/nay criteria |
| [[269-domain-research-therapy-compliance-automation/market-and-switching]] | Incumbent (manual), why facilities/owners switch, buyer, competitors, regulatory/PHI/liability risks |
| [[269-domain-research-therapy-compliance-automation/business-plan]] | Phase-2 deliverable: business plan for facility owners, gated on a "yay" research verdict |

## Requirements
- Resolve RT-vs-PT scope first (source doc = RT; message says PT; prior project = RT)
- Ground the compliance logic in the attached source doc (copied to `projects/therapy-compliance-automation/medicare-part-b-eligibility-source.docx`)
- Deliver a clear **GO / NO-GO** with an honest explanation — feasibility (Isagawa fit) AND market viability, not just technical optimism
- Identify what is deterministic (rule-based, high-confidence) vs. model-assisted (probabilistic, needs review) in the compliance checks — this is the accuracy argument
- Surface the hard risks explicitly: HIPAA/PHI handling, Medicare billing-compliance liability (a wrong "eligible" flag = false-claim exposure), audit-trail requirements, and who carries liability
- The business plan is a SEPARATE downstream deliverable, produced only after a "yay" verdict

## References
- Source doc: `projects/therapy-compliance-automation/medicare-part-b-eligibility-source.docx` (Medicare Part B RT eligibility spec)
- Existing venture: `projects/rt-automation/` (design baseline, 3-layer pattern, email-to-cousin; equity + monthly comp discussed)
- Isagawa Kernel + Playwright (the delivery vehicle); SSH compliance platform (architectural precedent per rt-automation baseline)
- On-the-ground validators: the PTs/RTs who built the current workflow and report the manual-error pain

## Task Builder Input
- **Deliverable:** Research reports in `projects/therapy-compliance-automation/` — (1) domain+compliance analysis, (2) Isagawa feasibility verdict, (3) market/switching analysis, (4) a consolidated GO/NO-GO recommendation with explanation. Business plan is a downstream deliverable gated on the verdict.
- **Location:** subproject:therapy-compliance-automation
- **Scope:** RESEARCH
- **Constraints:** Web research for Medicare Part B compliance rules, CPT coding, HIPAA/PHI + billing-compliance liability, and the competitive landscape (cite sources + dates). This is a real business/regulatory decision — flag liability and PHI-handling as first-class risks, not footnotes. No code build in this backlog; the harness build is a separate BUILD backlog if GO. Resolve RT-vs-PT before deep scoping. Not blocked by other backlogs.
