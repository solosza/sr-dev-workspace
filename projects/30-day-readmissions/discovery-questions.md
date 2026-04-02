# Discovery Questions — 30-Day Readmissions

Questions to ask before finalizing the test automation approach. Grouped by who to ask.

---

## For the Business Analyst (DRG/MDC Mapping Owner)

1. What file format are the DRG-to-MDC mapping files? (CSV, Excel, fixed-width, other?)
2. What file format are the DRG/APR DRG exclusion files?
3. Where exactly are these files dropped for Tidal to pick up? (network share path, SFTP location?)
4. Is there a file naming convention or versioning scheme?
5. How many rows are typically in a mapping file? An exclusion file?
6. Is there a known-good reference file we can use as a baseline for validation?
7. When the annual update happens, is it a full replacement or a delta/incremental update?
8. Who validates the files today before they get loaded? Is there any manual review step?

---

## For the Database / SQL Team

1. What are the names of the custom tables that store the DRG/MDC mappings and exclusions?
2. What are the stored procedure names for the pend logic (Item 4) and deny logic (Item 5)?
3. Can we get the stored procedure source code, or is it in a source control repo we can access?
4. Is there a test/dev QNXT database we can run queries and stored procedures against without affecting other teams?
5. Can we create and insert synthetic test claims into the dev database, or do we need to go through a specific process?
6. What does the claim data model look like for readmission matching? (which tables, which join keys — member ID, admit/discharge dates, DRG, MDC?)
7. How does the 30-day window get calculated? Is it from discharge date of the original claim to admit date of the readmission?
8. What does Post Mass do, and how do we verify it ran correctly for all LOBs?

---

## For the DBA / Environment Admin

1. What test/dev environments exist for QNXT? (names, connection strings, refresh schedule)
2. How often is the test database refreshed from production? Do we lose test data on refresh?
3. Do we have write access to the test database, or read-only?
4. Can we execute stored procedures in the test environment, or do we need elevated permissions?
5. Is there a separate sandbox where we can insert test claims without interfering with other testers?
6. Are there any restrictions on running automated queries against the test database? (rate limits, approval needed, VPN required?)

---

## For the Integration / MuleSoft Team

1. Which option was selected for QNXT-to-Aerial integration — existing ETL (SAS/MapForce/SFTP) or MuleSoft?
2. Which option was selected for Aerial-to-QNXT integration — existing ETL or MuleSoft?
3. If MuleSoft: are there API contracts/Swagger specs we can test against?
4. If MuleSoft: is there a sandbox/mock environment for the APIs?
5. If existing ETL: what does the XML schema look like for the Aerial import?
6. If existing ETL: can we access the SAS job output and MapForce transformation logs in the test environment?
7. How is the C code assigned to pended claims? Is it configurable per readmission type?
8. What does the SFTP handoff look like — file naming, polling interval, error handling?

---

## For the Aerial / Medecision Admin

1. Is there a test/sandbox Aerial environment we can use?
2. Can we create test cases/requests in the sandbox via API, or only through the UI?
3. What does the disposition data look like when it comes back from Aerial? (format, fields, structure)
4. The system design notes the MM response report "is not in a proper format that can be programmatically implemented" — what format is it in today, and what format does QNXT need?
5. How does claim ordering get preserved between QNXT and Aerial?
6. Is there an Aerial API we can call to verify a case was created correctly?

---

## For the Cotiviti Team

1. How do claims get sent to Cotiviti today? (SFTP, API, batch file?)
2. What file format does Cotiviti expect?
3. How do we verify that pended/denied claims were correctly excluded from the Cotiviti feed?
4. After implementation, how does Cotiviti turn off their 30-day readmission process on their end? Is that coordinated with us or independent?
5. Is there a test/sandbox environment for the Cotiviti integration?

---

## For the Compliance / Security Team

1. What is the data classification for claims data in the test environment? (PHI, CUI, de-identified, synthetic?)
2. Can we use synthetic/fake member data for automated testing, or must we use production-like data?
3. If we use synthetic data, are there requirements for how it's generated? (must look realistic, must use specific ID ranges, etc.)
4. Can an LLM (like Claude, GPT) be used to generate synthetic test data or evaluate test results? Any restrictions on sending claims data — even synthetic — to an external AI service?
5. Can we run automated test scripts against the test environment, or does that require a security review / approval?
6. Are there any audit logging requirements for automated test activity in QNXT?

---

## For the Tidal / Job Scheduling Team

1. What are the Tidal job names for the readmission batch processing (pend and deny)?
2. What time does the nightly batch run in the test environment?
3. Can we trigger a batch run on-demand in the test environment, or do we have to wait for the scheduled time?
4. How do we monitor batch job status and check for failures?
5. What job stream will the new readmission process be added to (Item 10)?
6. What are the job dependencies — what runs before and after the readmission jobs?

---

## Priority Order

Get answers to these first — they unblock everything else:

1. **Security/Compliance** — PHI/CUI constraints determine whether we can use AI tooling at all
2. **DBA/Environment** — test database access determines whether L1/L2 automation is feasible
3. **BA** — file formats determine L1 (data validation) approach
4. **Database/SQL** — stored proc access determines L2 (logic validation) approach
5. **Integration** — MuleSoft vs ETL decision determines L3 approach
6. **Tidal** — on-demand batch capability determines L4 approach
7. **Aerial/Cotiviti** — sandbox access determines L3/L5 scope
