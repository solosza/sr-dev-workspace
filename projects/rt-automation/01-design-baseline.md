# RT Automation Design Baseline

**Status:** Design Phase
**Updated:** 2026-05-26
**Domain:** Respiratory Therapy Compliance Automation

---

## Executive Summary

Build an AI-native respiratory therapy (RT) automation platform using Isagawa Kernel + Playwright, modeled on the SSH compliance platform. Domain expertise (your cousin's) encodes into JSON config + Python validators. Compliance is non-bypassable via hooks. Everything runs as CLI commands (`/rt/filter-patients`, `/rt/chart-patient`, `/rt/submit-billing`). No separate UI — RTs use command interface like any SNF staff tool.

---

## SSH Platform Architecture → RT Automation Blueprint

### SSH Compliance Architecture (3 Layers)

| Layer | SSH Example | How It Works |
|-------|------------|-------------|
| **Config (JSON)** | `host_configs.json` — declarative list of hosts, packages, services, expected states | Declarative: "These packages must exist" — no HOW |
| **Validators (Python)** | `PackageValidator`, `KernelValidator`, `ServiceValidator` — stateless, call SSH interface, return results | Execution: "Check if package installed" — enforces HOW |
| **Kernel Enforcement** | Isagawa hooks + protocol — gates prevent non-compliant operations | Safety: "Can't deploy until all validators pass" |

### RT Automation → Same Pattern

| Layer | RT Equivalent | What It Does |
|-------|---|---|
| **Config (JSON)** | `patient_configs.json` — list of SNFs, patient eligibility rules, billing mappings | **Declarative:** "Patient qualifies if age > 18 AND diagnosis = COPD" |
| **Validators (Python)** | `EligibilityValidator`, `ChartingValidator`, `BillingValidator` — stateless, read EMR/charting, return pass/fail | **Execution:** "Check if patient qualifies" |
| **Kernel Enforcement** | Isagawa hooks + protocol — gates prevent billing without complete charting | **Safety:** "Can't submit billing until charting complete" |

---

## End Product: AI-Native CLI Architecture

```
rt-automation/
├── .claude/                           # Isagawa kernel config
│   ├── commands/rt/
│   │   ├── filter-patients.md         ← /rt/filter-patients
│   │   ├── chart-patient.md           ← /rt/chart-patient [PATIENT_ID]
│   │   └── submit-billing.md          ← /rt/submit-billing
│   └── skills/rt-workflow/
│       ├── SKILL.md                   ← Entry point
│       └── references/
│           ├── eligibility-rules.json ← 15+ patient filters
│           ├── charting-template.md   ← Required fields
│           ├── billing-codes.json     ← (Charting) → (CPT codes)
│           ├── compliance-rules.md    ← Reimbursement gates
│           └── emr-integration.md     ← Playwright paths
│
├── framework/_reference/
│   ├── validators.py                  ← EligibilityValidator, ChartingValidator, BillingValidator
│   ├── playwright_tasks.py            ← EMR automation (Playwright MCP)
│   └── tests/                         ← Unit + integration tests
│
├── fixtures/
│   ├── snf_configs.json              ← SNF-specific configs (EMR type, rules)
│   └── patient_test_data.json        ← Test cases
│
└── hooks/
    ├── rt-billing-gate.py            ← Block if charting incomplete
    └── rt-audit-log.py               ← Compliance audit trail
```

---

## Workflow: Three Commands

### 1. `/rt/filter-patients`

**What it does:** Import SNF census, identify qualifying patients

```
Input:  SNF census (CSV or EMR export)
Output:
  - Qualified patients (list)
  - Ineligible with reasons
  - Edge cases (manual review needed)

Process:
  1. Read patient census (Playwright automation if EMR, CSV if uploaded)
  2. For each patient: EligibilityValidator checks against eligibility-rules.json
  3. Output results + audit trail
  4. [Gate: Can't proceed to charting without qualifying list]
```

**Rules to encode** (from your cousin):
- Age minimum?
- Diagnosis requirements (COPD, asthma, post-op respiratory)?
- Insurance coverage (Medicare? Medicaid? Private)?
- Exclusions (already receiving RT, palliative care)?
- Geographic (which units in SNF)?

---

### 2. `/rt/chart-patient [PATIENT_ID]`

**What it does:** Auto-fill RT charting template, collect data, submit to EMR

```
Input:  Patient ID
Output: Charting submitted to EMR, logged for billing

Process:
  1. Verify patient in filtered list (gate prevents unqualified charting)
  2. Pull patient data from EMR (Playwright)
     - Demographics, vitals (SpO2, HR, RR, BP), prior visits
  3. Auto-fill charting template (from charting-template.md)
     - Some fields auto-populated (vitals, patient info)
     - Some fields RT must enter manually (assessment, intervention codes)
  4. ChartingValidator checks completeness
  5. RT reviews + approves (or edits)
  6. Submit to EMR (Playwright automation)
  7. [Gate: Charting complete, billing now enabled]
```

**Fields to encode** (from your cousin):
- Assessment type (initial, follow-up, discharge)?
- Intervention codes (nebulizer, oxygen, trach care)?
- Required documentation (vital trends, clinical note)?
- Frequency requirements (daily? PRN)?
- Discharge criteria?

---

### 3. `/rt/submit-billing`

**What it does:** Generate + submit CMS billing from charting, with full audit trail

```
Input:  Date range (e.g., "last 7 days")
Output: Billing submission file + audit log (why code X was chosen)

Process:
  1. Get all charted patients in date range
  2. For each charting record:
     - BillingValidator checks completeness (gate prevents incomplete billing)
     - Map charting fields → CPT/HCPCS codes (from billing-codes.json)
     - Audit: "CPT 93000 (ECG) chosen because charting includes [respiratory assessment + ECG ordered]"
  3. Calculate billable units
  4. Generate billing submission (CMS format)
  5. Log for compliance review (defendable against audits)
  6. Submit to billing system (Playwright automation)
```

**Mappings to encode** (from your cousin):
- CPT codes → charting requirements (what must be documented to justify each code)?
- Billing frequency (can patient bill daily? Weekly? Monthly)?
- Prior authorization rules (which codes need pre-approval)?
- Documentation triggers (what assessment finding triggers which code)?
- Modifiers (which codes need modifiers, which modifiers)?

---

## Why This Beats Competitors

| Competitor Problem | Your Solution |
|---|---|
| Rules scattered in code | Rules live in **references** (JSON + Markdown) — auditable, updatable |
| Can't explain why patient rejected | **Validator logic is transparent** — "Patient age 15, rule says >=18, rejected" |
| Regulations change → rewrite code | Update **eligibility-rules.json** → redeploy → done |
| No audit trail for CMS review | **Kernel logs every action** — "Patient billed CPT 93000 on 2026-05-20 because charting included [assessment + ECG]" |
| Can't adapt to new SNF | Deploy **rt-automation** + customize **snf_configs.json** → works immediately |
| Billing fails silently | **Hooks block submission** if charting incomplete — can't make the mistake |
| Manual work still dominates | **Playwright automation** handles EMR navigation, charting entry, billing submission |

---

## Execution Plan: Use Domain Spec Factory

### Phase 1: Design & Rules Capture (2-3 weeks)
1. Your cousin documents compliance rules in detail (we help format into JSON/markdown)
   - Eligibility rules (15-20 criteria)
   - Charting requirements (20-30 fields, logic for auto-population)
   - Billing code mappings (50+ CPT codes, prerequisites, modifiers)
   - Compliance gates (reimbursement rules that block billing)

2. Identify EMR system(s) used by target SNFs
   - What system? (Epic, Cerner, something custom?)
   - Playwright automation paths? (CSS selectors, wait logic)
   - Data exports? (CSV, API, manual download?)

### Phase 2: Domain Spec Build (4-6 weeks)
1. Run `/kernel/task-builder` or `/kernel/execute-pipeline` on RT backlog
   - Factory auto-generates: validators, Playwright tasks, test fixtures, config structure
   - Produces 70%+ of the code automatically
   - You + cousin review + customize remaining 30% (domain tweaks)

2. Deliverables:
   - EligibilityValidator, ChartingValidator, BillingValidator
   - Playwright automation for EMR navigation
   - Unit + integration tests
   - Reference fixtures (test patients, sample charting)

### Phase 3: SNF Testing & Iteration (4-8 weeks)
1. Partner with 1-2 SNFs to test live
   - Run `/rt/filter-patients` on real census
   - Chart real patients with Playwright automation
   - Submit real billing, verify CMS acceptance

2. Capture feedback:
   - "This eligibility rule is wrong"
   - "Charting automation doesn't work with our EMR version"
   - "Billing code isn't accepted by CMS"

3. Update rules + validators
   - Isagawa self-improves: each failure → cousin explains → protocol updates → system learns

### Phase 4: Productionize & Deploy (2-4 weeks)
1. Package rt-automation for distribution
2. Document SNF deployment steps
3. Ready to sell to next SNF (just customize snf_configs.json)

---

## Timeline & Compensation Structure

**Total timeline to MVP:** 4-6 months (phases 1-3)

**Compensation recommendation:**
- **Equity:** 15-25% (you're building defensible technology)
- **Monthly stipend:** $3-5K for 6 months (runway to first SNF revenue)
- **Post-revenue:** Move to salary or equity vesting schedule

**Why:** You're not just coding. You're encoding your cousin's domain expertise into an automated system. Without the expertise, the product fails (like competitors). Without you, it stays manual. Both essential.

---

## Key Decisions to Confirm with Your Cousin

Before starting Phase 1, get answers:

| Question | Why It Matters | Example Answer |
|----------|---|---|
| Which EMR system(s)? | Determines Playwright automation paths | Epic, Cerner, VersaSoft |
| How many SNFs? | Scope of initial testing | 1-2, or 5? |
| What's the top pain point? | Prioritize automation (charting vs. billing?) | "Charting copy-paste kills us" |
| Regulations change how often? | Update cadence for rules | Quarterly? Annually? |
| Do SNFs have IT support? | Can they deploy and run CLI tools? | Yes / Limited / Need MSP help |
| What's the monthly margin per SNF? | Revenue potential | $5K? $20K? $100K+? |

---

## Requirements Capture: What We Need from Your Cousin

**Status:** Awaiting cousin feedback
**Format:** Fill in checklists below. Rough answers okay — we'll refine during build.
**When ready:** Create `02-requirements-from-cousin.md` with detailed answers.

### COMMAND 1: `/rt/filter-patients`

**Input & Data Source:**
- [ ] What's the source of patient census? (CSV export? EMR API? Manual upload?)
- [ ] What columns/fields are in the census? (Name, DOB, Diagnosis, Insurance, Admit date, etc.)
- [ ] Who accesses this data? (RTs pull themselves? Admin provides?)
- [ ] How often changes? (Daily? Weekly?)

**Eligibility Rules** (exact logic):
- [ ] **Age:** Min? Max? Exceptions?
- [ ] **Diagnosis:** Which diagnoses qualify? (List all: COPD, asthma, post-op, pneumonia, etc.)
- [ ] **Insurance:** Which cover RT? (Medicare? Medicaid? Private? Exclude any?)
- [ ] **Exclusions:** Who's NOT eligible? (Already receiving RT? Palliative? DNR? Trach placed?)
- [ ] **Location:** Which units in SNF? (Med-surg? Exclude ICU?)
- [ ] **Prior visits:** Can same patient bill twice in stay? Time limit between billable visits?
- [ ] **Other gates?** (Weight? Comorbidities? Pregnancy? Pending surgery?)

**Output Requirements:**
- [ ] Output format? (CSV list? JSON? Display?)
- [ ] What fields in output? (Patient ID, Name, Reason, Billing eligibility?)
- [ ] Flag edge cases for manual review? What counts as edge case?

---

### COMMAND 2: `/rt/chart-patient [PATIENT_ID]`

**EMR System & Access:**
- [ ] **Which EMR system(s)?** (Epic? Cerner? VersaSoft? Custom?)
- [ ] How to access? (Web interface? VPN? Network?)
- [ ] Automate login? (Username/password? SSO? API token?)

**Data Sources** (what to auto-pull):
- [ ] Patient demographics: Where in EMR? (CSS selectors? API endpoint?)
- [ ] Vitals (SpO2, HR, RR, BP): Where? How often updated? (Real-time? Last 24hrs?)
- [ ] Prior charting: Where? To check "already charted today"?
- [ ] Medication list: Needed?
- [ ] Labs: Needed?
- [ ] Other data?

**Charting Template** (fields to auto-fill vs. manual):
- [ ] **Auto-populated** (system fills):
  - Patient name, DOB, Admit date, Room?
  - Vitals (auto-pulled)?
  - Medication list?
  - Others?

- [ ] **RT must enter manually** (with validation):
  - Assessment type? (Initial, follow-up, discharge — options?)
  - Respiratory status assessment? (Free text? Dropdown? Required fields?)
  - Intervention codes? (Nebulizer, O2, chest PT, etc. — full list?)
  - Clinical note? (Required? Length? Templates?)
  - Outcome? (Improved, stable, declined — options?)
  - Others?

- [ ] **Required fields** (can't submit without):
  - Which are mandatory?
  - Validation rules? (Length? Format? Allowed values?)

**Where Does It Submit?**
- [ ] Which form in EMR? (Page? API?)
- [ ] Playwright paths: (CSS selectors, input names, button locations)
- [ ] Success confirmation? (Message? Page?)

**Frequency & Gates:**
- [ ] Chart same patient twice/day? Once per billing period?
- [ ] Prevent duplicates how?
- [ ] Time-based restrictions? (Can't chart after X hours?)

---

### COMMAND 3: `/rt/submit-billing`

**Charting to Billing Mapping** (critical rules):
- [ ] **For EACH billable CPT code, provide:**
  - CPT code (e.g., 94060)
  - Code description
  - **Prerequisites:** What MUST be in charting? (e.g., "Initial assessment documented + clinical note")
  - Billing frequency: Once per stay? Daily? Weekly?
  - Modifiers: Required?
  - Units: How many per charting entry?

**Example format:**
```
CPT 94060 (Initial Respiratory Evaluation)
  Prerequisites: Assessment type = "Initial" AND clinical note > 100 chars AND (Dx = COPD OR asthma OR post-op)
  Frequency: Once per stay
  Units: 1
  Modifiers: -25 if same day as other eval

CPT 93000 (EKG)
  Prerequisites: SpO2 < 90 OR HR > 110 AND charting mentions "EKG ordered"
  Frequency: Daily
  Units: 1
  Modifiers: None
```

- [ ] Any billing rules that BLOCK submission? (e.g., "Can't bill if 5+ charges this month")

**Billing Format & Submission:**
- [ ] Format needed? (HCFA 1500? UB-04? Vendor-specific XML/JSON?)
- [ ] Submit where? (CMS portal? Insurance? 3rd-party billing software?)
- [ ] How submit? (Web form? API? SFTP? Email?)
- [ ] Playwright paths or API details?

**Audit & Compliance:**
- [ ] What must be logged? (Who, what, when, why?)
- [ ] Compliance rules? (Retain audit trail how long?)
- [ ] What triggers manual review before submission? (Any code billed first time?)

**Edge Cases & Failures:**
- [ ] Incomplete charting: Block billing? Flag? Manual?
- [ ] Insurance denies code: Log it? Retry? Intervention?
- [ ] CMS rejects submission: How fix? Resubmit?

---

### Cross-Cutting

**System Architecture:**
- [ ] Multiple SNF locations with different rules? (Same everywhere, or custom per SNF?)
- [ ] SNF IT support? (Can deploy code? Run CLI? Or remote managed?)
- [ ] How often regulations change? (Quarterly? Annually?)
- [ ] Legal frameworks? (HIPAA? CMS rules? State-specific?)

**Data Sensitivity:**
- [ ] Log patient data? (Names, IDs, diagnoses?)
- [ ] Data storage location? (Local? Cloud? Secure?)
- [ ] PII restrictions? (What can log for audit?)

---

## Next Steps

1. **This week:** Share design baseline with cousin, get initial feedback
2. **Week 2:** Cousin fills requirements checklist above (rough answers okay)
3. **Week 3:** Create `02-requirements-from-cousin.md` with detailed answers
4. **Week 4:** Kick off `/kernel/execute-pipeline` with RT automation backlog
5. **Week 8:** First SNF pilot testing

---

**This is your baseline + requirements capture. Ready to share with cousin?**
