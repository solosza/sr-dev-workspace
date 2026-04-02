# 30-Day Readmissions

## Source Document

Claims - Payment Integrity Readmissions System Design v0.10

## Problem Statement

**Problem:** Insufficient care coordination by hospitals prior to discharge leads to readmission for the same condition, drives up medical care costs and negatively impacts patient outcomes.

**Objective:** Enhanced patient outcomes from greater care coordination, reduced preventable readmissions, and increased affordability.

**Financial Impact:** $7.7M in annual cost savings and improved member experience, driven by better hospital incentives that lead to better patient outcomes. Additionally, Cotiviti takes a 22% cut ($1.4M annually) for claim edits — an in-house solution captures the full savings.

**Mandate:** Not a mandate. EAO initiative; priority.

### Proposed Solution

1. For readmissions within 30 days with the **same diagnosis (same Dx)**, identify through **Cotiviti payment edits** and auto-deny
2. For readmissions within 30 days with the **same condition (same DRG and Dx)**, identify through **in-house edits** and auto-deny
   - 80% realization rate for same DRG/MDC readmissions
   - Considers readmissions only to **same facility**
   - Excludes: Cancer, trauma, pregnancy, delivery, neonatal, BH IP claims; IP with discharge status 7, 20, 30 as well
3. For readmissions with **similar conditions (same MDC)**, identify through **MD review** and recoup payment

## Tech Stack

| System | Purpose |
|--------|---------|
| QNXT (MCR, PB, QST) | Claims adjudication platform |
| Tidal | Job scheduler / batch orchestration |
| SSIS | ETL for loading DRG/MDC mappings |
| Stored Procedures / Custom Tables | Core pend/deny logic |
| MuleSoft | API integration layer |
| Aerial / Medecision (SaaS) | Medical Management / UM clinical review platform |
| Cotiviti | Payment integrity vendor |
| DRG Active (Micro-Dyn) | DRG grouper for MCR and PB |
| 3M | DRG grouper for QST |
| SAS | Daily process for claim selection (existing ETL option) |
| MapForce | XML conversion for Aerial integration (existing ETL option) |

### QNXT (Cognizant/TriZetto)
- **Web-based** — .NET/IIS/SQL Server, browser-delivered (historically IE-dependent, newer versions support Edge)
- **APIs:** SOAP/XML web services (QNXT Gateway), EDI processing (837/835/270/271/834), direct database integration via stored procedures
- **Key UI modules:**
  - Claims Workbench — primary examiner screen (header, lines, dx/proc codes, pricing, status, pend/deny/pay)
  - Claims Inquiry/Search — by member, provider, claim number, date range, status
  - Pend Management/Work Queues — configurable routing of pended claims to examiners
  - Authorization/Referral Linkage
  - Adjustment/Void
  - Correspondence/Letters (EOBs)
- **Common testing approaches:** Manual UI testing, Selenium (noted as challenging due to dynamic HTML), SQL-based validation against the database, EDI test harnesses (submit 837, validate 835)

### Aerial (Medecision)
- **Web-based SaaS** — browser + VPN, no desktop install, HITRUST CSF certified
- **APIs:** FHIR/SMART on FHIR for EMR integration, standard web services API, open architecture
- **Key features:** AI-driven policy management, automated approvals, intelligent routing, utilization tracking, clinical risk prediction, care management workflows
- **Data integration:** Ingests medical/pharmacy claims, ADT feeds, EMR data, SDOH data via data lakehouse architecture
- **Caveat:** KLAS reviews note longer-term customers have had challenges with claims system integration — some workflows still involve manual work

### Cotiviti
- **Cloud-based SaaS** — web portals (MyCotiviti, CotivitiConnect, Payment Clarity)
- **APIs:** Likely exist but not publicly documented — requires client portal access
- **Payment integrity features:**
  - Payment Policy Management — automated prepay claim editing (99.9% accuracy stated)
  - Clinical Chart Validation (CCV) — DRG, short stay, readmission, SNF, IRF review with ML
  - COB recovery, FWA pattern review
- **Readmission handling:** Readmission is a specific claim type in CCV (pre-pay and post-pay), but specific 30-day rules, DRG pairing logic, and exceptions are proprietary

## System Design — Full Flow (10 Items)

### Item 1 — Denial Message Configuration
- **Method:** Manual
- Config architect configures denial messages used for reporting on RTM, RTP, and 835
- BA maps denial reason codes to HIPAA messages (835) and to appropriate RTM/RTP messages

### Item 2 — MS DRG & APR DRG to MDC Data Mapping
- **Method:** Manual → Tidal → SSIS → Custom Table
- BA saves DRG-to-MDC mapping files into a folder
- Tidal monitors the folder, triggers SSIS ETL to load into custom table, tracks deletes/updates
- Used by the auto pend and deny processes
- Annual update (APR DRG, MDC, MS DRG, Medicare Severity DRG)

### Item 3 — MS DRG & APR DRG Exclusion
- **Method:** Manual → Tidal → SSIS → Custom Table
- Same flow as Item 2 but for exclusion files
- Tracking assists in troubleshooting claim processing issues
- Annual update

### Item 4 — Claims Processing: Pend (depends on 2, 3)
- **Method:** Batch → Tidal → Stored Procedure → Custom Table
- Custom process pends inpatient and acute readmission claims with the **same MDC** for services within 30 days
- Held from claim processing, sent to Medical Management for clinical review
- DRG grouping: Micro-Dyn / DRG Active for MCR and PB, 3M product for QST
- Implement Post Mass for all LOBs

### Item 5 — Claims Processing: Deny (depends on 1, 3)
- **Method:** Batch → Tidal → Stored Procedure → Custom Table
- If the inpatient/acute readmission claim is **excluded from clinical review**, custom process auto-denies claims with the **same DRG** for services within 30 days
- Same DRG grouper setup (Micro-Dyn for MCR/PB, 3M for QST)
- Implement Post Mass for all LOBs

### Item 6 — QNXT to Aerial Data Integration (two options)
- **Method:** API → MuleSoft, Stored Procedure, Tidal
- Collect pended claims from QNXT MCR, PB, and QST databases
- Load into Aerial as a case/request for Medical Management to review
- Dependency: Claims must be adjudicated from QNXT during nightly batch

**Option 1 — Existing ETL:**
- Daily SAS process selects claims with a C code (c, c1, c2, c3...up to c40) memo
- MapForce converts to XML, SFTPed to Aerial
- Loaded as skeleton case/request via Request Program Import Utility
- Pros: Minimal dev effort, reuse existing processes, new C code coordinated between DAS/Aerial/Medical Management
- Cons: Multiple technologies = multiple points of failure, increased coordination between teams

**Option 2 — MuleSoft:**
- API integration for seamless data flow between QNXT and Aerial
- Pros: More robust, fewer components, fewer points of failure
- Cons: New components = added development and testing effort

### Item 7 — Medical Management Clinical Review (depends on 6)
- **Method:** Manual → UM System (Medecision, cloud-based SaaS)
- C code determines who to route review requests to
- Medical Management indicates whether to pay or deny the case
- Clinical reviewer can specifically assign Pay or Deny disposition for the entire claim/lines

### Item 8 — Aerial to QNXT Data Integration (two options)
- **Method:** API → MuleSoft
- Load case/claims response and disposition from Aerial into QNXT as a claim memo for Claims Examiner to review
- Data from Aerial must be in a structured format consumable by QNXT
- **Claim order must match** the same order as originally sourced from QNXT

**Option 1 — Existing ETL:**
- Reuse existing data integration, minimal dev effort
- Cons: Multiple technologies, multiple points of failure

**Option 2 — MuleSoft:**
- API integration between Aerial and QNXT
- Pros: More robust, fewer failure points
- Cons: More dev and testing effort

### Item 9 — QNXT Claims Processing: Deny or Pay (depends on 1)
- **Method:** Manual → Stored Procedure, Custom Table
- Medical Management response report contains disposition from the UM system
- Claims examiner uses it to determine whether to pay or deny the claim
- Note: Disposition on the MM response report is not in a proper format that can be programmatically implemented

### Item 10 — QNXT Claims Processing: Cotiviti
- **Method:** Batch → Tidal, Stored Procedure, SFTP
- Ensure the new process is placed in the appropriate job stream and scheduled accordingly
- Claims released to Pay will continue to be sent to Cotiviti
- Claims pended for review and denied will **not** be sent to Cotiviti
- Note: After implementation, Cotiviti to turn off their 30-day readmission process

## End-to-End Flow

```
DRG/MDC Mappings (2,3) loaded via SSIS
            |
Nightly Batch Claims Processing
    |-- Pend (4): same MDC within 30 days --> hold for clinical review
    |-- Deny (5): excluded from review + same DRG within 30 days --> auto-deny
            |
Pended claims --> QNXT to Aerial (6) --> Medical Management Review in Medecision (7)
            |
Aerial disposition --> back to QNXT (8) --> Claims Examiner Pay/Deny (9)
            |
Released claims --> Cotiviti (10), but not pended/denied ones
```

## Demand Tracking

- Demand: DMN D0002863
- Multiple Epics and Features across items (see attachment_1.jpeg for full mapping)

## Key Questions (TBD)

- PHI/CUI constraints — can an LLM touch test data? What's the data classification?
- What test environments are available?
- How is testing done today?
- What test data exists? Synthetic data pipelines?
- Which integration option was selected for Items 6 and 8? (Existing ETL vs MuleSoft)

## Test Strategy (TBD)

Pending answers to the questions above.
