# Market & Switching Analysis: RT Compliance Automation

**Task:** 003 (RC-03) | **References:** `domain-and-compliance.md` (task 001, rule set) + `isagawa-feasibility.md` (task 002, det-vs-judgment split, GO/NO-GO preconditions)

---

## 1. The Incumbent (Manual Model)

Already characterized in full in task 001 §4-5 — not re-derived here, restated for market framing:

The incumbent is the RT (or admin/billing staff) doing filtering, charting, and CPT mapping entirely by hand against PCC/PointClickCare, with no systematic filter, no lookup aid for CPT-prerequisite matching, and no gate that can block an unsupported claim before submission (task 001 §4). Errors are caught by self-review or downstream audit, not at the point of charting/billing (task 001 §4.5). The two highest-risk error modes — Part A/B miscoding and refused-treatment-billed-anyway — sit on rules that are mechanically deterministic but still fail today because the incumbent process is manual (task 001 §5). This is the switching wedge: the automation targets the exact failure modes the incumbent's own process structurally cannot prevent, not a speed-up of something already working.

---

## 2. Switch Value Levers (quantified, cited)

### 2.1 Denied-claim reduction
- SNF/post-acute-care claims broadly see denial rates of **35-56%** under Medicare Advantage utilization review, driven by MA plans applying restrictive criteria versus traditional Medicare (24/7 Medical Billing Services, "Medicare Advantage Denials Rise With Prior Authorizations," accessed 2026-07-22).
- Traditional Medicare fee-for-service: **over 17% of all post-acute-care denials are tied to eligibility/benefit issues** (CMS 2024-2025 data, cited via 24/7 Medical Billing Services, accessed 2026-07-22) — directly the category E1-E3/D1-D3 deterministic checks (task 001) are built to gate.
- **79.1% of improper payments in 2023 were caused by insufficient documentation alone**, not medical necessity failures (Skilled Nursing News, "CMS Tightens Audit Oversight As Improper Payments Rise and Nursing Homes Lead in Doc Errors," accessed 2026-07-22, citing 2023/2024 CMS improper-payment data) — this is the D6/documentation-completeness judgment layer's exact target.
- SNF services' 2024 improper-payment rate hit **17.2%, ≈ $5.9 billion** in potential losses system-wide (same source) — the scale of the problem this system addresses, not a per-facility claim.

### 2.2 Clawback/recoupment reduction
- FCA enforcement is at record levels: **$6.8 billion recovered in FY2025** DOJ-wide (Medical Economics, "False Claims Act recoveries hit a record $6.8 billion in 2025," accessed 2026-07-22); HHS-OIG returned **$12.70 per dollar spent** Oct 2025-Mar 2026 (OIG newsroom, accessed 2026-07-22).
- OIG's active SNF-reimbursement work-plan item (`SRS-A-25-010`, "Skilled Nursing Facility Reimbursement" series, oig.hhs.gov, accessed 2026-07-22) and Skilled Nursing News' reporting confirm SNFs are a named 2026 audit-oversight priority, specifically for **PDPM upcoding, lack of medical necessity, improper therapy billing** (medicalbillersandcoders.com, "Best SNF Billing Services Companies 2026," accessed 2026-07-22, summarizing the OIG audit focus). No SNF-specific *respiratory therapy* settlement was found in this pass (closest comparable: a non-SNF respiratory therapy FCA settlement for **$852,378**, unlicensed-personnel billing, North Atlantic Medical Services/Regional Home Care, OIG enforcement page, accessed 2026-07-22) — flagged as a gap, not a null result: SNF-RT-specific clawback precedent should be a follow-up search before this figure is used in a pitch deck.

### 2.3 Labor savings / throughput
- Facilities adopting the right technology reported **ROI of 418%**, **$132K+/year in PDPM-penalty savings**, and **260 extra staff-hours/year per nurse** (MyFieldAudits, "5 Best Skilled Nursing Software Tools in 2026," accessed 2026-07-22) — figures reflect broader SNF software adoption, not RT-specific tooling; directionally supportive, not a like-for-like estimate.
- No RT-specific per-claim correction-labor-cost figure was found in this pass (searched directly; sources returned facility-level liability/cost figures like $380K/year undocumented-falls cost and $3,000/occupied-bed liability cost — PointClickCare, "Hidden Costs Of SNF Documentation Gaps," accessed 2026-07-22 — but not a granular per-claim number). **This is a real gap in the market case** — the business plan (task 004+) should not assert a specific per-claim labor-savings number without a primary source or a facility-level time study.

### 2.4 Audit-defensibility
- Covered architecturally in task 002 §5 (kernel ledger maps directly to "why was CPT X billed for patient Y" — CMS's own stated audit-defensibility gap). Market-side support: the "documentation-not-medical-necessity" finding above (§2.1) means audit-defensibility and denial-reduction are largely the *same lever* — a system that produces a structured, judgment-verdict-plus-rationale record for every bill is directly answering the CMS finding that most improper payments are documentation failures, not care failures.

**Overall read:** the levers are real and directionally well-supported by cited system-wide data, but two specific quantified claims a business plan would want — SNF-RT-specific clawback dollar figures and per-claim labor-correction cost — are not yet independently sourced. Flag forward to task 004 as a stated data gap, not a blocker.

---

## 3. Buyer Dynamic

- Decision authority varies by SNF ownership structure: **for independent/single-facility operators, the administrator is often also the owner — decisions happen fast**; for larger or multi-facility operators, **CFOs/VPs of Finance are the right contact for platform-level technology spend with significant contract value** (The SNF List, "How to Find the Right Decision Maker at a Skilled Nursing Facility," accessed 2026-07-22).
- This confirms the assumed buyer path (admin champion → owner approves) for the **independent-operator segment** the cousin's own SNF likely represents, but flags that **multi-facility groups route through finance, not just the administrator** — a distinct, longer sales cycle if the business plan targets beyond a single-facility pilot.
- What owners weigh, per the software-ROI sourcing above (§2.3): PDPM-penalty exposure, staff-hour recovery, and denial/audit exposure are the stated financial levers facilities cite for adopting compliance/billing tech — i.e., the pitch to an owner should lead with clawback/denial risk reduction and staff-hour recovery, not "AI automation" as the headline, consistent with task 002's honest framing (a human-gated review tool, not lights-out billing).
- **Liability-aversion as a buyer lever, not just a risk:** because the incumbent's own audit-defensibility gap (task 001 §4.5) is a named CMS 2026 enforcement focus (§2.2 above), an owner's fear of being the next audit target is itself a purchase driver, not solely a switching risk to overcome.

---

## 4. Competitive Landscape

### 4.1 Existing SNF billing/compliance platforms
Established SNF billing/compliance vendors include **PointClickCare, MatrixCare, Optima Therapy, myUnity, Inovalon, and SNF Metrics** — the market's core infrastructure providers for MDS integration, PDPM HIPPS coding, Triple Check modules, ERA processing, and AR management (MedicalBillersAndCoders, "Best SNF Billing Services Companies 2026," accessed 2026-07-22). For contract therapy specifically, **Innova Health** offers a therapy-specific EHR/compliance platform for contract rehab providers in SNFs (Innova Health, accessed 2026-07-22).

### 4.2 Critical finding — EMR-native AI compliance/billing already shipping (direct competitive threat)
**PointClickCare launched "Advisor Suite" on 2026-06-02**, an AI-native workflow-automation product line for skilled nursing, including two directly overlapping products (PointClickCare press release + PR Newswire, both accessed 2026-07-22):
- **Billing Advisor** — scans clinical documentation to identify billable services and revenue risk *before claims submission*, maps billing codes, creates ancillary batches for review. This is functionally the same job as this system's charting→billing mapping layer (task 002 §1), shipped natively inside the target EMR.
- **MDS Advisor** (beta, 2026) — AI-informed completion of functional-assessment questions and documentation-accuracy visibility for PDPM compliance.
- PCC's AI charting ecosystem also already includes third-party scribe integrations (RevMaxx, Sully.ai, Twofold) under PCC's own BAA/SOC2/HITRUST posture, plus a **$65/month FHIR API tier** (2026 HIPAA-compliance analysis cited via Sully.ai blog, accessed 2026-07-22).

**This materially changes the competitive answer to "is AI-native governed differentiated?"** — the honest answer is **no longer clearly yes**. The incumbent EMR vendor is *already* building AI-native billing-risk and documentation-accuracy tooling, with the structural advantage of already holding the EMR relationship, the BAA, and the data — the exact frictions task 002 §3 and §6 name as this system's hardest external dependencies (API access, BAA). A wedge-in still has two real differentiators worth naming honestly, not overclaiming:
1. **RT-specific judgment layer** (skilled-vs-routine, diagnosis→intervention mapping at the depth of task 001 §2-3) — PCC's Advisor Suite as reported is billing-code-and-documentation-general, not built around RT's specific clinical judgment rubric (E4/E5/D4/D6/D7 in task 001 §6). Whether that specificity survives PCC's own roadmap is unknown and should be monitored, not assumed permanent.
2. **Independent human-review posture** (task 002's structural never-auto-bill gate) — a differentiator only if it's a trust/liability selling point to owners, not solely a technical one; PCC's own Billing Advisor is also framed as "before claims submission" (i.e., pre-submission review, not auto-bill), so the human-in-the-loop framing may not be unique either — this needs direct product comparison, not assumed from the press release alone.

**Verdict for task 004:** the competitive landscape is materially worse than task 002 assumed (task 002 did not have this finding). This does not kill the deterministic-layer-plus-RT-judgment niche, but it removes "AI-native automation, judgment-layer + never-auto-bill" as a clean differentiator versus the EMR vendor itself — the realistic position is a narrow, defensible RT-specific wedge (or an explicit non-PCC-EMR target market), not a general SNF billing-AI pitch.

---

## 5. KILL Risks

### 5.1 Medicare false-claim/OIG liability for a wrong eligible flag — who is liable
Liability is **shared and multi-party, not contained to one actor**: clinicians remain accountable for approving/denying AI recommendations under several states' medical-board rules; healthcare organizations deploying the AI face organizational FCA exposure; and **AI vendors themselves can be liable** — the FCA imposes liability on third parties who "cause" a false claim, and vendors selling to entities that bill government payers face exposure if they know their product is subject to government billing requirements (O'Melveny, "False Claims Act Enforcement Risks for Companies Using AI," accessed 2026-07-22). HHS-OIG has separately flagged AI-generated EHR prompts/queries as a **potentially abusive/fraudulent conduct pattern** under DOJ-HHS's FCA AI enforcement priorities (same source). **Direct implication for this build:** the vendor (Isagawa) is not insulated by "the RT signed off" — a judgment-layer prompt/rubric that systematically nudges toward "eligible" verdicts could itself become an FCA-relevant "cause," independent of the human countersign. Task 002's never-auto-bill gate mitigates clinician/facility risk but does **not** fully mitigate vendor risk if the rubric design itself is negligent or biased toward billable outcomes — this should be an explicit design constraint (rubric must not optimize for billing yield) and a legal-review item before any judgment-layer prompt ships to a real patient chart.

### 5.2 HIPAA/BAA/PHI
Covered in depth in task 002 §4 (BAA precondition, PHI minimization, log-inherits-PHI) — not re-derived. Market-side addition: PCC's own 2026 posture already includes **BAA + SOC2 + HITRUST attestations for its native AI tools** (§4.2 above) — this is the bar a third-party wedge product must match or exceed to be credible to a risk-averse owner-buyer, not merely "have a BAA in place."

### 5.3 EMR integration friction
- Real-world FHIR/API integration timelines run **4-8 weeks for a single-system integration up to 6-18 months for multi-system enterprise integration**, with **$2,000-$8,000/month per system in ongoing maintenance** due to vendor API-version churn, and integration work is commonly characterized as "20% development, 80% negotiation and coordination" (Groovyweb / Momentum sourcing, accessed 2026-07-22). Even single-EMR-vendor (PCC-only) scope does not fully avoid this — task 002 §3 already flags PCC's 3-legged OAuth authorization requirement as a per-facility relationship dependency, and this friction data corroborates that the integration risk is **schedule and coordination risk, not primarily technical risk** — consistent with task 002's "business/relationship dependency, not engineering task" framing.

### 5.4 CMS rule drift
CMS issued its CY2026 final rule with continued emphasis on documentation accuracy and improper-payment prevention (AHA News, "CMS issues final rule on CY 2026 policy and technical changes," accessed 2026-07-22), and CMS routinely revises payment-policy and coverage rules on an annual (Physician Fee Schedule) cycle plus ad hoc LCD/article revisions — task 001 §2 already found **multiple candidate successor/companion CMS articles and jurisdiction-specific LCDs** not in the source doc's original reference, confirming this is a live, not hypothetical, drift risk for this specific rule set. **Implication:** the config-layer rules (task 002 §1, `eligibility-rules.json`/`billing-codes.json`) are not "build once" — they require an explicit rule-currency maintenance process (a recurring CMS-source recheck, not a one-time build), which is an ongoing cost the honest business plan (task 004) should name, not treat as sunk into the initial build estimate.

---

## 6. Summary for Task 004

- **Value case:** real and cited at the system-wide level (denial rates, improper-payment share, FCA enforcement scale); two specific numbers (SNF-RT clawback precedent, per-claim labor cost) are gaps, not blockers — name them as open items.
- **Buyer case:** administrator-owner fast-decision path holds for single-facility/independent operators (the cousin's likely segment); multi-facility targets require a finance-buyer motion instead.
- **Competitive case — the material new finding:** PointClickCare's own June-2026 Advisor Suite (Billing Advisor, MDS Advisor) is a direct, EMR-native competitive threat that did not exist in task 002's framing. The differentiation case narrows to an RT-specific judgment wedge or a non-PCC target, not a general "AI-native governed" pitch.
- **Kill risks:** vendor-side FCA exposure is broader than task 002 assumed (not fully mitigated by human countersign alone — rubric-design liability is a distinct exposure); PCC's own BAA/SOC2/HITRUST posture raises the credibility bar for a third-party wedge; EMR integration friction is confirmed as coordination-dominated, matching task 002; CMS rule drift is confirmed as a live, ongoing maintenance cost, not a one-time build risk.
