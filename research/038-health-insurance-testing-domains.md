# Health Insurance Testing Domains — Comprehensive Research

> **Purpose:** Map all testing domains within a health insurance company (modeled on HMSA / Blue Cross Blue Shield affiliates) to identify candidates for AI agent domain spec automation.
>
> **Date:** 2026-03-06
> **Status:** Complete

---

## 1. Executive Summary

Health insurance payers operate some of the most complex, regulation-heavy software ecosystems in any industry. A company like HMSA (Hawaii Medical Service Association — the largest insurer in Hawaii, a BCBS licensee) runs dozens of interconnected systems that must comply with HIPAA, ACA, CMS rules, state mandates, and accreditation standards (NCQA, URAC) simultaneously.

This document maps **12 primary testing domains**, scores each on five dimensions, and recommends a priority order for building AI agent domain specs. The domains span the full lifecycle — from member enrollment through claims adjudication, payment, compliance reporting, and member communications.

**Key findings:**

- **EDI Testing** and **Claims Testing** are the highest-value automation targets due to extreme repetitiveness, well-documented standards, and high pain intensity.
- **Benefits/Plan Configuration** and **Compliance/Regulatory** testing are the most complex but also the most error-prone when done manually.
- **CMS-0057-F** (effective January 2026) creates urgent new testing requirements around FHIR APIs and prior authorization — making **Integration/API Testing** a timely priority.
- Core administration platforms (Facets, QNXT, HealthEdge, Javelina) dominate the market — specs built against these systems have broad applicability.

---

## 2. Domain Map — Scoring Overview

Scoring key (1-5 scale):
- **RC** = Regulatory Complexity (how many regulations drive testing)
- **RP** = Repetitiveness (how routine/templated the test cycles are)
- **DA** = Documentation Availability (public standards, specs, guides)
- **AP** = Automation Potential (feasibility of AI agent automation)
- **PI** = Pain Intensity (how painful manual testing is today)
- **Total** = Sum of all scores (max 25)

| # | Domain | RC | RP | DA | AP | PI | Total | Priority |
|---|--------|----|----|----|----|----|----|----------|
| 1 | EDI Testing | 5 | 5 | 5 | 5 | 5 | 25 | 1 |
| 2 | Claims Testing | 5 | 5 | 4 | 5 | 5 | 24 | 2 |
| 3 | Benefits/Plan Configuration | 4 | 5 | 3 | 5 | 5 | 22 | 3 |
| 4 | Membership/Enrollment | 4 | 4 | 4 | 4 | 4 | 20 | 4 |
| 5 | Compliance/Regulatory | 5 | 4 | 4 | 3 | 5 | 21 | 5 |
| 6 | Authorization/UM | 5 | 4 | 3 | 4 | 5 | 21 | 6 |
| 7 | Integration/API | 4 | 4 | 4 | 4 | 4 | 20 | 7 |
| 8 | Billing/Premium | 3 | 4 | 3 | 4 | 4 | 18 | 8 |
| 9 | Provider Testing | 3 | 4 | 4 | 4 | 3 | 18 | 9 |
| 10 | Data/Analytics | 4 | 4 | 3 | 3 | 4 | 18 | 10 |
| 11 | Portal/Digital | 2 | 3 | 3 | 4 | 3 | 15 | 11 |
| 12 | Correspondence/Communication | 3 | 4 | 3 | 3 | 3 | 16 | 12 |

---

## 3. Detailed Domain Analysis

---

### 3.1 EDI Testing

**What it is:** Validation of electronic data interchange transactions between health plans, providers, clearinghouses, and trading partners using ASC X12 standards mandated by HIPAA.

**Key transactions tested:**

| Transaction | Code | Direction | Purpose |
|-------------|------|-----------|---------|
| Health Care Claim | 837P/I/D | Provider → Payer | Professional, Institutional, Dental claims |
| Claim Payment/Remittance | 835 | Payer → Provider | Payment advice and ERA |
| Eligibility Inquiry/Response | 270/271 | Bidirectional | Real-time eligibility checks |
| Claim Status Inquiry/Response | 276/277 | Bidirectional | Where is my claim? |
| Benefit Enrollment | 834 | Sponsor → Payer | Enrollment, changes, terminations |
| Premium Payment | 820 | Sponsor → Payer | Premium remittance with EFT |
| Prior Authorization | 278 | Provider → Payer | Auth requests and responses |
| Acknowledgments | 999/TA1 | Receiver → Sender | Syntax and content validation |

**Specific test scenarios:**
- Segment-level validation (ISA, GS, ST, SE, GE, IEA envelope structure)
- Loop and element-level compliance (2000A/B/C/D hierarchical loops in 837)
- Code set validation (ICD-10, CPT, HCPCS, NDC, taxonomy codes)
- Trading partner-specific companion guide compliance
- Clearinghouse routing and transformation accuracy
- Acknowledgment generation (999 functional ack, TA1 interchange ack)
- Batch vs. real-time transaction processing
- Version compliance (5010A1 for all transactions)
- Cross-transaction consistency (837 claim → 835 payment → 277 status)
- Reject/denial reason code accuracy

**Systems/tools commonly involved:**
- Core admin platforms: TriZetto Facets, QNXT, HealthEdge
- EDI gateways: Edifecs, Emdeon/Change Healthcare, Availity
- Clearinghouses: Change Healthcare, Availity, Trizetto
- Testing tools: Edifecs EDI testing suite, custom X12 parsers
- Validation engines: SNIP levels 1-7 testing

**Regulatory requirements:**
- HIPAA Administrative Simplification (45 CFR Parts 160, 162)
- ASC X12 Version 5010 (adopted standard)
- CMS Companion Guides
- State-specific companion guides
- Trading partner agreements

**Data formats and standards:**
- ASC X12 5010A1 (all healthcare transactions)
- NCPDP (pharmacy — retail)
- Flat file delimited formats (legacy systems)

**Pain points / automation opportunity:**
- Volume: large payers process millions of transactions daily — manual validation is impossible
- Companion guide variations: each trading partner may have unique requirements
- Regression testing after system upgrades requires re-validating all transaction types
- Parsing X12 segment/element structures is tedious but highly deterministic
- Test data generation for edge cases (e.g., COB claims, split claims) is time-consuming

**Scores:** RC=5 | RP=5 | DA=5 | AP=5 | PI=5 | **Total=25**

---

### 3.2 Claims Testing

**What it is:** End-to-end testing of the claims lifecycle from submission through adjudication, payment, and reporting. The core business function of any health insurer.

**Specific test scenarios:**
- **Auto-adjudication rules:** Verify claims that meet criteria are automatically processed without human intervention (target: 85-95% auto-adjudication rate)
- **Manual review routing:** Claims flagged for medical review, coding review, or special handling
- **Pricing/reimbursement calculations:** Fee schedule lookups, allowed amounts, contracted rates, Medicare/Medicaid fee schedules
- **Claim edits and audits:** CCI edits (Correct Coding Initiative), MUE limits, frequency limitations
- **Duplicate claim detection:** Exact and near-duplicate identification
- **Coordination of Benefits (COB):** Primary/secondary/tertiary payer determination and payment calculation
- **Claim adjustments and voids:** Reprocessing, recoupments, provider disputes
- **Timely filing:** Enforcement of filing deadlines (typically 90-365 days)
- **EOB/ERA generation:** Explanation of Benefits accuracy, remittance advice codes
- **Claim status tracking:** Real-time status updates through lifecycle
- **Subrogation and third-party liability:** Identification and recovery
- **Provider reimbursement methods:** DRG, APC, RBRVS, per diem, case rate, capitation
- **Out-of-network claim processing:** Balance billing protections, No Surprises Act compliance

**Systems/tools commonly involved:**
- Core claims engines: Facets, QNXT, HealthEdge HealthRules Payor, Javelina (Mphasis), PLEXIS
- Claims editing: Cotiviti, Change Healthcare ClaimsXten, Optum
- Pricing engines: MultiPlan, FAIR Health
- Workflow: Pega, Appian (for manual review routing)
- Analytics: SAS, Tableau, custom BI

**Regulatory requirements:**
- HIPAA transaction standards (837/835)
- ACA essential health benefits
- No Surprises Act (NSA) — balance billing protections
- State prompt payment laws
- CMS Medicare/Medicaid claims processing requirements
- DOL/ERISA requirements for self-funded plans

**Data formats and standards:**
- X12 837P/I/D (inbound claims)
- X12 835 (outbound payment/remittance)
- ICD-10-CM/PCS, CPT, HCPCS, Revenue Codes
- DRG grouper logic
- Place of Service codes, Type of Bill codes

**Pain points / automation opportunity:**
- Claims adjudication rules are extremely complex but deterministic — ideal for automated regression testing
- Each plan year brings benefit changes that require comprehensive re-testing
- Provider contract changes cascade into pricing test scenarios
- Test data must cover thousands of code/modifier/place-of-service combinations
- Manual QA of auto-adjudication accuracy is the single largest QA effort in most payer organizations

**Scores:** RC=5 | RP=5 | DA=4 | AP=5 | PI=5 | **Total=24**

---

### 3.3 Benefits/Plan Configuration Testing

**What it is:** Validation that benefit plans are correctly configured in the core admin system — copays, coinsurance, deductibles, out-of-pocket maximums, exclusions, limitations, and accumulators all behave as designed.

**Specific test scenarios:**
- **Benefit plan loading:** Verify SBC (Summary of Benefits and Coverage) matches system configuration
- **Cost-sharing calculations:**
  - Copay amounts by service type (PCP visit, specialist, ER, urgent care, Rx tiers)
  - Coinsurance percentages (in-network vs. out-of-network)
  - Deductible application (individual vs. family, embedded vs. aggregate)
  - Out-of-pocket maximum tracking and enforcement
- **Accumulator testing:**
  - Deductible accumulators track correctly across claims
  - OOP max accumulators include/exclude correct cost-sharing types
  - Family accumulator cross-member tracking
  - Copay accumulator programs (manufacturer coupon handling)
  - Plan year rollover / reset
  - Mid-year plan changes and accumulator transfers
- **Coordination of Benefits (COB):**
  - Birthday rule for dependent children
  - Primary/secondary determination
  - Medicare as primary vs. secondary
  - Maintenance of Benefits vs. Standard COB
  - Non-duplication of benefits
- **Plan hierarchy and tiering:**
  - Multi-tier pharmacy benefits (Tier 1-6)
  - In-network / out-of-network tier structures
  - Centers of Excellence / preferred facility tiers
- **Exclusions and limitations:**
  - Pre-existing condition rules (grandfathered plans)
  - Cosmetic procedure exclusions
  - Experimental/investigational exclusions
  - Annual/lifetime maximums (where permitted)
  - Visit limits (PT/OT/ST, mental health, chiropractic)
- **Preventive care / ACA mandates:**
  - $0 cost-sharing for preventive services
  - Correct coding for preventive vs. diagnostic

**Systems/tools commonly involved:**
- Benefit configuration modules in Facets, QNXT, HealthEdge
- Benefits testing tools: typically custom-built
- Actuarial modeling: Milliman, custom tools
- SBC generation engines

**Regulatory requirements:**
- ACA essential health benefits (10 categories)
- ACA preventive care mandates
- Mental Health Parity and Addiction Equity Act (MHPAEA)
- State-mandated benefits (vary by state — Hawaii has unique requirements)
- CMS Medicare Advantage bid/benefit requirements

**Data formats and standards:**
- SBC templates (standardized by CMS/DOL)
- Benefit grids and plan documents
- Internal configuration tables

**Pain points / automation opportunity:**
- Plan configuration errors are among the most costly mistakes — incorrect cost-sharing hits members directly
- Annual benefit changes (plan year) require mass re-testing
- Accumulator edge cases are notoriously difficult to test manually (mid-year changes, COB interactions)
- COB rules are complex and vary by state
- A single payer may have hundreds or thousands of unique plan configurations

**Scores:** RC=4 | RP=5 | DA=3 | AP=5 | PI=5 | **Total=22**

---

### 3.4 Membership/Enrollment Testing

**What it is:** Testing the member lifecycle — from initial enrollment through eligibility maintenance, plan changes, and termination. Ensures members have correct coverage at the correct time.

**Specific test scenarios:**
- **New enrollment processing:**
  - Individual enrollment (marketplace, direct)
  - Group enrollment (employer-sponsored)
  - Medicare Advantage enrollment
  - Medicaid managed care enrollment
  - CHIP enrollment
- **834 transaction processing:**
  - Initial enrollment (subscriber + dependents)
  - Changes (add/drop dependents, plan changes)
  - Reinstatements
  - Terminations
  - Retroactive enrollment/termination
  - Audit (reconciliation) transactions
- **Eligibility verification:**
  - Real-time 270/271 eligibility checks
  - Eligibility effective/term date accuracy
  - Coverage type and benefit package assignment
  - Dependent eligibility (age-off rules, student status)
  - COBRA eligibility and continuation
- **Open enrollment:**
  - Plan selection and comparison tools
  - Auto-renewal processing
  - Plan migration mapping
  - Rate change application
  - Enrollment deadline enforcement
- **Life event processing:**
  - Qualifying life events (marriage, birth, job loss, relocation)
  - Special enrollment period validation
  - Documentation requirements and verification
- **ID card generation:**
  - Member/subscriber/group number accuracy
  - PCP assignment
  - Plan identifier
  - Pharmacy BIN/PCN/Group
- **Reconciliation:**
  - Carrier-employer enrollment reconciliation
  - Exchange (marketplace) reconciliation
  - Premium binder payment verification

**Systems/tools commonly involved:**
- Core admin enrollment modules: Facets, QNXT, HealthEdge
- Marketplace connectivity: SERFF, FFM (Federally Facilitated Marketplace)
- Eligibility engines: real-time 270/271 gateways
- CRM: Salesforce Health Cloud, Pega
- ID card print vendors

**Regulatory requirements:**
- ACA enrollment periods and qualifying life events
- HIPAA enrollment/disenrollment standards (834)
- CMS Medicare Advantage enrollment requirements
- State continuation of coverage laws
- COBRA/mini-COBRA requirements
- Hawaii Prepaid Health Care Act (unique to Hawaii — employer mandate since 1974)

**Data formats and standards:**
- X12 834 (Benefit Enrollment and Maintenance)
- X12 820 (Premium Payment)
- CMS HIOS (Health Insurance Oversight System)
- SERFF filings

**Pain points / automation opportunity:**
- Open enrollment creates massive testing surges (seasonal)
- Retroactive enrollment changes cascade into claims reprocessing
- 834 file processing errors cause member complaints and regulatory issues
- Reconciliation between employers, exchanges, and the payer is tedious and error-prone
- Dependent eligibility rules (age-off, student certification) have many edge cases

**Scores:** RC=4 | RP=4 | DA=4 | AP=4 | PI=4 | **Total=20**

---

### 3.5 Compliance/Regulatory Testing

**What it is:** Ensuring the health plan meets all federal, state, and accreditation requirements. This is a cross-cutting concern that touches every other domain but has its own dedicated testing activities.

**Specific test scenarios:**
- **HIPAA compliance:**
  - Privacy rule (PHI handling, minimum necessary, authorization tracking)
  - Security rule (access controls, encryption, audit logging)
  - Breach notification procedures
  - Transaction and code set compliance
  - Unique identifier requirements (NPI, HPID)
- **ACA compliance:**
  - Essential health benefits coverage
  - Preventive care at $0 cost-sharing
  - Mental Health Parity (MHPAEA) — quantitative and non-quantitative treatment limitations
  - Section 1557 non-discrimination (language access, accessibility)
  - Medical Loss Ratio (MLR) reporting
  - Risk adjustment (EDGE server submissions)
  - Rate review and justification
- **CMS requirements (Medicare Advantage, Medicaid):**
  - Stars quality ratings data submission
  - HEDIS measure reporting
  - Part D formulary and benefit testing
  - Medicare secondary payer (MSP) compliance
  - Model of care requirements
  - Network adequacy standards
  - Marketing material review
  - Grievance and appeal processing timelines
- **State mandates:**
  - State-specific mandated benefits
  - State prompt payment requirements
  - State continuation of coverage laws
  - State data reporting (e.g., APCD — All-Payer Claims Database)
  - Hawaii-specific: Prepaid Health Care Act compliance
- **Accreditation (NCQA / URAC):**
  - NCQA Health Plan Accreditation standards (QI, PHM, UM, credentialing, member rights)
  - URAC Health Plan Accreditation
  - HEDIS data collection and reporting accuracy
  - CAHPS survey data handling
- **Audit readiness:**
  - CMS program audit preparation
  - State DOI examination readiness
  - OIG compliance program elements
  - SIU (Special Investigations Unit) fraud detection testing

**Systems/tools commonly involved:**
- GRC platforms: RSA Archer, ServiceNow GRC, LogicGate
- HEDIS engines: Inovalon, Cotiviti
- Compliance management: custom-built
- Audit trail: Splunk, ELK stack
- Risk adjustment: Episource, Cotiviti, Ciox

**Regulatory requirements:**
- HIPAA (45 CFR Parts 160, 162, 164)
- ACA (42 USC 18001 et seq.)
- CMS Medicare Advantage regulations (42 CFR Part 422)
- CMS Medicaid managed care (42 CFR Part 438)
- State insurance code
- No Surprises Act
- Transparency in Coverage rule

**Pain points / automation opportunity:**
- Regulatory changes are constant — CMS publishes annual rule updates, states pass new mandates
- Audit preparation is extremely labor-intensive (pulling evidence, documentation)
- MHPAEA compliance testing (NQTL analysis) is complex and subjective
- Cross-regulatory conflict resolution (federal vs. state) requires expert judgment
- Accreditation cycles (every 3 years for NCQA) create surge testing needs

**Scores:** RC=5 | RP=4 | DA=4 | AP=3 | PI=5 | **Total=21**

---

### 3.6 Authorization/Utilization Management Testing

**What it is:** Testing prior authorization, concurrent review, and retrospective review processes. Ensures clinical criteria are applied consistently and regulatory timelines are met.

**Specific test scenarios:**
- **Prior authorization:**
  - Service/procedure-specific auth requirements (does this service need auth?)
  - Auth request submission (278 transactions, portal, fax-to-digital)
  - Clinical criteria application (InterQual LOC, MCG guidelines)
  - Auto-approval rules for routine requests
  - Peer-to-peer review routing
  - Decision timeframes (CMS-0057-F: 72 hours urgent, 7 days standard)
  - Notification to providers and members
  - Auth number generation and tracking
  - Auth expiration and extension
  - Retroactive authorization
- **Concurrent review:**
  - Inpatient length-of-stay monitoring
  - Level of care transitions (ICU → step-down → acute → SNF)
  - Continued stay authorization
  - Discharge planning integration
- **Retrospective review:**
  - Post-service medical necessity determination
  - Claim-level retrospective denial
  - Provider dispute/appeal handling
- **Appeals and grievances:**
  - Member appeal processing (internal, external/IRO)
  - Provider dispute resolution
  - Expedited appeal handling
  - CMS-mandated timeframes (MA: 30 days standard, 72 hours expedited)
  - State-specific appeal requirements
- **Clinical criteria engine testing:**
  - InterQual criteria version updates
  - MCG guideline application
  - Custom clinical guidelines
  - Criteria override documentation
  - Consistent criteria application across reviewers

**Systems/tools commonly involved:**
- UM platforms: TruCare (Casenet), Jiva (ZeOmega), Guiding Care, HealthEdge
- Clinical criteria: InterQual (Optum), MCG (Hearst Health)
- Auth portals: Availity, Surescripts, custom
- Fax integration: RightFax, OpenText
- Workflow: Pega, custom BPM

**Regulatory requirements:**
- CMS-0057-F (Prior Authorization API — FHIR, effective 2026-2027)
- CMS Medicare Advantage UM requirements (42 CFR 422.137)
- NCQA UM accreditation standards
- State prior auth reform laws (many states have passed "gold card" or auto-approval laws)
- No Surprises Act (out-of-network emergency auth)
- ACA mental health parity for UM processes

**Data formats and standards:**
- X12 278 (Health Care Services Review)
- FHIR Prior Authorization API (CMS-0057-F)
- InterQual/MCG proprietary formats
- Clinical documentation (unstructured)

**Pain points / automation opportunity:**
- Prior auth is the #1 provider complaint in healthcare — automation reduces friction
- CMS-0057-F creates new FHIR API testing requirements (urgent timeline)
- Clinical criteria updates (InterQual/MCG publish quarterly) require regression testing
- Decision timeframe compliance tracking is critical and auditable
- Inconsistent criteria application is a major audit finding

**Scores:** RC=5 | RP=4 | DA=3 | AP=4 | PI=5 | **Total=21**

---

### 3.7 Integration/API Testing

**What it is:** Testing the interconnections between the core admin system and all upstream/downstream systems — including FHIR APIs mandated by CMS, pharmacy (PBM), dental, vision, and third-party vendors.

**Specific test scenarios:**
- **FHIR API testing (CMS-mandated):**
  - Patient Access API (member-facing — claims, encounters, clinical data)
  - Provider Access API (provider-facing — member attribution, clinical data)
  - Payer-to-Payer API (payer-to-payer data exchange)
  - Prior Authorization API (278 replacement via FHIR)
  - Drug Formulary API (Part D / Marketplace)
  - SMART on FHIR authorization and authentication
  - Bulk data export
- **Pharmacy/PBM integration:**
  - NCPDP SCRIPT (e-prescribing)
  - Real-time pharmacy benefit check
  - Formulary data exchange
  - Claims crossover (medical ↔ pharmacy)
  - Specialty pharmacy coordination
- **Dental/Vision integration:**
  - Carved-out benefit coordination
  - Claims crossover for combined deductibles
  - Eligibility file exchange
- **Provider data integration:**
  - CAQH ProView data import
  - NPI registry validation
  - Provider directory feeds
  - Network adequacy reporting
- **Third-party vendor APIs:**
  - Lab results (HL7 v2, FHIR)
  - HIE (Health Information Exchange) connectivity
  - Care management platform integration
  - Disease management vendor feeds
  - Telemedicine platform integration (Teladoc, Amwell)
- **Real-time eligibility:**
  - 270/271 gateway performance under load
  - Response time SLA compliance
  - Multi-system eligibility aggregation
- **Data exchange with government:**
  - CMS EDGE server (risk adjustment)
  - State APCD submissions
  - Medicare Part D PDE (Prescription Drug Event) submissions
  - HIOS/SERFF marketplace submissions

**Systems/tools commonly involved:**
- Integration engines: MuleSoft, Rhapsody, InterSystems HealthShare
- API gateways: Apigee, Kong, AWS API Gateway
- FHIR servers: HAPI FHIR, Smile CDR, Firely
- Testing tools: Postman, SoapUI, ReadyAPI, custom test harnesses
- Message brokers: Kafka, RabbitMQ, IBM MQ

**Regulatory requirements:**
- CMS-0057-F (Interoperability and Prior Authorization Final Rule)
- CMS Patient Access API rule (effective since 2021, expanded 2026-2027)
- HIPAA transaction standards for EDI
- 21st Century Cures Act (information blocking)
- ONC certification requirements

**Data formats and standards:**
- HL7 FHIR R4 (CMS-mandated APIs)
- HL7 v2 (ADT, ORU — legacy)
- X12 (all HIPAA transactions)
- NCPDP (pharmacy)
- C-CDA (clinical documents)
- JSON/REST (modern APIs)
- SOAP/XML (legacy web services)

**Pain points / automation opportunity:**
- CMS-0057-F creates a hard compliance deadline (Jan 2027 for APIs) — testing backlog is severe
- Integration points multiply with every new vendor, creating combinatorial test scenarios
- FHIR is relatively new to payers — testing expertise is scarce
- Real-time APIs require performance/load testing in addition to functional testing
- Regression risk is high when any connected system changes

**Scores:** RC=4 | RP=4 | DA=4 | AP=4 | PI=4 | **Total=20**

---

### 3.8 Billing/Premium Testing

**What it is:** Testing premium billing, payment collection, grace periods, subsidies, and financial reconciliation for all lines of business.

**Specific test scenarios:**
- **Premium billing:**
  - Individual premium billing (monthly, quarterly, annual)
  - Group billing (list bill, self-accounting, composite rates)
  - Medicare Advantage premium billing (CMS withheld vs. direct billed)
  - Medicaid managed care capitation
- **Rate calculations:**
  - Age-rated premiums (ACA 3:1 age curve)
  - Area factors (rating regions)
  - Tobacco surcharge
  - Family tier pricing (individual, couple, parent+child, family)
  - COBRA rate calculation (102% of full premium)
  - Subsidized premiums (APTC — Advance Premium Tax Credit)
- **Payment processing:**
  - ACH/EFT processing
  - Credit card payments
  - Lock-box processing
  - Payment application to correct account/period
  - Overpayment/underpayment handling
  - EDI 820 premium payment processing
- **Grace periods:**
  - ACA marketplace: 90-day grace period for subsidized members (first 30 days payer pays claims, next 60 days claims pend)
  - COBRA: 30-day grace period for ongoing premiums, 45-day initial payment
  - Group: varies by contract
- **Financial reconciliation:**
  - Premium-to-enrollment reconciliation
  - Commission/broker fee calculations
  - Reinsurance/risk corridor settlements
  - State premium tax calculations
  - MLR (Medical Loss Ratio) rebate calculations

**Systems/tools commonly involved:**
- Billing modules in Facets, QNXT, HealthEdge
- Payment platforms: Stripe, PayPal, custom lockbox
- Financial systems: Oracle EBS, SAP, PeopleSoft
- Banking/EFT: ACH network, treasury management systems

**Regulatory requirements:**
- ACA premium stabilization (risk adjustment, reinsurance)
- ACA APTC rules (26 USC 36B)
- COBRA premium and billing rules (ERISA, IRC)
- State premium billing requirements
- CMS Medicare Advantage premium rules
- Hawaii Prepaid Health Care Act (employer premium requirements)

**Data formats and standards:**
- X12 820 (Premium Payment)
- X12 834 (enrollment ↔ billing reconciliation)
- NACHA/ACH formats
- Custom billing file formats

**Pain points / automation opportunity:**
- Rate changes at plan year require mass regression testing
- Grace period logic is complex and varies by line of business
- Subsidy calculations (APTC) involve IRS/exchange data that changes annually
- Payment application errors cause member coverage gaps
- Reconciliation between enrollment and billing is a chronic pain point

**Scores:** RC=3 | RP=4 | DA=3 | AP=4 | PI=4 | **Total=18**

---

### 3.9 Provider Testing

**What it is:** Testing provider data management — directory accuracy, credentialing, network management, contracting, and provider portal functionality.

**Specific test scenarios:**
- **Provider directory:**
  - Directory accuracy validation (CMS requires 90-day review cycle)
  - Provider search functionality (specialty, location, language, accepting new patients)
  - Network adequacy reporting (time/distance standards)
  - Real-time directory updates
  - Machine-readable file publication (Transparency in Coverage)
- **Credentialing:**
  - Primary source verification (license, DEA, board certification, education, malpractice)
  - CAQH ProView data import and validation
  - Re-credentialing cycle management (every 3 years per NCQA)
  - Exclusion list checking (OIG LEIE, SAM, state exclusion lists)
  - Ongoing monitoring (license expiration, sanctions)
- **Network management:**
  - Contract loading and fee schedule assignment
  - Provider/group/facility hierarchy management
  - Tax ID / NPI management (billing vs. rendering)
  - Network participation status tracking
  - Narrow network / tiered network configuration
- **Provider portal:**
  - Claim submission and status inquiry
  - Eligibility verification
  - Prior authorization submission
  - Remittance advice / payment lookup
  - Patient roster and panel management
  - Secure messaging

**Systems/tools commonly involved:**
- Provider data management: CAQH, Availity, symplr (formerly Vistar)
- Credentialing: symplr, Modio Health, VerityStream
- Provider portals: Availity, custom-built
- Network adequacy: Quest Analytics, HGS
- Directory compliance: Kalderos, custom

**Regulatory requirements:**
- CMS provider directory accuracy requirements (MA, Marketplace)
- No Surprises Act (provider directory accuracy obligations)
- NCQA credentialing standards (CR 1-8)
- State provider directory laws
- Transparency in Coverage (machine-readable files)
- CMS network adequacy (time/distance, appointment wait time)

**Data formats and standards:**
- CAQH ProView data format
- NPPES (NPI registry) data
- CMS HIOS provider network templates
- JSON machine-readable files (Transparency in Coverage)

**Pain points / automation opportunity:**
- Provider data changes constantly — average provider has 20+ data attributes that can change
- Directory inaccuracy is a top CMS audit finding and member complaint
- Credentialing primary source verification is manual and time-consuming
- Fee schedule loading errors directly impact claim payment accuracy
- Network adequacy analysis requires geospatial calculations

**Scores:** RC=3 | RP=4 | DA=4 | AP=4 | PI=3 | **Total=18**

---

### 3.10 Data/Analytics Testing

**What it is:** Testing data pipelines, quality measures, risk adjustment, actuarial feeds, and reporting systems that support clinical quality, financial performance, and regulatory submissions.

**Specific test scenarios:**
- **HEDIS measures:**
  - Measure calculation accuracy (90+ measures across effectiveness of care, access, utilization)
  - Hybrid data collection (administrative data + medical record review)
  - Supplemental data source integration
  - HEDIS Interactive Data Submission System (IDSS) file validation
  - Year-over-year trending and benchmarking
- **Risk adjustment / HCC coding:**
  - HCC (Hierarchical Condition Category) model application
  - RAF (Risk Adjustment Factor) score calculation
  - Diagnosis code capture accuracy
  - RADV (Risk Adjustment Data Validation) audit preparation
  - EDGE server submission validation (ACA marketplace)
  - Encounter data submission (Medicare Advantage)
- **Quality reporting:**
  - CMS Stars ratings data submission
  - CAHPS survey data handling
  - QRS (Quality Rating System) for marketplace plans
  - State quality reporting requirements
- **Actuarial data feeds:**
  - Claims triangle development
  - IBNR (Incurred But Not Reported) estimation
  - Loss ratio monitoring
  - Trend analysis feeds
- **Data warehouse testing:**
  - ETL pipeline validation
  - Data quality rules (completeness, accuracy, consistency, timeliness)
  - Dimensional model accuracy
  - Historical data integrity (slowly changing dimensions)
  - Cross-system data reconciliation
- **Regulatory data submissions:**
  - CMS encounter data
  - State APCD (All-Payer Claims Database) submissions
  - MLR reporting data
  - DOL Form 5500 data
  - IRS 1095 data

**Systems/tools commonly involved:**
- HEDIS engines: Inovalon, Cotiviti, Optum
- Risk adjustment: Episource, Cotiviti, Ciox, HCC Coder
- Data warehouse: Snowflake, Databricks, Teradata, SQL Server
- ETL: Informatica, Talend, dbt, SSIS
- BI: Tableau, Power BI, Looker
- Quality: MedInsight, Milliman

**Regulatory requirements:**
- NCQA HEDIS specifications (annual updates)
- CMS Medicare Advantage Stars program
- CMS risk adjustment methodology (annual updates)
- ACA risk adjustment (EDGE server requirements)
- State APCD mandates
- CMS data validation requirements

**Data formats and standards:**
- HEDIS IDSS format
- CMS encounter data formats
- RAPS (Risk Adjustment Processing System) format
- EDGE server submission formats
- ICD-10-CM (diagnosis coding)
- CPT/HCPCS (procedure coding)

**Pain points / automation opportunity:**
- HEDIS measure specifications change annually — requires re-validation of calculation logic
- Risk adjustment audits (RADV) have financial stakes in the billions
- Data quality issues compound across the pipeline — catching them early is critical
- ETL testing is repetitive but requires domain knowledge to validate business rules
- Reconciliation between source systems and the data warehouse is chronically under-tested

**Scores:** RC=4 | RP=4 | DA=3 | AP=3 | PI=4 | **Total=18**

---

### 3.11 Portal/Digital Testing

**What it is:** Testing member-facing, provider-facing, and broker-facing web portals, mobile applications, and digital experiences.

**Specific test scenarios:**
- **Member portal:**
  - Registration and authentication (SSO, MFA)
  - View/download ID cards
  - Claims history and EOB viewing
  - Benefit summary and accumulator display
  - Provider search/find-a-doctor
  - Cost estimator tools
  - Prescription drug lookup/formulary
  - Appointment scheduling
  - Telehealth visit initiation
  - Secure messaging with customer service
  - Premium payment
  - Plan comparison and enrollment
  - FSA/HSA/HRA account management
- **Provider portal:**
  - Claim submission and status
  - Eligibility verification
  - Prior authorization submission and status
  - Patient roster management
  - Remittance/payment lookup
  - Fee schedule access
  - Quality reporting dashboards
- **Broker portal:**
  - Group quoting and proposal generation
  - Enrollment management
  - Commission tracking
  - License verification
  - Census upload
- **Mobile app testing:**
  - iOS and Android compatibility
  - Push notifications
  - Biometric authentication
  - Digital ID card (Apple Wallet, Google Wallet)
  - Offline functionality
- **Accessibility testing:**
  - WCAG 2.1 AA compliance
  - Screen reader compatibility
  - Keyboard navigation
  - Color contrast
  - Section 508 compliance

**Systems/tools commonly involved:**
- Portal platforms: Zipari, Healthx, custom (React, Angular)
- Mobile: React Native, Flutter, native iOS/Android
- Testing: Selenium, Playwright, Cypress, Appium
- Accessibility: axe, WAVE, JAWS, NVDA
- Performance: JMeter, Gatling, k6
- CX platforms: Salesforce Health Cloud, Pega

**Regulatory requirements:**
- ADA / Section 508 (accessibility)
- Section 1557 ACA (non-discrimination, language access)
- HIPAA security (authentication, session management, PHI display)
- CMS Medicare Advantage website requirements
- State website content requirements

**Data formats and standards:**
- WCAG 2.1
- OAuth 2.0 / OpenID Connect
- FHIR (for patient-facing APIs behind portals)
- HTML/CSS/JS standards

**Pain points / automation opportunity:**
- UI testing is inherently less stable than API testing — frequent UI changes break tests
- Multi-browser and multi-device testing multiplies effort
- Accessibility testing requires specialized knowledge
- Portal testing is well-served by existing tools (Playwright, Selenium) — lower marginal value for a new AI agent spec
- Performance under open enrollment load is critical but hard to simulate

**Scores:** RC=2 | RP=3 | DA=3 | AP=4 | PI=3 | **Total=15**

---

### 3.12 Correspondence/Communication Testing

**What it is:** Testing all outbound communications to members, providers, and other stakeholders — print, email, SMS, and digital.

**Specific test scenarios:**
- **Explanation of Benefits (EOB):**
  - Claim-level detail accuracy (charges, allowed, paid, member responsibility)
  - Accumulator display (deductible met, OOP remaining)
  - Provider information accuracy
  - Benefit plan and group information
  - Appeal rights language (mandatory)
  - Language and format compliance (Section 1557)
- **Member correspondence:**
  - Welcome kits and new member packets
  - ID cards (physical and digital)
  - Annual Notices of Change (ANOC) for Medicare Advantage
  - Evidence of Coverage (EOC) documents
  - Summary of Benefits and Coverage (SBC)
  - Renewal notices
  - Termination notices
  - Coordination of Benefits questionnaires
- **Regulatory notices:**
  - HIPAA Notice of Privacy Practices
  - Adverse determination letters (denials)
  - Appeal decision letters
  - Grievance acknowledgment and resolution letters
  - COBRA election notices
  - Special enrollment period notices
- **Language and accessibility:**
  - Translation to required languages (Section 1557: top 15 languages in state)
  - Taglines in top 15 languages
  - Large print, Braille, audio formats
  - Reading level (6th-8th grade target)
- **Digital communications:**
  - Email notifications (claim processed, payment received, ID card ready)
  - SMS alerts (auth status, appointment reminders)
  - Push notifications (mobile app)
  - Secure message center
- **Template management:**
  - Variable data merge accuracy
  - Conditional content logic (plan-specific, state-specific, LOB-specific)
  - Version control and approval workflows
  - Print vendor file generation

**Systems/tools commonly involved:**
- Correspondence engines: OpenText Exstream, Quadient Inspire, custom
- Template management: custom, DocuSign, Adobe Experience Manager
- Print vendors: RR Donnelley, Broadridge
- Email: Salesforce Marketing Cloud, Mailchimp (transactional)
- SMS: Twilio, custom
- Translation: TransPerfect, Lionbridge, custom

**Regulatory requirements:**
- Section 1557 ACA (language access, notice of availability)
- CMS Medicare Advantage marketing/communications guidelines (MCMG)
- State-specific notice requirements
- ERISA disclosure requirements
- HIPAA privacy notices
- No Surprises Act (good faith estimate, balance billing notices)
- DOL/IRS notice requirements

**Data formats and standards:**
- PDF/A (archival)
- XML/JSON (variable data)
- Print-ready formats (PostScript, PDF)
- Email standards (CAN-SPAM compliance)

**Pain points / automation opportunity:**
- Template logic gets extremely complex (hundreds of conditional variables)
- Regulatory language requirements change frequently
- Multi-language testing multiplies effort by 15x+ (Section 1557)
- Visual QA of formatted documents is difficult to automate
- Errors in member-facing communications are visible and generate complaints/regulatory findings
- Print vendor file validation is tedious but critical

**Scores:** RC=3 | RP=4 | DA=3 | AP=3 | PI=3 | **Total=16**

---

## 4. Cross-Cutting Concerns

### 4.1 Common Core Administration Platforms

| Platform | Vendor | Market Share | Notes |
|----------|--------|-------------|-------|
| **Facets** | TriZetto (Cognizant) | ~25% of US lives | Legacy workhorse, Cognizant's flagship |
| **QNXT** | TriZetto (Cognizant) | ~25% of US lives | More modern than Facets, same vendor |
| **HealthRules Payor** | HealthEdge | Growing | Cloud-native, rules-based, high auto-adjudication rates |
| **Javelina** | Mphasis | Niche | 35+ years in healthcare, analytics-focused |
| **PLEXIS** | PLEXIS Healthcare | Small/mid | Focuses on Medicaid, TPA market |
| **QicLink** | TriZetto (Cognizant) | Regional | Part of TriZetto portfolio |

Combined, Facets and QNXT cover over 50% of insured lives in the US.

### 4.2 Testing Frameworks Used in Health Insurance

| Framework/Tool | Type | Common Use |
|---------------|------|------------|
| Selenium/Playwright | UI automation | Portal testing, regression |
| Postman/ReadyAPI | API testing | FHIR APIs, web services |
| Edifecs | EDI validation | SNIP level 1-7 testing |
| JMeter/Gatling | Performance | Open enrollment load testing |
| Cucumber/Gherkin | BDD | Business-readable test specs |
| Custom X12 parsers | EDI | Transaction validation |
| Cotiviti/Inovalon | Claims editing | Auto-edit and audit testing |
| dbt | Data testing | Data warehouse validation |
| SAS | Analytics | HEDIS calculations, actuarial |

### 4.3 HMSA-Specific Information

HMSA (Hawaii Medical Service Association) is:
- The largest health insurer in Hawaii
- A Blue Cross Blue Shield Association licensee (nonprofit)
- Founded in 1938
- Covers ~700,000 lives (roughly half of Hawaii's population)
- Offers commercial, Medicare Advantage, and QUEST Integration (Medicaid) plans
- Subject to the unique **Hawaii Prepaid Health Care Act** (1974) — the first state employer health insurance mandate in the US, predating ACA by decades
- Built a new data center in recent years for IT modernization
- Adopted Stellarus technology platform in 2025 for member experience improvement
- Operates HMSA Online (member portal) with digital claims, benefits, and provider search

Hawaii-specific testing considerations:
- **Prepaid Health Care Act** compliance (employer mandate, minimum benefit standards)
- **QUEST Integration** (Medicaid managed care) contract requirements
- Geographic isolation creates unique network adequacy challenges (inter-island provider access)
- Small market with limited trading partners (less EDI complexity, deeper partner relationships)
- High cost of living impacts premium testing (actuarial factors)

### 4.4 Industry Test Automation Approaches

Current state of test automation in health insurance payer organizations:

1. **Manual-dominant (majority):** Most payer QA teams still rely heavily on manual testing, especially for claims adjudication and benefits configuration. Spreadsheet-driven test cases are common.

2. **Record-and-playback (some):** Selenium-based UI automation for portal regression. Fragile, high maintenance.

3. **API-first (growing):** FHIR API mandates are pushing payers toward API test automation. Postman collections and ReadyAPI projects are expanding.

4. **AI-assisted (emerging):** Tools like Virtuoso, Applitools, and Testim are being adopted for intelligent test generation and visual regression. Still early.

5. **Domain-specific tools (niche):** Edifecs for EDI, Cotiviti for claims editing. These are not general-purpose test automation — they serve specific validation functions.

6. **Data-driven testing (underserved):** Test data management is the single biggest bottleneck. Synthetic data generation for PHI-compliant test environments is a major unsolved problem.

---

## 5. Recommended Priority Order for Spec Building

Based on the scoring and strategic considerations:

### Tier 1 — Build First (highest ROI)

| Priority | Domain | Score | Rationale |
|----------|--------|-------|-----------|
| 1 | **EDI Testing** | 25 | Perfectly structured (X12 standards), extremely repetitive, well-documented, massive volume. Ideal for deterministic AI agent automation. |
| 2 | **Claims Testing** | 24 | Core business function, highest pain, deterministic rules. Claims adjudication regression testing is the single largest QA effort. |
| 3 | **Benefits/Plan Configuration** | 22 | High error cost, extremely repetitive (every plan year), accumulator testing is notoriously painful. |

### Tier 2 — Build Next (high value, moderate complexity)

| Priority | Domain | Score | Rationale |
|----------|--------|-------|-----------|
| 4 | **Membership/Enrollment** | 20 | Seasonal surges (open enrollment), 834 processing is EDI-adjacent. |
| 5 | **Compliance/Regulatory** | 21 | High pain but lower automation potential — requires judgment. Best automated as checklist/audit agents. |
| 6 | **Authorization/UM** | 21 | CMS-0057-F creates urgency. Clinical criteria testing is highly structured. |

### Tier 3 — Build Later (solid value, good candidates)

| Priority | Domain | Score | Rationale |
|----------|--------|-------|-----------|
| 7 | **Integration/API** | 20 | FHIR mandate creates urgency but API testing tools already exist (Postman, etc.). Spec adds value for domain-specific validation. |
| 8 | **Billing/Premium** | 18 | Important but lower volume and complexity than claims. |
| 9 | **Provider Testing** | 18 | Directory accuracy is a CMS audit hot spot. Credentialing is structured. |

### Tier 4 — Build When Ready (lower marginal value)

| Priority | Domain | Score | Rationale |
|----------|--------|-------|-----------|
| 10 | **Data/Analytics** | 18 | HEDIS and risk adjustment are high-value but require deep actuarial/clinical knowledge. |
| 11 | **Correspondence/Communication** | 16 | Visual QA is hard to automate. Template logic testing is more feasible. |
| 12 | **Portal/Digital** | 15 | Well-served by existing tools (Playwright spec already exists). Lowest marginal value for a new spec. |

---

## 6. Sources

- [EDI Transactions and Code Sets — UnitedHealthcare](https://www.uhcprovider.com/en/resource-library/edi/edi-transactions.html)
- [Health Care Transaction Flow — X12](https://x12.org/flow/health-care)
- [HIPAA EDI Document Standard — EDI Basics](https://www.edibasics.com/edi-resources/document-standards/hipaa/)
- [EDI Files in Healthcare — AccountableHQ](https://www.accountablehq.com/post/edi-files-in-healthcare-what-they-are-common-transactions-837-835-270-271-and-how-they-work)
- [9 Key Healthcare EDI Transactions — Invene](https://www.invene.com/blog/demystifying-healthcare-edi-the-9-critical-transactions-explained)
- [Adopted Standards and Operating Rules — CMS](https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/hipaa/adopted-standards-operating-rules)
- [Auto-Adjudication — MedVision](https://www.medvision-solutions.com/blog/auto-adjudication-processing-claims-with-ease)
- [Test Automation Healthcare Compliance — QA Financial](https://qa-financial.com/test-automation-becomes-healthcares-new-compliance-lifeline/)
- [Best Practices for AI in Claims Adjudication — Health Affairs](https://www.healthaffairs.org/content/forefront/best-practices-ai-health-insurance-claims-adjudication-and-decision-making)
- [QNXT in Healthcare — Sulekha](https://techjobs.sulekha.com/techpulse/what-is-qnxt-in-healthcare_23388)
- [Leading Healthcare Claims Software — GHIT Digital](https://www.ghit.digital/insight/detail/leading-healthcare-claims-software-platforms)
- [InterQual Criteria — Optum](https://business.optum.com/en/operations-technology/clinical-decision-support/interqual/criteria.html)
- [MCG and InterQual Guide — Nurse Fern](https://nursefern.com/remote-nurses-guide-to-mcg-and-interqual/)
- [Utilization Management — Wikipedia](https://en.wikipedia.org/wiki/Utilization_management)
- [HEDIS Measures — NCQA](https://www.ncqa.org/hedis/measures/)
- [HEDIS 2026 Updates — MedInsight](https://medinsight.com/healthcare-data-analytics-resources/blog/looking-ahead-preparing-for-key-hedis-2026-updates/)
- [HCC Coding — AAFP](https://www.aafp.org/family-physician/practice-and-career/getting-paid/coding/hierarchical-condition-category.html)
- [834 File in Healthcare — HIPAA Journal](https://www.hipaajournal.com/834-file-in-healthcare/)
- [EDI 834 — Cleo](https://www.cleo.com/edi-transactions/edi-834)
- [Health Plan Accreditation — NCQA](https://www.ncqa.org/programs/health-plans/health-plan-accreditation-hpa/)
- [NCQA and URAC Recognition — Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/cms-formally-recognizes-ncqa-and-urac-as-accrediting-entities-for-qhps)
- [Health Plan Accreditation — URAC](https://www.urac.org/accreditation-cert/health-plan-accreditation/)
- [Section 1557 Language Access — HHS](https://www.hhs.gov/civil-rights/for-individuals/section-1557/fs-limited-english-proficiency/index.html)
- [Section 1557 Final Rule FAQs — HHS](https://www.hhs.gov/civil-rights/for-individuals/section-1557/faqs/index.html)
- [CMS Interoperability and Prior Authorization Final Rule CMS-0057-F](https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-and-prior-authorization-final-rule-cms-0057-f)
- [CMS-0057-F Decoded — Firely](https://fire.ly/blog/cms-0057-f-decoded-must-have-apis-vs-nice-to-have-igs-for-2026-2027/)
- [Provider Credentialing — CAQH](https://www.caqh.org/solutions/provider-data/credentialing-suite)
- [Network Directory Accuracy — AMA](https://www.ama-assn.org/topics/network-directory-accuracy)
- [Provider Data Accuracy — Atlas Systems](https://www.atlassystems.com/blog/provider-data-accuracy)
- [COBRA Grace Period — CMS](https://www.cms.gov/cciio/programs-and-initiatives/other-insurance-protections/cobra_fact_sheet)
- [ACA Grace Periods — HealthCare.gov](https://www.healthcare.gov/apply-and-enroll/health-insurance-grace-period/)
- [Health Insurance Portal ROI — ScienceSoft](https://www.scnsoft.com/insurance/health-insurance-portal)
- [Zipari CX Platform](https://zipari.com/)
- [CMS APIs and Implementation Guides](https://www.cms.gov/priorities/burden-reduction/overview/interoperability/implementation-guides-and-standards/application-programming-interfaces-apis-and-relevant-standards-and-implementation-guides-igs)
- [FHIR About — eCQI Resource Center](https://ecqi.healthit.gov/fhir/about)
- [Test Automation in Healthcare — AlgoShack](https://medium.com/@algoshack/test-automation-in-healthcare-a658b552bc5f)
- [Healthcare Testing Tools 2025 — PractiTest](https://www.practitest.com/resource-center/article/best-healthcare-test-management-tools/)
- [AI-Powered Test Automation for Insurance — Virtuoso](https://www.virtuosoqa.com/solutions/insurtech-test-automation)
- [Coordination of Benefits — CMS](https://www.cms.gov/medicare/coordination-benefits-recovery/overview/coordination-benefits)
- [HMSA](https://hmsa.com/)
- [HMSA Data Center — Data Specialties](https://webuilddatacenters.com/portfolio_page/hawaii-medical-service-association/)
- [EDI 276 — 1EDISource](https://www.1edisource.com/resources/edi-transactions-sets/edi-276/)
- [EDI 277 — Cleo](https://www.cleo.com/edi-transactions/edi-277)
- [HIPAA 820 Premium Payment — HIPAA Suite](https://www.hipaasuite.com/hipaa-premium-payment-master-820)
- [Copay Accumulators — National Infusion Center Association](https://infusioncenter.org/understanding-copay-accumulators-who-really-benefits/)
