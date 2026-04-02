# Epic 591204 — Mapping File

**Title:** Mapping File to be used to identify DRG that belong to the same MDC
**State:** Active — Implementation started
**Priority:** 2
**Value Area:** Business
**Parent:** 590047 (30-Day Readmissions)

## Description

As a user, I want to provide a mapping files to be used to identify DRG that belong to the same MDC.

## Features

### Feature 591211 — Provide a mapping file to identify DRG that belong to same MDC
**State:** Active — Implementation started
**Priority:** 2
**Description:** As a user, I want to provide MS DRG and APR DRG Mapping Files that will identify DRG that belong to same MDC

**Child Stories (2):**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 591214 | Processing of APR DRG to MDC mapping file | Active | 3/24/2026 |
| 591213 | Processing of MS DRG mapping file | Active | 3/19/2026 |

---

#### Story 591214 — Processing of APR DRG to MDC mapping file
**State:** Active — Implementation started
**Iteration:** IT Portfolio\PF-Planning-2602\Sprint-260305
**Priority:** 2
**Impacted LOB:** QST

**Description:**
1. As a user, I want to be able to navigate where the APR DRG to MDC file will be located
2. As a user, I want to be able to upload the mapping file
3. As a user, I want to be able to download the mapping file via path
4. As a user, I want to be able to upload new mapping file via path

As an Admin, I want 30-day readmission APR DRG mapping file to be available and loaded into tables, so that data can be used to identify DRG groups information for claims processing.

**Description (detail):**
- APR DRG Mapping file to be available path <<PATH>>
- System should read data from path and validate the file format, data in the file
- APR DRG mapping file should be processed and loaded into TABLE <<Table Name - TBD>> with custom job

**Notes / Assumptions:**
- APR (All Patient Refined) DRG file to be available or file format to be available
- Required Access to the sharepoint and tables will be available

**Dependencies:**
- Data: Business to confirm the data format

**Tested By (10+):**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 593614 | AC01-002 file not found in shareldrive/networkd... | Design | 3/18/2026 |
| 593740 | AC02-001 Happy path: valid template and data | Design | 3/18/2026 |
| 593741 | AC02-002 Missing required column... | Design | 3/18/2026 |
| 593742 | AC03-001 Insert new re... | Design | 3/18/2026 |
| 593743 | AC04-001 Success email... | Design | 3/18/2026 |
| + more | Show more (6 of 18) | | |
| | Not shown: Tested By (5), Child (7) | | |

**Acceptance Criteria:**

**AC01 — File Availability & Readability**
- Scenario: Verify the file exists in the configured SharePoint/share path and can be opened
- File is present at the expected location and accessible by the service account
- File extension is an approved type (e.g., .csv, .xlsx)

**AC02 — File Structure & Data Validation**
- Scenario: Validate file format, headers, required columns, and basic data rules before processing
- File format matches expected type
- Required columns exist and match the template (names and datatype)
- Basic data rules pass (datatype, length, mandatory fields, domain values)

**AC03 — Processing: Insert/Update/Terminate & Missing Values**
- Scenario: Process new, update, and terminate records; handle blanks/missing per rules
- New records are inserted with correct defaults
- Existing records are updated using documented match/business keys
- Terminated records are end-dated per rule (inclusive/exclusive as specified)
- Blank/nullable fields follow rule (skip/default/fail) and are logged
- **Partial issues do not stop the full run unless configured as Mandatory** (highlighted)

**AC04 — Success Email Notification**
- Scenario: Send a completion email to the DL after a successful run
- Email delivered to the configured DL/stakeholders
- Email includes file name, start/end time, total, processed, and failed counts

**AC05 — Record Count Reconciliation**
- Scenario: Reconcile total vs processed vs failed counts
- Total records = Processed + Failed
- Processed = Inserted + Updated + Terminated
- Counts appear in logs and in the notification email

**AC06 — Failure Logging & Confirmation**
- Scenario: Capture failed records with reasons in a dedicated store
- Each failed record includes an identifier, error reason, and timestamp
- Failures are updated in to a failure table/report
- A failure summary is available for business review or Email is not sent for failed runs

**AC07 — Input File Archiving**
- Scenario: Archive the input file after processing
- File is moved/copied to the configured archive location
- Archive retains original name and timestamp (or appends run metadata)
- Archive log records file name, size, and archive datetime (and checksum if used)

---

#### Story 591213 — Processing of MS DRG mapping file
**State:** Active — Implementation started
**Iteration:** IT Portfolio\PF-Planning-2602\Sprint-260305
**Priority:** 2
**Impacted LOB:** PB, MCR
**5 comments**

**Description:**
1. As a user, I want to be able to navigate where the MS DRG to MDC file will be located
2. As a user, I want to be able to upload the mapping file
3. As a user, I want to be able to download the mapping file via path
4. As a user, I want to be able to upload new mapping file via path

As an Admin, I want 30-day readmission MS DRG mapping file to be available and loaded into tables, so that data can be used to identify DRG groups information for claims processing.

**Description (detail):**
- MS DRG Mapping file to be available path <<PATH>>
- System should read file from path and validate the file format, read the data
- MS DRG mapping file should be processed and loaded into TABLE <<Table Name - TBD>> with custom job

**Notes / Assumptions:**
- MS (Medicare Severity Diagnosis) DRG file to be available or file format to be available
- Required access has been placed for SharePoint and tables

**Dependencies:**
- Data: Business to data format

**Tested By (9):**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 593614 | AC01-0xx | Design | 3/23/2026 |
| 593740 | AC02-0xx | Design | 3/25/2026 |
| 593741 | AC02-0xx | Design | 3/18/2026 |
| 593742 | AC03-0xx | Design | 3/18/2026 |
| 593743 | AC04-0xx | Design | 3/18/2026 |
| + more | (9 total) | | |

**Acceptance Criteria:**

**AC01 — File Availability & Readability**
- Scenario: Verify the file exists in the configured SharePoint/share path and can be opened
- File is present at the expected location and accessible by the service account
- File extension is an approved type (.Xlsx)
- File path location:
  - Dev: <<>>
  - UAT: <<>>
  - PROD: <<>>

**AC02 — File Structure & Data Validation**
- Scenario: Validate file format, headers, required columns, and basic data rules before processing
- File Format: -
- File format matches expected type
- Required columns exist and match the template (names and datatype)
- Basic data rules pass (datatype, length, mandatory fields, domain values)

**AC03 — Processing: Insert/Update/Terminate & Missing Values**
- Scenario: Process new, update, and terminate records; handle blanks/missing per rules
- New records are inserted with correct defaults
- Existing records are updated using documented match/business keys
- Terminated records are end-dated per rule (inclusive/exclusive as specified)
- Blank/nullable fields follow rule (skip/default/fail) and are logged
- **Partial issues do not stop the full run unless configured as Mandatory** (highlighted)

**AC04 — Success Email Notification**
- Scenario: Send a completion email to the DL after a successful run
- Email delivered to the configured DL/stakeholders
- DL List - Dev, Test and **PROD?** (highlighted — unclear if PROD DL is defined)
- Email includes file name, start/end time, total, processed, and failed counts

**AC05 — Record Count Reconciliation**
- Scenario: Reconcile total vs processed vs failed counts
- Total records = Processed + Failed
- Processed = Inserted + Updated + Terminated
- Counts appear in logs and in the notification email

**AC06 — Failure Logging & Confirmation**
- Scenario: Capture failed records with reasons in a dedicated store
- Each failed record includes an identifier, error reason, and timestamp
- Failures are updated in to a failure table/report
- A failure summary is available for business review or Email is not sent for failed runs

**AC07 — Input File Archiving**
- Scenario: Archive the input file after processing
- File is moved/copied to the configured archive location
- Archive retains original name and timestamp (or appends run metadata)
- Archive log records file name, size, and archive datetime (and checksum if used)
- Archive Location for **DEV, TEST, PROD - TBD** (highlighted)

---

## Overlap & Differences: 591214 (APR DRG) vs 591213 (MS DRG)

Both stories share the **same test case IDs** (593614, 593740, 593741, 593742, 593743+) and have **identical AC01-AC07 acceptance criteria structure**.

| Attribute | 591214 (APR DRG) | 591213 (MS DRG) |
|-----------|------------------|-----------------|
| Impacted LOB | QST | PB, MCR |
| DRG type | APR (All Patient Refined) | MS (Medicare Severity Diagnosis) |
| File format | .csv or .xlsx (AC01) | .Xlsx (AC01) |
| File path locations | Not specified per env | Dev/UAT/PROD placeholders (highlighted) |
| DL list for email | Not specified | Dev, Test, PROD? (highlighted) |
| Archive location | Not specified per env | DEV, TEST, PROD - TBD (highlighted) |
| Tested By count | 10+ (6 of 18 shown) | 9 |
| Comments | 1 | 5 |
| Child items | 7 | Not shown |

**Key takeaway:** MS DRG (591213) has more env-specific detail (path placeholders per env, DL list question, archive location TBD) but both share the same AC structure and test cases. The LOB split is significant — APR DRG serves QST while MS DRG serves PB and MCR.
