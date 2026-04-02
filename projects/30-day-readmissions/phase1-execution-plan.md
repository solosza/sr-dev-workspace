# Phase 1 Execution Plan — File Load Pipeline Testing

Items 2 & 3: DRG/MDC Mapping File + Exclusion File

---

## Standup Notes — 2026-04-02

### Where I Am (Onboarding Layers)

| Layer | What | Status |
|-------|------|--------|
| 1. Project requirements | Business context, 3 paths, LOBs, DRG systems | ✅ Done (Gap 2 waiting) |
| 2. Test plan / test cases | 19 repo TCs mapped, 11 gaps identified, SIT/UAT structure | ✅ Done (Gaps 3 & 6 need ADO check) |
| 3. Access & environment | VPN, RDP, S: drive, SSMS, Tidal, mailbox | ❌ Not started |

### Testing Layers (Phase 1 scope)

| Layer | What It Tests | Status |
|-------|--------------|--------|
| 1. File processing | Pipeline works — place file → Tidal → SSIS → SP → DB → email → archive | Existing TCs mostly cover this. 11 gaps to add. |
| 2. File content | Data in the file is correct BEFORE pipeline — column names, types, values, ranges | No TCs exist. Need column specs first. |
| 3. Data integrity | Data in the DB is correct AFTER pipeline — correct inserts/updates/terminates, no orphans, no duplicates | No TCs exist. Need table access first. |
| 4. Cross-file consistency | Mapping and exclusion files agree — every DRG in exclusion exists in mapping | No TCs exist. New category. |

### Standup (pick by audience)

### Standup Script

**Opening — what I did:**

I went through the test plan and mapped everything in the repo — 19 test cases across SIT and UAT. I found 11 gaps in the existing test cases, mostly on the exclusion file side.

**The bigger finding — testing layers:**

But the bigger thing I noticed is that all our current test cases are at one layer — file processing. "Did the job run, did data load, did the email send." That's Layer 1. I see three more layers we should be covering:

- **Layer 2 — File content:** Are the column names right? Are the data types valid? Are values in range? Right now nothing validates the file itself before it hits the pipeline.
- **Layer 3 — Data integrity:** After the job runs, is the data in the DB actually correct? Did updates overwrite the right rows? Are business keys unique? No duplicates?
- **Layer 4 — Cross-file consistency:** Does every DRG in the exclusion file exist in the mapping table? If not, the downstream pend/deny logic references a DRG it can't map.

**The question that determines scope:**

Before I start writing TCs for Layers 2-3, I need to know — **what validation is already built into the SPs and SSIS packages?** If the stored procedures already reject bad column types, duplicate keys, missing required fields — then my TCs verify that works in DEV with real files. If they don't, then my TCs are the only validation and I need a lot more of them. That's the difference between writing ~11 new TCs and ~35.

→ **Can I review the SP logic and SSIS packages to see what's already covered?**
→ **Is there dev unit test coverage I can look at?**

**Follow-up on the exclusion file ACs:**

I also sent a message about the exclusion file stories — 590587 has detailed ACs but 590589 is high-level. Are those supposed to match? That determines whether QST needs 8 more test cases.

**Clarification on SIT vs UAT:**

The repo has separate folders for SIT and UAT with different test cases. I need to understand the process:

→ **What does SIT mean here — System Integration Testing?** Who's responsible for executing SIT vs UAT?
→ **What's the flow?** Dev tests → SIT → UAT → Prod? Or is there overlap?
→ **Am I responsible for SIT, UAT, or both?** The repo has SIT TCs written one way and UAT TCs written differently (UAT has shared steps, different structure). Need to know my scope.
→ **Who wrote the existing TCs?** Were SIT and UAT written by different people? That might explain why some look like duplicates but have different steps.

```
Mental Map — What I Think the Flow Is (need to confirm)

  DEV (developer)                    SIT                         UAT
  ┌──────────────┐         ┌──────────────────┐        ┌──────────────────┐
  │ Unit tests   │         │ System testing   │        │ User acceptance  │
  │ SP logic     │───→     │ End-to-end with  │───→    │ Business users   │
  │ SSIS package │         │ real files in    │        │ verify it works  │
  │              │         │ DEV/TEST env     │        │ as expected      │
  │ WHO: Dev     │         │ WHO: QA? Dev?    │        │ WHO: BA? Users?  │
  └──────────────┘         │      Me?         │        │      Me?         │
                           └──────────────────┘        └──────────────────┘

  If I own SIT only → focus on the 14 SIT TCs + gaps
  If I own both → need to understand why UAT TCs are structured differently
  If someone else owns UAT → I just need to make sure SIT is solid
```

**What I need to move forward:**

- Clarification on SIT/UAT ownership and flow
- Access to the SP code / SSIS packages so I can map what's validated vs what's not
- Environment access — VPN, S: drive, SSMS, Tidal — so I can start executing
- Answer on the exclusion file ACs

```
Mental Map — How the Standup Flows

  "I mapped the test plan"
       |
  "Found 11 gaps in Layer 1 (file processing)"
       |
  "But also found 3 layers with zero coverage"
       |
  "Before I write TCs for those → what does the SP already validate?"
       |
       ├── SP covers it → fewer TCs, my tests verify it works end-to-end
       └── SP doesn't → more TCs, my tests ARE the validation
       |
  "Also need to clarify — am I owning SIT, UAT, or both?"
       |
  "I need SP access + environment access + SIT/UAT clarity to move forward"
```

---

## Business Context — Why This Matters

### What Is a 30-Day Readmission?

**Problem Statement (from demand document):** Insufficient care coordination by hospitals prior to discharge leads to readmission for the same condition, drives up medical care costs and negatively impacts patient outcomes.

**Objective:** Enhanced patient outcomes from greater care coordination, reduced preventable readmissions, and increased affordability.

A patient is discharged from an **inpatient** (overnight hospital stay, not a doctor's office visit) hospital stay. Within 30 days, they're admitted **to the same facility** for a related condition. The **health plan** (the insurance company paying the hospital) needs to decide: **pay the second claim, deny it, or hold it for clinical review?**

> **Claim** — a bill submitted by a hospital to the health plan requesting payment for services provided to a member (patient).

> **Pend** — put the claim on hold. Don't pay it yet, don't deny it yet. Send it to a doctor to review.

> **Deny** — reject the claim. The health plan will not pay the hospital for this admission.

Today this is done manually or not at all — the health plan is losing **$7.7M annually** on readmission claims that should have been denied or sent for clinical review. Additionally, Cotiviti (external vendor) takes a 22% cut ($1.4M annually) for claim edits — building an in-house solution captures the full savings.

**This is not a regulatory mandate** — it's a voluntary cost savings and patient outcomes initiative (EAO priority). But the financial impact makes it one of the highest-priority projects.

```
Mental Map — The Money Problem

  Patient discharged ──── 30 days ────→ Patient readmitted (SAME facility)
                                              |
                                     Claim comes in ($$$)
                                              |
                          ┌───────────────────┼───────────────────┐
                     TODAY (manual)       SHOULD BE            GOAL
                          |                   |                  |
                    Nobody catches it    Caught & reviewed   Automated system
                          |                   |              catches EVERY one
                    Plan pays $$$        Some saved $$$            |
                          |                   |            $7.7M saved/year
                   $7.7M LOST/yr        Still losing some   + $1.4M saved
                   + $1.4M to Cotiviti                      by replacing Cotiviti
```

### The Proposed Solution (3 Paths)

The demand document defines three approaches working together:

```
Mental Map — The Three Paths

  Readmission within 30 days, same facility?
        |
        YES — which path?
        |
        ├── Path 1: Same Dx (diagnosis)
        |   → Identify through COTIVITI payment edits → auto-deny
        |   (Cotiviti's existing capability — but they charge 22%)
        |
        ├── Path 2: Same DRG and Dx, in-house
        |   → Identify through IN-HOUSE edits → auto-deny
        |   → 80% realization rate for same DRG/MDC readmissions
        |   → Same facility only
        |   → Excludes: cancer, trauma, pregnancy, delivery,
        |     neonatal, BH IP, discharge status 07/20/30
        |   (THIS is the new system being built)
        |
        └── Path 3: Same MDC (similar conditions)
            → Identify through MD review → recoup payment
            → Doctor reviews, decides pay or deny
            (The pend path — routes to Aerial/Medical Management)
```

> **Realization rate** — the percentage of identified readmissions that actually result in a denied/recovered payment. 80% means for every $100 in identified readmissions, $80 is actually recovered.

> **Same facility** — readmissions only count if the patient returns to the same hospital. A readmission to a different hospital is NOT flagged by this system.

> **Dx (Diagnosis)** — the medical condition the patient was treated for, coded using ICD-10 codes.

### The Two DRG Systems

DRG (Diagnosis-Related Group) is how hospitals get paid — each admission is assigned a DRG code based on diagnoses and procedures. Think of it as a category label for "what happened to the patient."

> **DRG (Diagnosis-Related Group)** — a classification system that groups hospital stays into ~750 categories based on diagnosis, procedures, age, and complications. Each DRG has a payment weight — the hospital gets paid based on which DRG the admission falls into, not by how many days the patient stayed.

> **MDC (Major Diagnostic Category)** — a broader grouping that organizes DRGs into ~25 body-system categories. Example: MDC 04 = "Diseases and Disorders of the Respiratory System." Multiple DRGs roll up into one MDC.

> **Grouper** — the software that takes a patient's diagnosis codes, procedure codes, age, and other factors as input, runs them through an algorithm, and outputs a DRG code. Different groupers (MS-DRG vs APR-DRG) use different algorithms, so the same patient data can produce different DRG codes.

That DRG maps to an MDC, which groups related DRGs together (e.g., "Diseases of the Respiratory System").

```
Mental Map — DRG → MDC Hierarchy

  Patient has pneumonia + heart failure
        |
        ↓
  [DRG Grouper Software]
        |
        ├── MS-DRG grouper (Micro-Dyn) ──→ MS-DRG 291 ──→ MDC 04 (Respiratory)
        |   Used by: MCR, PB
        |
        └── APR-DRG grouper (3M) ────────→ APR-DRG 137 ──→ MDC 04 (Respiratory)
            Used by: QST                        |
                                          Has extra detail:
                                          SOI (severity) + ROM (mortality risk)
                                          that MS-DRG doesn't have

  SAME patient, DIFFERENT DRG code depending on grouper.
  MDC might be the same — or might not.
```

| DRG System | Full Name | Used By | LOB | Grouper Software |
|-----------|-----------|---------|-----|-----------------|
| **MS-DRG** | Medicare Severity DRG | CMS (federal) | MCR (Medicare), PB (Commercial/PPO) | Micro-Dyn / DRG Active |
| **APR-DRG** | All Patient Refined DRG | 3M (used by state Medicaid programs) | QST (Quest Integration / Hawaii Medicaid) | 3M v37.1 |

**Key difference:** APR-DRG has severity-of-illness (SOI) and risk-of-mortality (ROM) subclasses that MS-DRG does not. The same diagnosis can produce different DRG/MDC assignments depending on which grouper is used.

> **SOI (Severity of Illness)** — a 1-4 scale in APR-DRG measuring how sick the patient is. 1 = minor, 4 = extreme.

> **ROM (Risk of Mortality)** — a 1-4 scale in APR-DRG measuring how likely the patient is to die. MS-DRG doesn't have these subclasses — it uses "with CC" (complication/comorbidity) and "with MCC" (major CC) instead.

### The Three LOBs

```
Mental Map — Who's Who

  ┌─────────────────────────────────────────────────────────────┐
  │                    THE HEALTH PLAN                          │
  │                                                             │
  │   ┌─────────┐      ┌─────────┐      ┌──────────────────┐   │
  │   │   MCR   │      │   PB    │      │       QST        │   │
  │   │Medicare │      │Commercial│     │  Quest/Medicaid  │   │
  │   ├─────────┤      ├─────────┤      ├──────────────────┤   │
  │   │65+,     │      │Employer,│      │Kids, families,   │   │
  │   │disabled │      │individ. │      │aged/blind/disabled│  │
  │   ├─────────┤      ├─────────┤      ├──────────────────┤   │
  │   │ MS-DRG  │      │ MS-DRG  │      │    APR-DRG       │   │
  │   │Micro-Dyn│      │Micro-Dyn│      │   3M v37.1       │   │
  │   ├─────────┤      ├─────────┤      ├──────────────────┤   │
  │   │Federal  │      │Plan     │      │State (Hawaii     │   │
  │   │rules    │      │policy   │      │Med-QUEST)        │   │
  │   │(CMS/    │      │         │      │                  │   │
  │   │ HRRP)   │      │         │      │                  │   │
  │   └─────────┘      └─────────┘      └──────────────────┘   │
  │                                                             │
  │   MCR + PB share MS-DRG        QST is on its own with      │
  │   (same grouper, same files)   APR-DRG (different grouper, │
  │                                 different files)            │
  └─────────────────────────────────────────────────────────────┘
```

> **LOB (Line of Business)** — a distinct insurance product the health plan offers to a specific population. Each LOB has its own rules, contracts, regulations, and often its own QNXT database instance. Think of it as a separate "business unit" inside the same company.

> **QNXT** — the claims adjudication platform (made by Cognizant/TriZetto). It's the system that receives claims, applies business rules, and determines whether to pay, deny, or pend each claim. The health plan runs 3 separate QNXT instances — one per LOB.

| LOB | Full Name | Population | DRG Type | QNXT Instance |
|-----|-----------|-----------|----------|---------------|
| **MCR** | Medicare | Seniors 65+, disabled | MS-DRG | MCR |
| **PB** | Preferred Provider / Commercial | Employer-sponsored, individual plans | MS-DRG | PB |
| **QST** | Quest Integration | Hawaii Medicaid (~360K members) — children, families, aged/blind/disabled | APR-DRG | QST |

**Quest Integration** is Hawaii's comprehensive Medicaid managed care program (Med-QUEST Division, Section 1115 waiver). Created January 2015 by merging QUEST (families) and QExA (aged/blind/disabled). Virtually all Hawaii Medicaid enrollees are in managed care through Quest.

> **Medicaid** — government health insurance for low-income individuals, funded jointly by federal and state governments. Each state runs its own Medicaid program. Hawaii's is called Quest Integration.

> **Medicare** — federal health insurance for people 65+ and certain disabled individuals. Funded and regulated by CMS (Centers for Medicare & Medicaid Services).

> **Managed care** — instead of the government paying hospitals directly, the government pays a health plan a fixed monthly amount per member. The health plan then manages the care and pays the claims. The health plan takes on the financial risk — which is why catching readmissions matters.

### The Business Rules (What This System Automates)

```
Mental Map — The Three Decision Paths

  Readmission within 30 days, SAME FACILITY?
        |
        YES — which path?
        |
        ├── Path 1: Same Dx (diagnosis)                    ← Cotiviti handles this today
        |   → Cotiviti's existing payment edits                (no dedicated epic)
        |   → Costs $1.4M/yr (22% cut)
        |   → No epic for replacing this directly —
        |     Item 10 says "Cotiviti to turn off their
        |     30-day readmission process" after Paths
        |     2 & 3 go live. In-house system absorbs it.
        |
        ├── Path 2: Same DRG + on exclusion list?          ← BEING BUILT (in-house)
        |   → IN-HOUSE auto-deny (no human needed)
        |   ("exclusion list" = excluded from needing
        |    clinical review — NOT excluded from denial.
        |    It's the opposite: straight to denial.)
        |
        └── Path 3: Same MDC (similar conditions)?         ← BEING BUILT (in-house)
            → PEND → route to Aerial → MD reviews
            → Doctor decides: Pay or Deny → recoup payment

  Key distinction:
    Path 2 (DENY) = same DRG (specific) + on exclusion list → clear-cut, no opinion needed
    Path 3 (PEND) = same MDC (broad category) → needs a doctor's opinion

  And NONE of these paths are Phase 1.
  Phase 1 = loading the REFERENCE DATA (mapping + exclusion files)
  that Paths 2 & 3 will use to make decisions.
```

> **Aerial / Medecision** — a cloud-based SaaS platform for utilization management. Medical Management (the department of doctors and nurses who review claims) uses Aerial to make clinical decisions: should we pay or deny this readmission?

> **Medical Management (MM)** — the clinical review team inside the health plan. These are doctors and nurses who look at the medical details and decide if a readmission was medically necessary.

> **Cotiviti** — an external payment integrity vendor. They already catch some readmissions (Path 1, same diagnosis), but charge 22% of recovered dollars ($1.4M/yr). The in-house system (Paths 2 & 3) captures savings without the vendor cut. After implementation, Cotiviti turns off their 30-day readmission process.

> **Exclusion list** — a file listing DRG codes that are **excluded from needing clinical review** (NOT "excluded from denial" — the name is counterintuitive). If a readmission's DRG is on this list, it means "this is clear-cut, no doctor needs to look at it" → the system **auto-denies** it. DRGs NOT on the list go through the normal pend-for-review path where a doctor decides. Think of it as: "excluded from the review process, straight to denial."

**Path 2 — Auto-deny (in-house, replaces Cotiviti):**
- Readmission within 30 days, **same facility**
- **Same DRG** as the original admission
- The DRG is on the **exclusion list** (excluded from clinical review)
- → Auto-deny the claim, no human review needed
- 80% realization rate
- Applies to all 3 LOBs (epics: 590772 MCR, 590794 PB, 590781 QST)

**Path 3 — Pend (hold for clinical review):**
- Readmission within 30 days, **same facility**
- **Same MDC** as the original admission (similar conditions, broader than same DRG)
- → Pend the claim, route to Medical Management in Aerial for clinical review
- Doctor decides: pay or deny → recoup payment
- Applies to all 3 LOBs (epics: 590778 MCR, 590789 PB, 590784 QST)

**The exclusion list** identifies DRGs where readmission denial doesn't need clinical judgment:
- Cancer, trauma, pregnancy, delivery, neonatal, behavioral health IP
- Discharge status: 07 (left AMA), 20 (expired), 30 (still a patient)

> **Discharge status** — a code on the claim indicating what happened when the patient left the hospital. Status 07 means the patient left against medical advice (AMA). Status 20 means the patient died. Status 30 means the patient is still in the hospital. These are excluded because readmission denial doesn't make sense in these scenarios.

### Why LOB Matters for Testing

```
Mental Map — Same Patient, Different LOB, Different Outcome

  Patient: pneumonia readmission within 30 days

  IF MCR (Medicare):                    IF QST (Medicaid):
    MS-DRG grouper runs                  APR-DRG grouper runs
    → MS-DRG 291                         → APR-DRG 137, SOI=2, ROM=1
    → MDC 04                             → MDC 04
    → Check MS DRG exclusion list        → Check APR DRG exclusion list
    → Not excluded → PEND               → Not excluded → PEND

  But change the diagnosis slightly...
    MS-DRG might → MDC 04               APR-DRG might → MDC 05
    Same MDC as prior? → PEND           Different MDC → NO PEND

  DIFFERENT grouper = DIFFERENT DRG = POTENTIALLY DIFFERENT MDC = DIFFERENT DECISION
```

The pend/deny **logic** is the same across LOBs, but the **inputs** differ:

| Factor | MCR / PB | QST |
|--------|---------|-----|
| DRG grouper | MS-DRG (Micro-Dyn) | APR-DRG (3M) |
| Same diagnosis → DRG code | May differ | May differ |
| Same DRG → MDC mapping | MS-DRG to MDC table | APR-DRG to MDC table |
| Exclusion list | MS DRG exclusion file | APR DRG exclusion file |
| Regulatory context | Medicare HRRP (federal hospital penalty) | Hawaii P4P readmission quality measure (state) |

> **HRRP (Hospital Readmissions Reduction Program)** — a federal CMS program that penalizes hospitals (up to 3% payment reduction) for excess readmissions. Important: HRRP penalizes the *hospital*, not the *claim*. Your project denies/pends individual *claims* — different mechanism, similar concept.

> **P4P (Pay for Performance)** — Hawaii's state program that rewards or penalizes hospitals based on quality measures, including readmission rates. Similar concept to HRRP but state-level for Medicaid.

**Same claim, different LOB = potentially different DRG, different MDC, different pend/deny decision.** This is why there are separate mapping files, separate exclusion files, and separate validation jobs per DRG type.

### Where Phase 1 Fits

```
Mental Map — The Foundation

  Phase 1 is the FOUNDATION. Everything else depends on it.

  ┌──────────────────────────────────────────────────────────┐
  │  Phase 2+: Pend/Deny Logic, Aerial, Cotiviti (FUTURE)   │
  │  "Does the system make the RIGHT decision?"              │
  ├──────────────────────────────────────────────────────────┤
  │  Phase 1: File Load Pipeline (THIS PLAN)                 │
  │  "Is the reference data in the database CORRECT?"        │
  │                                                          │
  │  Mapping files:   DRG → MDC lookup tables                │
  │  Exclusion files: which DRGs skip clinical review        │
  │                                                          │
  │  If these are wrong, EVERY pend/deny decision is wrong.  │
  └──────────────────────────────────────────────────────────┘
```

Phase 1 tests the **data load pipeline** — getting the DRG/MDC mappings and exclusion lists into the database correctly. This is the foundation. If the mapping or exclusion data is wrong, every downstream pend/deny decision is wrong.

> **Pipeline** — the sequence of steps that moves data from point A to point B. Here: .xlsx file on a network share → Tidal detects it → SSIS loads it → stored procedure validates it → data lands in a database table → file gets archived.

> **Tidal** — the job scheduler. Think of it as a cron job manager with a UI. It monitors folders, triggers jobs on schedule or on-demand, and logs results.

> **SSIS (SQL Server Integration Services)** — Microsoft's ETL (Extract, Transform, Load) tool. It reads the .xlsx file, transforms the data if needed, and loads it into SQL Server tables.

> **Stored Procedure (SP)** — a pre-written SQL script saved in the database that runs on demand. The validation SPs check the loaded data for errors and update a process status column.

---

## Step 1: Confirm Test Inventory & Gaps

```
Mental Map — Two Layers of Gaps (resolve Layer 1 BEFORE Layer 2)

  LAYER 1: STORY GAPS                        LAYER 2: TEST CASE GAPS
  "What don't I understand                   "What TCs are missing
   about the requirements?"                    based on the ACs?"
  ┌──────────────────────────┐               ┌──────────────────────────┐
  │ Stories have conflicting │               │ Can't identify these     │
  │ or missing info:         │               │ until Layer 1 is clear:  │
  │                          │               │                          │
  │ - Two stories, different │──── THEN ───→ │ - Which ACs need TCs?    │
  │   AC detail levels       │               │ - How many TCs total?    │
  │ - TCs mapped to wrong AC?│               │ - What test data needed? │
  │ - Column spec unknown    │               │                          │
  │ - Table names unknown    │               │                          │
  └──────────────────────────┘               └──────────────────────────┘
   Resolve with TEAM first.                   Resolve AFTER Layer 1.
```

> **TC (Test Case)** — a single documented test with steps, actions, and expected results. Stored in Azure DevOps (ADO). Each TC maps to one or more acceptance criteria.

> **AC (Acceptance Criteria)** — the "definition of done" for a user story. Written by the BA/product owner. Each AC describes a condition the system must meet. Test cases are written to verify the ACs.

> **ADO (Azure DevOps)** — Microsoft's project management and CI/CD platform. Where all work items (epics, features, stories, test cases) are tracked.

---

### Layer 1: Story Gaps (resolve with team FIRST)

These are things you don't understand about the stories themselves. Until these are answered, the TC gap analysis below is incomplete.

#### The Four Stories in Phase 1

| Story | Description | LOB | DRG Type | ACs |
|-------|-------------|-----|----------|-----|
| 591213 | Processing of MS DRG mapping file | PB + MCR | MS-DRG | AC01-AC07 (detailed) |
| 591214 | Processing of APR DRG mapping file | QST | APR-DRG | AC01-AC07 (detailed) |
| 590587 | Processing of MS DRG exclusion file | PB + MCR | MS-DRG | AC01-AC04 (detailed, with negative scenarios) |
| 590589 | Processing of APR DRG exclusion file | QST | APR-DRG | AC01-AC03 (brief, high-level) |

#### What's Unclear About the Stories

**Gap 1 — Exclusion file stories have different AC detail levels:** ✅ RESOLVED

| | 590587 (MS DRG excl / PB+MCR) | 590589 (APR DRG excl / QST) |
|---|---|---|
| AC01 | Detailed: file exists, missing file → "file not found", access denied → "permission" failure, corrupt → actionable error | Brief: "file available in SharePoint, readable format" |
| AC02 | Detailed: empty fields fail with row numbers, invalid dates fail, duplicate keys rejected | Brief: "validation of file format, layout, data" |
| AC03 | "Auditing" — commit artifact, build number, validation reports + add/update/terminate | "Job processes: add new, update existing, terminate/end-date" |
| AC04 | "Error Handling" — machine-readable validation_report.report | (doesn't exist) |

**Answer:** Both ACs should be similar. 590589 was incomplete. → The 8 "unknown" exclusion gaps below are now **confirmed gaps** — QST needs the same TCs as PB+MCR.

**Gap 2 — AC03 means different things on each exclusion story:** ⏳ WAITING

- On 590587 (MS DRG excl / PB+MCR): AC03 = "Auditing" (build numbers, artifacts)
- On 590589 (APR DRG excl / QST): AC03 = "Processing" (add, update, terminate)

**Question for team:** Is AC03 auditing, processing, or both? — No response yet.

**Gap 3 — TC 593948 may be mapped to the wrong AC:** 🔍 NEED TO CHECK MANUALLY

- TC 593948 is labeled "AC03-001" but its content is "failure summary/report availability"
- That sounds like AC04 (error handling/reporting), not AC03 (auditing or processing)

**Action:** Check in ADO whether 593948 is covering AC03 or AC04. If it's AC04, then AC03 has zero test coverage.

**Gap 4 — Exclusion file column spec is unknown:** ✅ RESOLVED

- Column specs and table names now available for all 4 file types: MS DRG mapping, APR DRG mapping, MS DRG exclusion, APR DRG exclusion.
- **Action:** Add the actual column specs and table names to this document (see Step 2 answers).

**Gap 5 — Target table names are unknown:** ✅ RESOLVED

- All table names now available for mapping and exclusion files.
- **Action:** Add the actual table names to this document (see Step 2 answers).

**Gap 6 — TC 593949 (archive) has no corresponding AC:** 🔍 NEED TO CHECK MANUALLY

- 593949 tests archive-on-success, but archiving isn't in either exclusion story's ACs
- (It IS in the mapping file stories as AC07)

**Action:** Check in ADO whether archiving should be added as an AC to the exclusion stories, or if 593949 is just inherited convention.

---

### Layer 2: Test Case Inventory & Gaps (from TFS review)

#### TFS Test Plan Structure

```
Team - 30days Readmission
├── Test Case Inventory (REPO)              ← master TCs live here
│   ├── Auto Deny                           ← TBD: haven't reviewed contents
│   └── DRG to MDC File processing
│       └── MS and APR DRG to MDC
│           ├── SIT
│           │   ├── DRG Mapping File (7)
│           │   ├── Exclude DRG File (4)
│           │   └── Audit and Report (3)
│           └── UAT
│               └── DRG Mapping (5)
└── Test Execution                          ← clones per sprint + DRG config
    ├── 01 Sprint 260305 - 3/5-3/25/2026
    │   ├── SIT (28)                        ← 14 TCs × 2 configs (MS DRG + APR DRG)
    │   └── UAT
    ├── 02 Sprint 260326 - 3/26-4/15/2026
    └── 03 Sprint 260416 - 4/16-5/6/2026
```

**Execution pattern:** One TC in repo → duplicated per DRG config in sprint execution folder. 14 SIT repo TCs × 2 = 28 SIT execution runs.

#### Repo — SIT: DRG Mapping File (7 TCs, Suite 593114)

| Order | TC ID | AC | Title |
|-------|-------|----|-------|
| 1 | 593613 | AC01-001 | Validate file exists and File format |
| 2 | 593614 | AC01-002 | File not found in sharedrive/networkdrive |
| 3 | 593740 | AC02-001 | Happy path: valid template and data |
| 4 | 593741 | AC02-002 | Missing required column |
| 5 | 593742 | AC03-001 | Insert new records with defaults |
| 6 | 593743 | AC04-001 | Success email |
| 7 | 593744 | AC05-001 | Reconciliation on clean success |

#### Repo — SIT: Exclude DRG File (4 TCs, Suite 593115)

| Order | TC ID | AC | Title |
|-------|-------|----|-------|
| 1 | 593946 | AC01-001 | Exclude File - Validate file exists and is accessible and File format |
| 2 | 593947 | AC02-001 | Exclude File - Validation of exception file processing |
| 3 | 593948 | AC03-001 | Exclude file - Failure summary/report availability |
| 4 | 593949 | AC04-001 | Exclude File Archive on successful run |

#### Repo — SIT: Audit and Report (3 TCs, Suite 593116)

| Order | TC ID | AC | Title |
|-------|-------|----|-------|
| 1 | 593747 | AC07-001 | Archive on successful run |
| 2 | 593745 | AC06-001 | Failure record content |
| 3 | 593746 | AC06-002 | Failure summary/report availability |

#### Repo — UAT: DRG Mapping (5 TCs, Suite 593761)

| Order | TC ID | Label | Title |
|-------|-------|-------|-------|
| 1 | 593762 | UAT-01 | File Processing of valid data (happy path) |
| 2 | 593763 | UAT-02 | Update & Terminate/change in same successful run |
| 3 | 593765 | UAT-03 | Success email notification to UAT DL |
| 4 | 593776 | UAT-04 | Record count reconciliation on success |
| 5 | 593777 | UAT-04 | Input file archiving after successful run |

**Note:** UAT has a shared step reference: 593775 "Prerequisite" (used by 593776).

#### SIT vs UAT — Duplicate Analysis

| SIT | UAT | Duplicate? |
|-----|-----|-----------|
| 593740 Happy path | 593762 Happy path | **Likely** — need to compare steps |
| 593743 Success email (DEV DL) | 593765 Success email (UAT DL) | **Not duplicate** — different recipient by environment |
| 593744 Reconciliation (basic steps) | 593776 Reconciliation (with shared steps, more detailed) | **Not duplicate** — UAT version is more mature, different steps |
| — | 593763 Update & Terminate | **Unique to UAT** — no SIT equivalent |
| — | 593777 Archive | **Unique to UAT** — SIT has 593747 but in Audit and Report folder |

#### Sprint 1 Execution Status (3/5-3/25/2026 — COMPLETED)

Some SIT TCs already show **Passed** for both DRG configs: 593613, 593614, 593740. Others still **Active** (593741 onward). Sprint 2 (3/26-4/15) is currently in progress.

#### Confirmed TC Gaps — To Add to Repo (11)

**Mapping file (1):**

| # | AC | Gap |
|---|-----|-----|
| 1 | AC03 | Partial failure — some rows bad, good rows still load |

Note: Update & Terminate already covered by UAT TC 593763.

**Exclusion file (10):**

| # | AC | Gap |
|---|-----|-----|
| 2 | AC01 | File not found |
| 3 | AC01 | Access denied / permission error |
| 4 | AC01 | Corrupt file → actionable error |
| 5 | AC02 | Empty required fields → fail with row numbers |
| 6 | AC02 | Invalid types / malformed dates → fail |
| 7 | AC02 | Duplicate exclusion keys → rejected |
| 8 | AC03 | Update existing exclusion data |
| 9 | AC03 | Terminate/end-date exclusion records |
| 10 | AC03 | Build number / commit artifact captured |
| 11 | AC04 | Machine-readable validation report |

#### Testing Layers Framework

```
Mental Map — Four Layers of Testing (current coverage vs gaps)

  Layer 1: FILE PROCESSING              ← Most existing TCs live here
  "Does the pipeline work?"
  Place file → Tidal → SSIS → SP → DB → email → archive
  Coverage: 19 repo TCs. 11 gaps to add.

  Layer 2: FILE CONTENT                 ← NO existing TCs
  "Is the data in the file correct BEFORE it hits the pipeline?"
  Column names, types, values, ranges, constraints
  Shift-left: catch bad files before they enter the pipeline.

  Layer 3: DATA INTEGRITY               ← NO existing TCs
  "Is the data in the DB correct AFTER the pipeline?"
  - After Update: did old values actually change?
  - After Terminate: is end date set correctly?
  - Are there duplicate rows in the target table?
  - Do row counts between source file and target table match exactly?
  - Are business keys unique?

  Layer 4: CROSS-FILE CONSISTENCY       ← NO existing TCs
  "Do the mapping and exclusion files agree with each other?"
  - Every DRG in the exclusion file should exist in the mapping table
  - If exclusion references DRG 470, does DRG 470 have a valid MDC mapping?
  - Orphaned exclusion = downstream pend/deny references a DRG it can't map

  Layer 1 tells you "the job ran."
  Layers 2-4 tell you "the job ran CORRECTLY."
```

| Layer | What | Existing TCs | Gaps |
|-------|------|-------------|------|
| 1. File processing | Pipeline works end-to-end | 19 repo TCs | 11 confirmed gaps |
| 2. File content | File data valid before pipeline | None | TBD — need column specs |
| 3. Data integrity | DB data correct after pipeline | None | TBD — need table access |
| 4. Cross-file consistency | Mapping + exclusion agree | None | TBD — new category |

---

#### Column Spec Validation TCs (TBD — need specs added to this doc)

```
Mental Map — What Existing TCs Test vs What's Missing

  EXISTING TCs:                          MISSING:
  ┌────────────────────────────┐         ┌────────────────────────────┐
  │ "Is the file there?"       │         │ "Are the COLUMNS right?"   │
  │ "Did the job run?"         │         │ "Are the VALUES valid?"    │
  │ "Did data load?"           │         │ "Are the TYPES correct?"   │
  │ "Did email send?"          │         │ "Are the RANGES valid?"    │
  │                            │         │                            │
  │ Generic — would pass with  │         │ Specific — catches the     │
  │ ANY .xlsx that has the     │         │ difference between a file  │
  │ right number of columns    │         │ that loads and a file      │
  │                            │         │ that loads CORRECTLY       │
  └────────────────────────────┘         └────────────────────────────┘
```

No existing TC validates against the **actual column spec** for each file type. The current tests check "does the file have the right number of columns" and "does the job succeed" — but not "is column B actually named MS-DRG" or "is the Effective Date in MM/DD/YYYY format."

**4 file types, each needs column-level validation:**

| File Type | LOB | Columns | Status |
|-----------|-----|---------|--------|
| MS DRG mapping file | PB + MCR | Action, MS-DRG, MDC, MS-DRG Title, Effective Date, Term Date | Known from TC 593613 |
| APR DRG mapping file | QST | TBD — may have additional columns (SOI, ROM) | Need to confirm |
| MS DRG exclusion file | PB + MCR | TBD — user has spec, not yet added here | Need to add |
| APR DRG exclusion file | QST | TBD — user has spec, not yet added here | Need to add |

**Potential TCs per file type:**

| # | Scenario | What It Catches |
|---|----------|----------------|
| 1 | Column names match spec exactly | Renamed/misspelled column headers |
| 2 | Column order matches spec | Columns present but in wrong position |
| 3 | Data types per column are valid | Text in a numeric DRG field, wrong date format |
| 4 | Required values present (no blanks in mandatory columns) | Missing DRG code, missing Action value |
| 5 | Value ranges valid | DRG code outside valid range, Action value not in {Add, Update, Terminate} |
| 6 | Cross-column consistency | Effective Date after Term Date, Action="Terminate" but no Term Date |

**Multiply by 4 file types = up to 24 column spec TCs.** Some may collapse if file types share the same structure.

TBD — need actual column specs added to this doc before writing these TCs.

#### Shift-Left Testing (TBD)

```
Mental Map — Where Testing Happens Today vs Shift-Left

  TODAY (all testing happens AFTER the job runs):

  Place file → Tidal → SSIS → SP → DB ──→ CHECK HERE (SSMS queries)
                                              |
                                         If bad data?
                                              |
                                         Already in the DB.
                                         Job already ran.
                                         Email already sent.
                                         File already archived.
                                         Cleanup required.

  SHIFT-LEFT (catch problems BEFORE the job runs):

  Place file → CHECK HERE ──→ Bad? → STOP. Fix file. Never hits pipeline.
                   |
              Validate:          Good? → Tidal → SSIS → SP → DB
              - Column names         (confident it will succeed)
              - Data types
              - Value ranges
              - Row count
              - No duplicates
```

> **Shift left** — moving testing earlier in the process. Instead of finding problems after the pipeline runs (expensive — requires cleanup, re-run, investigation), catch them at the source before the pipeline ever touches the file. Cheaper, faster, less risk.

**Why this matters for this project:**
- The current pipeline has **no pre-validation** — Tidal picks up whatever .xlsx is in the folder
- If a bad file gets loaded, the data is already in the QNXT table — you need to know how to roll it back
- A shift-left check takes seconds (open file, validate columns/data) vs minutes/hours (wait for job, check DB, find errors, clean up)

**What shift-left TCs would cover:**

| # | Check | When | How |
|---|-------|------|-----|
| 1 | File structure validation | Before placing file on S: drive | Script or manual: open .xlsx, verify headers match spec |
| 2 | Data type validation | Before placing file | Script: check each column's values match expected types |
| 3 | Business rule pre-check | Before placing file | Script: no duplicate keys, dates make sense, Action values valid |
| 4 | Row count sanity check | Before placing file | Compare to prior load — sudden 10x increase or empty file is suspicious |
| 5 | Diff against previous file | Before placing file | What changed? New rows, removed rows, modified rows — expected? |

**These could be:**
- Manual checks (open in Excel, eyeball it)
- Python scripts (openpyxl — validate programmatically)
- Eventually automated as pre-pipeline gates

TBD — blocked on column specs being added to this doc.

#### Other Items Not Yet Addressed (TBD)

| # | Item | Status |
|---|------|--------|
| 1 | **Auto Deny folder contents** — repo has an "Auto Deny" folder we haven't reviewed. May have TCs that overlap or inform file processing tests. | TBD |
| 2 | **UAT exclusion file TCs** — UAT folder only has DRG Mapping, no exclusion file TCs. Intentional or gap? | TBD |
| 3 | **End-to-end TC** — no TC covers the full chain in one run (place file → Tidal → SSIS → SP → data in table → email → archive). All TCs test individual steps. | TBD |
| 4 | **Rollback/cleanup TC** — what happens if bad data is loaded? How to undo? No TC covers recovery. | TBD |
| 5 | **TC-to-story linkage audit** — verify all TCs are linked to the correct stories in ADO. 593744 links to both 591214 and 591213 — haven't verified others. | TBD |
| 6 | **Test data strategy** — who creates .xlsx test files? Templates? Existing test data? | TBD |
| 7 | **Sprint 1 passed test verification** — did the Passed tests (593613, 593614, 593740) actually pass correctly, or marked prematurely? | TBD |

---

### Summary: What to Bring to the Team

```
Mental Map — Gap Status Tracker

  Gap 1: ACs should match?              ✅ RESOLVED — yes, both should be similar
  Gap 2: AC03 = auditing or processing? ⏳ WAITING — no response yet
  Gap 3: TC 593948 mapped to right AC?  🔍 CHECK MANUALLY in ADO
  Gap 4: Exclusion file column spec?    ✅ RESOLVED — have all specs
  Gap 5: Target table names?            ✅ RESOLVED — have all tables
  Gap 6: Archive AC for exclusion?      🔍 CHECK MANUALLY in ADO

  3 resolved, 1 waiting, 2 need manual check.
```

**Remaining actions:** Get Gap 2 answer, manually check Gaps 3 and 6 in ADO. Then Layer 2 TC gaps are fully confirmed.

---

## Step 2: Learn How to Run Tests

```
Mental Map — The Testing Chain (sequential — each step feeds the next)

  YOU at your desk
    |
    1. VPN/RDP ──→ DEV Server ──→ S: drive
    |                                |
    |                          Place .xlsx file here
    |                                |
    2. Tidal UI/CLI ──→ Trigger job on-demand
    |                        |
    |                   Job detects file → runs SSIS → runs SP
    |                        |
    |                   ┌────┴────────────────────┐
    |                   |                         |
    |              Loads data into            Archives file
    |              QNXT DEV DB               (moves from S: to archive)
    |                   |
    |              Sends email to DL
    |
    3. SSMS ──→ QNXT DEV DB ──→ SELECT queries to VERIFY data loaded correctly
    |
    4. Outlook/Mailbox ──→ Check success email arrived

  The sequence matters:
    Place file FIRST → Tidal loads it → THEN you verify with SSMS
    (SSMS is for checking AFTER the job runs, not before)
```

Before you can execute, you need to know the what/where/how for each action in the test steps.

> **SSMS (SQL Server Management Studio)** — Microsoft's GUI tool for connecting to SQL Server databases. You use it to write and run SQL queries, browse tables, and inspect data. This is how you'll verify that jobs loaded data correctly.

> **VPN (Virtual Private Network)** — secure tunnel into the corporate network. Required to access DEV servers, S: drive, and databases from your workstation.

> **RDP (Remote Desktop Protocol)** — remote login to a Windows server. You may need this to place files on the S: drive if it's not mapped to your local machine.

> **DL (Distribution List)** — an email group. The success notification email goes to a DL so the whole team sees it, not just one person.

> **S: drive** — a network share (mapped drive letter). The file drop location where Tidal watches for new .xlsx files. `S:\QNXTCOM_Claims_Readmission_Dev\Process` is the DEV path.

### Questions to Answer (grouped by who to ask)

**Ask the Dev Lead / Chuck Atoa:**

| # | Question | Why You Need It |
|---|----------|----------------|
| 1 | What is the exclusion file column spec? (Mapping file has: Action, MS-DRG, MDC, MS-DRG Title, Effective Date, Term Date — is exclusion the same?) | Can't create test files without knowing the columns |
| 2 | What are the exclusion file job names? (Mapping has `hmsa_com_imp_readmiss_apr_drg_to_mdc_load` — what's the exclusion equivalent?) | TC 593947 says `<JOB_NAME>` — need the real name |
| 3 | What are the exclusion file stored procedures? (Mapping has `readmiss_apr_drg_to_mdc_error_rpt.sp` — exclusion equivalent?) | TC 593946 step 2 needs a validation SP |
| 4 | What is the target table name for mapping file loads? (Currently `<<Table Name - TBD>>`) | Need to query it to verify inserts/updates |
| 5 | What is the target table name for exclusion file loads? | Same reason |
| 6 | What are the business keys for matching? (MS-DRG + Effective Date? Something else?) | Need for update/terminate/duplicate tests |
| 7 | What are the NULL rules for optional fields? | TC 593742 references `<NULL_RULES>` — need actual rules |
| 8 | What is the archive path for DEV? (`<<Env_ARCHIVE_PATH>>`) | TC 593747 / 593949 need the real path |
| 9 | Is there a test data prep file or template already? | Task 591498 says "identify test data" — has anyone started? |

**Ask the DBA / DB Team:**

| # | Question | Why You Need It |
|---|----------|----------------|
| 10 | DEV database connection info (server, database name) | Need to run verification queries |
| 11 | What account/access do I need to query the readmission tables? | Need SELECT access at minimum |
| 12 | Is there an audit/log table for job runs? (Table name?) | TC 593744/593745 reference run logs |
| 13 | Is there a failure/error table? (Table name?) | TC 593745 references failure records |
| 14 | Is there an email log table, or do I check a mailbox? | TC 593743 — how to verify email was sent |

**Ask Tidal Admin:**

| # | Question | Why You Need It |
|---|----------|----------------|
| 15 | How do I trigger a job on-demand in DEV? (Tidal UI? CLI? API?) | Every TC that says "Run" needs this |
| 16 | Where are the Tidal job logs? | Need to verify "file not found" message (593614) |
| 17 | Can I see job status (running/complete/failed) from my workstation? | Need to know when to check results |

**Ask your Lead / Manager:**

| # | Question | Why You Need It |
|---|----------|----------------|
| 18 | Do I have RDP/VPN access to the DEV server? | Need to place files on S: drive |
| 19 | Do I have access to the S:\QNXTCOM_Claims_Readmission_Dev\Process share? | TC 593613 step 1 |
| 20 | Which DL/mailbox receives the success email in DEV? | TC 593743 — need to monitor it |
| 21 | Should I create test cases in ADO for the identified gaps, or wait? | Process question |

---

## Step 3: Run Tests Manually

```
Mental Map — 5 Rounds, 24 Runs

  Round 1: MS DRG Mapping (PB + MCR)     ← Happy path, prove it works
  Round 2: APR DRG Mapping (QST)         ← Same tests, different grouper
  Round 3: Negative / Edge Cases          ← Break it on purpose
  Round 4: MS DRG Exclusion (PB + MCR)   ← Different file, same pipeline
  Round 5: APR DRG Exclusion (QST)       ← Same tests, different grouper

  Why this order:
  1. Start with the file type that has MORE test detail (mapping)
  2. Test both DRG types for that file
  3. THEN break things (negatives only make sense after you've seen success)
  4. THEN do the other file type (exclusion)
  5. Document EVERYTHING — especially differences between DRG types
```

Once you have answers from Step 2, execute in this order. Each test run is one row.

> **Happy path** — a test where everything is valid and correct. No errors, no edge cases. You're proving the system works under ideal conditions before you start breaking things.

> **Negative test** — a test where you intentionally provide bad input (missing file, corrupt data, wrong format) to verify the system fails gracefully with a clear error message instead of crashing.

> **Business keys** — the combination of columns that uniquely identify a record. For example, if MS-DRG + Effective Date is the business key, then two rows with the same DRG code and same date are considered the "same record" for update/terminate purposes.

### Round 1 — MS DRG Mapping File (PB + MCR LOBs)

| Run | TC | DRG/LOB | What You Do | What You Check | Document |
|-----|-----|---------|-------------|---------------|----------|
| 1 | 593613 | MS DRG | Place valid MS_DRG_*.xlsx at DEV path | File is there, opens, has correct columns | Screenshot of file + opened contents |
| 2 | 593740 | MS DRG / PB | Run `pb_validate_readmiss_ms_drg_to_mdc_load` | SP completes, data in work table, process status = success | SP output, query results |
| 3 | 593740 | MS DRG / MCR | Run `mcr_validate_readmiss_ms_drg_to_mdc_load` | Same checks for MCR | SP output, query results |
| 4 | 593742 | MS DRG | Place file with Action="Add" rows, run job | New rows in target table, defaults applied | Before/after row counts |
| 5 | 593743 | MS DRG | Check DEV DL mailbox | Email with file name, timestamps, counts | Screenshot of email |
| 6 | 593744 | MS DRG | Check counts from run #4 | Total = Processed + Failed | Query results + email counts |
| 7 | 593747 | MS DRG | Check archive path | File archived with name + timestamp | Screenshot of archive |

### Round 2 — APR DRG Mapping File (QST LOB)

| Run | TC | DRG/LOB | What You Do | What You Check | Document |
|-----|-----|---------|-------------|---------------|----------|
| 8 | 593613 | APR DRG | Place valid APR_DRG_*.xlsx at DEV path | File is there, opens, has correct columns | Screenshot |
| 9 | 593740 | APR DRG / QST | Run `qst_validate_readmiss_apr_drg_to_mdc_load` | Data validated, process status = success | SP output, query results |
| 10 | 593742 | APR DRG | Place file with Action="Add" rows, run job | New rows in target table | Before/after row counts |
| 11 | 593743 | APR DRG | Check mailbox | Email sent | Screenshot |
| 12 | 593744 | APR DRG | Check counts | Counts balance | Query results |
| 13 | 593747 | APR DRG | Check archive | File archived | Screenshot |

**Note:** Pay attention to whether APR DRG file has additional columns (SOI, ROM) or different column names vs MS DRG. Document any differences.

### Round 3 — Negative / Edge Cases (Mapping File)

| Run | TC | What You Do | What You Check | Document |
|-----|-----|-------------|---------------|----------|
| 14 | 593614 | Remove all files from DEV path, trigger `hmsa_com_imp_readmiss_apr_drg_to_mdc_load` | Job logs "file not found", no crash | Tidal job log |
| 15 | 593741 | Place file with one column removed, run job | Job fails validation, names the missing column | Error message |
| 16 | 593745 | Place file with intentional bad rows, run job | Failure table has: row ID, error reason, timestamp, run ID | Query of failure table |

### Round 4 — MS DRG Exclusion File (PB + MCR)

| Run | TC | DRG/LOB | What You Do | What You Check | Document |
|-----|-----|---------|-------------|---------------|----------|
| 17 | 593946 | MS DRG | Place valid MS DRG exclusion .xlsx at path | File is there, correct format | Screenshot |
| 18 | 593947 | MS DRG | Run exclusion load job | Rows inserted, defaults applied | Query target table |
| 19 | 593948 | MS DRG | Check failure summary report | Filterable by run ID/date | Screenshot |
| 20 | 593949 | MS DRG | Check archive path | Exclusion file archived | Screenshot |

### Round 5 — APR DRG Exclusion File (QST)

| Run | TC | DRG/LOB | What You Do | What You Check | Document |
|-----|-----|---------|-------------|---------------|----------|
| 21 | 593946 | APR DRG | Place valid APR DRG exclusion .xlsx at path | File is there, correct format | Screenshot |
| 22 | 593947 | APR DRG | Run exclusion load job | Rows inserted, defaults applied | Query target table |
| 23 | 593948 | APR DRG | Check failure summary report | Filterable by run ID/date | Screenshot |
| 24 | 593949 | APR DRG | Check archive path | Exclusion file archived | Screenshot |

**Note:** Document whether the exclusion file columns differ between MS DRG and APR DRG. Document whether the exclusion criteria (cancer, trauma, pregnancy, etc.) are the same or different per LOB.

---

## Step 4: Document What You Observe

```
Mental Map — Why This Step Matters

  Before manual testing:              After manual testing:
  ┌─────────────────────┐             ┌─────────────────────┐
  │ <<TARGET_TABLE>>    │             │ dbo.readmiss_ms_drg │
  │ <<ARCHIVE_PATH>>   │             │ S:\...\Archive      │
  │ <<JOB_NAME>>       │             │ hmsa_com_imp_...    │
  │ <<DB_SERVER>>      │             │ SQLDEV03\QNXT       │
  │ "job should work"  │             │ "job takes 45 sec,  │
  │                    │             │  emails go to DL_X,  │
  │ 20+ unknowns      │             │  archive adds _YYYYM │
  │                    │             │  MDD suffix"         │
  └─────────────────────┘             └─────────────────────┘
    Can't automate this.               Can automate this.

  Every <<placeholder>> you fill in = one less blocker for automation.
```

During manual execution, fill in this table. This becomes the source of truth for automation.

| Placeholder | Actual Value (fill in during testing) |
|-------------|--------------------------------------|
| Target table (mapping) | |
| Target table (exclusion) | |
| Audit/log table | |
| Failure/error table | |
| Email log table (if exists) | |
| Archive path (DEV) | |
| Archive path (TEST) | |
| DEV DB server | |
| DEV DB name | |
| Exclusion file columns | |
| Exclusion file job name(s) | |
| Exclusion file SP name(s) | |
| Business keys (mapping) | |
| Business keys (exclusion) | |
| NULL rules for optional fields | |
| How to trigger job (Tidal UI/CLI/API) | |
| Job log location | |
| Success email DL (DEV) | |
| Success email DL (TEST) | |
| Job completion time (approx) | |
| Anything unexpected | |

---

## Step 5: Automation Plan

```
Mental Map — The Payoff

  Steps 1-4 give you:                  Step 5 turns it into:
  ┌─────────────────────┐              ┌─────────────────────┐
  │ Confirmed TCs       │              │ "Automate these 15  │
  │ Real table names    │──────────→   │  tests first using  │
  │ Real job behavior   │              │  pytest + pyodbc.   │
  │ Real timing         │              │  Runs in 2 hours    │
  │ Real edge cases     │              │  instead of 3 days. │
  │ PHI/CUI answer      │              │  AI-augmented if    │
  │                     │              │  PHI allows it."    │
  └─────────────────────┘              └─────────────────────┘

  You can't write a credible automation plan without doing it by hand first.
  That's why Step 5 is LAST.
```

**Do not write this until Steps 1-4 are complete.**

After manual execution, you will have:
- Confirmed test inventory (existing 13 + any new TCs from gap analysis)
- All `<<TBD>>` placeholders filled in with real values
- Firsthand knowledge of system behavior, timing, edge cases
- Evidence of what's automatable vs what requires manual verification

> **PHI (Protected Health Information)** — any health data that can identify a specific patient (name, SSN, medical record number, diagnosis linked to a person). Regulated by HIPAA. If test data contains PHI, strict controls apply.

> **CUI (Controlled Unclassified Information)** — a federal marking for sensitive but not classified data. Some organizations classify database schemas, table names, or system architecture as CUI. If yours does, even sharing column names with an LLM could be a compliance issue.

> **pytest** — Python's most popular testing framework. You write test functions, pytest discovers and runs them, and reports pass/fail with details.

> **openpyxl** — Python library for reading/writing .xlsx Excel files. Used in Layer 1 to validate file structure without needing Excel installed.

> **pyodbc** — Python library for connecting to SQL Server (and other databases) via ODBC. Used in Layer 2 to run verification queries after jobs complete.

The automation plan will cover:
- Which tests to automate first (highest ROI)
- Which approach: traditional automation vs AI-augmented (informed by PHI/CUI answer)
- Tool stack (pytest + openpyxl + pyodbc — already proven in automation-approach.md)
- Test data strategy (synthetic .xlsx generation)
- CI integration (how often, triggered by what)
- Estimated effort

---

## Timeline Estimate

```
Mental Map — The 2-Week Path

  Week 1                              Week 2
  ┌─────────────────────────┐         ┌─────────────────────────┐
  │ Mon: Team meeting       │         │ Mon-Wed: Manual testing  │
  │       (Step 1 — gaps)   │         │   (Step 3 — 24 runs)    │
  │                         │         │   (Step 4 — fill table)  │
  │ Tue-Thu: Chase answers  │         │                          │
  │   (Step 2 — 21 Qs)     │         │ Thu-Fri: Automation plan │
  │   Dev lead, DBA, Tidal  │         │   (Step 5 — the payoff) │
  │                         │         │                          │
  │ Fri: Access confirmed?  │         │ Ready to present.       │
  │   VPN, S: drive, SSMS   │         │                          │
  └─────────────────────────┘         └─────────────────────────┘
```

| Step | Effort | Depends On |
|------|--------|-----------|
| 1. Confirm gaps | 1 meeting | Team availability |
| 2. Get answers | 1-3 days | Dev lead, DBA, Tidal admin responses |
| 3. Run manually | 3-5 days | Access to DEV environment |
| 4. Document observations | During step 3 | — |
| 5. Automation plan | 1-2 days | Steps 1-4 complete |

**Total: ~2 weeks** from kickoff to automation plan ready.
