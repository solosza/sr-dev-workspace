# RT Compliance Business Plan — Internal Strategy Brief (Technical)

> **Note:** This is the detailed internal strategy brief with full citations, technical architecture details, and research grounding. It is the foundation for the owner-facing business plan (business-plan.md). Do not share this directly with non-technical stakeholders; use the owner-facing version instead.

---

# RT Compliance Business Plan — Pre-Submission Validation Gate

**Backlog:** 274 | **Status:** Phase-1 plan complete (gate BP-05 passed) + Phase 2+ roadmap added
**Grounded in:** `compliance-research/domain-and-compliance.md`, `compliance-research/isagawa-feasibility.md`, `compliance-research/market-and-switching.md`, `compliance-research/go-no-go.md` (backlog 269), plus `research-notes.md` (task 001, this backlog).

---

## SCOPE BOUNDARY (load-bearing — read this first)

This product is a **pre-submission compliance / validation gate**. It reads the RT's existing PCC charting and the CPT code about to be billed, runs eligibility and documentation checks against that existing work, and flags or blocks unsupported claims before they reach a payer — with a full audit ledger recording why every verdict was reached.

**In Phase 1 it never auto-charts, never auto-bills, and never automates patient filtering** — it adds exactly one step, a check, between finished charting and claim submission. Broader workflow automation (charting-assist, patient-filtering) is a deliberate **Phase 2+ roadmap** item — the original and still-intended long-term direction, kept explicitly on the roadmap (see Roadmap), not Phase 1. Two invariants hold in **every** phase and are the liability firewall the rest of this plan is built on: **billing *submission* is never automated**, and **no automated step ever acts on a clinical or billing decision without a human sign-off — human-in-the-loop is mandatory wherever a decision applies.** Every automated step, in any phase, only ever *proposes*; a human *approves*. This is carried through every section of this document, not stated once and forgotten.

---

## Problem

Respiratory Therapy billing at an independent SNF today runs entirely by hand. The RT (or admin/billing staff) manually reviews the census for qualifying patients, hand-charts the clinical assessment into PCC, and manually maps the finished charting to a CPT code by re-reading the entry against that code's prerequisites — with no systematic filter, no lookup aid, and no gate anywhere in the process that can catch an unsupported claim before it is submitted. Errors are caught only by the RT's own self-review or, worse, by a downstream payer denial or a CMS audit (`domain-and-compliance.md` §4).

That absence of a pre-submission gate matters because the errors it would catch are not evenly distributed — they rank sharply by financial and compliance risk (`domain-and-compliance.md` §5):

1. **Part A vs. Part B miscoding** — billing Part B for RT that is actually bundled into an active Part A SNF stay. This is a bright-line rule, not a judgment call, yet it still happens because Part A/B status can change day-to-day and isn't always visible to the RT at the moment of charting.
2. **Refused-treatment billed anyway** — a missed "R" (refused) initial in a fast, manual eMAR read under time pressure, billed as if the treatment occurred.
3. **Missing order or unsupported medical necessity billed** — an RT pattern-matches on a "usual" diagnosis and bills without confirming the specific order or necessity link for *this* patient.
4. **Wrong CPT code selected** — e.g., 94640 (nebulizer) billed when the charting actually supports G0237 (incentive spirometry), or vice versa. Lower dollar impact per instance than #1-3, but the highest-frequency error given six-plus overlapping-sounding codes with no lookup aid.

The first two are mechanically preventable — they are deterministic rule violations, not disputable clinical judgment — and they are exactly the errors an unaided manual process is worst positioned to catch, because manual review depends on a human remembering to check a status field or read an eMAR symbol correctly on every single chart, every single day.

Compounding the error exposure is an audit-defensibility gap: the incumbent process has no systematic, queryable record of *why* a given CPT code was billed for a given patient on a given date (`domain-and-compliance.md` §4.4). When CMS or a payer asks "why was this billed," the honest answer today is "the RT's documentation habits and institutional memory" — not a record. This is a named, active 2026 CMS/OIG audit-oversight focus for SNFs specifically (PDPM upcoding, lack of medical necessity, improper therapy billing — `market-and-switching.md` §2.2), and documentation failures, not medical-necessity failures, already drive 79.1% of 2023 CMS improper payments system-wide (`market-and-switching.md` §2.1). The owner-facing framing of this problem is therefore not "billing takes too long" — it is **"every claim submitted today carries an un-gated, unrecorded risk of a denial, a clawback, or an audit finding, and there is no way to show CMS why a specific bill was supportable after the fact."**

---

## Solution

The product is a **pre-submission validate-and-flag gate** that sits between the RT's existing charting workflow and claim submission. For each proposed CPT code, it:

1. **Reads** the patient's existing PCC charting and the CPT code the RT is about to bill — it does not write, select, or generate either of those inputs.
2. **Runs the eligibility rules and the "three checks"** from the domain rule set (`domain-and-compliance.md` §1.3): does the patient need RT, does the diagnosis support the intervention, does the documentation support billing this specific CPT code.
3. **Flags or blocks** any claim that fails a check — never silently denies, never silently approves. A block means "do not submit this claim without resolving the flag," not "this patient cannot receive care."
4. **Writes an audit-ledger entry** for every verdict — which checks passed, which failed, the judgment rationale where applicable, and the human countersign — so "why was CPT X billed for patient Y on date Z" has a queryable answer for the first time (`isagawa-feasibility.md` §5).

**Restating the scope boundary in-place, because it is the design, not a caveat on the design:** the gate validates over the RT's existing charting and the RT's proposed CPT code. It does not chart, it does not select which patients to see, and it does not submit claims. The RT keeps doing the clinical work and keeps doing the charting; this system adds one new step — a check — between "charting is done" and "claim goes out." That is the entire product surface. Automating billing *submission* is never in scope in any phase — that line is permanent, because the vendor-side liability case below depends on it. Automating the *drafting* of charting or the *surfacing* of the patient list is out of scope for Phase 1 but is on the Phase 2+ roadmap (see Roadmap); there too, every automated step only ever *proposes* and a human approves. What never happens, in any phase, is an automated step acting on a clinical or billing decision without a human sign-off.

The architecture maps directly onto Isagawa's existing 3-layer pattern, with one addition (`isagawa-feasibility.md` §1):

- **Config layer** (`eligibility-rules.json`, `billing-codes.json`) — the deterministic half of every rule: Part A/B status field, order-presence field, refusal-flag symbol convention, CPT prerequisite field lists, unit/time math constants, the manual-review code list.
- **Validator layer** (`EligibilityValidator`, `ChartingValidator`, `BillingValidator`) — pure-function presence/absence checks and numeric extraction, no LLM call, no judgment.
- **Judgment layer** (`MedicalNecessityJudge`, `SkilledVsRoutineJudge`, `DocSupportsCPTJudge`) — an LLM call against a structured rubric prompt for the checks that require clinical reasoning, always returning `{verdict, confidence, rationale}` — never a silent pass.
- **Kernel enforcement** — two gates, not one: a deterministic gate (blocks on any failed deterministic check) and a **human-review gate** that blocks billing on any judgment verdict of "eligible/supported" that has not been countersigned by a human, regardless of confidence score. This second gate is what makes "never auto-bill" a structural property of the system rather than a policy the system could later drift away from.

---

## Proof / Accuracy Model

The product's accuracy claim is deliberately split in two, because the underlying rules split in two (`domain-and-compliance.md` §6, `isagawa-feasibility.md` §2):

**Deterministic hard-gates — no LLM in the loop, no accuracy uncertainty.** Part A/B coverage status, payor/coverage presence, MD/NP order presence, the refusal-flag check, manual-review-code-list membership, and unit/time/numeric math (G0237 time increments, 94762 SpO2 thresholds) are field lookups and presence checks. These map directly onto error modes #1 and #2 above — the two highest-severity, highest-frequency-preventable errors in the domain — and the gate catches them with the same certainty a correctly-run lookup always has. This is the part of the accuracy story that requires no clinical judgment claim at all.

**Model-assisted judgment, gated by mandatory human review — no accuracy claim stands alone.** Medical necessity, the skilled-vs-routine/custodial distinction (the single hardest clinical call in this domain), diagnosis-supports-intervention matching, and documentation-supports-CPT narrative matching all require clinical reasoning that a config lookup cannot perform. For these, the system's job is not to be right on its own — it is to produce a structured verdict and rationale that makes the RT's or reviewer's countersign a **check**, not a **redo**. The proof standard for this layer is explicitly an accuracy *baseline* against the cousin's own clinical judgment (informal, cousin-labeled charting examples run through a draft rubric), not a claimed pass rate — and per the four gating preconditions below, that baseline has not yet been established. Until it is, the honest claim is architectural (the human-review gate cannot be bypassed), not statistical (the judgment layer's agreement rate is not yet measured).

This split is also why the product can never auto-bill: nearly every CPT code's prerequisite includes at least one judgment element, so almost no bill ships without at least one human-reviewed judgment verdict attached (`isagawa-feasibility.md` §2). The system automates the deterministic floor and the audit paperwork; it does not, and structurally cannot, automate the clinical call.

---

## ROI

The ROI case is built on avoided cost, not generated revenue — a validate-and-flag gate prevents bad claims from going out; it does not create billable volume. Three avoided-cost categories, each grounded in cited figures, apply:

1. **Denied-claim avoidance.** Medicare Advantage SNF denial rates run **35-56%** system-wide (`market-and-switching.md` §2.1). Documentation failures — exactly the class of error the deterministic gate targets (Part A/B miscoding, missing order, refused-treatment-billed-anyway) — drove **79.1% of 2023 CMS improper payments** (`market-and-switching.md` §2.1). A pre-submission gate that catches the two deterministic, highest-frequency error modes before a claim is ever submitted converts a share of that denial rate into avoided rework and avoided delayed/lost revenue.
2. **Clawback/FCA-exposure avoidance.** FCA healthcare recoveries totaled **$6.8B in FY2025** (`go-no-go.md`, `market-and-switching.md` §2.2), and CMS/OIG have named SNF PDPM upcoding and improper therapy billing as an active 2026 audit-oversight focus (`market-and-switching.md` §2.2). The closest available comparables are **not RT-specific and must be presented with that caveat**: a Symphony Healthcare Facilities SNF-rehab-therapy FCA settlement of **$300,000** (medically-unnecessary-services allegation, three Illinois SNFs, May 2026 — DOJ/HHS-OIG, independent government source, but "rehabilitation services" is not confirmed to include RT specifically) and a non-SNF respiratory-therapy FCA settlement of **$852,378** (unlicensed personnel, already flagged in `go-no-go.md`). **No SNF-RT-specific billing/coding FCA settlement is publicly documented** — this gap has now been checked across two independent research passes (269 + `research-notes.md` §1) and should be stated to the owner as an honest open item, not papered over with an extrapolated figure.
3. **Audit-defensibility value.** Independent of any denial or clawback event, the audit ledger converts "why was this billed" from an undocumented answer ("the RT's memory and habits") into a queryable, per-claim record (`isagawa-feasibility.md` §5). This has value even in a year with zero denials or audits, because SNF respiratory/quality-of-care deficiencies are an active enforcement target in their own right (St. Margaret's Center, $1.3M CMP settlement naming respiratory/tracheostomy care deficiencies, Feb 2026 — cited here only as evidence of enforcement attention, not as a billing-clawback comparable per `research-notes.md` §1).

**What is deliberately NOT modeled here, and why:** a per-claim or per-year dollar savings estimate for the cousin's specific facility. That would require a **per-claim labor-correction cost** figure that no research pass — 269's or this one's — has been able to find (`research-notes.md` §1, §5). Fabricating that number to complete an ROI formula would violate the gate contract's "never fabricate" rule. **This is owner/expert-to-confirm**: the cousin (or the facility's own billing staff) is the only credible source for current denial/rework volume and per-incident correction cost at their facility, and the ROI case should be finalized with that input rather than a market-average placeholder.

---

## Pricing

Three models were evaluated (`research-notes.md` §2):

| Model | Fit for this product | Verdict |
|---|---|---|
| **Flat per-facility SaaS** (comparable range: $150-300/bed/month for full SNF EHR platforms, aggregator-estimated, not vendor-quoted — `research-notes.md` §2.1) | Matches a single-facility, owner-operator, fast-decision customer with no CFO-gated procurement (`market-and-switching.md` §3); no metering friction; predictable cost for the pilot | **Recommended** |
| **Per-claim** ($5-25/claim, industry-survey aggregated — `research-notes.md` §2.2) | Scales with volume, but this is a gate that runs on *every* claim regardless of outcome, not a recovery tool that only runs on flagged claims — a harder pitch for a prevention product | Named as an alternative, not recommended |
| **Revenue-share / percentage-of-collections** (3-8% of collections, industry-survey aggregated — `research-notes.md` §2.3) | Actively works against this product's positioning: a rev-share fee creates a financial incentive to find claims billable, which is close to the FCA "cause" liability exposure this system exists to avoid (`go-no-go.md`) | **Rejected** — conflicts with the liability-first, never-auto-bill positioning |

**Recommendation:** a flat per-facility monthly SaaS fee, priced below the low end of the $150-300/bed/month full-EHR-platform range (this is an add-on compliance gate, not a full EHR). The exact dollar figure is a pilot-negotiation variable dependent on the target facility's bed count, which is not yet known — it should be set with the cousin directly, not asserted here as a researched market rate (`research-notes.md` §2.4, §5).

---

## Go-to-Market

**Segment and entry point:** the cousin's single-facility independent SNF is both the design target and the pilot customer — an admin-approximates-owner, fast-decision segment with no multi-stakeholder procurement cycle (`market-and-switching.md` §3). GTM for this segment is **pilot-first**, not sales-cycle-first: prove the gate on real (or shadow-mode) claims at the cousin's facility before any broader positioning is attempted.

**Champion path:** RT and billing/administrative staff are the day-to-day champions — they are the ones who feel the current process's lack of a pre-submission check — and the owner/administrator is the approver. This mirrors the segment finding above: at a single independent SNF, "champion" and "approver" are close to the same small group of people, which shortens the adoption path relative to a multi-facility chain.

**Proof point:** RT-performed validation of the judgment layer's rubric outputs against the RT's own clinical judgment (the accuracy-baseline precondition named in Proof/Accuracy Model above) doubles as the GTM proof artifact — "here is where the system agreed with your own RT's judgment, and here is where it correctly deferred to human review" is a concrete, facility-specific demonstration, not a generic accuracy claim.

**Positioning — liability/audit-defensibility, not automation speed.** This is the central differentiation decision, and it is deliberate: PointClickCare's own Billing Advisor (part of Advisor Suite) is already available today, at zero incremental cost, to every SNF already on the PCC EHR (`research-notes.md` §3), and PCC's own press-release language frames it as **revenue-forward** — finding missed/under-billed charges — not compliance-forward (`research-notes.md` §3). Competing on automation speed or "catches more charges" against a free, EHR-native incumbent is a losing position. This product instead leads with what Billing Advisor does not claim: a structural, audit-ready, never-auto-bill compliance gate whose entire value proposition is liability reduction and audit-defensibility for claims *already* being billed — a narrower, RT-specific judgment wedge (`go-no-go.md`), not a general "AI-native billing platform" claim.

---

## Roadmap — Phased Direction (Phase 1 now, Phase 2+ future)

The compliance/validation gate above is **Phase 1** — deliberately the entire near-term product and pitch, and the wedge that gets in the door. It is not the ceiling. The original and still-intended long-term direction is a broader RT workflow platform, sequenced *after* the gate earns trust and the Phase-1 preconditions (BAA, PCC API access) clear. It is kept explicitly on the roadmap so it is not lost — but it is strictly **secondary**, and it is governed by two invariants that never relax in any phase.

**Two invariants that hold in every phase:**

- **Human-in-the-loop is mandatory wherever a human decision applies.** Every automated step *proposes*; a human *approves*. This is enforced structurally by the kernel (gated outputs + human-review checkpoints), not left to policy. No step that makes a clinical or billing decision ever acts without a human sign-off.
- **Billing *submission* is never automated — permanently.** The system may assemble and prepare a claim; a human always approves before it reaches a payer. This is the FCA firewall from the Risk section below, and it is a property of every phase, not a Phase-1 limitation.

**Phased sequence (each phase ships only after the prior earns trust; each is HITL-gated):**

1. **Phase 1 — Compliance / validation gate (now).** Validate-and-flag over existing charting + proposed CPT; a human adjudicates every judgment flag. *(This document.)*
2. **Phase 2 — Patient-filtering assist.** The system *proposes* the qualifying-patient census list from the EMR; the RT reviews and confirms who to see. Automates the *surfacing*, never the clinical decision to treat.
3. **Phase 3 — Charting assist.** The system *drafts* the structured clinical assessment from vitals/orders/prior notes for the RT to review, edit, and **sign**. No chart is ever finalized under the RT's name without the RT's explicit sign-off — the draft is a starting point, not a submission.
4. **Phase 4 — Billing preparation.** The system *assembles* the CPT-coded claim from signed charting for a human to **approve before submission**. This is claim *preparation*, not *submission* — the never-auto-submit invariant above applies here in full.

Each later phase reuses the same 3-layer + judgment-layer + audit-ledger architecture and the same human-review gate; the platform grows by adding assist steps *in front of* the gate, never by removing the human from a decision. For an owner, this is the difference between adopting a one-feature tool and adopting the entry point to a governed RT workflow platform — without, at any phase, taking on auto-billing liability.

---

## Risk & Compliance Posture

**HIPAA / BAA.** The judgment layer reads PHI (existing PCC charting) to run its checks, which makes a Business Associate Agreement a hard precondition, not a launch-week formality. PointClickCare's own Advisor Suite already ships with PCC's existing BAA/SOC2/HITRUST attestations in place (`go-no-go.md`) — a third-party wedge is compared against that bar, not against "has no BAA at all" as the alternative. No PHI flows through the judgment layer until a named LLM provider has signed a BAA covering that flow in writing (see Preconditions below).

**The never-auto-bill / never-auto-chart boundary is the liability firewall, restated here because this is where it matters most.** The deterministic gate and the human-review gate (Solution, above) exist specifically to keep clinician- and facility-side liability off this system's shoulders. But the FCA exposure this system is designed to avoid can still attach **directly to the vendor**, independent of the human countersign, if the judgment layer's rubric is designed — even unintentionally — to nudge its verdicts toward "billable" (`go-no-go.md` §"Why this isn't a clean, unconditional GO"). That risk is not mitigated by the human-in-the-loop gate; it is a separate, upstream risk in how the rubric prompt itself is written. Consequently: **legal review of the judgment-layer rubric design for FCA "cause" exposure is a precondition to writing the first judgment prompt against real PHI, not a step that happens after the harness is built.** This is currently the single highest-severity, least-mitigated risk in the whole system.

**Human-review guarantee.** Every judgment-layer verdict of "eligible/supported" is blocked from reaching a billable claim until a human countersigns it, regardless of the verdict's confidence score. This is enforced as a structural kernel gate (Solution, above), not a policy setting the system could later drift away from — the same property that makes "never auto-bill" true today stays true as the rubric, the model, or the codebase changes.

## Preconditions (the four gating items — honest open items, not yet satisfied)

None of the following are satisfied as of this writing. All four gate the start of the harness build itself, and the first two — BAA and the accuracy baseline — are the two most likely to force a design change if they come back negative (`go-no-go.md`):

1. **BAA confirmed in writing.** A named LLM provider has not yet been confirmed, in writing, to sign a Business Associate Agreement covering the judgment-layer's PHI flow.
2. **PCC FHIR/API read access.** The cousin's target SNF's PointClickCare instance has not yet been confirmed to expose FHIR/developer API read access. If access is denied, MVP scope shrinks to CSV-export-assisted charting review — it does not fall back to browser automation against live PHI-bearing sessions.
3. **Judgment-accuracy baseline.** No informal accuracy baseline yet exists showing the judgment layer's verdicts agree with the RT's own clinical judgment on cousin-labeled charting examples run through a draft rubric — the evidence needed to know the human countersign will function as a check, not a redo.
4. **Audit-ledger export validated against a real CMS audit.** The audit-ledger export format has not yet been reviewed against what an actual CMS audit response requires — only against what the kernel's existing ledger mechanism produces internally.

These are stated here as open items the owner should know about before committing to a pilot timeline, not as solved problems being reported after the fact.
