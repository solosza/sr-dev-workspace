# Test Cases — Mapping File (591213 / 591214)

All test cases apply to both MS DRG (591213) and APR DRG (591214) mapping file processing.
All are currently **Design** state, **Not Automated**, Priority 2.
All linked to Tests (2): 591214 Processing of APR DRG to MDC mapping file, 591213 Processing of MS DRG mapping file.

---

## AC01 — File Availability & Readability

### 593613 — AC01-001 Validate file exists and File format

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Identify a valid .xlsx file in testing SharePoint | File should be present in the path: S:\QNXTCOM_Claims_Readmission_Dev\Process and file should be closed |
| 2 | Verify file format and data part of the specifications | File should contain below. Action MS-DRG MDC MS-DRG Title Effective Date Term Date. File should start with APR_DRG/MS_DRG |
| 3 | (empty) | |

**References:** 593794 MS DRG (Active, updated 3/17/2026)

**Key detail: Actual DEV path revealed — `S:\QNXTCOM_Claims_Readmission_Dev\Process`**

**Key detail: File columns — Action, MS-DRG, MDC, MS-DRG Title, Effective Date, Term Date**

**Key detail: File naming — must start with APR_DRG or MS_DRG**

---

### 593614 — AC01-002 File not found in sharedrive/networkdrive

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Ensure no file exists at S:\QNXTCOM_Claims_Readmission_Dev\Process or S:\QNXTCOM_Claims_Readmission_Test\Process PATH | |
| 2 | Trigger hmsa_com_imp_readmiss_apr_drg_to_mdc_load | Job logs "file not found" and exits as per design (failure or no-op), without crash |
| 3 | (empty) | |

**Key detail: TEST path revealed — `S:\QNXTCOM_Claims_Readmission_Test\Process`**

**Key detail: Job name revealed — `hmsa_com_imp_readmiss_apr_drg_to_mdc_load`**

---

## AC02 — File Structure & Data Validation

### 593740 — AC02-001 Happy path: valid template and data

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Validate the data by running the SP: `readmiss_apr_drg_to_mdc_error_rpt.sp`, `readmiss_ms_drg_to_mdc_error_rpt.sp` | Validates the data in work table and updated the process status with error messages/success |
| 2 | Place at S:\QNXTCOM_Claims_Readmission_Dev\Process and run: `qst_validate_readmiss_apr_drg_to_mdc_load`, `pb_validate_readmiss_ms_drg_to_mdc_load`, `mcr_validate_readmiss_ms_drg_to_mdc_load` | Data Validated against the shared file and processed successfully |
| 3 | (empty) | |

**Key detail: Stored procedures revealed:**
- `readmiss_apr_drg_to_mdc_error_rpt.sp` (APR DRG validation)
- `readmiss_ms_drg_to_mdc_error_rpt.sp` (MS DRG validation)

**Key detail: LOB-specific validation jobs revealed:**
- `qst_validate_readmiss_apr_drg_to_mdc_load` (QST — APR DRG)
- `pb_validate_readmiss_ms_drg_to_mdc_load` (PB — MS DRG)
- `mcr_validate_readmiss_ms_drg_to_mdc_load` (MCR — MS DRG)

---

### 593741 — AC02-002 Missing required column

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Remove one required column from header | |
| 2 | Run <JOB_NAME> | Job fails validation with clear message naming missing column(s); no records processed |

---

## AC03 — Processing: Insert/Update/Terminate & Missing Values

### 593742 — AC03-001 Insert new records with defaults

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | File with rows marked Status="Add" not present in target table | |
| 2 | Some optional fields blank (per <NULL_RULES>) | |
| 3 | Run | New rows inserted; defaults applied to optional blanks; insert count increments; logs show detail |

---

## AC04 — Success Email Notification

### 593743 — AC04-001 Success email

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute a fully successful run in DEV | |
| 2 | Monitor mailbox for <<DEV_DL>> | Email received by DL; subject/body contains file name, start/end timestamps, totals, processed, failed |
| 3 | (empty) | |

---

## AC05 — Record Count Reconciliation

### 593744 — AC05-001 Reconciliation on clean success

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Prepare file with only valid rows (mixture of New/Update/Terminate) | Total=Processed; Failed=0; Processed=Inserted+Updated+Terminated. Counts consistent across logs and email |
| 2 | Run | |
| 3 | Check logs and email | |

---

## AC06 — Failure Logging & Confirmation

### 593745 — AC06-001 Failure record content

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Run with intentional invalid row(s) | Each failure contains: row identifier (e.g., <BUSINESS_KEYS> or row number), error reason, timestamp, and file/run id |

---

## AC07 — Input File Archiving

### 593747 — AC07-001 Archive on successful run

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute successful run in DEV | |
| 2 | Check <<Env_ARCHIVE_PATH>> and logs | File present in archive with original name + timestamp/metadata; logs show name, size, archive datetime, checksum (if enabled) |

---

---

## Child Task — Test Data Preparation

### 591498 — 05 Test Data/Preparation of file
**Type:** Task (child of 591213 — Processing of MS DRG mapping file)
**State:** New
**Assigned to:** Unassigned
**Updated by:** Chuck Atoa
**Priority:** 2
**Implementation:** Integrated in Build

**Description:**
Identify test data for required scenarios.
1. Include File validation with valid information
2. Prepare file processing with empty data
3. Prepare file processing with existing data to validate reprocessing of file
4. Include Scenarios for data append, update, remove/terminate etc.

**This is the test data prep task — it defines the test file variants needed to execute all the test cases above.**

---

## Critical Details Extracted

### File Paths
| Environment | Path |
|-------------|------|
| DEV | `S:\QNXTCOM_Claims_Readmission_Dev\Process` |
| TEST | `S:\QNXTCOM_Claims_Readmission_Test\Process` |
| UAT | TBD |
| PROD | TBD |

### File Specification
| Attribute | Value |
|-----------|-------|
| Format | .xlsx |
| Naming | Must start with `APR_DRG` or `MS_DRG` |
| Columns | Action, MS-DRG, MDC, MS-DRG Title, Effective Date, Term Date |
| Action values | Add (at minimum — Update/Terminate implied by AC03) |

### Job Names
| Job | LOB | DRG Type |
|-----|-----|----------|
| `hmsa_com_imp_readmiss_apr_drg_to_mdc_load` | QST | APR DRG |
| `qst_validate_readmiss_apr_drg_to_mdc_load` | QST | APR DRG |
| `pb_validate_readmiss_ms_drg_to_mdc_load` | PB | MS DRG |
| `mcr_validate_readmiss_ms_drg_to_mdc_load` | MCR | MS DRG |

### Stored Procedures
| SP Name | Purpose |
|---------|---------|
| `readmiss_apr_drg_to_mdc_error_rpt.sp` | APR DRG validation/error reporting |
| `readmiss_ms_drg_to_mdc_error_rpt.sp` | MS DRG validation/error reporting |

---

## Comparison: Mapping File TCs vs Exclusion File TCs

| Aspect | Exclusion File (4 TCs) | Mapping File (9 TCs) |
|--------|----------------------|---------------------|
| AC01 — File exists | Generic <<PATH>> | Actual path: S:\QNXTCOM_Claims_Readmission_Dev\Process |
| AC01 — File not found | Not covered | 593614 — specific negative test with job name |
| AC02 — Happy path | Generic "run job" | Specific SPs and LOB-specific validation jobs |
| AC02 — Missing column | Not covered | 593741 — remove column, verify clear error |
| AC03 — Insert/Update | Generic "new rows inserted" | Status="Add", NULL_RULES, defaults applied |
| AC04 — Email | Not covered (archive instead) | 593743 — email to DL with counts |
| AC05 — Reconciliation | Not covered | 593744 — Total=Processed+Failed formula |
| AC06 — Failure logging | Not covered | 593745 — row identifier, error reason, timestamp, run id |
| AC07 — Archive | 593949 — basic archive check | 593747 — identical to exclusion file TC |

**The exclusion file tests are missing 5 test cases that the mapping file has.** The exclusion file stories should be updated to match.
