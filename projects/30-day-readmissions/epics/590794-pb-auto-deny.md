# Epic 590794 — PB: Auto-Deny

**Title:** PB: Auto-deny inpatient and readmission claim
**State:** New
**Priority:** 2
**Value Area:** Business
**Parent:** 590047 (30-Day Readmissions)
**Demand:** DMND0002863

## Description

As a user, I want to exclude discharge status codes 07 (left against medical advice or discontinued care), 20 (expired), 30 (still a patient)

As a user I want to auto-deny PB inpatient and acute readmission claims for the same member and facility when the admit date is within 30 days of the discharge date (end date) of the first claim and the DRG is the same as the first claim

## Features

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 590798 | PB: Add a denial reason for claim that is auto-denied | New | 3/17/2026 |
| 591506 | PB: Auto-deny claim if readmit DRG same as first admit within 30 days | New | 3/17/2026 |
| 595147 | PB: Exclude specific discharge status codes | New | 3/24/2026 |
| 590796 | PB: If PB member has dual coverage, 2nd claim to follow disposition of primary claim | New | 3/16/2026 |

### Feature 595147 — PB: Exclude specific discharge status codes
**State:** New
**Priority:** 2
**Parent:** 590794
**Demand:** DMND0002863
**Description:** As a user, I want to automatically exclude claims with discharge codes 07, 20, and 30 from being evaluated in readmission rules.

**Child Stories:**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 595151 | PB: Discharge status exclusion logic | New | Updated Tuesday |

#### Story 595151 — PB: Discharge status exclusion logic
**State:** New
**Iteration:** IT Portfolio\PF-Planning-2602\Sprint-260326
**Priority:** 2
**Comments:** 0
**Demand:** DMND0002863
**Parent:** 595147
**Value Area:** Business

**Description:**
As a claims system user, I want the system to automatically exclude claims with discharge status codes 07, 20, and 30, so that these claims are not evaluated for readmission logic or included in denial processing where inappropriate.

**Scenarios:**
1. If initial admission is NOT discharge status code 07, 20, 30, but the second readmission IS 07, 20, 30 → no action
2. If initial admission discharge status code is 07 (left against medical advice) and readmission discharge status codes IS NOT 07, 20, 30 → no action
3. If initial admission discharge status code 20, 30, and readmission discharge status code IS NOT 07, 20, 30 → DENY

**Acceptance Criteria:** TBD — not yet defined in ADO

### Feature 590796 — PB: If PB member has dual coverage, 2nd claim to follow disposition of primary claim
**State:** New
**Priority:** 2
**Parent:** 590794
**Demand:** DMND0002863
**Description:** As a user in situations where a PB member has dual coverage, I want the secondary claim to follow the disposition of the primary claim.

**Child Stories:**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 590797 | PB: 2nd claim to follow disposition of primary claim | New | 3/16/2026 |

#### Story 590797 — PB: 2nd claim to follow disposition of primary claim
**State:** New
**Iteration:** IT Portfolio\PF-Planning-2602
**Priority:** 2
**Comments:** 1 (Sharat Uragonda, Mar 3 — "Discussion for Refinement:")
**Demand:** DMND0002863
**Parent:** 590796
**Value Area:** Business

**Description:**
1. As a user, I want to auto deny a readmission claim
2. As a user, when claim is auto-deny, the secondary claim will follow the disposition of the primary claim.

**Acceptance Criteria:** TBD — not yet defined in ADO

### Feature 590798 — PB: Add a denial reason for claim that is auto-denied
**State:** New
**Priority:** 2
**Parent:** 590794
**Description:** As a user, I want to add a denial reason for PB claims that auto-denied by the custom job in this epic.

**Child Stories:**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 590799 | PB: Add denial reason | New | 3/24/2026 |

#### Story 590799 — PB: Add denial reason
**State:** New
**Iteration:** IT Portfolio\PF-Planning-2602
**Priority:** 2
**Comments:** 1
**Demand:** DMND0002863
**Parent:** 590798

**Description:**
When the claim is auto-denied, provide a denial reason. Denial reason inserted onto claim.

**Denial Reason Text:**
"NO PAYMENT CAN BE MADE. THIS CLAIM IS FOR READMISSION AND IS NOT ON THE LIST OF ELIGIBLE DRGS THAT ARE PAYABLE FOR READMISSION."

**Definition of Done (DoD):**
- All acceptance criteria met
- Tests added and passing (unit/functional as applicable)
- Code reviewed and merged
- Logging/monitoring and error handling in place
- Docs/notes updated (user/admin/dev as needed)
- Demoed to stakeholders (or PO sign-off)
- Deployed to target environment(s); no Sev-1/Sev-2 defects

**Notes / Assumptions:**
- Requirements — Business needs to provide denial reason(s)
- Data — TBD

**Acceptance Criteria:** TBD — not yet defined in ADO

### Feature 591506 — PB: Auto-deny claim if readmit DRG same as first admit within 30 days
**State:** New
**Priority:** 2
**Parent:** 590794
**Description:** As a user I want to auto-deny PB inpatient and acute readmission claims for the same member and facility when:
1. The admit date is within 30 days of the discharge date (end date) of the first claim and the DRG is the same as the first claim
2. Not on the MS DRG exclusion file

**Child Stories:**

| ID | Title | State | Updated |
|----|-------|-------|---------|
| 591508 | PB: Auto-deny claim when readmit DRG same as first admit within 30 days and not on exclusion file | New | Updated 34 min ago |

---

## Story 591508 — PB: Auto-deny claim when readmit DRG same as first admit within 30 days and not on exclusion file

**State:** New
**Iteration:** IT Portfolio\PF-Planning-2602\Sprint-260326
**Priority:** 2
**Comments:** 6
**Demand:** DMND0002863
**Parent:** 591506

### Description

As a user I want to auto-deny PB inpatient and acute readmission claims for the same member and facility when:

1. The admit date is within 30 days of the discharge date (end date) of the first claim and the DRG is the same as the first claim
2. Not on the MS DRG exclusion file
3. Is within the effective date range

### No Action Scenarios

- If initial admission DRG is ON exclusion list, no action
- If readmission DRG is ON exclusion list, no action
- If initial admission and readmission DRG is ON exclusion list, no action

### Business Rules

- Identify First Claim based on status (pending confirmation)
- Validate 2nd claim is within 30 days of discharge date of 1st claim
  - 2nd claim status — TBD (PAY, PEND)
  - What are parameters to identify 2nd claim — Inpatient and Acute claims? Type of Bill = 11, 13?
- Compare DRG codes between First and Second claim
- If DRG matches:
  - Compare MDC categories between the two claims
  - Validate Effective Date of DRG codes (File DRG Effective dates to be compared with claim admit and discharge dates?)
  - Validate if DRG is in exclusion condition (Exclusion file — DRG Effective dates to be compared with claim admit and discharge dates?). While AutoDeny, does system need to look at both DRG code list and exclusion DRG code?
  - What if first claim doesn't have DRG or second claim DRG claim, system need to look at DRG codes list?
  - If MDC category is the same → **Deny Second Claim**
- If first claim is in Pend status
  - 2nd claim should Pending for MM review
- If First claim in deny
  - 2nd claim should (?)

### No MDC Exclusion List Applies

- Readmission claim for same member and facility when second claim is within 30 days of earlier claim with same DRG
- The identified claim DRG is then looked up if it is on the DRG exclusion file
- If identified claim DRG is on exclusion file, no action
- If identified claim DRG is NOT on exclusion file, auto deny
- Is within effective date range

### Matching Criteria

- Same member = exact match on member ID
- Same facility = exact match on Provider ID / QNXT Legacy ID
- Same DRG = exact match of the MS-DRG code (version-aligned)
- Within 30 days = inclusive of exactly 30 calendar days (0-30 days → true; ≥31 → false)
- Discharge/End date = end date of the first claim; admit date = start date of the second claim

### Claim Inclusion / Exclusion Rules

**Include:**
- History claims in PAID status that has not been subsequently adjusted

**Exclude:**
- For out-of-order claims, pend the history claim and readmission claim will pay
- Exclude certain discharge codes from auto denied — Discharge Codes = 7, 20 and 30
  - History Claim: exclude 7
  - Readmission Claim: exclude 7, 20, 30
- Exclude dual-member secondary claim
- Exclude Med COB
- Exclude FEP & BC Home claims

### Notes / Assumptions

- BlueCard Host claims is excluded for the April 30th release and will be for a future phase
- What happens if there is multiple admits within a 30 day period? Does the clock reset with each new subsequent admit?
- DRG Codes and Exclude file should have Effective date and termination dates from business. Before denied, claim should validate DRG, Exclude code and effective dates.

### Dependencies

- Requirements to be finalized for auto denial reasons
- Denial reason codes to be finalized

### Open Questions (from story — highlighted yellow)

1. File DRG Effective dates — to be compared with claim admit and discharge dates?
2. Exclusion file DRG Effective dates — to be compared with claim admit and discharge dates?
3. While AutoDeny, does system need to look at both DRG code list and exclusion DRG code?
4. What if first claim doesn't have DRG or second claim DRG claim — system need to look at DRG codes list?
5. What are parameters to identify 2nd claim as Inpatient and Acute claims? Type of Bill = 11, 13?
6. First claim status for identification — pending confirmation
7. 2nd claim status — TBD (PAY, PEND)
8. Multiple admits within 30 days — does the clock reset?

### Acceptance Criteria

**AC01 — Same Member + Same Provider + Same DRG within 30 Days**

Description: A second readmission for the same member at the same facility with the same DRG must be detected when the discharge date of the initial claim is within 30 days of the admission date of the new claim.

Scenario:
- Claim #1 (Initial): DRG = 470, Provider A, Member M1
- Discharge date = Jan 01
- Claim #2 (Readmission): DRG = 470, Provider A, Member M1
- Admission date = Jan 25 (within 30 days)

Acceptance Criteria:
- System identifies Claim #2 as a readmission
- Claim #2 is flagged for auto-denial unless DRG is in exclusion list
- System uses Claim #1 discharge date for 30-day calculation

**AC02 — Different Provider, Same DRG within 30 Days**

Description: Second claim should still be evaluated for readmission even if submitted by a different facility, as long as the DRG matches and occurs within 30 days.

Scenario:
- Claim #1: DRG = 470, Provider A
- Claim #2: DRG = 470, Provider B
- Time between Claim #1 discharge and Claim #2 admission = 18 days

Acceptance Criteria:
- Readmission logic must detect cross-provider readmissions
- Claim #2 should follow the same denial/exclusion rules as AC01
- Provider ID should not restrict readmission detection
- Claim should PAID

**AC03 — Claims with DRG in Exclusion List**

Description: If the DRG is on the exclusion list, the readmission rule does not apply.

Scenario:
- Claim #2 submitted with DRG = 002
- DRG 002 is on exclusion list
- Occurs within 30 days of previous claim

Acceptance Criteria:
- System must bypass readmission rule
- Claim #2 must process normally
- No auto-denial triggered
- Exclusion file must be referenced before denial logic

**AC04 — Auto Denial When DRG is NOT in Exclusion List**

Description: If a DRG is not part of the exclusion file and it meets readmission criteria, the system must auto-deny it.

Scenario:
- DRG = 470 (not excluded)
- Readmission detected within 30 days

Acceptance Criteria:
- System auto-denies the readmission claim
- Denial code and reason are populated correctly
- Audit trail logs readmission match (Member, DRG, dates)

**AC05 — First Claim Must Pay, Second Claim Must Deny**

Description: Ensure the first claim processes normally and pays correctly within allowable amount. The second claim should be evaluated and denied based on readmission rule.

Scenario:
- Claim #1: Initial visit, DRG 470 → Should pay normally (allowable amount 30K, Paid 25K)
- Claim #2: Readmission within 30 days → Should be denied

Acceptance Criteria:
- Claim #1 passes through pricing & pays within allowed limits
- Claim #2 is flagged by readmission logic
- Claim #2 is denied with correct denial reason unless DRG is in exclusion list

**AC06 — First Claim Must Pay, Second Claim processed after 31 days of discharge date**

Description: Ensure the first claim processes normally and pays correctly within allowable amount. The second claim Processed after 31 days of 1st claim discharge date, 2nd claim must process as normal.

Scenario:
- Claim #1: Initial visit, DRG 470, discharge date 1st of Jan → Should pay normally
- Claim #2: Readmission after 31 days, admit date 1st of Feb → Should be paid

Acceptance Criteria:
- Claim #1 Paid as expected
- Claim #2 Paid as expected

### Truth Table (TBD)

| Condition Set | Same Member | Same Facility | Same DRG | Admit within 30 days of prior discharge | DRG on Exclusion File | Expected Outcome |
|--------------|------------|--------------|----------|----------------------------------------|----------------------|-----------------|
| Only case that denies | Yes | Yes | Yes | Yes | No | **Auto Deny** |
| All other combinations | Any | Any | Any | Any | Any | **No Action** |
