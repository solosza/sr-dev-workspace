# Layer Classification

How to assign a Python file to a layer (1-5).

---

## Primary: Directory-Based

| Directory Pattern | Layer | Confidence |
|-------------------|-------|-----------|
| `interfaces/` | 1 | High |
| Platform-specific Layer 2 dirs (`pages/`, `metrics/`, `queries/`, `commands/`) | 2 | High |
| `tasks/` | 3 | High |
| `roles/` | 4 | High |
| `tests/` | 5 | High |
| `_reference/[any of above]/` | Same as above | High |
| `resources/utilities/` | Utility (skip layer check, verify shared contract only) | High |

## Secondary: AST-Based (for unrecognized directories)

When a file is not in a recognized directory, inspect its code:

| AST Signal | Layer | Confidence |
|-----------|-------|-----------|
| Imports SDK directly (`selenium`, `deepeval`, `paramiko`) | 1 | High |
| Imports Interface class, no `@automation_logger`, returns `self` | 2 | Medium |
| Has `@automation_logger("Task")` decorator | 3 | High |
| Has `@automation_logger("Role")` or `@automation_logger("Role Constructor")` | 4 | High |
| Has `pytest` imports, `test_` method prefix, `@pytest.fixture` | 5 | High |
| Imports from `tasks/` module | 4 (Role imports Tasks) | Medium |
| Imports from layer 2 module, has `@automation_logger` | 3 | Medium |

## Excluded Files

| Pattern | Reason |
|---------|--------|
| `__init__.py` | Package marker — no layer rules apply |
| `conftest.py` | Pytest fixture config — not a layer file. Verify it provides the Interface fixture that Layer 5 setup expects. |
| `resources/utilities/*.py` | Shared utilities — not a layer file. Verify `autologger.py` exists with `automation_logger` function. |

## Layer 2 Directory Discovery

Layer 2 directories vary by platform. Discovery algorithm:

1. List all directories under `framework/` (and `framework/_reference/`)
2. Remove known non-Layer-2 directories: `interfaces/`, `tasks/`, `roles/`, `tests/`, `resources/`, `_reference/`, `fixtures/`
3. Remaining directories are Layer 2 candidates
4. Confirm by checking if files inside import from Interface layer

**Examples:**
- Selenium: `pages/` → Layer 2
- DeepEval: `metrics/` → Layer 2
- SSH: `commands/` or `resources/` → Layer 2 (context-dependent)
- Database: `queries/` or `tables/` → Layer 2

## Ambiguous Files

If a file cannot be classified with medium or high confidence:
- Report as INFO finding: "Unable to classify [file] — not in a recognized directory and AST signals are ambiguous"
- Include the AST signals found for manual review
- Do NOT skip the file — flag it
