# Test Cases — Exclusion File (590587 / 590589)

All 4 test cases apply to both MS DRG (590587) and APR DRG (590589) exclusion file processing.
All are currently **Design** state, **Not Automated**, Priority 2.

---

## 593946 — AC01-001 Exclude File: Validate file exists and is accessible and File format

**Scenario:** Verify the exclusion file exists at the configured path and is in the correct format.

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Place a valid .xlsx file at <<PATH>> | File is visible and opens without error |
| 2 | Navigate to <<PATH>> | |
| 3 | Confirm file presence and open it (read-only) | |
| 4 | File format | File format should be *.xlsx |

---

## 593947 — AC02-001 Exclude File: Validation of exception file processing

**Scenario:** Validate row-level content, business rules, and data load.

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Place a valid .xlsx file at <<PATH>> | File is visible and opens without error |
| 2 | Run <JOB_NAME> | New rows inserted; defaults applied to optional blanks; insert count increments; logs show detail |

---

## 593948 — AC03-001 Exclude File: Failure summary/report availability

**Scenario:** Verify failure summary dashboard/report is available and filterable.

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Access failure summary dashboard/report | Summary shows counts by reason, links to records; suitable for business review |
| 2 | Filter by run id/date | |

---

## 593949 — AC04-001 Exclude File: Archive on successful run

**Scenario:** Verify file is archived after successful processing.

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute successful run in DEV | File present in archive with original name + timestamp/metadata; logs show name, size, archive datetime, checksum (if enabled) |
| 2 | Check <<Env_ARCHIVE_PATH>> and logs | |

---

## Observations

1. **File format is .xlsx** — this is confirmed in TC 593946 step 4. Answers one of our discovery questions.
2. **All test cases are manual** — Automation status: Not Automated on all 4.
3. **Parameterized** — PATH, JOB_NAME, Env_ARCHIVE_PATH are all placeholders. Need actual values from the dev/test environment.
4. **Gap: No negative test cases** — what happens when:
   - File is wrong format (CSV instead of xlsx)?
   - File has corrupt data?
   - File is empty?
   - File has duplicate exclusion keys?
   - File path doesn't exist or access is denied?
   These are in the acceptance criteria (AC01 on story 590587) but not in the test cases yet.
5. **Gap: AC03 from the stories (job processes and updates existing data)** — add new, update existing, terminate/end date — is not fully covered by any test case. TC 593947 covers inserts but not updates or end-dating.
6. **Gap: No test for the actual exclusion logic** — these tests verify the file load pipeline, not whether the loaded exclusions correctly prevent claims from being auto-denied. That would be tested at the stored procedure level (Layer 2 in our shift-left model).
