# Domain & Compliance: Medicare Part B RT Eligibility, Charting, Billing

**Task:** 001 (RC-01) | **Domain:** Respiratory Therapy (RT), SNF setting | **EMR:** PCC / PointClickCare
**Primary source:** `medicare-part-b-eligibility-source.docx` (domain expert: licensed RT, cousin) — read in full for this document.
**Secondary sources:** CMS Medicare Coverage Database, AAPC, industry billing guides — cited inline, accessed 2026-07-22.

---

## 1. Eligibility Rules

### 1.1 Eligible-if (ALL must hold — conjunctive)

| # | Rule | Deterministic / Judgment |
|---|------|---------------------------|
| E1 | Pt is NOT currently under a Medicare Part A covered SNF stay (or the service is being handled under Part B) | **Deterministic** — Part A/B status is a coded field, not inferred |
| E2 | Pt has active Medicare Part B coverage, or another payor that allows outpatient/ancillary RT billing | **Deterministic** — coverage/payor is a lookup |
| E3 | Pt has a valid MD/NP order for RT or the specific RT service | **Deterministic** — order exists or it doesn't (presence check) |
| E4 | Pt has a diagnosis and clinical condition supporting medical necessity | **Judgment** — "supports medical necessity" requires clinical reasoning over diagnosis + condition, not a binary field |
| E5 | Pt requires skilled RT services that cannot be safely/effectively performed independently | **Judgment** — "skilled" vs "routine/custodial" is the single hardest clinical distinction in this domain (see §5) |
| E6 | Documentation shows respiratory findings, skilled intervention, response to treatment, and continued need | **Judgment** (documentation-quality assessment) layered on **deterministic** (field presence) |

**Source (E1):** CMS consolidated billing rules — RT is bundled into the Part A SNF per diem and is *not* on the consolidated-billing exclusion list; it cannot be billed separately to Part B during a covered Part A stay (247 Medical Billing Services, "SNF Consolidated Billing Exclusions List 2026," accessed 2026-07-22; corroborated by Medium/Gregory Pino, "Bundled or Billable: Can SNFs Bill Part B for Respiratory Therapy?," accessed 2026-07-22). This is an external, independently-sourced confirmation of the domain doc's E1/D1 rule — not merely restated from the source docx.

### 1.2 Do-not-bill-if (ANY triggers a block — disjunctive; each maps to a specific eligible-if failure)

| # | Rule | Deterministic / Judgment |
|---|------|---------------------------|
| D1 | Pt is under a covered Part A stay and the service is included in the Part A SNF benefit | **Deterministic** (¬E1) |
| D2 | Pt lacks active Part B / approved payor coverage | **Deterministic** (¬E2) |
| D3 | No MD/NP order | **Deterministic** (¬E3) |
| D4 | No respiratory diagnosis or medical necessity | **Judgment** (¬E4) |
| D5 | Treatment was refused | **Deterministic** — presence of a refusal flag/initial ("R") in eMAR |
| D6 | Charting does not support the CPT code | **Judgment** — requires matching charting narrative against per-code prerequisites (§3) |
| D7 | Service is routine, custodial, or not skilled | **Judgment** (¬E5) |
| D8 | CPT code requires manual review or physician/NPP performance | **Deterministic** for the flag (code is on a manual-review list, e.g. 31720); the underlying judgment of *whether it qualifies* is not |

**System behavior on any D-rule hit:** flag for manual review, never silently deny or silently bill. Source doc is explicit: "The system should flag these cases for manual review instead of allowing billing."

### 1.3 The Three Checks (source doc's own framing — kept as the canonical gate sequence)

1. **Does the Pt need RT?** — Pt has a respiratory problem, breathing risk, or condition supporting RT services. **Judgment** (clinical-condition matching against a broad, non-exhaustive qualifying-condition list — see §2).
2. **Does the diagnosis support the intervention?** — the RT treatment must relate to the Pt's diagnosis/respiratory condition (diagnosis→intervention mapping, §2). **Judgment**, but bounded by a mapping table — closer to model-assisted-with-lookup than open clinical reasoning.
3. **Does the documentation support billing the CPT code?** — charting shows the treatment was ordered, performed, medically needed, tolerated, and not refused. **Judgment** (narrative-quality check) + **deterministic** (refusal flag, order presence).

**Key invariant (source doc, verbatim intent):** a patient can clinically need RT and still be non-billable if diagnosis, intervention, and documentation do not all three match — need alone is never sufficient.

---

## 2. Diagnosis → Intervention → CPT Mapping

| Diagnosis / Clinical Finding | Supports Intervention | CPT/HCPCS | Det. / Judgment |
|---|---|---|---|
| COPD, asthma, wheezing, SOB | Nebulizer/inhaler treatment | 94640 | **Judgment** (diagnosis-to-intervention link is clinical, not a strict lookup — condition list is illustrative, not exhaustive per source doc) |
| Atelectasis, pneumonia, weak cough, retained secretions | Incentive spirometry (IS) or chest physiotherapy (CPT) | G0237 (IS/lung expansion) or 94667/94668 (CPT/percussion) | **Judgment** |
| Desaturation, COPD, CHF, OSA, respiratory failure | Overnight pulse oximetry | 94762 | **Judgment** |
| Aerosol/nebulizer/MDI technique deficiency | Inhaler/nebulizer education | 94664 | **Judgment** |
| Documented CPAP/BiPAP need (OSA, hypoxemia, orders) | CPAP/BiPAP assessment/management | 94660 | **Judgment** |
| Broader qualifying condition list (see below) | Any of the above, if diagnosis-intervention-documentation all align | varies | **Judgment** |

**Broader qualifying-condition list** (source doc, non-exhaustive): COPD, asthma, pneumonia, respiratory failure, pleural effusion, atelectasis, CHF with breathing issues, pulmonary edema, OSA, pulmonary embolism, trach, post-COVID breathing issues, SOB, wheezing, dyspnea, orthopnea, desaturation, hypoxemia — plus indirect contributors: muscle weakness, dementia, CVA, encephalopathy, obesity, anemia, CKD, A-fib, poor mobility, malnutrition, recent hospitalization.

**CMS coverage source (cited in domain doc, verified live 2026-07-22):**
- CMS Medicare Coverage Database, Article A57224, "Billing and Coding: Respiratory Care" — https://www.cms.gov/medicare-coverage-database/view/article.aspx?articleId=57224 (confirmed live and indexed by CMS/search as of 2026-07-22; direct fetch blocked by CMS's bot protection — title and existence corroborated via web search, not hallucinated).
- Related/superseding CMS articles found during verification: A57225 ("Billing and Coding: Respiratory Care," a companion/revision article) and A56717 ("Billing and Coding: Respiratory Therapy (Respiratory Care)") — both live in the CMS Medicare Coverage Database as of 2026-07-22. **Discrepancy flag:** the source doc cites only A57224; A57225 and A56717 were not in the source doc and should be reconciled with the domain expert before the LCD is treated as final for implementation — CMS frequently maintains parallel/successor articles per MAC jurisdiction.
- LCD L34149, "Respiratory Care (Respiratory Therapy)" — https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?lcdId=34149&ver=43 (confirmed live, version 43, as of 2026-07-22). Related LCDs found: L34430, L37293, L33446 — same discrepancy flag applies (jurisdiction-specific LCDs vary by MAC; the domain doc does not specify which MAC/jurisdiction the target SNFs fall under).
- CMS coverage requirement (independently corroborated, not just source-doc-derived): "There must be a specific written order by the physician or appropriate NPP for all respiratory care services, and respiratory therapy services must be fully documented in the medical records" — consistent with E3/D3 above.

**Note on citation confidence:** CMS.gov blocks automated fetching (HTTP 403 on direct retrieval); URLs and titles above are confirmed via search-engine indexing rather than direct page fetch. This is sufficient to confirm the articles/LCDs exist and are current, but a human (or a future automation with authenticated/allowed access) should directly verify full LCD text and effective dates before any rule is hard-coded into a validator.

---

## 3. CPT Billing Rules (per-code prerequisites)

| CPT/HCPCS | Description | Prerequisites (charting must show) | Frequency/Units | Modifiers | Det. / Judgment |
|---|---|---|---|---|---|
| **94640** | Nebulizer/inhalation treatment | Treatment given + diagnosis supports it + Pt response/tolerance documented; refused treatments never counted | Per treatment | 76 (repeat treatment, same day) | **Judgment** (documentation sufficiency) + **deterministic** (refusal exclusion) |
| **94664** | Inhaler/nebulizer education | Education, demonstration, or technique correction documented; Pt needs instruction/assistance | Per session | — | **Judgment** |
| **94667 / 94668** | Chest physiotherapy / manual percussion | Reason documented (retained secretions, congestion, rhonchi, coarse breath sounds, diminished aeration, pneumonia/atelectasis risk) + Pt response/tolerance; refused treatments excluded | Per session | — | **Judgment** |
| **G0237** | Respiratory therapy / lung expansion (IS) | IS/lung expansion documented + time/unit support + Pt performance + skilled instruction/assistance/technique correction + rationale for why Pt cannot do independently; refused excluded | 1u=15min, 2u=30min, 3u=45min, 4u=60min | 59 (distinct service, jurisdiction-dependent) | **Judgment** (clinical rationale) + **deterministic** (unit/time math) |
| **94762** | Overnight pulse oximetry | Reason documented (desaturation, COPD, OSA, resp. failure, CHF, suspected nocturnal hypoxemia); results (lowest SpO₂, time <90%/<88%, O₂ use, recording time) included when available | Per study | — | **Judgment** (reason) + **deterministic** (numeric results extraction) |
| **94660** | CPAP/BiPAP assessment/management | Order + settings + O₂ bleed-in if used + mask/humidification + tolerance + skin check + leaks + respiratory status + skilled monitoring, all documented | Per assessment | — | **Judgment** (completeness of the 8-part checklist is itself a judgment call on "sufficient" documentation) |
| **31720** | Nasotracheal suction | Detected but always flagged for manual billing review — payer/performer rules vary | N/A | — | **Deterministic** — this code is a hard manual-review trigger, no auto-bill path exists |

**Independent corroboration (2026-07-22 web search, AAPC/CMS-derived CPT descriptions):**
- 94640: "pressurized or nonpressurized inhalation treatment for acute airway obstruction or for sputum induction" (AAPC / CMS article A57224 summary).
- 94664: "demonstration and/or evaluation of patient utilization of an aerosol generator, nebulizer, metered dose inhaler or IPPB device" (AAPC).
- 94667/94668: "'hands on' manipulation of the chest wall, per session" (AAPC).
- 94762: "noninvasive measurement" of oxygen saturation, distinct from 94760 (spot check) and 94761 (exercise) (AAPC/CMS).
- 94660: "continuous positive airway pressure ventilation (CPAP), initiation and management" (AAPC/CMS).
- G0237-G0239: "therapeutic procedures with an individualized physical conditioning and exercise program using proper breathing techniques ... for a patient with activity limitations" (search synthesis; source doc's framing of G0237 as IS/lung-expansion-specific should be reconciled against the fuller G0237-G0239 family with the domain expert, since public summaries describe the family more broadly than the single-code IS usage in the source doc — **discrepancy flag**).
- Modifier guidance (AARC/industry sources, not directly fetchable — PDF binary, could not extract text — flagged as **unverified pass-through** of source-doc modifier claims: 94640→mod 76, G0237→mod 59): general CMS guidance corroborates that modifier 59 requires "detailed documentation outlining the time and clinical rationale for each distinct service" when multiple services are billed same-day, which is consistent with, but does not independently confirm, the source doc's specific G0237/59 pairing.

### 3.1 Billing validation rules (block conditions — ANY blocks submission)

No order · no diagnosis support · no treatment documented · treatment refused · no skilled-need documented · no breath sounds/respiratory findings · no Pt response/tolerance · CPT not supported by charting · documentation incomplete · code requires manual review.

All block conditions above are **deterministic presence/absence checks** at the validator layer, EXCEPT "CPT not supported by charting" and "documentation incomplete," which require **judgment** (narrative-to-requirement matching).

**eMAR/charting symbol conventions (deterministic, source doc verbatim):** checkmarks = completed; initials = completed; "R" = refused.

---

## 4. Manual Workflow Today (incumbent — cousin, licensed RT, working by hand)

1. **Filtering:** RT (or admin) manually reviews SNF census/EMR to identify patients with a qualifying respiratory diagnosis or breathing-affecting condition — no systematic filter, relies on RT's memory of the qualifying-condition list and manual chart review in PCC/PointClickCare.
2. **Charting:** RT manually pulls demographics, vitals, orders, and prior notes from PCC, then hand-enters the skilled clinical assessment (breath sounds, breathing pattern, cough, secretions, O₂ status, SpO₂ response, work of breathing, IS volume, treatment given, Pt response, skilled-need rationale, plan) into free-text/structured EMR fields.
3. **Billing:** RT or billing staff manually maps completed, non-refused charting entries to CPT codes by re-reading each chart entry against the code's prerequisites (e.g., does this entry justify 94640 vs G0237?), manually excluding refused treatments, and manually flagging ambiguous codes (e.g., 31720) for physician/manual review.
4. **Compliance/audit-trail:** The incumbent process relies on the RT's own documentation habits and institutional memory to be "defensible" under a CMS audit — there is no systematic, queryable log of "why CPT X was billed for Pt Y on date Z."
5. **Correction loop:** Errors are caught by the RT/incumbent themselves (self-review) or downstream by billing staff/facility audits — no gate exists at the point of charting or billing that could block an unsupported claim before submission.

---

## 5. Human-Error Modes, Ranked (highest financial/compliance risk first)

| Rank | Error Mode | Why It's Ranked Here | Root Cause |
|---|---|---|---|
| 1 | **Part A vs Part B miscoding** — billing Part B for RT that is actually bundled into an active Part A stay | Direct, mechanical Medicare false-claim exposure; RT is *not* on the consolidated-billing exclusion list, so this is a bright-line rule violation, not a judgment call, yet still occurs because Part A/B status can change day-to-day and isn't always visible to the RT at charting time (247 Medical Billing Services 2026; Medium/Pino, accessed 2026-07-22) | Status-lookup failure (deterministic data, manually tracked) |
| 2 | **Refused-treatment billed anyway** | Deterministic rule (never bill refused treatment) violated under time pressure/manual eMAR reading — a missed "R" initial in a fast-paced chart review | Manual scan of eMAR symbols under volume/time pressure |
| 3 | **Missing order or unsupported medical necessity billed** | No MD/NP order, or diagnosis doesn't actually support the intervention, but billed because the RT assumed necessity rather than verifying the order/diagnosis link explicitly | Judgment shortcut — experienced RTs pattern-match on "usual" diagnoses without confirming the specific order exists for this patient |
| 4 | **Wrong CPT code selected** — e.g., billing 94640 (nebulizer) when charting actually supports G0237 (IS), or vice versa | Financially smaller per-instance than #1-3 (same-family code substitution, not a bundling violation) but highest-frequency error given 6+ codes with overlapping-sounding criteria | Manual cross-reading of charting narrative against code prerequisites without a lookup aid |

**Deterministic-vs-judgment takeaway:** Errors #1 and #2 sit on rules the system can enforce as **hard, deterministic gates** (Part A/B status lookup; refusal-flag exclusion) — these are the highest-leverage, lowest-risk automation targets. Errors #3 and #4 require **model-assisted judgment with mandatory human review** — automating these outright (auto-bill) would convert a human judgment error into a systematic, repeatable false-claim risk at scale, which is a materially worse failure mode than the status quo (see task 002 feasibility framing).

---

## 6. Summary: What's Deterministic vs. What's Judgment (cross-reference)

**Deterministic (rule/lookup, safe to hard-gate):**
- Part A/B coverage status (E1/D1)
- Payor/coverage presence (E2/D2)
- MD/NP order presence (E3/D3)
- Refusal flag presence (D5, eMAR "R"/checkmark/initial conventions)
- Manual-review-required code list membership (D8, e.g. 31720)
- Unit/time math for G0237 (15-min increments)
- Numeric result extraction for 94762 (SpO₂ thresholds)

**Judgment (model-assisted + mandatory human review, never auto-bill):**
- Medical necessity determination (E4/D4)
- Skilled-vs-routine/custodial distinction (E5/D7) — the single hardest and most consequential judgment call in the domain
- Diagnosis-supports-intervention matching (§2 mapping, "three checks" #2)
- Documentation-supports-CPT narrative matching (§1.3 "three checks" #3, D6)
- Documentation completeness/sufficiency (94660's 8-part checklist; G0237's rationale requirement)

This deterministic/judgment split is the load-bearing input to task 002 (Isagawa feasibility), which maps each category onto the 3-layer pattern (config/validators for deterministic checks, LLM-assisted-with-human-gate for judgment checks).

---

## 7. Open Items / Discrepancies to Reconcile with Domain Expert (cousin)

1. Source doc cites only CMS article A57224; live search surfaced companion/successor articles A57225 and A56717 that were not in the source doc — need to confirm which MAC jurisdiction and article version applies to the target SNFs.
2. Source doc's LCD reference (L34149) has related jurisdiction-specific LCDs (L34430, L37293, L33446) — need the specific MAC jurisdiction for the target SNFs to confirm the correct LCD.
3. G0237 modifier-59 and 94640 modifier-76 guidance in the source doc could not be independently verified (AARC coding-guidelines PDF was not machine-readable) — treat as domain-expert-asserted, not independently CMS-confirmed, pending a follow-up check.
4. Public CPT summaries describe G0237-G0239 as a broader "individualized physical conditioning and exercise program" family; the source doc frames G0237 narrowly as IS/lung-expansion-specific — confirm this narrower usage is what the target SNFs actually bill under, since a broader/incorrect G0237 framing could itself be a source of miscoding.

None of these open items block task 002-004; they are flagged as inputs for the eventual requirements-capture step with the cousin (per `projects/rt-automation/01-design-baseline.md`'s Phase 1) before any validator is hard-coded.
