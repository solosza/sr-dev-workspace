# Gap Categories

Gap types organized by corpus type. Each category has detection logic and examples from real usage.

---

## Universal Categories (all corpus types)

### 0. CHAIN_GAP — Dependency Chain Gap

**What:** A downstream dependency referenced by the target is missing, incomplete, or internally inconsistent. Applies to any file that references other files — commands, skills, design docs, test cases, backlogs, task folders.

**Detection:** During dependency traversal (Step 1), follow every `→` link, wikilink, backtick-quoted path, and named reference. For each:
- Does the referenced file/folder exist?
- If folder: does it contain expected files? (SKILL.md for skills, index.md for design docs, numbered tasks for task folders)
- Do files within the dependency have consistent cross-references? (step counts match, schema agrees, IDs align)
- Do downstream files pass their own corpus-type checks?

**Examples:**
```
# Skill chain
SKILL.md:67 → "steps/step-01-discover.md" — exists ✓
SKILL.md:71 → "references/INDEX.md" — exists ✓
INDEX.md:15 → design doc "references/workflow.md" — exists ✓

# Test case chain
test-cases.md → TC-001 through TC-020
tc-queries.sql → queries for TC-001 through TC-018 — MISSING TC-019, TC-020 ✗
verification-dump.sql → UNION includes TC-001 through TC-018 — consistent with queries ✓

# Backlog chain
docs/backlog/014-*.md → "tasks/build-command/" — exists ✓
tasks/build-command/000-index.md → 18 tasks listed — 18 task files found ✓
```

**Severity:** ERROR if any link in the chain is broken. WARN if a referenced file exists but has its own internal gaps.

### 1. DEAD_REF — Dead Reference

**What:** A wikilink, file path, or filename mentioned in text that doesn't resolve to a real file.

**Detection:** Extract all `[[...]]` wikilinks, backtick-quoted paths, and `→` references. Glob for each. Flag unresolved.

**Example:**
```
SKILL.md:29 — References "step-04-monitor.md" but file was deleted
Fix: Update to "step-04-report.md" (the replacement file)
```

### 2. COUNT_MISMATCH — Count Mismatch

**What:** An index or table claims N items but the actual count differs.

**Detection:** Parse tables with numbered rows (step tables, task indexes, file lists). Count actual files matching the pattern. Compare.

**Example:**
```
SKILL.md:40 — Workflow table lists 5 steps but steps/ folder has 4 files
Fix: Add missing step file or remove extra table row
```

---

## Skill Corpus Categories

### 3. SCHEMA_MISMATCH — Schema Mismatch

**What:** Two files describe the same data structure with different fields.

**Detection:** Find JSON examples or schema descriptions. Extract field names. Compare across files that reference the same structure.

**Example:**
```
step-02-create-manifest.md:18 — Manifest schema has "last_completed" field
SKILL.md:78 — Manifest example does NOT have "last_completed" field
Fix: Remove "last_completed" from step-02 (SKILL.md is authoritative)
```

### 4. STALE_TERM — Stale Terminology

**What:** A file uses a term that was replaced or removed in the authoritative vocabulary.

**Detection:** Build term registry from SKILL.md `## Vocabulary`. Scan all files for terms not in vocabulary, or old terms that were renamed.

**Example:**
```
step-03-spawn-agents.md:52 — Uses "monitor" but vocabulary defines "status check"
Fix: Replace "monitor" with "status check"
```

### 5. FLOW_GAP — Step Flow Gap

**What:** A step says "proceed to step N" or "next step" but the target step doesn't exist or has a different name.

**Detection:** Extract "proceed to," "next step," "see step" patterns. Verify target step exists and name matches.

**Example:**
```
step-03-spawn-agents.md:70 — Says "proceed to Step 5 (Report)" but Step 5 doesn't exist (renamed to Step 4)
Fix: Update to "proceed to Step 4 (Report)"
```

---

## Test Case Corpus Categories

### 6. COVERAGE_GAP — AC Coverage Gap

**What:** An acceptance criterion exists in stories but has no corresponding test case.

**Detection:** Extract all `AC-NNN` identifiers from stories. Extract all AC references from test-cases.md and traceability-matrix.md. Flag ACs with no TC.

**Example:**
```
stories/595341.md — AC-005 (discharge status 30) has no test case
Fix: Add TC covering AC-005 or document exclusion reason in traceability matrix
```

### 7. QUERY_ALIGNMENT — TC-Query Alignment Gap

**What:** A test case exists but has no matching query in tc-queries.sql, or a query exists with no matching TC.

**Detection:** Extract TC identifiers from test-cases.md. Extract query comment headers from tc-queries.sql (e.g., `-- TC-001:`). Cross-reference.

**Example:**
```
tc-queries.sql — No query for TC-014 (found in test-cases.md)
Fix: Add TC-014 query to tc-queries.sql
```

### 8. TRACEABILITY_GAP — Traceability Matrix Gap

**What:** Traceability matrix references a TC or AC that doesn't exist, or misses a mapping.

**Detection:** Parse traceability-matrix.md table. Verify every TC ID exists in test-cases.md. Verify every AC ID exists in stories.

**Example:**
```
traceability-matrix.md:25 — Maps AC-012 → TC-012 but TC-012 not found in test-cases.md
Fix: Add TC-012 to test-cases.md or update matrix
```

### 9. VERIFICATION_GAP — Verification Dump Gap

**What:** A TC query exists in tc-queries.sql but isn't included in verification-dump.sql's UNION ALL.

**Detection:** Extract TC query names from tc-queries.sql. Check each appears in verification-dump.sql.

**Example:**
```
verification-dump.sql — Missing TC-008 from UNION ALL (present in tc-queries.sql)
Fix: Add TC-008 SELECT to verification-dump.sql UNION ALL
```

### 10. EXPECTED_RESULT_GAP — Missing Expected Result

**What:** A test case has no expected result, or the expected result contradicts the AC it tests.

**Detection:** Parse test-cases.md for each TC. Check `Expected Result` field is populated and semantically consistent with the AC.

**Example:**
```
test-cases.md TC-006 — Expected result says "PEND" but AC-006 requires "DENY"
Fix: Update expected result to "DENY" per AC-006
```

---

## Design Doc Corpus Categories

### 11. COMPLETENESS_GAP — Missing Required Section

**What:** A section required by build-command's input-contract is missing from the design doc.

**Detection:** Check for 7 required sections: Skill Identity, Philosophy, Vocabulary, Critical Rules, Workflow Summary, Step Specs, File Structure.

**Example:**
```
index.md — Missing "## Vocabulary" section (required by input-contract)
Fix: Add Vocabulary table with at least 3 domain terms
```

### 12. DEPTH_GAP — Section Below Minimum Depth

**What:** A required section exists but doesn't meet minimum depth requirements.

**Detection:** Check minimum depths: identity (1 sentence), philosophy (3+ principles), vocabulary (3+ terms), rules (2+ rules), workflow (2+ steps), step specs (purpose + procedure each).

**Example:**
```
index.md — Philosophy has only 2 principles (minimum 3)
Fix: Add at least 1 more guiding principle
```

---

## Onboard Run Corpus Categories

### 13. ARTIFACT_MISSING — Missing Onboard Artifact

**What:** An expected artifact from the onboard run is missing.

**Detection:** Check for the 7 standard artifacts: epics/metadata.json, test-cases.md, test-cases.xlsx, traceability-matrix.md, tc-queries.sql, verification-dump.sql, evidence/.

**Example:**
```
onboard-runs/2026-06-15T23-30-32Z/ — Missing verification-dump.sql
Fix: Generate verification-dump.sql from tc-queries.sql
```

---

## Severity Guide

| Severity | When | Examples |
|----------|------|---------|
| **ERROR** | Something is broken — will cause failures | DEAD_REF, COVERAGE_GAP, ARTIFACT_MISSING, COMPLETENESS_GAP |
| **WARN** | Something is suspicious — may indicate drift | STALE_TERM, DEPTH_GAP, EXPECTED_RESULT_GAP |
