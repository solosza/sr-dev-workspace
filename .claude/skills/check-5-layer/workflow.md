# Workflow — check-5-layer

## Phases

| Phase | Steps | Gate |
|-------|-------|------|
| Resolve | Step 1 | Platform type detected, scope resolved |
| Classify | Step 2 | All `.py` files assigned to layers |
| Check | Step 3 | Findings list generated |
| Report | Step 4 | Compliance report output |
| Fix | Step 5 | Fixes applied (if requested) |

## Step Details

### Step 1: Resolve Target

**Input:** `target-path` (required), optional `--layer N` or file path scope

**Procedure:**
1. Validate `target-path` exists and contains `framework/` directory
2. Find Interface class: glob `framework/interfaces/*.py` (exclude `__init__.py`)
3. Read Interface file — extract SDK import, constructor params, class name
4. Resolve platform type from SDK import (selenium→Browser, deepeval→LLM Eval, paramiko→SSH, psycopg2→DB, requests→API)
5. Resolve Layer 2 directory: glob `framework/` for dirs not in {interfaces, tasks, roles, tests, resources, _reference}
6. Apply scope if provided

**Output:** Platform type, Interface class name, Layer 2 directory name(s), scoped file list

**Failure:** No `framework/` dir or no Interface file → report and stop

### Step 2: Classify Files

**Input:** File list from Step 1

**Procedure:**
1. Glob all `.py` files under `framework/` (including `_reference/`)
2. Exclude `__init__.py`, `conftest.py`
3. Classify by directory first (interfaces→L1, Layer 2 dirs→L2, tasks→L3, roles→L4, tests→L5)
4. For unrecognized directories, use AST inspection (imports, decorators, test prefixes)
5. For `_reference/` subdirectories, apply same classification
6. Flag unclassifiable files as INFO

**Output:** File inventory with layer assignments

**See:** `steps/step-02-classify-files.md` for detailed classification rules

### Step 3: Check Compliance

**Input:** Classified file inventory + 5-layer contract

**Procedure:**
1. Load `5-layer-contract.md` — parse into rule sets per layer + global rules
2. For each file, run checks in order: global rules → per-layer rules
3. Use `ast.parse()` for structural checks
4. Use raw source grep for comment/header checks
5. Classify each finding: FAIL / WARN / INFO
6. Check excluded files: conftest.py provides Interface fixture, autologger.py exists

**Output:** Findings list with severity, file:line, rule reference, description, proposed fix

**See:** `steps/step-03-check-compliance.md` for AST implementation details

### Step 4: Report

**Input:** Findings list

**Procedure:**
1. Group findings by layer
2. Within each layer, sort by severity (FAIL first, then WARN, then INFO)
3. Output per-layer section with file:line references
4. Output scorecard at end

**Output:** Plain text compliance report in conversation

### Step 5: Fix

**Input:** Report findings (FAIL only by default)

**Trigger:** Only runs if user requests after seeing report

**Procedure:**
1. Present each FAIL finding one at a time with proposed fix
2. User responds: approve / modify / skip / approve all / stop
3. Apply approved fixes via Edit tool
4. Report fixes applied / skipped count
5. Suggest re-run to verify

**Output:** Modified files + fix summary

## State

**Stateless.** No persistent state between runs. Each invocation is a fresh scan.

## HITL Checkpoints

| Step | Checkpoint | Trigger |
|------|-----------|---------|
| 5 | Per-finding approval | Each FAIL finding presented for approve/modify/skip |
