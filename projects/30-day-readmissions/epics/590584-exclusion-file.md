# Epic 590584 — Exclusion File

**Title:** Exclusion file that has criteria to be used to exclude claims
**State:** Active — Implementation started
**Priority:** 2
**Value Area:** Business
**Parent:** 590047 (30-Day Readmissions)

## Description

As a user, I want to provide an Exclusion File that will have criteria to identify DRG for cancer, trauma, pregnancy, delivery, neonatal, BH IP claims. In addition, 1 IP with discharge status 07 (left against medical advice/discontinued care), 20 (expired), 30 (still a patient) that will be used to exclude claims from the policy.

## Exclusion Criteria

**By DRG category:**
- Cancer
- Trauma
- Pregnancy
- Delivery
- Neonatal
- Behavioral Health IP

**By discharge status:**
- 07 — Left against medical advice / discontinued care
- 20 — Expired
- 30 — Still a patient

## Features

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 590586 | Provide an exclusion file to identify codes to exclude from denying/pending | Active | 3/24/2026 |

### Feature 590586 — Provide an exclusion file to identify codes to exclude from denying/pending
**Assigned to:** Chuck Atoa
**State:** Active — Implementation started
**Priority:** 2
**Updated:** 3/24/2026
**Description:** As a user, I want to provide MS DRG and APR DRG Exclusion Files that will identify codes to exclude from the auto-denying or pending

**Child Stories:**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 590589 | Processing of APR DRG exclusion file | Active | 3/26/2026 |
| 590587 | Processing of the MS DRG exclusion file | Active | 3/26/2026 |

#### Story 590589 — Processing of APR DRG exclusion file
**State:** Active — Implementation started
**Iteration:** IT Portfolio\PF-Planning-2602\Sprint-260326
**Priority:** 2

**Description:**
1. As a user, I want to be able to navigate where the exclusion file will be located
2. As a user, I want to be able to upload the exclusion file
3. As a user, I want to be able to download the mapping file via path
4. As a user, I want to be able to upload new mapping file via path

As an Admin, I want 30-day readmission APR DRG exclusion file to be available and loaded into tables, so that data can be used to identify diagnoses to exclude for claims processing.

**Description (detail):**
- APR DRG exclusion file to be available path <<PATH>>
- System should read data from path and validate the file format, data available
- APR DRG exclusion file should be processed and loaded into TABLE <<Table Name - TBD>> with custom job

**Notes / Assumptions:**
- APR (All Patient Refined) DRG file to be available or file format to be available

**Dependencies:** -
**Requirements:** -
**Data:** Business to provide APR DRG exclusion file

**Tested By (4):**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 593946 | AC01-001 Exclude File - Validate file exists and is readable | Design | 3/18/2026 |
| 593947 | AC02-001 Exclude File - Validation of exception... | Design | 3/18/2026 |
| 593948 | AC03-001 Exclude File - Failure summary/report... | Design | 3/18/2026 |
| 593949 | AC04-001 Exclude File Archive on successful run | Design | 3/24/2026 |

**Acceptance Criteria:**

**AC01:** File to be available in provided SharePoint/sharepath and its readable format

**AC02:** Validation of file format, layout, data available in the file

**AC03:** Validate if the job processes and updates existing data (add new, update existing data, terminate/end date existing data)

#### Story 590587 — Processing of the MS DRG exclusion file
**State:** Active — Implementation started
**Iteration:** IT Portfolio\PF-Planning-2602\Sprint-260326
**Priority:** 2

**Description:**
1. As a user, I want to be able to navigate where the exclusion file will be located
2. As a user, I want to be able to upload the exclusion file
3. As a user, I want to be able to download the mapping file via path
4. As a user, I want to be able to upload new mapping file via path

As an Admin, I want 30-day readmission MS DRG exclusion file to be available and loaded into tables, so that data can be used to identify diagnoses to exclude for claims processing.

**Description (detail):**
- MS DRG exclusion file to be available path <<PATH>>
- System should read data from path and validate the file format, data available
- MS DRG mapping file should be processed and loaded into TABLE <<Table Name - TBD>> with custom job

**Notes / Assumptions:**
- MS (Medicare Severity Diagnosis) DRG file to be available or file format to be available

**Dependencies:** -
**Requirements:** -

**Tested By (4):**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 593946 | AC01-001 Exclude File - Validate file exists and is readable | Design | 3/18/2026 |
| 593947 | AC02-001 Exclude File - Validation of exception... | Design | 3/18/2026 |
| 593948 | AC03-001 Exclude File - Failure summary/report... | Design | 3/18/2026 |
| 593949 | AC04-001 Exclude File Archive on successful run | Design | 3/24/2026 |

**Child (6):** TBD — need to capture child work items

**Acceptance Criteria:**

**AC01 — File Availability & Readability**
- Scenario: Verify the file exists in the configured SharePoint/network share path and can be opened
- File exists at <SharePoint / network share path> and is readable without errors
- Missing file causes the job to fail with a clear "file not found" message
- Access denied results in a clear "permission" failure with remediation guidance
- Corrupted/unopenable file fails fast with an actionable error
- File to be available in provided SharePoint/share path and in readable format

**AC02 — Data Rules & Data Quality and data load**
- Scenario: Validate row-level content and business rules
- Empty required fields fail with row numbers and column names
- Invalid types or malformed dates (yyyy-MM-dd) fail with row numbers
- Duplicate exclusion keys (e.g., <CustomerId, EffectiveDate>) are rejected
- Validation of file format, layout and data available in the file

**AC03 — Auditing**
- Scenario: Track which exclusion version is used for every run
- Commit artifact build number is captured
- Exclusion artifacts and validation reports ?
- Validate if the job processes and updates existing data (add new, update existing data, terminate/end date existing data)

**AC04 — Error Handling & Reporting**
- Scenario: Make failures clear, actionable, and visible
- Validation failures produce a machine-readable validation_report.report
