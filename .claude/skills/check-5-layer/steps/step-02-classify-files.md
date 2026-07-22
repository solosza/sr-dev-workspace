# Step 2: Classify Files

## Purpose

Assign every `.py` file to a layer (1-5) using directory structure and AST inspection.

## Input

- File list from Step 1
- Layer 2 directory name(s) from Step 1

## Procedure

### Primary: Directory-Based Classification

| Directory Pattern | Layer | Confidence |
|-------------------|-------|------------|
| `interfaces/` | 1 | High |
| Layer 2 dirs (from Step 1) | 2 | High |
| `tasks/` | 3 | High |
| `roles/` | 4 | High |
| `tests/` | 5 | High |
| `_reference/[any of above]/` | Same as above | High |
| `resources/utilities/` | Utility (skip layer checks) | High |

### Secondary: AST-Based (for unrecognized directories)

When a file is not in a recognized directory:

| AST Signal | Layer | Confidence |
|-----------|-------|------------|
| Imports SDK directly | 1 | High |
| Imports Interface, no `@automation_logger`, returns `self` | 2 | Medium |
| Has `@automation_logger("Task")` | 3 | High |
| Has `@automation_logger("Role")` or `("Role Constructor")` | 4 | High |
| Has `pytest` imports, `test_` prefix, `@pytest.fixture` | 5 | High |
| Imports from `tasks/` module | 4 | Medium |
| Imports from Layer 2, has `@automation_logger` | 3 | Medium |

### Excluded Files

| Pattern | Handling |
|---------|----------|
| `__init__.py` | Skip — package marker |
| `conftest.py` | Excluded from layer checks. Verify provides Interface fixture. |
| `resources/utilities/*.py` | Excluded from layer checks. Verify `autologger.py` exists with `automation_logger`. |

### Ambiguous Files

If a file cannot be classified with medium+ confidence:
- Report as INFO: "Unable to classify [file] — not in recognized directory, AST signals ambiguous"
- Include AST signals found
- Do NOT skip — flag it

## Output

Pass to Step 3:
- File inventory: `{ file_path: layer_number }` for each classified file
- Excluded files list (conftest, utilities) for separate validation
- Unclassifiable files list (reported as INFO)
