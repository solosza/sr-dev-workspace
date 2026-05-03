# Phase 2 Execution Plan — Auto-Deny Claims Processing

Items 1 & 5: Denial Message Configuration + Claims Processing: Deny

Epic 590794 — PB: Auto-deny inpatient and readmission claim

---

## What I Need to Know

### 1. What's CLEAR (confirmed, no ambiguity)

**The deny decision:**
- Same member (exact member ID)
- Same facility (exact provider ID)
- Same DRG (exact MS-DRG code)
- Second admit within 30 days of first discharge (0-30 days = true, ≥31 = false)
- DRG is NOT on the exclusion list
- All five must be true → **auto-deny the second claim**
- Any one is false → **no action**

**What gets excluded from auto-deny (claim pays normally):**
- DRG on the exclusion file (cancer, trauma, pregnancy, etc.)
- Discharge status codes: 07 (left AMA), 20 (expired), 30 (still patient)
- FEP claims — separate LOB entirely (not PB), identified by "R" prefix on member ID
- BC Home claims — not a separate LOB, it's a BlueCard claim routing type (HMSA member treated out of state, Host Plan priced it, HMSA adjudicates as Home Plan). Excluded because it follows BlueCard rules, not HMSA local rules.
- Med COB claims — not a separate LOB, it's a processing designation within PB. Member has both Medicare (primary) and HMSA PB coverage. Excluded because Medicare already made the readmission decision as primary payer.
- Dual-member secondary claims
- BlueCard Host claims (future phase — not in April 30th release)

**How the SP filters each exclusion (3 different mechanisms):**

| Exclusion | Type | How SP Filters |
|-----------|------|---------------|
| FEP | Different LOB | LOB code or member ID prefix ("R") |
| BC Home | Claim routing type | BlueCard source indicator flag |
| Med COB | Payer coordination | COB indicator / primary payer field |
| Discharge codes | Claim attribute | Discharge status code on claim |
| DRG exclusion | Reference data | Lookup against exclusion table (Phase 1) |
| Dual secondary | Claim attribute | Secondary claim indicator |
| BlueCard Host | Claim routing type | BlueCard host flag (future phase) |

**When a claim is denied:**
- Denial reason attached: "NO PAYMENT CAN BE MADE. THIS CLAIM IS FOR READMISSION AND IS NOT ON THE LIST OF ELIGIBLE DRGS THAT ARE PAYABLE FOR READMISSION."
- Claim status updated
- Audit trail logged
- Claim NOT sent to Cotiviti

**How it runs:**
- Nightly batch job (but we can trigger on demand in test)
- Tidal triggers the stored procedure
- SP reads claims from QNXT, checks against mapping + exclusion tables (Phase 1 data)
- First claim always pays. Only the second (readmission) claim gets denied.

### 2. What's UNCLEAR (need answers before testing)

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | **DRG only, or DRG + MDC?** The ACs and truth table use DRG only. But the business rules section says "compare MDC categories" after DRG match. Which is it? | Changes what we test — if MDC matters, we need scenarios where DRG matches but MDC doesn't |
| 2 | **What status is the first claim?** Story says "history claims in PAID status not subsequently adjusted" but also asks "what if first claim is in PEND or DENY?" | Determines which claims the SP even looks at |
| 3 | **What status is the second claim?** TBD — PAY or PEND? | Need to know what the SP is scanning for |
| 4 | **How to identify inpatient/acute?** Type of Bill = 11, 13? | Need this to set up test claims correctly |
| 5 | **Effective dates on DRG codes** — compared against claim admit/discharge dates? | Could mean a DRG match is valid in January but not in June |
| 6 | **Effective dates on exclusion file** — same question | An excluded DRG might only be excluded during certain date ranges |
| 7 | **Does the SP check both DRG code list AND exclusion list?** | Need to know the order of operations |
| 8 | **What if a claim has no DRG?** | Edge case — does the SP skip it or error? |
| 9 | **Multiple admits within 30 days — does the clock reset?** | Claim 1 → Claim 2 (day 10) → Claim 3 (day 20 from Claim 2). Is Claim 3 compared to Claim 1 or Claim 2? |
| 10 | **Discharge status logic** — 3 scenarios defined but no formal ACs yet | Can't write TCs without acceptance criteria |
| 11 | **Dual coverage** — secondary follows primary disposition, but how exactly? | No ACs defined yet |
| 12 | **What tables do claims live in?** Table name, key columns for claim ID, member ID, provider ID, DRG, dates, status, denial reason | Need this to write before/after queries and to know where to insert test data |
| 13 | **Do we have insert access in the test environment?** Can we create our own test claims, or do we work with existing data only? | Determines whether we control test scenarios precisely or hunt for matches |
| 14 | **What data is already seeded in the test environment?** What PB inpatient claims exist, and is anyone else using this env? | Need to know baseline before running the SP, and avoid stepping on other testers |

### 3. What I Can TEST Now (mapped to clear items only)

| Test | What It Proves | Based On |
|------|---------------|----------|
| Same member + facility + DRG + ≤30 days + not excluded → denied | Core happy path works | AC01, AC04 |
| Same everything but DRG on exclusion list → no action | Exclusion file protects correctly | AC03 |
| Same everything but 31 days apart → no action | Boundary is correct | AC06 |
| First claim pays, second denied (with amounts) | Only readmission is denied | AC05 |
| Different provider, same DRG → still denied | Cross-provider detection works | AC02 |
| FEP claim matching all criteria → no action | SP filters out non-PB LOB | Exclusion rules (LOB filter) |
| BC Home claim matching all criteria → no action | SP filters out BlueCard routing | Exclusion rules (source flag) |
| Med COB claim matching all criteria → no action | SP filters out secondary-to-Medicare | Exclusion rules (COB indicator) |
| Dual secondary claim → no action | SP filters out dual secondary claims | Exclusion rules (claim attribute) |
| Discharge status 07/20/30 → no action | Discharge code exclusion works | 595151 scenarios |

**Can't test yet (blocked on unclear items):**
- MDC comparison scenarios (question 1)
- First claim in PEND/DENY status (question 2)
- Claims with no DRG (question 8)
- Multiple readmissions / clock reset (question 9)
- Dual coverage follow-primary logic (question 11)

---

## Where I Am (QA Process Steps)

| Step | What | Status |
|------|------|--------|
| 1. Business context | Why auto-deny exists, financial impact, 3 paths | ✅ Done |
| 2. System design | Batch flow: Tidal → SP → QNXT, depends on Phase 1 data | ✅ Done |
| 3. Requirements | 4 features, 4 child stories, 591508 has 6 ACs, 8 open questions | In progress |
| 4. Existing coverage | No test cases exist yet for Phase 2 | Not started |
| 5. Testing layers | Identified below | In progress |
| 6. Shift-left analysis | Not started | Not started |
| 7. Gap analysis | Not started — need requirements finalized first | Not started |
| 8. Dev overlap check | Not started — need SP code walkthrough | Not started |
| 9. Ownership & process | SIT/UAT question pending | Not started |
| 10. Environment access | Same as Phase 1 — S: drive, SSMS, Tidal | In progress |

---

## Business Context — Why Auto-Deny Exists

HMSA loses $7.7M annually on readmission claims that should be denied. When a PB member gets discharged and readmitted within 30 days to the same facility for the same DRG, the second admission is likely the same problem that wasn't resolved the first time. Today that second claim pays out. This epic makes the system automatically deny it.

The exclusion file (loaded in Phase 1) protects DRGs where readmission is expected — cancer, trauma, pregnancy, delivery, neonatal, behavioral health. Those claims are excluded from auto-deny and process normally.

```
Mental Map — What Auto-Deny Does

  Claim comes in (PB inpatient/acute)
    │
    Is there a prior claim?
    Same member + same facility?
      No → process normally
      Yes ↓
    │
    Is the admit date within 30 days of prior discharge?
      No → process normally
      Yes ↓
    │
    Is the DRG the same?
      No → process normally
      Yes ↓
    │
    Is the DRG on the exclusion file?
      Yes → process normally (protected)
      No ↓
    │
    Is it within the effective date range?
      No → process normally
      Yes ↓
    │
    AUTO-DENY
      → Denial reason attached
      → Audit trail logged
      → Claim NOT sent to Cotiviti
```

---

## System Design — How It Works

### Method

Batch → Tidal → Stored Procedure → Custom Table (Item 5 from system design doc)

This is a **nightly batch job**, not real-time. Tidal triggers the SP, the SP reads claims from the QNXT database, evaluates them against the mapping and exclusion tables (loaded in Phase 1), and auto-denies qualifying claims.

### Dependencies

| Dependency | What | Phase |
|-----------|------|-------|
| Item 1 — Denial message config | Denial reason codes and messages must be configured | Phase 2 prerequisite |
| Item 2 — DRG/MDC mapping data | Mapping tables must be populated | Phase 1 (done) |
| Item 3 — Exclusion data | Exclusion tables must be populated | Phase 1 (done) |

### System Flow

```
Mental Map — Phase 2 in the Full Pipeline

  Phase 1 (completed):
    Mapping .xlsx → Tidal → SSIS → Custom Table (DRG-to-MDC mappings)
    Exclusion .xlsx → Tidal → SSIS → Custom Table (excluded DRGs)

  Phase 2 (this plan):
    Nightly batch:
      Tidal triggers SP
        │
        SP reads claims from QNXT (PB inpatient/acute)
        SP reads mapping table (Phase 1 data)
        SP reads exclusion table (Phase 1 data)
        │
        ├─ Matches readmission criteria + NOT excluded → AUTO-DENY
        │     → Denial reason inserted on claim
        │     → Claim status updated
        │     → Audit trail logged
        │
        └─ Does not match or IS excluded → no action

  Downstream (future phases):
    Denied claims stay in QNXT, NOT sent to Cotiviti (Item 10)
    Pended claims → Aerial → Medical Management review (Items 4, 6, 7)
```

### Pend vs Deny (Item 4 vs Item 5)

| | Pend (Item 4) | Deny (Item 5) |
|--|--------------|---------------|
| Match criteria | Same **MDC** within 30 days | Same **DRG** within 30 days |
| Action | Hold for clinical review | Auto-deny |
| Destination | Sent to Aerial/Medical Management | Stays in QNXT |
| Who decides | Doctor reviews, decides pay/deny | System decides automatically |
| Exclusion check | TBD | Yes — exclusion file protects DRGs |

DRG is more specific than MDC. A claim could match at MDC level (pend for review) but not at DRG level (no auto-deny).

---

## Requirements — What's Defined

### Epic 590794 — 4 Features

| Feature | Title | Child Story | ACs Defined |
|---------|-------|------------|-------------|
| 590798 | Add denial reason for auto-denied claim | 590799 — Add denial reason | TBD |
| 591506 | Auto-deny if readmit DRG same within 30 days | 591508 — Auto-deny logic | 6 ACs |
| 595147 | Exclude specific discharge status codes | 595151 — Discharge status exclusion logic | TBD |
| 590796 | Dual coverage — 2nd claim follows primary disposition | 590797 — 2nd claim follows primary | TBD |

Full details for each feature/story: see `epics/590794-pb-auto-deny.md`

### Story 591508 — The Core Logic (6 ACs)

| AC | Description | Category |
|----|------------|----------|
| AC01 | Same member + same provider + same DRG within 30 days → deny | Happy path |
| AC02 | Different provider, same DRG within 30 days → still detect | Edge case |
| AC03 | DRG on exclusion list → bypass, process normally | Negative (no deny) |
| AC04 | DRG NOT on exclusion list → auto-deny | Happy path |
| AC05 | First claim pays, second claim denied (with dollar amounts) | Happy path |
| AC06 | Second claim after 31 days → both pay | Boundary |

### Story 595151 — Discharge Status Exclusion (3 Scenarios, no ACs)

| Scenario | Initial Admission | Readmission | Expected |
|----------|------------------|-------------|----------|
| 1 | NOT 07, 20, 30 | IS 07, 20, 30 | No action |
| 2 | IS 07 (left AMA) | NOT 07, 20, 30 | No action |
| 3 | IS 20 or 30 | NOT 07, 20, 30 | DENY |

### Story 590799 — Denial Reason

Denial text: "NO PAYMENT CAN BE MADE. THIS CLAIM IS FOR READMISSION AND IS NOT ON THE LIST OF ELIGIBLE DRGS THAT ARE PAYABLE FOR READMISSION."

### Story 590797 — Dual Coverage

When claim is auto-denied and PB member has dual coverage, secondary claim follows disposition of primary. ACs TBD. Discussion for refinement started (Sharat Uragonda, Mar 3).

### Matching Criteria (from 591508)

- Same member = exact match on member ID
- Same facility = exact match on Provider ID / QNXT Legacy ID
- Same DRG = exact match of MS-DRG code (version-aligned)
- Within 30 days = 0-30 calendar days inclusive (≥31 = false)
- Discharge/End date = end date of first claim; admit date = start date of second claim

### Claim Inclusion / Exclusion Rules (from 591508)

**Include:**
- History claims in PAID status not subsequently adjusted

**Exclude from auto-deny:**
- DRG on exclusion file → process normally
- Discharge status codes: History claim exclude 7; Readmission claim exclude 7, 20, 30
- Dual-member secondary claim
- Med COB
- FEP & BC Home claims
- BlueCard Host claims (future phase, excluded from April 30th release)

---

## Open Questions (from 591508 — highlighted yellow in ADO)

| # | Question | Status |
|---|----------|--------|
| 1 | File DRG Effective dates — to be compared with claim admit and discharge dates? | Open |
| 2 | Exclusion file DRG Effective dates — to be compared with claim admit and discharge dates? | Open |
| 3 | While AutoDeny, does system need to look at both DRG code list and exclusion DRG code? | Open |
| 4 | What if first claim doesn't have DRG or second claim DRG — system need to look at DRG codes list? | Open |
| 5 | What are parameters to identify 2nd claim as Inpatient and Acute? Type of Bill = 11, 13? | Open |
| 6 | First claim status for identification — pending confirmation | Open |
| 7 | 2nd claim status — TBD (PAY, PEND) | Open |
| 8 | Multiple admits within 30 days — does the clock reset? | Open |

### Dependencies (from 591508)

- Requirements to be finalized for auto denial reasons
- Denial reason codes to be finalized

---

## Testing Layers (Phase 2 scope)

| Layer | What It Tests | Status |
|-------|--------------|--------|
| 1. Business rule validation | Does the SP make the right deny/no-action decision for each scenario? | Not started — core testing layer |
| 2. Data integrity | After the SP runs, are denial reasons, claim statuses, and audit trails correct in the DB? | Not started |
| 3. Exclusion logic | Does the exclusion file correctly protect DRGs from auto-deny? | Not started |
| 4. Boundary / edge cases | Day 30 vs day 31, cross-provider, out-of-order claims, multiple readmissions | Not started |
| 5. Integration | Does the batch job work end-to-end? Tidal → SP → QNXT claim updated | Not started |
| 6. Downstream impact | Denied claims NOT sent to Cotiviti? Excluded claims flow correctly? | Not started — may be Phase 3+ |

```
Mental Map — Phase 2 Testing Layers

  Layer 1: BUSINESS RULES                ← Core of Phase 2 testing
  "Does the system make the right decision?"
  Same member + same facility + same DRG + within 30 days + not excluded = deny
  Any other combination = no action
  Coverage: 591508 has 6 ACs. Other stories have 3 scenarios + TBD ACs.

  Layer 2: DATA INTEGRITY                ← Verify after SP runs
  "Is the data correct after the decision?"
  Denial reason on claim, claim status updated, audit trail logged
  Coverage: None yet.

  Layer 3: EXCLUSION LOGIC               ← Critical safety net
  "Does the exclusion file protect the right claims?"
  DRG on list = no deny. Discharge status 07/20/30 = no deny.
  Coverage: AC03 covers basic case. Need more scenarios.

  Layer 4: BOUNDARY / EDGE CASES         ← Where bugs hide
  "What about the weird scenarios?"
  Day 30 vs 31, cross-provider, no DRG on claim, multiple readmissions,
  out-of-order claims, first claim in pend/deny status
  Coverage: AC02 (cross-provider), AC06 (day 31). Open questions cover the rest.

  Layer 5: INTEGRATION                   ← End-to-end
  "Does the batch job work?"
  Tidal triggers → SP runs → claims updated in QNXT
  Coverage: None yet. Need environment access.
```

---

## Truth Table (from 591508)

| Same Member | Same Facility | Same DRG | Within 30 Days | NOT on Exclusion | Expected |
|------------|--------------|----------|---------------|-----------------|----------|
| Yes | Yes | Yes | Yes | Yes (not on list) | **Auto Deny** |
| Any other combination | | | | | **No Action** |

This truth table is the foundation for parametric testing. Each "Any" can be expanded into specific test cases — e.g., same member + different facility = no action.

---

## Testing Method — Before/After Compare

The SP runs against claims in QNXT. Before it runs, claims have a certain status. After it runs, some are denied, some are untouched. The core testing method is a before/after comparison:

```
Mental Map — Before/After Compare Method

  1. SET UP test claims in QNXT (various scenarios from truth table)

  2. BEFORE — snapshot
     SELECT * FROM claims WHERE [test claims] → save as "before"

  3. RUN the batch job (Tidal → SP)

  4. AFTER — snapshot
     SELECT * FROM claims WHERE [test claims] → save as "after"

  5. COMPARE — what changed?
     ┌─────────────────────────────────┬──────────────────────────┐
     │ Claims that SHOULD be denied    │ Status changed?          │
     │                                 │ Denial reason correct?   │
     │                                 │ Audit trail logged?      │
     ├─────────────────────────────────┼──────────────────────────┤
     │ Claims that should NOT be denied│ Status unchanged?        │
     │                                 │ No denial reason added?  │
     │                                 │ Nothing touched?         │
     └─────────────────────────────────┴──────────────────────────┘
```

### What This Catches

- **False denies** — a claim that shouldn't have been denied but was (SP filtered too aggressively)
- **Missed denies** — a claim that should have been denied but wasn't (SP missed it)
- **Wrong denial reason** — denied but with incorrect reason code
- **Collateral damage** — claims that don't meet criteria should be completely untouched

### How It Maps to the ACs

Each AC from 591508 becomes a test claim scenario. The truth table IS the expected results matrix. Set up claims that match each AC, run the job, compare.

| AC | Test Claim Setup | Expected After |
|----|-----------------|----------------|
| AC01 | Same member, same provider, same DRG, within 30 days, not excluded | Denied |
| AC02 | Same member, different provider, same DRG, within 30 days | Denied |
| AC03 | Same member, same provider, same DRG, within 30 days, DRG on exclusion list | Unchanged |
| AC04 | Same member, same provider, same DRG, within 30 days, DRG not excluded | Denied |
| AC05 | Two claims — first should pay, second should deny | First paid, second denied |
| AC06 | Same member, same provider, same DRG, 31 days apart | Both unchanged (both pay) |

### Step-by-Step Walkthrough

**Step 1 — Set up test claims**

Set up claim pairs in the QNXT test database — each pair is a first claim (history) and a second claim (readmission). Each pair represents one test scenario.

| Pair | First Claim | Second Claim | Expected |
|------|------------|-------------|----------|
| A | Member M1, Provider P1, DRG 470, discharge Jan 1 | Member M1, Provider P1, DRG 470, admit Jan 25 | Second denied |
| B | Member M2, Provider P2, DRG 002 (excluded), discharge Jan 1 | Member M2, Provider P2, DRG 002, admit Jan 20 | Both unchanged |
| C | Member M3, Provider P3, DRG 470, discharge Jan 1 | Member M3, Provider P3, DRG 470, admit Feb 5 (31 days) | Both unchanged |
| D | Member M4, Provider P4, DRG 470, discharge status 07 | Member M4, Provider P4, DRG 470, admit Jan 15 | Both unchanged |
| E | FEP member (R prefix), DRG 470, matches everything | Same | Both unchanged |
| F | BC Home claim, DRG 470, matches everything | Same | Both unchanged |
| G | Med COB claim, DRG 470, matches everything | Same | Both unchanged |

Each claim needs: member ID, provider ID, DRG code, admit date, discharge date, claim status (PAID for history), and any flags (FEP prefix, COB indicator, BlueCard source flag, discharge status code).

**Step 2 — Record your claim IDs**

Write down every claim ID in a tracking sheet. This is your test matrix:

| Claim ID | Pair | Role | Scenario | Expected Outcome |
|----------|------|------|----------|-----------------|
| CLM-001 | A | History | Happy path | Unchanged (PAID) |
| CLM-002 | A | Readmission | Happy path | Denied |
| CLM-003 | B | History | Excluded DRG | Unchanged |
| CLM-004 | B | Readmission | Excluded DRG | Unchanged |
| ... | ... | ... | ... | ... |

You need this list for every query that follows.

**Step 3 — Take the "before" snapshot**

Run in SSMS against the test database:

```sql
SELECT claim_id, member_id, provider_id, drg_code,
       admit_date, discharge_date, claim_status,
       denial_reason, denial_code
FROM [claims table]
WHERE claim_id IN ('CLM-001', 'CLM-002', 'CLM-003', ...)
```

Save results — export to Excel or screenshot. Every claim should show its setup status (PAID), with no denial reason.

**Step 4 — Trigger the batch job**

Trigger the Tidal job on demand. Wait for it to complete — check the job log or Tidal status to confirm it finished successfully. If the job fails, that's a defect before you even get to compare.

**Step 5 — Take the "after" snapshot**

Run the exact same query from Step 3. Same claim IDs, same columns. Save the results.

**Step 6 — Compare before vs after**

Put the results side by side. For each claim:

| Claim | Check | Pass If |
|-------|-------|---------|
| Should be denied (Pair A readmission) | Status changed? | Yes — changed to denied |
| | Denial reason populated? | Yes — matches expected text |
| | Denial code correct? | Yes — matches configured code |
| Should be unchanged (all others) | Status changed? | No — still PAID |
| | Denial reason populated? | No — still null |
| | Any field changed at all? | No — completely untouched |

**Step 7 — Check the audit trail**

For denied claims only, query the audit table:

```sql
SELECT *
FROM [audit table]
WHERE claim_id IN ('CLM-002', ...)  -- only the denied claims
```

Verify it logged: which claim was denied, the matching member/DRG/dates, denial reason, and timestamp.

**Step 8 — Document results**

For each test pair, record pass/fail, expected vs actual. If anything failed — a claim was denied that shouldn't have been, a claim wasn't denied that should have been, or a denial reason was wrong — that's a defect. Note the claim ID, what went wrong, and which AC it maps to.

**Blocker:** Step 1 depends on whether we can insert test claims or need to find existing ones. This is the first question to answer before executing.

### Environment & Execution

- **Dedicated test environment** — SP runs in a dedicated test env, not shared production
- **On-demand Tidal trigger** — can trigger the batch job manually, no need to wait for nightly schedule
- **Isolation check needed** — confirm what other projects/jobs run in the test environment that might touch PB inpatient claims between snapshots

This means: snapshot before → trigger Tidal on demand → snapshot after → compare. Timing is fully controlled.

### Isolation Strategy

To keep comparisons clean, filter queries to specific test claims only (match on member IDs and claim IDs you set up). This way, even if other jobs run in the environment, they won't affect your comparison results.

**Open question:** Can we insert test claims into QNXT in the test environment, or do we need to work with existing claims? This determines whether we control scenarios precisely or hunt for matching claims in existing data. Need to ask the team.

### Shift-Left Value

This before/after compare method is **shift-left testing** — validating at the database level rather than manually checking each claim through the QNXT portal UI. Benefits:

- **Faster** — SQL queries vs clicking through a portal for each claim
- **Repeatable** — same queries run every time, no manual steps to miss
- **Comprehensive** — can check all test claims in one pass vs one-at-a-time portal validation
- **Auditable** — query results are saved, reviewable, shareable

Portal-level validation is still needed for smoke testing (does the denied claim display correctly to users?) but the bulk of decision-logic testing is more efficient at the DB level.

### What This Method Does NOT Cover

- Whether Tidal triggers the job correctly (integration — Layer 5)
- Whether denied claims stay out of Cotiviti downstream (Layer 6)
- Whether the denial reason displays correctly in the QNXT portal (UI validation)
- Whether the audit trail is usable by the business team (business acceptance)

---

## What's Blocked

| Blocker | What It Blocks | Who to Ask |
|---------|---------------|------------|
| 8 open questions unanswered | Can't write complete TCs | Dev team / BA |
| 3 stories have no ACs | Can't write TCs for 590799, 595151, 590797 | Lead / BA |
| No SP code access | Can't do dev overlap check (Step 8) | Dev team |
| Environment access | Can't execute anything | Manager |
| SIT/UAT ownership unclear | Don't know which TCs to write for which level | Manager / Lead |

---

## Next Steps

1. Send emails (manager + dev team) — in progress
2. Get answers to open questions at standup (4/2, 1:30pm)
3. Request SP code walkthrough from devs
4. When lead returns — walk through new exclusion TCs, clarify Phase 2 AC gaps
5. Start writing Phase 2 TCs once ACs are finalized and open questions answered
