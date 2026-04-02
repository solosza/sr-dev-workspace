# Automation Approach — 30-Day Readmissions

---

## Three Approaches Compared

### 1. Manual Testing (Current State)

How each test cycle works today:

```
Tester receives test case (e.g., AC01-001)
  → Opens Azure DevOps, reads steps
  → RDPs into DEV server
  → Navigates to S:\QNXTCOM_Claims_Readmission_Dev\Process
  → Manually places .xlsx file on share drive
  → Asks Tidal admin to trigger job (or waits for scheduled run)
  → Waits for job to complete
  → Opens SSMS, connects to QNXT database
  → Runs ad-hoc SELECT queries to verify rows loaded
  → Checks email inbox for success notification
  → Navigates to archive path, confirms file moved
  → Screenshots each step
  → Pastes screenshots into Azure DevOps test run
  → Marks test case Pass/Fail
  → Repeats for next test case
```

**Per test case:** ~30-60 minutes (including wait time, screenshots, documentation)

**Per regression cycle (13 TCs × 3 LOBs):** ~2-3 days of tester time

**Pain points:**
- Wait time between job trigger and completion is dead time
- Screenshots are brittle — UI changes break evidence, not the test
- Same SQL queries typed by hand each time — typos cause false failures
- No way to run overnight or on-demand
- Test data conflicts between testers sharing DEV environment
- Items 4-10 (pend/deny logic, Aerial, Cotiviti) have zero test cases — manual or otherwise
- Tester must understand SQL, Tidal, QNXT, file shares — high knowledge bar

---

### 2. Traditional Test Automation (No AI)

Python + pytest + openpyxl + pyodbc. Scripts replace the human steps.

```
pytest kicks off
  → Script generates/copies .xlsx test file to share drive
  → Script triggers job (Tidal API call or SP exec)
  → Script polls DB until job completes (or timeout)
  → Script runs SQL assertions against target tables
  → Script checks archive path for file
  → Script queries email log table for notification record
  → pytest produces Pass/Fail report with assertion details
  → Report uploaded to Azure DevOps via API
```

**Per test case:** ~2-5 minutes (mostly job execution wait)

**Per regression cycle (13 TCs × 3 LOBs):** ~1-2 hours unattended

**What you gain:**
- Repeatable — same test, same result, every time
- Runs overnight, on-demand, or in CI pipeline
- No screenshots needed — assertion output IS the evidence
- Catches regressions immediately on every code change
- Test data generated programmatically — no conflicts

**What you still do manually:**
- Write every test case by hand — read the AC, translate to Python
- Write every SQL assertion by hand — must know table schema
- Maintain test data — when schema changes, fixtures break
- Write new tests for every new requirement — no leverage from existing tests
- Debug failures by reading logs — no intelligent triage
- Decide what to test — coverage gaps are invisible unless you audit

**Effort to build:** ~2-4 weeks for Layer 1-2 covering existing 13 TCs. Months for full Items 4-10.

---

### 3. AI-Augmented Test Automation

Same Python + pytest foundation, but an LLM assists at every stage.

```
AI reads acceptance criteria from epic/story
  → AI generates test cases (including edge cases humans miss)
  → AI generates pytest code from AC + known schema
  → Human reviews and approves generated tests
  → Tests run same as traditional automation
  → On failure: AI reads logs + query results + schema
  → AI triages: "Row 47 failed because Term Date is NULL but Action=Terminate requires it"
  → AI suggests fix or flags as real defect vs test data issue
  → AI generates regression test from the bug
  → AI reviews coverage: "Items 4-10 have zero tests — here are the 23 tests needed"
```

**What AI adds at each phase:**

| Phase | Without AI | With AI |
|-------|-----------|---------|
| **Test design** | Tester reads AC, writes test cases manually | LLM reads AC + schema, generates test cases including boundary/negative cases. Human reviews. |
| **Test code** | Developer writes pytest from scratch | LLM generates pytest scaffolding from test case description. Human reviews + adjusts. |
| **Test data** | Tester creates .xlsx files manually | LLM generates synthetic test data matching column specs, edge cases, constraint violations. |
| **Failure triage** | Tester reads logs, runs queries, interprets | LLM reads failure output + schema, explains root cause in plain English. |
| **Coverage analysis** | Manual audit of TCs vs ACs vs epics | LLM maps existing tests to ACs, identifies gaps, suggests missing tests. |
| **Maintenance** | Schema change → find all broken tests, fix manually | LLM detects schema drift, suggests test updates. |
| **Regression from bugs** | Manual: "we should add a test for that" | LLM auto-generates regression test from bug description. |

**What AI does NOT replace:**
- Human judgment on whether a test result is a real defect
- Domain knowledge about business rules (30-day window, MDC grouping)
- Access decisions (who can query what)
- Final approval of generated tests before they run
- PHI/CUI handling — AI cannot see production data

**Effort to build:** ~1-2 weeks for Layer 1-2 (AI generates 60-70% of code, human reviews). Faster ramp for Items 4-10 because AI can read the epic and propose tests.

---

### Side-by-Side Summary

| Dimension | Manual | Traditional Automation | AI-Augmented |
|-----------|--------|----------------------|--------------|
| **Time per TC** | 30-60 min | 2-5 min | 2-5 min (same runtime) |
| **Regression cycle** | 2-3 days | 1-2 hours | 1-2 hours |
| **Time to create tests** | N/A (ad-hoc) | 2-4 weeks | 1-2 weeks |
| **Edge case coverage** | What tester thinks of | What developer codes | AI suggests + human approves |
| **Failure analysis** | Manual SQL + log reading | Read pytest output | AI explains in plain English |
| **Coverage gaps** | Invisible until audit | Invisible until audit | AI flags proactively |
| **Maintenance cost** | Low (no code) | High (code breaks) | Medium (AI assists fixes) |
| **Skill required** | SQL + domain knowledge | Python + SQL + pytest | Review + domain knowledge |
| **Runs unattended** | No | Yes | Yes |
| **PHI/CUI risk** | Tester sees real data | Scripts see real data | **Same as traditional** — AI sees code/schema, NOT data |

---

### The PHI/CUI Question

The AI-augmented approach has the **same PHI/CUI exposure as traditional automation** if designed correctly:

- **AI sees:** acceptance criteria, table schemas, column names, test code, error messages
- **AI never sees:** actual claim data, member IDs, PHI fields, production query results
- **Test data is synthetic** — generated from column specs, not copied from production

The risk surface is identical to traditional automation. The LLM is a code generation and triage tool, not a data access tool.

**However:** If the organization classifies table schemas or column names as CUI, that changes the calculus. This is the decision that needs to be made.

---

---

## Detailed Implementation (Layer by Layer)

Based on the 13 test cases across both active epics (exclusion file + mapping file).

## What We Know

| Attribute | Value |
|-----------|-------|
| DEV path | `S:\QNXTCOM_Claims_Readmission_Dev\Process` |
| TEST path | `S:\QNXTCOM_Claims_Readmission_Test\Process` |
| File format | .xlsx |
| File naming | Must start with `APR_DRG` or `MS_DRG` |
| Columns | Action, MS-DRG, MDC, MS-DRG Title, Effective Date, Term Date |
| Load job (APR) | `hmsa_com_imp_readmiss_apr_drg_to_mdc_load` |
| Validate jobs | `qst_validate_readmiss_apr_drg_to_mdc_load`, `pb_validate_readmiss_ms_drg_to_mdc_load`, `mcr_validate_readmiss_ms_drg_to_mdc_load` |
| Error SPs | `readmiss_apr_drg_to_mdc_error_rpt.sp`, `readmiss_ms_drg_to_mdc_error_rpt.sp` |
| Database | QNXT (SQL Server) |
| Target table | TBD |

---

## Layer 1: File Validation (Python — no environment needed)

These tests can run anywhere. They validate the .xlsx file before it ever touches the pipeline.

```python
# test_file_validation.py
import openpyxl
import os
import pytest

REQUIRED_COLUMNS = ["Action", "MS-DRG", "MDC", "MS-DRG Title", "Effective Date", "Term Date"]
VALID_ACTIONS = ["Add", "Update", "Terminate"]
VALID_PREFIXES = ["APR_DRG", "MS_DRG"]

class TestFileAvailability:
    """AC01 — File Availability & Readability"""

    def test_file_exists_at_path(self, file_path):
        """593613 step 1 / 593946 step 1"""
        assert os.path.exists(file_path), f"File not found at {file_path}"

    def test_file_is_xlsx(self, file_path):
        """593613 step 2 / 593946 step 4"""
        assert file_path.endswith(".xlsx"), f"Expected .xlsx, got {os.path.splitext(file_path)[1]}"

    def test_file_is_readable(self, file_path):
        """593946 step 3"""
        try:
            wb = openpyxl.load_workbook(file_path, read_only=True)
            wb.close()
        except Exception as e:
            pytest.fail(f"File is not readable: {e}")

    def test_file_naming_convention(self, file_path):
        """593613 step 2 — file should start with APR_DRG/MS_DRG"""
        filename = os.path.basename(file_path)
        assert any(filename.startswith(p) for p in VALID_PREFIXES), \
            f"Filename '{filename}' must start with APR_DRG or MS_DRG"

    def test_file_not_found_graceful(self, nonexistent_path):
        """593614 — negative test: file not found"""
        assert not os.path.exists(nonexistent_path)
        # Then trigger job and verify it logs "file not found" without crash
        # (requires job trigger — see Layer 2)


class TestFileStructure:
    """AC02 — File Structure & Data Validation"""

    def test_required_columns_present(self, file_path):
        """593741 — missing required column"""
        wb = openpyxl.load_workbook(file_path, read_only=True)
        ws = wb.active
        headers = [cell.value for cell in ws[1]]
        wb.close()
        missing = [col for col in REQUIRED_COLUMNS if col not in headers]
        assert not missing, f"Missing required columns: {missing}"

    def test_no_empty_required_fields(self, file_path):
        """AC02 acceptance criteria"""
        wb = openpyxl.load_workbook(file_path, read_only=True)
        ws = wb.active
        headers = [cell.value for cell in ws[1]]
        errors = []
        for row_num, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            for col_idx, col_name in enumerate(headers):
                if col_name in REQUIRED_COLUMNS and row[col_idx] is None:
                    errors.append(f"Row {row_num}, column '{col_name}' is empty")
        wb.close()
        assert not errors, f"Empty required fields:\n" + "\n".join(errors)

    def test_valid_action_values(self, file_path):
        """AC03 — action column should be Add/Update/Terminate"""
        wb = openpyxl.load_workbook(file_path, read_only=True)
        ws = wb.active
        headers = [cell.value for cell in ws[1]]
        action_idx = headers.index("Action")
        errors = []
        for row_num, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            if row[action_idx] not in VALID_ACTIONS:
                errors.append(f"Row {row_num}: invalid action '{row[action_idx]}'")
        wb.close()
        assert not errors, f"Invalid actions:\n" + "\n".join(errors)

    def test_date_format(self, file_path):
        """AC02 — dates should be valid"""
        from datetime import datetime
        wb = openpyxl.load_workbook(file_path, read_only=True)
        ws = wb.active
        headers = [cell.value for cell in ws[1]]
        date_cols = ["Effective Date", "Term Date"]
        errors = []
        for row_num, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            for col_name in date_cols:
                col_idx = headers.index(col_name)
                val = row[col_idx]
                if val is not None and not isinstance(val, datetime):
                    errors.append(f"Row {row_num}, '{col_name}': '{val}' is not a valid date")
        wb.close()
        assert not errors, f"Invalid dates:\n" + "\n".join(errors)

    def test_no_duplicate_keys(self, file_path):
        """AC02 — duplicate exclusion keys rejected"""
        wb = openpyxl.load_workbook(file_path, read_only=True)
        ws = wb.active
        headers = [cell.value for cell in ws[1]]
        drg_idx = headers.index("MS-DRG")
        eff_idx = headers.index("Effective Date")
        seen = set()
        dupes = []
        for row_num, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
            key = (row[drg_idx], row[eff_idx])
            if key in seen:
                dupes.append(f"Row {row_num}: duplicate key {key}")
            seen.add(key)
        wb.close()
        assert not dupes, f"Duplicate keys:\n" + "\n".join(dupes)
```

**What this covers:** 593613, 593614 (partial), 593741, 593946, 593947 (partial)
**What this doesn't need:** Database access, job execution, QNXT environment

---

## Layer 2: Job Execution & Database Validation (Python + SQL Server)

These tests trigger the actual job/stored procedure and validate results in the database.

```python
# test_job_processing.py
import pyodbc
import pytest
import shutil
import os

# Connection to QNXT test database
CONN_STRING = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=<<DEV_SERVER>>;DATABASE=<<DB>>;Trusted_Connection=yes"
DEV_PATH = r"S:\QNXTCOM_Claims_Readmission_Dev\Process"
ARCHIVE_PATH = r"<<Env_ARCHIVE_PATH>>"

# Job names per LOB
JOBS = {
    "apr_drg_load": "hmsa_com_imp_readmiss_apr_drg_to_mdc_load",
    "qst_validate_apr": "qst_validate_readmiss_apr_drg_to_mdc_load",
    "pb_validate_ms": "pb_validate_readmiss_ms_drg_to_mdc_load",
    "mcr_validate_ms": "mcr_validate_readmiss_ms_drg_to_mdc_load",
}

# Stored procedures
SPS = {
    "apr_drg_error_rpt": "readmiss_apr_drg_to_mdc_error_rpt",
    "ms_drg_error_rpt": "readmiss_ms_drg_to_mdc_error_rpt",
}


class TestInsertNewRecords:
    """AC03 — 593742: Insert new records with defaults"""

    def test_new_rows_inserted(self, db_conn, test_file_with_adds):
        """Place file with Status=Add rows, run job, verify inserts"""
        # 1. Place test file
        shutil.copy(test_file_with_adds, DEV_PATH)

        # 2. Trigger job (method TBD — Tidal API, command line, or SP call)
        # trigger_job(JOBS["apr_drg_load"])

        # 3. Verify rows in target table
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM <<TARGET_TABLE>>
            WHERE -- match on business keys from test file
        """)
        count = cursor.fetchone()[0]
        assert count > 0, "No new rows inserted"

    def test_defaults_applied_to_optional_blanks(self, db_conn, test_file_with_blanks):
        """593742 step 2 — optional fields blank, defaults should apply"""
        # Place file, run job
        # Then verify defaults were applied
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT <<OPTIONAL_COLUMN>> FROM <<TARGET_TABLE>>
            WHERE <<OPTIONAL_COLUMN_SOURCE>> IS NULL
            AND <<DEFAULT_VALUE_COLUMN>> IS NOT NULL
        """)
        rows = cursor.fetchall()
        for row in rows:
            assert row[0] is not None, "Default not applied to blank optional field"


class TestUpdateExistingRecords:
    """AC03 — update existing records using match/business keys"""

    def test_existing_record_updated(self, db_conn, test_file_with_updates):
        """File with Status=Update rows, verify existing records modified"""
        # 1. Record current state
        # 2. Place file, run job
        # 3. Verify records changed
        pass


class TestTerminateRecords:
    """AC03 — terminated records are end-dated"""

    def test_record_end_dated(self, db_conn, test_file_with_terminates):
        """File with Status=Terminate rows, verify end date set"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT term_date FROM <<TARGET_TABLE>>
            WHERE -- match terminated records
        """)
        rows = cursor.fetchall()
        for row in rows:
            assert row[0] is not None, "Terminated record not end-dated"


class TestReconciliation:
    """AC05 — 593744: Record count reconciliation"""

    def test_counts_balance(self, db_conn, test_file_mixed):
        """Total = Processed + Failed; Processed = Inserted + Updated + Terminated"""
        # After job runs, query the log/audit table
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT total_records, processed_records, failed_records,
                   inserted_count, updated_count, terminated_count
            FROM <<AUDIT_TABLE>>
            WHERE run_id = (SELECT MAX(run_id) FROM <<AUDIT_TABLE>>)
        """)
        row = cursor.fetchone()
        total, processed, failed, inserted, updated, terminated = row

        assert total == processed + failed, \
            f"Total ({total}) != Processed ({processed}) + Failed ({failed})"
        assert processed == inserted + updated + terminated, \
            f"Processed ({processed}) != Inserted ({inserted}) + Updated ({updated}) + Terminated ({terminated})"


class TestFailureLogging:
    """AC06 — 593745: Failure record content"""

    def test_failure_records_have_required_fields(self, db_conn, test_file_with_invalid_rows):
        """Each failure has: row identifier, error reason, timestamp, file/run id"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT row_identifier, error_reason, error_timestamp, run_id
            FROM <<FAILURE_TABLE>>
            WHERE run_id = (SELECT MAX(run_id) FROM <<FAILURE_TABLE>>)
        """)
        rows = cursor.fetchall()
        assert len(rows) > 0, "No failure records logged for invalid input"
        for row in rows:
            assert row[0] is not None, "Missing row identifier"
            assert row[1] is not None, "Missing error reason"
            assert row[2] is not None, "Missing timestamp"
            assert row[3] is not None, "Missing run id"


class TestFileNotFound:
    """AC01 — 593614: File not found scenario"""

    def test_job_handles_missing_file_gracefully(self, db_conn):
        """Ensure no file at path, trigger job, verify no crash"""
        # 1. Ensure no file at DEV_PATH
        for f in os.listdir(DEV_PATH):
            if f.startswith(("APR_DRG", "MS_DRG")):
                os.remove(os.path.join(DEV_PATH, f))

        # 2. Trigger job
        # trigger_job(JOBS["apr_drg_load"])

        # 3. Verify job logged "file not found" and exited cleanly
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT status, message FROM <<JOB_LOG_TABLE>>
            WHERE job_name = ? AND run_id = (SELECT MAX(run_id) FROM <<JOB_LOG_TABLE>>)
        """, JOBS["apr_drg_load"])
        row = cursor.fetchone()
        assert "file not found" in row[1].lower() or row[0] in ("no-op", "skipped"), \
            f"Job did not handle missing file gracefully: {row}"


class TestStoredProcValidation:
    """AC02 — 593740: Validate data via stored procedures"""

    def test_error_report_sp_runs(self, db_conn):
        """Run the error report SP and verify it processes without error"""
        cursor = db_conn.cursor()
        cursor.execute(f"EXEC {SPS['apr_drg_error_rpt']}")
        # Verify process status updated
        cursor.execute("""
            SELECT process_status FROM <<WORK_TABLE>>
            WHERE process_status IS NOT NULL
        """)
        rows = cursor.fetchall()
        assert len(rows) > 0, "SP did not update process status"
```

**What this covers:** 593614, 593740, 593742, 593744, 593745
**What this needs:** Database connection, job trigger mechanism, target table names

---

## Layer 3: Post-Processing Validation (Python — file system + email)

```python
# test_post_processing.py

class TestArchiving:
    """AC07 — 593747 / 593949: Archive on successful run"""

    def test_file_archived_after_success(self):
        """Verify file moved to archive with metadata"""
        archive_files = os.listdir(ARCHIVE_PATH)
        # Find most recent archive matching our test file
        matching = [f for f in archive_files if f.startswith(("APR_DRG", "MS_DRG"))]
        assert len(matching) > 0, "No archived file found"
        # Verify original name preserved with timestamp
        # Verify file size > 0

    def test_archive_log_entry(self, db_conn):
        """Verify archive log has name, size, datetime, checksum"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT file_name, file_size, archive_datetime, checksum
            FROM <<ARCHIVE_LOG_TABLE>>
            WHERE run_id = (SELECT MAX(run_id) FROM <<ARCHIVE_LOG_TABLE>>)
        """)
        row = cursor.fetchone()
        assert row[0] is not None, "Missing file name in archive log"
        assert row[1] > 0, "File size is 0"
        assert row[2] is not None, "Missing archive datetime"


class TestEmailNotification:
    """AC04 — 593743: Success email"""

    # Email testing options:
    # Option A: Check a shared mailbox via Exchange/Graph API
    # Option B: Check a log table that records sent emails
    # Option C: Use a test mail trap (if available)

    def test_success_email_sent(self, db_conn):
        """Verify email was sent with correct content"""
        # If email logging exists in DB:
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT subject, body, sent_to, sent_datetime
            FROM <<EMAIL_LOG_TABLE>>
            WHERE run_id = (SELECT MAX(run_id) FROM <<EMAIL_LOG_TABLE>>)
        """)
        row = cursor.fetchone()
        assert row is not None, "No email log entry found"
        assert "file name" in row[1].lower() or "processed" in row[1].lower(), \
            "Email body missing required content (file name, counts)"
```

---

## Layer 4: Selenium (QNXT UI Verification)

Only needed if you want to verify how the loaded data appears in QNXT to end users.

```python
# test_qnxt_ui.py
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestQNXTClaimsVerification:
    """Verify claim dispositions in QNXT UI after batch processing"""

    def test_claim_shows_denial_message(self, driver, denied_claim_id):
        """Item 1 — verify denial message displays correctly"""
        # Navigate to Claims Workbench
        driver.get("<<QNXT_URL>>/claims/search")
        # Search for claim
        driver.find_element(By.ID, "claimNumber").send_keys(denied_claim_id)
        driver.find_element(By.ID, "searchBtn").click()
        # Verify denial reason code and message
        denial_msg = driver.find_element(By.ID, "denialMessage").text
        assert denial_msg != "", "Denial message not displayed"

    def test_pended_claim_in_work_queue(self, driver, pended_claim_id):
        """Item 4 — verify pended claim routed to MM work queue"""
        # Navigate to Pend Management
        # Search for claim
        # Verify it's in the correct work queue
        pass
```

**Note:** Selenium tests are Layer 5 — most expensive, slowest feedback. Use only for UI-specific verification that can't be done at the database level.

---

## Test Data Strategy (based on Task 591498)

```
test_data/
├── mapping/
│   ├── MS_DRG_valid.xlsx              # Happy path — all valid rows
│   ├── MS_DRG_empty.xlsx              # Edge case — no data rows
│   ├── MS_DRG_missing_column.xlsx     # AC02 — missing required column
│   ├── MS_DRG_invalid_dates.xlsx      # AC02 — malformed dates
│   ├── MS_DRG_duplicate_keys.xlsx     # AC02 — duplicate business keys
│   ├── MS_DRG_mixed_actions.xlsx      # AC03 — Add + Update + Terminate rows
│   ├── MS_DRG_invalid_rows.xlsx       # AC06 — intentional bad data for failure logging
│   ├── APR_DRG_valid.xlsx             # Same set for APR DRG
│   └── APR_DRG_mixed_actions.xlsx
├── exclusion/
│   ├── MS_DRG_exclusion_valid.xlsx
│   ├── APR_DRG_exclusion_valid.xlsx
│   └── ...
└── conftest.py                        # pytest fixtures for file paths, DB connection
```

---

## What's Automatable Now vs What Needs Answers

| Test | Automatable Now? | Blocker |
|------|-----------------|---------|
| AC01 — File exists, format, naming | YES | None — pure file system |
| AC02 — Column validation, data rules | YES | None — pure file parsing |
| AC01 — File not found (593614) | PARTIAL | Need job trigger mechanism |
| AC02 — Happy path SP validation (593740) | PARTIAL | Need DB connection string + target table names |
| AC03 — Insert/Update/Terminate (593742) | PARTIAL | Need target table name + business key definition |
| AC04 — Success email (593743) | DEPENDS | Need email log table or mailbox API access |
| AC05 — Reconciliation (593744) | PARTIAL | Need audit/log table name |
| AC06 — Failure logging (593745) | PARTIAL | Need failure table name |
| AC07 — Archive (593747/593949) | PARTIAL | Need archive path per environment |
| Selenium — QNXT UI | LATER | Need QNXT URL, page object model, test claims |

---

---

## Coverage Beyond Test Cases — Full Epic Scope

The 13 test cases only cover the file load pipeline (Items 2, 3 from system design). The full epic has 10 items and 11 epics. Here's what's NOT covered by existing test cases but IS in scope.

### From System Design Items 4 & 5 — Pend/Deny Logic (Core Business Rules)

```python
# test_pend_deny_logic.py
"""
These are the highest-value tests in the entire project.
They validate the REASON this system exists.
"""

class TestPendLogic:
    """Epic 590778 (MCR), 590789 (PB), 590784 (QUEST)
    Item 4: Pend inpatient/acute readmission with same MDC within 30 days"""

    def test_same_mdc_within_30_days_is_pended(self, db_conn):
        """Core rule: readmission with same MDC within 30 days → pend"""
        # Setup: two claims for same member, same MDC, 15 days apart
        # Run batch
        # Assert: second claim status = pended
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT claim_status FROM <<CLAIMS_TABLE>>
            WHERE claim_id = ? -- readmission claim
        """, readmission_claim_id)
        assert cursor.fetchone()[0] == "PENDED"

    def test_same_mdc_at_day_30_boundary(self, db_conn):
        """Boundary: exactly 30 days — should this pend or not?"""
        pass

    def test_same_mdc_at_day_31_not_pended(self, db_conn):
        """Outside window: 31 days apart → should NOT pend"""
        pass

    def test_different_mdc_not_pended(self, db_conn):
        """Different MDC → should NOT be pended (even within 30 days)"""
        pass

    def test_pend_routes_to_mm_work_queue(self, db_conn):
        """Pended claim should appear in Medical Management work queue"""
        pass


class TestDenyLogic:
    """Epic 590772 (MCR), 590794 (PB), 590781 (QUEST)
    Item 5: Auto-deny excluded readmission with same DRG within 30 days"""

    def test_excluded_same_drg_within_30_days_denied(self, db_conn):
        """Core rule: excluded from clinical review + same DRG within 30 days → auto-deny"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT claim_status, denial_reason_code FROM <<CLAIMS_TABLE>>
            WHERE claim_id = ?
        """, readmission_claim_id)
        row = cursor.fetchone()
        assert row[0] == "DENIED"
        assert row[1] is not None, "Missing denial reason code"

    def test_non_excluded_same_drg_not_denied(self, db_conn):
        """Same DRG but NOT in exclusion list → should pend, not deny"""
        pass

    def test_excluded_different_drg_not_denied(self, db_conn):
        """In exclusion list but different DRG → not denied"""
        pass

    def test_denial_message_correct(self, db_conn):
        """Item 1: Verify denial reason code maps to correct HIPAA message"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT denial_reason_code, denial_message
            FROM <<CLAIMS_TABLE>> c
            JOIN <<DENIAL_CONFIG_TABLE>> d ON c.denial_reason_code = d.reason_code
            WHERE c.claim_id = ?
        """, denied_claim_id)
        row = cursor.fetchone()
        assert row[1] is not None, "No denial message mapped"


class TestExclusionRules:
    """Epic 590584 — Exclusion criteria applied correctly"""

    def test_cancer_drg_excluded_from_deny(self, db_conn):
        """Cancer DRG should be excluded → pend, not auto-deny"""
        pass

    def test_trauma_drg_excluded(self, db_conn):
        pass

    def test_pregnancy_drg_excluded(self, db_conn):
        pass

    def test_neonatal_drg_excluded(self, db_conn):
        pass

    def test_bh_ip_excluded(self, db_conn):
        """Behavioral health inpatient excluded"""
        pass

    def test_discharge_status_07_excluded(self, db_conn):
        """Left AMA / discontinued care → excluded from auto-deny"""
        pass

    def test_discharge_status_20_excluded(self, db_conn):
        """Expired → excluded"""
        pass

    def test_discharge_status_30_excluded(self, db_conn):
        """Still a patient → excluded"""
        pass


class TestDRGGrouper:
    """Verify correct DRG grouper used per LOB"""

    def test_mcr_uses_micro_dyn(self, db_conn):
        """MCR claims use Micro-Dyn / DRG Active"""
        pass

    def test_pb_uses_micro_dyn(self, db_conn):
        """PB claims use Micro-Dyn / DRG Active"""
        pass

    def test_qst_uses_3m(self, db_conn):
        """QST claims use 3M product"""
        pass
```

### From System Design Items 6 & 8 — QNXT ↔ Aerial Integration

```python
# test_aerial_integration.py
"""
Item 6: QNXT → Aerial (pended claims sent for MM review)
Item 8: Aerial → QNXT (disposition comes back)
"""

class TestQNXTToAerial:
    """Epic not yet created — Item 6"""

    def test_pended_claim_sent_to_aerial(self):
        """After batch, pended claims appear in Aerial as case/request"""
        # If MuleSoft: test API call was made with correct payload
        # If ETL: verify SAS output file generated, XML created, SFTP'd
        pass

    def test_c_code_assigned_to_pended_claim(self, db_conn):
        """C code memo attached to claim for Aerial routing"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT memo_text FROM <<CLAIM_MEMO_TABLE>>
            WHERE claim_id = ? AND memo_type = 'C'
        """, pended_claim_id)
        assert cursor.fetchone() is not None, "No C code memo on pended claim"

    def test_claim_order_preserved(self):
        """Item 8 requirement: claim order must match original QNXT order"""
        pass


class TestAerialToQNXT:
    """Item 8 — disposition flows back"""

    def test_disposition_loaded_as_claim_memo(self, db_conn):
        """Aerial Pay/Deny disposition appears as claim memo in QNXT"""
        pass

    def test_disposition_format_parseable(self):
        """Item 9 flag: MM response report format must be programmatically parseable"""
        pass
```

### From System Design Item 10 — Cotiviti Routing

```python
# test_cotiviti_routing.py

class TestCotivitiRouting:
    """Epic 590574 area — Item 10"""

    def test_paid_claims_sent_to_cotiviti(self, db_conn):
        """Claims released to Pay should be in Cotiviti feed"""
        pass

    def test_pended_claims_excluded_from_cotiviti(self, db_conn):
        """Pended claims should NOT be sent to Cotiviti"""
        cursor = db_conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM <<COTIVITI_FEED_TABLE>>
            WHERE claim_id IN (
                SELECT claim_id FROM <<CLAIMS_TABLE>> WHERE claim_status = 'PENDED'
            )
        """)
        assert cursor.fetchone()[0] == 0, "Pended claims found in Cotiviti feed"

    def test_denied_claims_excluded_from_cotiviti(self, db_conn):
        """Denied claims should NOT be sent to Cotiviti"""
        pass
```

### From Epics Not Yet Active — Cross-LOB Validation

```python
# test_cross_lob.py

class TestCrossLOB:
    """Verify pend/deny logic works consistently across all 3 LOBs"""

    @pytest.mark.parametrize("lob", ["MCR", "PB", "QST"])
    def test_pend_logic_per_lob(self, db_conn, lob):
        """Same test, all 3 LOBs — same MDC within 30 days → pend"""
        pass

    @pytest.mark.parametrize("lob", ["MCR", "PB", "QST"])
    def test_deny_logic_per_lob(self, db_conn, lob):
        """Same test, all 3 LOBs — excluded + same DRG within 30 days → deny"""
        pass

    def test_post_mass_applied_all_lobs(self, db_conn):
        """System design requirement: Post Mass implemented for all LOBs"""
        pass
```

---

## Full Test Coverage Map

| System Design Item | Epic(s) | Existing TCs | Automated Tests Needed |
|-------------------|---------|-------------|----------------------|
| 1. Denial message config | — | 0 | Denial code → HIPAA message mapping |
| 2. DRG/MDC mapping load | 591204 | 9 | File validation + DB load verification |
| 3. DRG exclusion load | 590584 | 4 | File validation + DB load verification |
| 4. Claims Processing: Pend | 590778, 590789, 590784 | 0 | Same MDC within 30 days → pend (per LOB) |
| 5. Claims Processing: Deny | 590772, 590794, 590781 | 0 | Excluded + same DRG → deny (per LOB) |
| 6. QNXT → Aerial | — | 0 | C code assignment, data transfer |
| 7. MM Clinical Review | — | 0 | Manual (Medecision SaaS) |
| 8. Aerial → QNXT | — | 0 | Disposition memo, claim ordering |
| 9. Claims Pay/Deny | — | 0 | Disposition format, examiner action |
| 10. Cotiviti routing | — | 0 | Paid → Cotiviti, pend/deny excluded |
| — Exclusion rules | 590584 | 0 | Cancer/trauma/pregnancy/BH/discharge status exclusions |
| — Cross-LOB consistency | All LOB epics | 0 | Same logic across MCR, PB, QST |
| — Cost savings | 595588 | 0 | TBD |

**Current test coverage: Items 2 & 3 only (file load pipeline). Items 4-10 have zero test cases.**

## Immediate Next Steps

1. **Start with Layer 1 (file validation)** — zero blockers, can build and run today
2. **Get these from the dev team to unblock Layer 2:**
   - DB connection string for DEV
   - Target table name(s) for DRG/MDC mappings
   - Audit/log table name
   - Failure table name
   - Archive path for DEV
   - How to trigger a job on-demand (Tidal CLI? SP call? Manual?)
3. **PHI/CUI decision** — determines if test data can be synthetic or must use controlled data
