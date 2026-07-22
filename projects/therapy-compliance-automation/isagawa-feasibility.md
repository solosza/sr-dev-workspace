# Isagawa Feasibility: RT Compliance Automation

**Task:** 002 (RC-02) | **Reference:** `projects/rt-automation/01-design-baseline.md` (3-layer pattern, not re-derived here) + `projects/therapy-compliance-automation/domain-and-compliance.md` (task 001, the rule set this feasibility maps)

---

## 1. Mapping the Checks to the 3-Layer Pattern

The rt-automation baseline's pattern (Config JSON + Python validators + Kernel enforcement) holds for RT, with one addition the baseline didn't need to make explicit for SSH: a **fourth surface for judgment checks** (LLM-assisted, gated by mandatory human review). SSH's checks are all deterministic (package installed? service running?); RT's are a mix — see §2.

| Layer | RT Instance | What Lives Here |
|---|---|---|
| **Config (JSON)** | `eligibility-rules.json`, `billing-codes.json` | The deterministic half of every rule in task 001 §1.1/§1.2/§3: Part A/B status field name, order-presence field, refusal-flag symbol convention, CPT prerequisite *field lists* (not narrative judgment), unit/time math constants, manual-review code list (e.g. 31720) |
| **Validators (Python)** | `EligibilityValidator`, `ChartingValidator`, `BillingValidator` | Deterministic presence/absence checks + numeric extraction (SpO₂ thresholds, G0237 unit math) — pure functions, no LLM call, no judgment |
| **LLM-judge layer (new — not in SSH)** | `MedicalNecessityJudge`, `SkilledVsRoutineJudge`, `DocSupportsCPTJudge` | The five judgment rows from task 001 §6 (medical necessity, skilled-vs-routine, diagnosis→intervention, documentation-supports-CPT, documentation completeness) — an LLM call with a structured rubric prompt, always returns `{verdict, confidence, rationale}`, never a silent pass |
| **Kernel Enforcement** | Isagawa hooks + protocol | Two gates, not one: (a) deterministic gate — blocks billing if any deterministic check fails (same as SSH's "can't deploy until validators pass"); (b) **human-review gate** — blocks billing if any judgment check's verdict is `eligible`/`supported` but has not been countersigned by a human, regardless of confidence score |

The judgment layer is the one real architectural addition over the SSH precedent. It is not a variant validator — it cannot return a boolean the kernel trusts unattended. It returns a recommendation the kernel is *structurally incapable* of auto-approving into a bill.

---

## 2. Deterministic vs. Model-Assisted Classification

Full rule-by-rule classification already lives in task 001 §6 (summary table) and is not re-derived here. Feasibility-relevant restatement:

**Deterministic (Config + Validator layer, safe to hard-gate, no LLM in the loop):**
- Part A/B coverage status (E1/D1) — field lookup
- Payor/coverage presence (E2/D2) — field lookup
- MD/NP order presence (E3/D3) — presence check
- Refusal-flag presence (D5) — eMAR symbol parse
- Manual-review-code-list membership (D8) — set membership
- G0237 unit/time math, 94762 numeric threshold extraction — arithmetic

**Model-assisted (LLM-judge layer, mandatory human-review gate, never auto-bill):**
- Medical necessity (E4/D4)
- Skilled-vs-routine/custodial distinction (E5/D7) — task 001 flags this as the single hardest call in the domain; it is also the one with the most direct false-claim exposure if wrong (see task 001 §5, error rank #3)
- Diagnosis-supports-intervention matching (§2 mapping table, "three checks" #2) — bounded by a lookup table, so this is closer to *retrieval-augmented judgment* than open clinical reasoning: the LLM's job is narrowing to the mapping table's candidate CPTs and flagging when the chart doesn't cleanly land on one, not diagnosing from scratch
- Documentation-supports-CPT narrative matching (D6, "three checks" #3)
- Documentation completeness/sufficiency (94660's 8-part checklist, G0237's rationale requirement) — this one is *closer to deterministic* than it looks: it can mostly be reduced to a checklist-completeness validator (are all 8 elements present as text) with only the *quality* of each element left to judgment. Recommend splitting this specific check into a deterministic presence sub-check (7 of 8 elements) + a judgment sub-check (does the rationale/tolerance narrative actually support skilled need) rather than routing the whole 8-part check through the LLM.

**Ratio:** 7 deterministic rule-families vs. 5 judgment rule-families at the rule level (task 001 §6), but judgment checks gate a larger share of *billing volume* — nearly every CPT code's prerequisite includes at least one judgment element (§3 of task 001), so almost no bill ships without at least one human-reviewed judgment verdict attached. This is the central feasibility fact: **this is not a "mostly automated, occasionally reviewed" system — it is a system where automation does the deterministic floor and the paperwork, and a human signs every bill that touches a judgment call.** That is a real efficiency gain over the fully-manual incumbent (task 001 §4) but not the "lights-out billing" pitch a naive read of "AI automation" might imply.

---

## 3. Data Access: EMR Integration vs. Playwright vs. Export

Three options, evaluated against the target EMR (PointClickCare/PCC, per task 001 header):

| Option | Fit | Notes |
|---|---|---|
| **PCC FHIR/developer API** | **Preferred, if reachable** | PointClickCare runs a self-service developer program with a FHIR API and a "USCDI Connector" for ONC-compliant third-party integration, plus a Marketplace for validated API connections (PointClickCare Developer Program press release, accessed 2026-07-22; PointClickCare FHIR API docs, accessed 2026-07-22). As of 2026, PCC is moving Marketplace partners to **3-legged OAuth** (deadline April 15, 2026, per category) — meaning the target SNF's own PCC admin must authorize the integration; this cannot be silently automated around, it's a relationship/paperwork item, not a technical blocker (DocNow, "PointClickCare's Move to 3-Legged Authentication," accessed 2026-07-22). |
| **Playwright UI automation (rt-automation baseline's default assumption)** | **Fallback, higher hard-part risk** | Works without SNF/vendor cooperation, but per `sr_dev-protocol.md`'s own lessons (`.claude/lessons/lessons.md`, "Machine-wide Chrome input loss," "click-initiated cross-document navigation" entries) this project's own Playwright/Selenium stack has hit multiple environment-level click-delivery regressions on multi-document navigation flows — exactly the shape of flow (login → census → patient detail → chart form) that `/rt/chart-patient` and `/rt/submit-billing` require. This is not hypothetical risk; it's a recorded, recurring failure class in this codebase's own history, on unrelated projects, using the same automation stack this baseline proposes reusing. |
| **CSV/manual export** | **Lowest integration risk, weakest automation value** | PCC supports data exports; this sidesteps both API-approval friction and Playwright fragility, but reduces `/rt/chart-patient` to "assist filling a form the RT still submits by hand" rather than end-to-end automation — a legitimate, lower-risk MVP scope-down, not a failure mode. |

**Recommendation:** scope the MVP around the FHIR/API path for read operations (census pull, demographics, vitals, prior charting — all read-only, lower liability if imperfect) and treat write-back (chart submission, billing submission) as the harder, later phase — via API if the SNF's PCC tier supports write scopes, via Playwright only after this repo's own environment-level click-delivery regression is independently resolved (it is currently an open, unresolved item per the lessons file — not this project's blocker to fix, but a precondition to inherit).

---

## 4. PHI Handling

Under HIPAA, an AI/automation vendor that creates, receives, maintains, or transmits PHI on behalf of a covered entity (the SNF) is a **business associate**, and a signed BAA is required regardless of whether a human reviews every output — automated PHI access counts as access (Paubox, "When does AI become a business associate under HIPAA?," accessed 2026-07-22; HIPAA Journal, "HIPAA Business Associate Agreement — 2026 Update," accessed 2026-07-22). Business associates have been directly liable for HIPAA violations since the 2013 Omnibus Rule, with penalties up to $2.13M per violation category (Medcurity, "HIPAA BAA Requirements 2026," accessed 2026-07-22).

Implications for this system, concretely:
- A BAA with each target SNF (and with any LLM API vendor used for the judgment layer, since patient charting narrative is PHI and would be sent to that vendor) is a **precondition to build, not a launch-week formality**. If the chosen LLM provider will not sign a BAA covering the judgment-layer calls, that provider is disqualified regardless of model quality.
- Charting narrative sent to the judgment layer is the highest-PHI-density data in the whole pipeline (free-text clinical notes, diagnoses, treatment response) — this is the one place minimization should be aggressive: send only the fields the specific judgment check needs (e.g., the relevant chart section + diagnosis code), not the full chart.
- Local/state audit logs (§5 below) will themselves contain PHI (patient ID, diagnosis, CPT code, rationale text) and inherit the same BAA/access-control obligations as the EMR data itself — this is not a lower-sensitivity byproduct.

---

## 5. Audit-Trail Requirement

The rt-automation baseline's stated audit pitch ("Kernel logs every action — 'Patient billed CPT 93000 because charting included X'") is directly buildable on Isagawa's existing attestation/state machinery, with no internals exposed to the SNF or CMS:

- Isagawa already has an append-only actions ledger pattern (`actions.jsonl` / anchor-log archival, this very session's mechanism) and a structured decision-ledger pattern (the `context.ledger` field with `decision`/`constraint`/`failure` entries) — both map directly onto "why was CPT X billed for patient Y on date Z": one ledger entry per judgment-layer verdict, containing the CPT code, the deterministic checks that passed, the judgment verdict + rationale text, and the human reviewer's countersign timestamp.
- This is a **fit, not a stretch** — the existing kernel mechanism was designed for "every decision has a recorded rationale," which is exactly the CMS audit-defensibility requirement (task 001 §4 names "no systematic, queryable log" as the incumbent's #1 audit weakness).
- What must NOT be exposed: kernel internals (protocol files, hook implementation, lesson history) are operator-facing, not SNF/CMS-facing. The audit surface exposed externally should be a narrow export — one row per billed CPT code, with the supporting rationale — not the raw kernel state.
- The PHI-in-logs point from §4 applies here directly: this audit log is itself a PHI store requiring the same access controls as the EMR connection.

---

## 6. Honest Effort Estimate and Hard Parts

The rt-automation baseline's Phase 1-2 timeline (2-3 weeks requirements capture + 4-6 weeks build, `01-design-baseline.md` §"Execution Plan") is **optimistic for the reasons below** — not wrong on the mechanical parts (config/validator generation via task-builder is genuinely fast, per this workspace's own track record on other domains), but it does not budget for the four hardest parts:

1. **The judgment-layer prompt/rubric design and validation is the real unknown, not the plumbing.** Five judgment checks (§2) each need a rubric prompt, few-shot examples grounded in real (de-identified) charting, and an accuracy baseline against the cousin's own clinical judgment before any human reviewer would trust the tool enough to make review faster rather than just redundant. This is a clinical-domain LLM-eval problem, not a software-build problem, and the baseline's timeline treats it as part of the same 4-6 week build phase as the deterministic validators. It is not the same kind of work and should not share a timeline bucket.
2. **PCC API access is a business/relationship dependency, not an engineering task.** 3-legged OAuth as of 2026 means the SNF's own PCC administrator must authorize the integration through PointClickCare's process — this has its own lead time, outside engineering's control, and is a hard external dependency the baseline's Phase 1 (2-3 weeks) does not explicitly account for as a *schedule risk* (it's listed as a question to ask, not a timeline risk).
3. **Playwright fallback inherits this workspace's own unresolved environment regression.** Per §3, this project's own history has multiple entries of click-delivery failures on multi-document navigation using this exact automation stack. If the PCC API path stalls on SNF-side approval, the fallback path is not a known-good fallback — it's a path with an open reliability question in this codebase's own recent history.
4. **BAA negotiation (with SNF and with LLM vendor) is a legal/business timeline, not a build timeline.** This can run in parallel with build, but it gates *launch*, not code-complete — and per §4 it can disqualify an LLM vendor late in the process if that vendor won't sign.

**Honest total-to-first-real-use estimate:** the baseline's 4-6 month MVP timeline is achievable for the deterministic layer + CLI shell + audit ledger alone (this is squarely in this workspace's demonstrated build velocity for config/validator/kernel-gate patterns). Getting the judgment layer to a state a human reviewer trusts, PLUS the PCC API relationship, PLUS signed BAAs, realistically extends the *first live SNF pilot* timeline by 6-10 weeks beyond the baseline's Phase 3 start, run mostly in parallel rather than serial, but each is a genuine external dependency this team does not fully control.

---

## 7. Technical GO/NO-GO Criteria

**GO if all of the following hold before Phase 2 (build) starts:**
- A named LLM provider willing to sign a BAA covering the judgment-layer PHI flow (§4) is identified and confirmed in writing
- At least one target SNF's PCC instance is confirmed to expose FHIR/developer API read access (§3) — if API access is denied or indefinitely delayed, the MVP scope must shrink to CSV-export-assisted charting, not silently fall back to Playwright against PHI-bearing production EMR sessions
- A judgment-check accuracy baseline (even informal — a set of cousin-labeled charting examples run through a draft rubric prompt) shows the LLM's verdicts agree with the RT's own judgment often enough that human review is a *countersign*, not a *redo* — if the LLM is wrong often enough that the RT has to re-derive the verdict independently every time, the tool provides no time savings and the honest verdict is NO-GO on that check (fall back to manual for that specific judgment category, keep only the deterministic layer + audit ledger automated)
- The audit-ledger export format (§5) is reviewed against what an actual CMS audit response requires — not just what Isagawa's kernel already produces internally

**NO-GO / hard-stop conditions (any one is disqualifying, not just a risk to manage):**
- No LLM vendor will sign a BAA covering the specific PHI data flow this system needs (§4) — there is no compliant path around this, it is not a "ship now, fix later" item
- The system design allows any path where a judgment-layer `eligible`/`supported` verdict reaches billing submission without a human countersign — this converts a human judgment error (task 001's ranked error mode #3/#4, already occurring at real but bounded rates) into a systematic, LLM-scale false-claim risk, which task 003's market analysis should weigh as the dominant kill risk (flagged forward, not analyzed here)
- Playwright automation is the only available data-access path (PCC API unreachable) AND this workspace's own click-delivery regression (§3) remains unresolved at the point automation of the write-back flows (`chart-patient`, `submit-billing`) would begin

**Verdict for this task:** technically GO **on the deterministic layer + audit ledger + human-gated judgment layer as designed** — the 3-layer-plus-judgment-layer architecture is sound and has a direct precedent in this workspace's own kernel/attestation mechanism (§5). The GO is conditional on the four criteria above, none of which are architecture problems — they are vendor-relationship, legal, and clinical-validation dependencies outside this document's scope to resolve, and are carried forward to task 003 (market/switching) and task 004 (consolidated GO/NO-GO) as named preconditions rather than assumed-solved inputs.
