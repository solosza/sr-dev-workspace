# Gaps Analysis — Fraud Detection App

## Critical Gaps (Must solve before building)

### Gap 1: Attorney Partnership — No Tech Solution Without Legal

**Status:** BLOCKER
**Why:** FCA requires attorney representation. Can't file qui tam pro se. Can't receive FinCEN award without counsel.

**What's missing:**
- No attorney identified or engaged
- No engagement letter or fee structure defined
- No process for attorney review of evidence packages before filing
- No understanding of which federal districts are most favorable for filing

**Fix:** Phase 1 of the build must be attorney outreach. Target qui tam specialty firms that work on contingency (they take 25-40% of the whistleblower's share but bear all legal costs). Firms to research: Phillips & Cohen, Constantine Cannon, Whistleblower Law Collaborative, Kohn Kohn & Colapinto.

---

### Gap 2: First-to-File Risk — Speed vs. Quality

**Status:** HIGH RISK
**Why:** If someone else files the same fraud allegation first, our case is barred. The agent may discover fraud that's already being investigated or that another whistleblower already filed on.

**What's missing:**
- No PACER monitoring for existing qui tam filings (sealed cases are invisible, but some are partially unsealed)
- No deduplication against DOJ press releases about ongoing investigations
- No process for determining if fraud is "already publicly known" (which weakens the case)

**Fix:** Layer 0 (pattern discovery) should also scan for existing investigations. If an entity is already under investigation or indictment, flag it as "low-priority" for new filing but "high-priority" for evidence addition to existing case.

---

### Gap 3: Evidence Preservation — Chain of Custody

**Status:** HIGH RISK
**Why:** Web pages change, 990s get amended, SAM.gov records get updated. If we find evidence today and file in 3 months, the source may be gone.

**What's missing:**
- No archiving/snapshotting of evidence at discovery time
- No hash verification of downloaded documents
- No timestamped retrieval logs
- No Wayback Machine / archive.org integration

**Fix:** Every piece of evidence must be:
1. Downloaded and stored locally at discovery time
2. SHA-256 hashed with timestamp
3. Screenshot of web page captured (Playwright MCP)
4. Retrieval URL + date logged in source-index.md
5. Optionally submitted to archive.org for independent timestamp

---

### Gap 4: Materiality Threshold — Not All Anomalies Are Fraud

**Status:** MEDIUM
**Why:** An anomaly score is not fraud. A nonprofit with a 990 that looks weird may have a legitimate explanation. Filing a weak case wastes attorney time and damages credibility.

**What's missing:**
- No confidence threshold defined (at what score do we escalate to attorney?)
- No false-positive filtering (legitimate reasons for anomalies)
- No human review step between "flagged" and "evidence package generated"
- No feedback loop from attorney rejections back to scoring model

**Fix:**
- Define a 3-tier scoring system: LOW (log, no action), MEDIUM (queue for human review), HIGH (auto-generate evidence package)
- Attorney rejection reasons feed back into the scoring model (kernel learn loop)
- First 10-20 packages should go through manual review to calibrate the model

---

### Gap 5: Scale vs. Quality — Daily Scanning May Produce Noise

**Status:** MEDIUM
**Why:** USASpending.gov publishes thousands of awards daily. Running all 22+ fraud patterns against every award will produce a flood of low-quality flags.

**What's missing:**
- No prioritization of which federal programs to scan first (highest fraud rate programs)
- No volume management (rate limiting, batch processing)
- No "focus sectors" based on known high-fraud areas

**Fix:** Start narrow:
- Phase 1: Homeless services nonprofits (LAHSA, HUD CoC grants) — validated by CA cases
- Phase 2: Healthcare (Medicare/Medicaid) — validated by Feeding Our Future, Treasury advisory
- Phase 3: COVID relief residual (PPP, EIDL) — statute of limitations expiring 2026
- Phase 4: Political nonprofits (501c4) — validated by NoKings investigation
- Expand sectors only after attorney validates first batch from each sector

---

### Gap 6: FinCEN Track Requirements — Different from Qui Tam

**Status:** MEDIUM
**Why:** FinCEN whistleblower program covers different statutes (BSA, IEEPA) with different evidence requirements. Not every fraud case has a money laundering angle.

**What's missing:**
- No process for determining which cases qualify for FinCEN track vs. qui tam vs. both
- No FinCEN-specific evidence formatting
- No understanding of how FinCEN tips interact with qui tam filings (can you file both? timing?)

**Fix:** Add a "channel routing" step to Layer 6 that evaluates each case against:
- Does it involve false claims to the government? → Qui tam
- Does it involve money laundering, foreign transfers, sanctions? → FinCEN
- Both? → File both (complementary, not exclusive)

---

### Gap 7: State False Claims Acts — Multiplied Reward Channels

**Status:** LOW (enhancement)
**Why:** 31 states + DC have their own False Claims Acts with separate reward programs. A single fraud case touching state funds could be filed at both federal AND state level.

**What's missing:**
- No mapping of which states have FCA equivalents
- No state-specific filing requirements
- No analysis of which states are most aggressive in pursuing fraud

**Fix:** Research phase — catalog state FCAs, identify states with highest homeless/healthcare spending (CA, NY, TX, FL, IL), understand dual-filing procedures.

---

### Gap 8: Entity Verification at Scale — API Rate Limits

**Status:** LOW (engineering)
**Why:** Cross-referencing every award against 8+ databases will hit API rate limits.

**What's missing:**
- No API rate limit analysis for USASpending, ProPublica, SAM.gov
- No caching strategy for repeated lookups
- No fallback for when APIs are down

**Fix:** Engineering concern — solve during build phase. Use caching, batch queries, and off-peak scheduling.

---

## Summary

| Gap | Severity | Phase |
|-----|----------|-------|
| Attorney partnership | BLOCKER | Phase 1 |
| First-to-file risk | HIGH | Phase 1 |
| Evidence preservation | HIGH | Phase 2 (build) |
| Materiality threshold | MEDIUM | Phase 2 (build) |
| Scale vs. quality | MEDIUM | Phase 2 (build) |
| FinCEN track routing | MEDIUM | Phase 2 (build) |
| State FCA mapping | LOW | Phase 3 (enhancement) |
| API rate limits | LOW | Phase 2 (engineering) |
