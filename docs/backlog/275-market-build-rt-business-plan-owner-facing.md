# RT Compliance Business Plan — Owner-Facing Rewrite (Real Business-Plan Format)

## Status
Open

## Priority
High — this is the document administrators actually push to facility owners. The 274 draft is substantively right but reads as an internal technical/strategy brief; it must be rewritten as a real, non-technical business plan before it goes to owners.

## Parent
Iteration of [[274-market-build-rt-compliance-business-plan]] (keeps that draft's substance; changes audience, language, and format).

## Summary
Rewrite the RT compliance business plan for a **non-technical audience** (facility owners and administrators) in the **format of a real business plan**, researched against how healthcare business plans are actually structured. Strip all internal/technical branding and jargon — **no "Isagawa," no "kernel," no "3-layer/config/validator/judgment layer," no "LLM/rubric/AST."** Refer to the product plainly as **"the application" / "the solution"** (or a neutral working product name). Preserve every piece of substance from 274 + the 269 research (the compliance-gate value, the phased roadmap, the HITL and never-auto-submit guarantees, the ROI/pricing/GTM, the honest gaps) — but say it in plain business language an owner reads in one sitting.

## Requirements
- **Audience:** facility owners + administrators — non-technical. Reading level and framing: revenue, risk, cost, audit exposure, patient care — NOT architecture, models, or engineering.
- **No internal branding or jargon (hard rule):** remove "Isagawa," "kernel," "3-layer pattern," "config/validator/judgment layer," "LLM," "rubric," "AST," "harness," and any engineering terminology. The product is **"the application"** / **"the solution."** Translate every technical mechanism into plain language (e.g., not "a deterministic validator + LLM judgment layer with a kernel human-review gate" but "the application automatically checks each claim against Medicare's rules and flags anything that needs a person to review before it's billed").
- **Real business-plan FORMAT (researched):** first look up how healthcare / medical-services business plans are actually structured (SBA-style + healthcare-startup conventions), then follow that structure. Expected sections (adapt to what the research shows is standard): **Executive Summary, Company/Business Description, Market Analysis (industry, target market, competition), Products & Services, Marketing & Sales Strategy, Operations, Organization & Management, Financial Plan / Projections, Funding (if applicable), Appendix.** Add the healthcare-specific pieces the research surfaces (regulatory/HIPAA posture, reimbursement/CMS context).
- **Preserve all 274 substance, translated:** the pre-submission compliance/validation gate as the Phase-1 product; the value case (catching Part A/B miscoding, refused-treatment, missing-necessity, wrong-CPT errors before submission); audit-defensibility; ROI as avoided denials/clawbacks/audit findings; flat per-facility pricing recommendation; pilot-first GTM at the single-facility SNF; competitive framing vs the EMR-native incumbent (in plain terms).
- **Preserve the guarantees in plain language:** **a person always reviews and approves before anything is billed** (HITL mandatory), and **the application never submits a claim on its own — ever** (never-auto-submit). Keep the phased roadmap (Phase 1 compliance gate → later: patient-list assist, charting assist, billing preparation), each described plainly and each with the human-approval guarantee.
- **Honesty preserved:** the unverified numbers stay flagged as owner/expert-to-confirm — never fabricated. The four preconditions (a signed data agreement, EMR data access, an accuracy check, audit-export validation) stated plainly as things to confirm before launch.
- **Preserve the technical draft:** keep the current detailed 274 plan as an INTERNAL strategy brief (rename it, e.g. `business-plan-strategy-brief-internal.md`) so its citations/analysis aren't lost; the new owner-facing plan becomes `business-plan.md`.

## References
- `projects/rt-automation/business-plan.md` (274 — the technical draft being rewritten; becomes the internal strategy brief)
- `projects/rt-automation/compliance-research/` (269 research: go-no-go, domain-and-compliance, market-and-switching, isagawa-feasibility) and `projects/rt-automation/research-notes.md`
- Web: standard healthcare/medical business-plan format + templates (research live, cite the format source)
- `projects/rt-automation/01-design-baseline.md` (venture context)

## Task Builder Input
- **Deliverable:** `projects/rt-automation/business-plan.md` rewritten as a non-technical, real-format healthcare business plan for owners; the prior technical draft preserved as `business-plan-strategy-brief-internal.md`; a `business-plan-format-notes.md` capturing the researched format.
- **Location:** workspace:projects/rt-automation/
- **Scope:** RESEARCH
- **Constraints:** Web research to ground the business-plan format (cite the source). NO internal branding/jargon — "the application"/"the solution" only; a gate task must verify zero occurrences of Isagawa/kernel/technical-layer terms. Keep the never-auto-submit + HITL guarantees and the honest unverified-number flags. No code. Runs PARALLEL to the 270-273 kernel-fix pipeline (different files) — this time spawned WITH worktree isolation.
