# Workflow: Steps 1-5

---

## Step 1: Resolve Target

**Purpose:** Validate the target repo, find the `framework/` directory, detect platform type.

**Procedure:**
1. Validate `target-path` exists and contains a `framework/` directory
2. Find the Interface class: glob `framework/interfaces/*.py` (exclude `__init__.py`)
3. Read the Interface file — extract:
   - SDK being wrapped (from imports: `selenium`, `deepeval`, `paramiko`, `requests`, etc.)
   - Constructor parameters (what config it takes)
   - Class name (e.g., `BrowserInterface`, `DeepEvalInterface`)
4. Resolve platform type from SDK import:
   - `selenium` → Browser
   - `deepeval` → LLM Eval
   - `paramiko` → Remote (SSH)
   - `psycopg2`/`sqlalchemy` → Database
   - `requests`/`httpx` → API
5. Resolve Layer 2 directory name: glob `framework/` for directories that aren't `interfaces/`, `tasks/`, `roles/`, `tests/`, `resources/`, `_reference/`
   - Remaining directories are Layer 2 candidates (e.g., `pages/`, `metrics/`)
   - Also check inside `_reference/` for the same pattern
6. Apply scope if provided (`--layer N` or single file path)

**Output:** Platform type, Interface class name, Layer 2 directory name(s), scoped file list.

**Failure:** If no `framework/` dir or no Interface file found → report and stop.

---

## Step 2: Classify Files

**Purpose:** Assign every `.py` file to a layer (1-5).

**Procedure:**
1. Glob all `.py` files under `framework/` (including `_reference/`)
2. Exclude `__init__.py`, `conftest.py` (fixtures — not a layer)
3. Classify by directory first:
   - `interfaces/` → Layer 1
   - Layer 2 directories (from Step 1) → Layer 2
   - `tasks/` → Layer 3
   - `roles/` → Layer 4
   - `tests/` → Layer 5
4. For files not in a recognized directory, use AST inspection:
   - Imports `Interface` class → likely Layer 2 or 3
   - Has `@automation_logger("Task")` → Layer 3
   - Has `@automation_logger("Role")` → Layer 4
   - Has `pytest` imports or `test_` prefix → Layer 5
5. For `_reference/` subdirectories, apply the same classification (e.g., `_reference/pages/` → Layer 2)
6. Flag unclassifiable files as INFO findings

**Output:** File inventory with layer assignments.

**See:** [[check-5-layer/references/layer-classification]] for detailed classification rules.

---

## Step 3: Check Compliance

**Purpose:** Compare each file against its layer's contract rules using AST parsing.

**Procedure:**
1. Load `5-layer-contract.md` — parse into rule sets per layer + global rules
2. For each classified file, run checks in order:

**Global rule checks (all files):**
- Module-level docstring exists and states purpose + layer
- Class docstring exists and lists structural rules
- Every method has a docstring
- Methods organized by category (section header comments)
- Composition over inheritance (no class inheritance except `object`)
- Imports only from layer below or utilities
- Type hints on all parameters and return types
- Constants as class-level attributes

**Per-layer checks:**
- Layer 1: no domain vocabulary, constructor takes SDK+config+logger, returns SDK primitives
- Layer 2: no decorators, identifiers as class constants, atomic methods return `self`, state-checks return primitives, takes Interface only
- Layer 3: `@automation_logger("Task")` on methods not constructor, returns `None`, parameters are domain values
- Layer 4: `@automation_logger("Role"/"Role Constructor")`, creates Tasks in constructor, workflow calls multiple Tasks, returns `None`
- Layer 5: setup fixture with autouse, creates Components on self, `@automation_logger("Test")`, creates Role in Arrange, asserts via Component state-checks

**Excluded file checks (conftest.py, utilities):**
- `conftest.py`: verify it provides an Interface fixture (e.g., `deepeval_interface`, `browser`) that Layer 5 setup expects
- `resources/utilities/autologger.py`: verify it exists and exports `automation_logger` function

3. Classify each finding: FAIL / WARN / INFO

**Output:** Findings list with severity, file:line, rule reference, description, proposed fix.

**See:** [[check-5-layer/references/ast-checks]] for AST implementation details.

---

## Step 4: Report

**Purpose:** Present findings in a scannable compliance report.

**Output format:**
```
COMPLIANCE REPORT: [target-path]
Platform type: [detected type]
Contract: 5-layer-contract.md v1.0
Files checked: N
Scope: [full | layer N | single file]

LAYER 1 — Interface (N files)
  FAIL  browser_interface.py:45 — [Global #3] Missing docstring on method `click`
        Fix: Add docstring describing click behavior
  WARN  browser_interface.py:12 — [Layer 1 #3] Config default not constructor-driven
        Fix: Move timeout default to constructor parameter

LAYER 2 — Component (N files)
  FAIL  login_page.py:30 — [Layer 2 #2] Decorator found on atomic method
        Fix: Remove @automation_logger — Layer 2 methods have no decorators
  INFO  employees_page.py — All 7 structural rules pass

...

SCORECARD
─────────────────────────────────────────
Layer 1 (Interface):   2 files —  2 PASS, 0 FAIL
Layer 2 (Component):  12 files — 10 PASS, 1 FAIL, 1 WARN
Layer 3 (Task):        7 files —  7 PASS
Layer 4 (Role):        3 files —  2 PASS, 1 FAIL
Layer 5 (Test):       10 files —  8 PASS, 1 FAIL, 1 INFO
─────────────────────────────────────────
Total: 34 files — 29 PASS, 3 FAIL, 1 WARN, 1 INFO
```

**Grouping:** By layer, then by severity within each layer (FAIL first, then WARN, then INFO).

**If fully compliant:**
```
COMPLIANCE REPORT: [target-path]
Platform type: [type]
Contract: 5-layer-contract.md v1.0
Files checked: N

All files compliant. Clean.
```

---

## Step 5: Fix

**Purpose:** Apply fixes with user approval.

**Trigger:** Only runs if user requests after seeing the report.

**Procedure:**
1. Present each FAIL finding one at a time:
   ```
   Finding 1/N: [FAIL] login_page.py:30
   Rule: Layer 2, Structural Rule #2 — No decorators on any methods
   Found: @automation_logger("POM") on method click_log_in
   Proposed fix: Remove the decorator

   [approve / modify / skip / approve all / stop]
   ```
2. `approve` → apply fix via Edit tool
3. `modify` → user provides alternative, apply that
4. `skip` → move to next
5. `approve all` → apply all remaining without asking
6. `stop` → exit fix mode

**After fixes:**
```
FIXES APPLIED: 4/6
  Applied: findings 1, 2, 3, 5
  Skipped: findings 4, 6

Re-run /check-5-layer to verify fixes.
```

**Note:** WARN and INFO findings are not auto-fixed — only FAIL findings enter fix mode. User can explicitly request WARN fixes.
