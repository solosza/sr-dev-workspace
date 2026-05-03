# Fraud Reporting Channels & Filing Requirements

## Three Parallel Reporting Tracks

The fraud detection agent should generate evidence packages formatted for ALL applicable channels simultaneously. Each channel has different requirements and reward structures.

---

## Track 1: False Claims Act — Qui Tam Filing

**Reward:** 15-30% of recovered funds (damages are trebled = 3x fraud amount)
**Authority:** DOJ + federal district courts
**Statute:** 31 U.S.C. § 3730

### Filing Requirements

1. **Attorney representation is MANDATORY** — FCA requires qui tam complaints be filed by an attorney. Cannot proceed pro se.

2. **Complaint filed under seal** in federal district court
   - Complaint and contents MUST remain confidential until seal is lifted
   - NOT served on the defendant
   - Violating the seal = case dismissed

3. **Written Disclosure Statement** — the critical document
   - Served confidentially on the US Attorney General AND the US Attorney for the district
   - Must contain "substantially all material evidence and information" in the relator's possession
   - This is the relator's chance to convince the government to intervene (intervention = much higher success rate)

### What the Disclosure Statement Must Contain

The disclosure statement must be a **clear roadmap** covering:

| Element | What to include | Our source |
|---------|----------------|------------|
| **Falsity** | The specific false claim — what was submitted to the government that was untrue | USASpending award data, 990 filings showing misrepresentation |
| **Knowledge** | Evidence defendant knew the claim was false (intent to deceive) | Timeline analysis, pattern matching, public statements vs. actual activity |
| **Materiality** | The government relied on the false claim in making payment | Award conditions, program requirements vs. entity compliance |
| **Who** | Specific defendants — names, roles, entities | SAM.gov registration, state incorporation, 990 officer lists |
| **What** | Specific false claims submitted | USASpending award records, contract/grant numbers |
| **When** | Timeline of fraudulent activity | Entity formation date → award date → spending anomalies |
| **Where** | Jurisdiction — which federal district | Entity address, award recipient location |
| **How much** | Quantified government damages | Award amounts, treble damage calculation |
| **Witnesses** | People with knowledge of the fraud | Officers, employees, beneficiaries (from OSINT) |
| **Supporting docs** | Contracts, billing records, financial records, emails | 990 filings, SAM.gov records, county assessor, PACER |

### Critical Rules

- **First-to-file rule** — if someone else filed the same allegations first, later cases are barred. Speed matters.
- **Statute of limitations** — 6 years from violation date, OR 3 years from when government knew/should have known. Max 10 years.
- **"Original source" / "materially adds" standard** — our AI analysis of public data qualifies as long as it goes beyond what's already known as a fraud allegation (2010 ACA amendment)

### 2026 Executive Order Boost

Executive Order "Establishing the Task Force to Eliminate Fraud" (March 2026):
- Section 6(a): AG directed to "promote the meritorious pursuit by private persons of civil actions under 31 U.S.C. 3730"
- Section 6(b): AG directed to "ensure prompt review" of intervention decisions within statutory 60-day window (historically delayed for months/years)
- Task Force chaired by VP, includes DOJ, Treasury, HHS, DOL, DHS

**Translation:** The government is actively encouraging qui tam filings and promising faster decisions on intervention. Best filing climate in decades.

---

## Track 2: FinCEN Whistleblower Program (NEW — February 2026)

**Reward:** 10-30% of monetary penalties exceeding $1M
**Authority:** Treasury / FinCEN
**Portal:** fincen.gov/whistleblower
**Statute:** 31 U.S.C. § 5323 (AML Act)

### What FinCEN Wants

FinCEN is "particularly interested" in:
- Fraud schemes misappropriating funds from government benefit programs
- Money laundering
- Sanctions violations
- Use of "deepfake" identities
- "Pig butchering" schemes

### How to Submit

1. Submit via fincen.gov/whistleblower portal
2. Can submit anonymously (but must be represented by counsel to receive award)
3. Upload supporting documentation with the tip
4. FinCEN confirms receipt + provides reference number
5. Tips can be submitted "as soon as possible" — no formal filing like qui tam

### Covered Statutes

- Bank Secrecy Act (BSA)
- International Emergency Economic Powers Act (IEEPA)
- Trading with the Enemy Act (TWEA)
- Foreign Narcotics Kingpin Designation Act

### When to Use This Track

When the fraud involves:
- Money laundering (funds routed through money services businesses — Pattern 4)
- Foreign fund transfers (Feeding Our Future → Somalia pattern)
- Sanctions evasion
- Foreign influence laundering (Singham → Shanghai pattern — Pattern 20)

**This track is COMPLEMENTARY to qui tam** — same evidence can be submitted to both channels for different reward programs.

### Status

- Portal launched February 2026
- NPRM published April 1, 2026 (comment period through June 1, 2026)
- $300M revolving fund for awards
- Awards will be processed once final rule is adopted

---

## Track 3: Treasury OIG / GAO FraudNet / Oversight.gov

**Reward:** None (no monetary reward)
**Purpose:** Official government reporting for accountability
**Use case:** Supplementary reporting after filing qui tam / FinCEN tip

### Channels

| Channel | URL | Best for |
|---------|-----|----------|
| Treasury OIG | oig.treasury.gov/report-fraud-waste-and-abuse | Treasury-related fraud, grant misuse |
| GAO FraudNet | gao.gov/about/what-gao-does/fraud | Federal program fraud, waste, mismanagement |
| Oversight.gov | oversight.gov/where-report-fraud-waste-abuse-or-retaliation | General federal fraud, cross-agency |

### When to Use

- After filing qui tam (supplementary)
- For fraud that doesn't meet qui tam or FinCEN thresholds
- For systemic issues (e.g., "audits are not getting done" — CA Controller pattern)

---

## Agent Evidence Package Output Format

The agent should produce a single evidence package per flagged entity that can be submitted to all three tracks:

```
evidence-packages/
  [entity-name]/
    summary.md              — Executive summary: entity, fraud type, estimated amount
    disclosure-statement.md — Full qui tam disclosure (who/what/when/where/how much)
    timeline.md             — Chronological: formation → awards → anomalies → evidence
    financial-analysis.md   — 990 analysis, award vs. spending, compensation ratios
    network-map.md          — Connected entities, shared officers, same-address matches
    source-index.md         — Every claim mapped to source URL + retrieval date
    fincen-tip.md           — FinCEN-formatted tip (money laundering / sanctions angle)
    attachments/
      990-filings/          — Downloaded 990 PDFs
      usaspending-records/  — Award detail exports
      sam-gov-records/      — Entity registration snapshots
      osint/                — PACER excerpts, news articles, public records
```

## Sources

- [FinCEN Whistleblower Program](https://www.fincen.gov/whistleblower-program)
- [FinCEN Submitting a Tip](https://www.fincen.gov/whistleblower-program/submitting-a-tip)
- [FinCEN Proposes Whistleblower Rule](https://www.fincen.gov/news/news-releases/fincen-proposes-rule-pay-whistleblowers)
- [White House — Task Force to Eliminate Fraud](https://www.whitehouse.gov/presidential-actions/2026/03/establishing-the-task-force-to-eliminate-fraud/)
- [Treasury Healthcare Fraud Advisory](https://home.treasury.gov/news/press-releases/sb0426)
- [Federal Register — Whistleblower Incentives](https://www.federalregister.gov/documents/2026/04/01/2026-06271/whistleblower-incentives-and-protections)
- [False Claims Act FAQ](https://www.whistleblowers.org/faq/false-claims-act-qui-tam/)
- [How to File Qui Tam](https://whistleblowerlaw.com/how-to-file-a-qui-tam-lawsuit/)
- [Qui Tam Guide 2026](https://lawfold.com/qui-tam-lawsuit/)
- [Treasury OIG](https://oig.treasury.gov/report-fraud-waste-and-abuse)
- [GAO FraudNet](https://www.gao.gov/about/what-gao-does/fraud)
- [Oversight.gov](https://www.oversight.gov/where-report-fraud-waste-abuse-or-retaliation)
