# Step 1: Resolve Target

## Purpose

Validate the target repo, find the `framework/` directory, detect platform type from the Interface class.

## Input

- `target-path` — platform repo root (required)
- Optional scope: `--layer N` or single file path

## Procedure

1. **Validate target exists:**
   - Check `target-path` is a valid directory
   - Check it contains a `framework/` subdirectory
   - If not → STOP: "No framework/ directory found at [path]"

2. **Find Interface class:**
   - Glob `framework/interfaces/*.py` (exclude `__init__.py`)
   - Read the Interface file(s)
   - Extract from imports: SDK being wrapped
   - Extract class name (e.g., `BrowserInterface`, `DeepEvalInterface`)
   - Extract constructor parameters

3. **Resolve platform type from SDK import:**

   | Import | Platform Type |
   |--------|--------------|
   | `selenium` | Browser |
   | `deepeval` | LLM Eval |
   | `paramiko` | Remote (SSH) |
   | `psycopg2` / `sqlalchemy` | Database |
   | `requests` / `httpx` | API |
   | `playwright` | Browser |

4. **Resolve Layer 2 directory:**
   - List directories under `framework/` (and `framework/_reference/`)
   - Remove known non-Layer-2: `interfaces/`, `tasks/`, `roles/`, `tests/`, `resources/`, `_reference/`, `fixtures/`
   - Remaining = Layer 2 candidates (e.g., `pages/`, `metrics/`, `commands/`)
   - Confirm by checking if files inside import from Interface layer

5. **Apply scope:**
   - No flags → all `.py` files under `framework/`
   - `--layer N` → filter after classification (Step 2)
   - File path → single file only

## Output

Pass to Step 2:
- Platform type (string)
- Interface class name (string)
- Layer 2 directory name(s) (list)
- Scoped file list or "all"

## Failure Conditions

| Condition | Action |
|-----------|--------|
| `target-path` doesn't exist | Stop with error message |
| No `framework/` directory | Stop with error message |
| No Interface file in `framework/interfaces/` | Stop with error message |
| No SDK import detected | Stop — cannot determine platform type |
| Unknown SDK | Stop — report import found, ask user to classify |
