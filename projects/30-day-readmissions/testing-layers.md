# Testing Layers — 30-Day Readmissions

Living document. Updated as each phase reveals new layers, shift-left opportunities, and coverage gaps. See `qa-process.md` for the framework behind this.

---

## How to Read This

Each phase has its own section with three things: the testing layers that apply to that phase, what shift-left looks like for each layer, and current coverage status. As you move through phases, add new sections. Some layers from earlier phases may reappear — that's expected.

---

## Phase 1 — File Load Pipeline (Items 2 & 3)

### What This Phase Tests

Loading DRG/MDC mapping files and exclusion files into the database via Tidal/SSIS/SP. The foundation that all downstream pend/deny decisions depend on.

### Layers

| Layer | What It Tests | Shift-Left Opportunity | Coverage |
|-------|--------------|----------------------|----------|
| 1. File processing | Pipeline works end-to-end: place file, Tidal triggers, SSIS loads, SP validates, data in DB, email sent, file archived | Validate file structure before placing it on S: drive. Catch bad files before they enter the pipeline. | 19 repo TCs. 11 confirmed gaps. |
| 2. File content | Column names, data types, value ranges, required fields in the .xlsx file itself | Inspect the file before it hits Tidal. A 30-second check prevents a 30-minute failed job + cleanup. | No TCs exist. Blocked on column spec documentation. |
| 3. Data integrity | After the job runs: correct rows inserted/updated/terminated, no orphans, no duplicates, business keys unique, counts match source file | Pre-calculate expected DB state from the input file before running the job. Compare actual vs expected after. | No TCs exist. Blocked on table access. |
| 4. Cross-file consistency | Every DRG in the exclusion file exists in the mapping table. Orphaned exclusions break downstream pend/deny logic. | Cross-reference exclusion file against mapping file before loading either. Catch orphans at the file level, not after two separate jobs have run. | No TCs exist. New category. |

### Dev Overlap (TBD)

What does the SP already validate? What does the SSIS package reject? Need to review before writing Layer 2-3 TCs. The answer determines whether these layers need 5 TCs or 25.

---

## Phase 2 — Pend/Deny Logic (Items 4 & 5)

### What This Phase Will Test

Batch stored procedures that evaluate inpatient claims against the mapping and exclusion data loaded in Phase 1. Same MDC within 30 days → pend for review. Same DRG + on exclusion list → auto-deny.

### Layers (anticipated — update when phase starts)

| Layer | What It Tests | Shift-Left Opportunity | Coverage |
|-------|--------------|----------------------|----------|
| 1. Decision logic | Given a claim with DRG X, does the SP correctly pend or deny based on mapping/exclusion data? | Validate decision rules as a truth table on paper before running claims through the SP. Desk-check every combination of: same/different DRG, same/different MDC, on/off exclusion list, within/outside 30 days, same/different facility. | TBD |
| 2. Boundary conditions | 30-day window edge cases: day 0, day 30, day 31. Same facility with different provider IDs. DRGs that map to same MDC vs different MDC. | Build a decision matrix before writing TCs. Map every boundary. | TBD |
| 3. Exclusion categories | Cancer, trauma, pregnancy, delivery, neonatal, BH IP, discharge status 07/20/30 — are these correctly excluded from denial? | Review the exclusion list against known DRG codes for each category before testing. Verify the list is complete. | TBD |
| 4. LOB differences | Same claim, different LOB → different DRG grouper → potentially different decision. Does the SP handle MCR, PB, and QST correctly? | Run the same test scenario through all 3 LOBs on paper first. Predict the outcome before the SP runs. | TBD |
| 5. Data dependency | Does the pend/deny logic produce correct results with the data loaded in Phase 1? If Phase 1 data is wrong, every decision here is wrong. | Verify Phase 1 data integrity BEFORE running Phase 2 tests. Don't assume it's correct because Phase 1 "passed." | TBD |

---

## Phase 3 — QNXT to Aerial Integration (Item 6)

### What This Phase Will Test

Pended claims collected from QNXT (MCR, PB, QST) and loaded into Aerial/Medecision as cases for Medical Management clinical review. Either via existing ETL (SAS/MapForce/SFTP) or MuleSoft API.

### Layers (anticipated — update when phase starts)

| Layer | What It Tests | Shift-Left Opportunity | Coverage |
|-------|--------------|----------------------|----------|
| 1. Data extraction | Are the right pended claims selected from QNXT? No missed claims, no extra claims. | Query the QNXT pend queue directly and compare against what the integration sends. Catch selection errors before they reach Aerial. | TBD |
| 2. Data transformation | Is the claim data transformed correctly into Aerial's expected format? Field mapping, data types, required fields. | Validate the payload/XML against Aerial's schema before sending. Catch format errors without hitting the SaaS system. | TBD |
| 3. Delivery confirmation | Did Aerial receive and acknowledge the cases? Error handling if Aerial is down or rejects. | Test with known-good payloads first, then introduce errors. Validate error handling without corrupting real cases. | TBD |
| 4. Claim ordering | "Claim order must match the same order as originally sourced from QNXT." Is ordering preserved? | Compare source order in QNXT to delivered order in Aerial. Catch ordering issues before clinical reviewers see mismatched cases. | TBD |

---

## Phase 4 — Aerial to QNXT Integration (Item 8)

### What This Phase Will Test

Clinical review dispositions (pay/deny) loaded back from Aerial into QNXT as claim memos for Claims Examiners to act on.

### Layers (anticipated — update when phase starts)

| Layer | What It Tests | Shift-Left Opportunity | Coverage |
|-------|--------------|----------------------|----------|
| 1. Disposition accuracy | Does the pay/deny decision from Aerial match what the reviewer actually entered? | Compare Aerial's disposition data directly against what lands in QNXT. Catch mapping errors before examiners act on wrong dispositions. | TBD |
| 2. Format compatibility | "Data from Aerial must be in a structured format consumable by QNXT." Is it? | Validate the response format against QNXT's expected schema before loading. Catch format mismatches before they break the import. | TBD |
| 3. Claim ordering | Same ordering requirement as Phase 3 but in reverse. | Same approach — compare source vs destination order. | TBD |
| 4. Round-trip integrity | Claim goes QNXT → Aerial → QNXT. Is the claim the same claim? No data loss, no corruption, no mismatched IDs. | Track a claim's full journey and verify every field at each stage. Catch drift early. | TBD |

---

## Phase 5 — Cotiviti Routing (Item 10)

### What This Phase Will Test

Claims released to Pay continue to Cotiviti. Claims pended for review or denied do NOT go to Cotiviti. After go-live, Cotiviti turns off their 30-day readmission process.

### Layers (anticipated — update when phase starts)

| Layer | What It Tests | Shift-Left Opportunity | Coverage |
|-------|--------------|----------------------|----------|
| 1. Routing rules | Pay → Cotiviti. Pend/Deny → NOT to Cotiviti. Is the routing correct? | Validate routing logic as a truth table before running claims. Every claim status should map to exactly one destination. | TBD |
| 2. No-send verification | Pended and denied claims must NOT appear in the Cotiviti feed. Negative testing. | Pre-filter the Cotiviti feed against the pend/deny list before it goes out. Catch leaks before they reach the vendor. | TBD |
| 3. Cutover | After Cotiviti turns off their readmission process, are those claims now caught by the in-house system? No gap in coverage during transition. | Run parallel processing before cutover — both systems active, compare results. Catch any claims one system catches that the other misses. | TBD |

---

## Cross-Phase Layers

Some testing layers span multiple phases and should be tracked separately.

| Layer | What It Tests | Phases Affected |
|-------|--------------|----------------|
| End-to-end flow | A claim enters the system and goes through every phase correctly — from file load through pend/deny through clinical review through final disposition through Cotiviti routing. | All |
| Data lineage | Can you trace a single claim's journey through every system (QNXT, Aerial, Cotiviti) and verify nothing was lost or corrupted? | 3, 4, 5 |
| Regression | When Phase N changes something, does Phase N-1 still work? | All (cumulative) |
| Performance / volume | Does the system handle production-scale volumes? Nightly batch with thousands of claims, not just 5 test rows. | 2, 3, 4, 5 |

---

## How This Document Grows

When you start a new phase:

1. Read the anticipated layers above
2. Update them based on what you actually find (requirements, system design, dev conversations)
3. Add shift-left opportunities as you discover them
4. Update coverage status as TCs are written and executed
5. Add new layers that weren't anticipated

The anticipated sections are starting points, not predictions. Reality will differ.
