# Workflow: Steps 1-5

---

## Step 1: Discover

**Purpose:** Load the target and all its downstream dependencies.

**Procedure:**
1. If target is a file: read it, extract all path references (Skill Reference, Design Reference, `→` links, wikilinks)
2. If target is a folder: glob recursively for `.md`, `.json`, `.sql`, `.py`, `.xlsx` files
3. **Dependency traversal:** For each reference found in any file:
   - If it points to a folder → glob that folder recursively, add all files to inventory
   - If it points to a file → add that file to inventory
   - Read newly added files and extract their references too (recursive, max depth 3)
4. Build file inventory: path, size, extension, last modified, how it was discovered (direct target vs dependency)
5. Report: "Found N files (M direct, K via dependency traversal)"

**Output:** File inventory list with dependency chain.

**Rule:** The scope is the target PLUS everything it references. A command file that points to a skill folder means the entire skill folder is in scope. See [[gap-check/references/corpus-detection#Dependency Traversal]].

---

## Step 2: Detect & Model

**Purpose:** Determine what kind of content this is and build an internal reference model.

**Procedure:**
1. Read file content (or headers for large files)
2. Apply corpus detection rules — see [[gap-check/references/corpus-detection]]
3. Based on detected type(s), build the appropriate model:

**Skill corpus model:**
- All wikilinks and file path references → expected targets
- Step counts from indexes/SKILL.md → expected file counts
- Vocabulary terms from SKILL.md → term registry
- Schema definitions (JSON structures described in markdown) → schema registry

**Test case corpus model:**
- AC identifiers from stories/user stories → AC registry
- TC identifiers from test-cases.md → TC registry
- TC↔AC mappings from traceability matrix → coverage map
- Query identifiers from tc-queries.sql → query registry
- TC↔query mappings → query coverage map

**Design doc corpus model:**
- Required sections from completeness checklist → section registry
- Wikilinks to payload files → expected payloads
- Design Documents table entries → expected references

**Mixed corpus:** Build multiple models. Apply all relevant check sets.

**Output:** Corpus type + internal reference model.

---

## Step 3: Check

**Purpose:** Apply corpus-appropriate gap checks against the model.

**Procedure:**
For each detected corpus type, apply the relevant gap categories from [[gap-check/references/gap-categories]].

**For all corpus types:**
- Dead references (wikilinks, paths that don't resolve)
- File mentions that don't exist

**For skill corpus, add:**
- Count mismatches (index says N steps, folder has M files)
- Schema mismatches (JSON structure described differently in two places)
- Stale terminology (term used but not in vocabulary, or removed concept still referenced)
- Step flow gaps (step N says "proceed to step N+1" but N+1 doesn't exist)

**For test case corpus, add:**
- Coverage gaps (AC with no TC, TC with no AC)
- Query alignment (TC exists but no matching query in tc-queries.sql)
- Traceability gaps (traceability matrix entries that don't match TC or AC IDs)
- Expected result gaps (TC has no expected result, or expected result contradicts AC)
- Verification dump gaps (tc-queries.sql TCs not in verification-dump.sql UNION)

**For design doc corpus, add:**
- Completeness gaps (required sections missing per input-contract)
- Payload gaps (Design Documents table lists file that doesn't exist)
- Depth gaps (section present but below minimum depth)

**Output:** Findings list — each finding has: category, severity, file, line, description, proposed fix.

---

## Step 4: Report

**Purpose:** Present findings in a scannable format.

**Output format:**
```
GAP REPORT: [target-path]
Corpus type: [detected type(s)]
Files scanned: N

ERRORS (must fix):
  1. [DEAD_REF] step-03-spawn-agents.md:14
     References "step-04-monitor.md" but file doesn't exist
     Fix: Update reference to "step-04-report.md"

  2. [COVERAGE] test-cases.md
     AC-015 has no corresponding test case
     Fix: Add TC for AC-015 or document exclusion reason

WARNINGS (should review):
  3. [STALE_TERM] SKILL.md:42
     Uses "monitor" but SKILL.md vocabulary defines "status check"
     Fix: Replace "monitor" with "status check"

Summary: 2 errors, 1 warning
```

**Grouping:** Errors first, then warnings. Within each, ordered by file path.

**If no gaps found:**
```
GAP REPORT: [target-path]
Corpus type: [type]
Files scanned: N

No gaps found. Clean.
```

---

## Step 5: Fix

**Purpose:** Apply fixes with user approval.

**Trigger:** Only runs if `--fix` flag was passed, or user requests after seeing report.

**Procedure:**
1. Present each finding one at a time:
   ```
   Finding 1/N: [DEAD_REF] step-03-spawn-agents.md:14
   References "step-04-monitor.md" but file doesn't exist
   Proposed fix: Update reference to "step-04-report.md"

   [approve / modify / skip / approve all / stop]
   ```
2. For `approve`: apply the fix (Edit tool)
3. For `modify`: user provides alternative fix text, apply that
4. For `skip`: move to next finding
5. For `approve all`: apply all remaining fixes without asking
6. For `stop`: exit fix mode

**Output:** Summary of fixes applied vs skipped.

```
FIXES APPLIED: 4/6
  Applied: findings 1, 2, 3, 5
  Skipped: findings 4, 6

Re-run /gap to verify fixes.
```
