# Step 3: Check Compliance

## Purpose

Compare each classified file against its layer's contract rules using AST parsing.

## Input

- Classified file inventory from Step 2
- 5-layer contract (loaded from design doc: `[[check-5-layer/references/5-layer-contract]]`)

## Procedure

### 1. Load Contract

Read `.claude/docs/design/check-5-layer/references/5-layer-contract.md` and parse into:
- Global rules (apply to all files)
- Per-layer rules (Layer 1-5 specific)
- Error handling rules
- Decorator rules
- Method scope rules

### 2. For Each File: Run Global Checks

| Rule | Check Method | Severity |
|------|-------------|----------|
| Module docstring | `ast.get_docstring(module)` not None, contains layer name | FAIL |
| Class docstring | `ast.get_docstring(class_node)` not None | FAIL |
| Method docstrings | Each `FunctionDef`: `ast.get_docstring(node)` not None | FAIL |
| Section headers | Grep raw source for `# ===` pattern | WARN |
| Composition | Class bases = only implicit `object` | FAIL |
| Import boundaries | `Import`/`ImportFrom` from layer below or utilities only | FAIL |
| Type hints | `args.annotation` + `FunctionDef.returns` not None | FAIL |
| Class constants | `Assign` nodes at class body level | WARN |

### 3. For Each File: Run Per-Layer Checks

**Layer 1 (Interface):** No domain vocabulary, constructor takes SDK+config+logger, returns SDK primitives, try/except with re-raise, no upward imports

**Layer 2 (Component):** No decorators, identifiers as class constants, atomic methods return `self`, state-checks return primitives, constructor takes Interface only, no upward imports

**Layer 3 (Task):** `@automation_logger("Task")` on methods not constructor, returns `None`, creates Components in constructor, domain parameters, import boundary

**Layer 4 (Role):** `@automation_logger("Role"/"Role Constructor")`, creates Tasks in constructor, workflow calls multiple Tasks, returns `None`, import boundary

**Layer 5 (Test):** Setup fixture with autouse, creates Components on self, `@automation_logger("Test")`, creates Role in Arrange, asserts via state-checks, no direct Task/Component calls

### 4. Check Excluded Files

- `conftest.py`: verify provides Interface fixture (e.g., `deepeval_interface`, `browser`)
- `resources/utilities/autologger.py`: verify exists, exports `automation_logger`

### 5. Check Error Handling

- Layer 1: methods contain try/except that logs and re-raises
- Layers 2-5: zero `Try` nodes in AST

### 6. Check Business Logic Boundaries

- Interface: no `if/for/while` beyond error handling
- Component: no `if/for/while` beyond guard clauses
- Test: no `if/for/while` in test methods

### 7. Check Method Scope

- Interface: one SDK call per method
- Component: one operation per method (calls Interface exactly once)
- Role: workflow calls ≥2 Task methods

### 8. Classify Findings

Each finding gets:
- **Severity:** FAIL / WARN / INFO
- **Location:** `file_path:line_number`
- **Rule reference:** e.g., "Global #3", "Layer 2, Structural Rule #2"
- **Description:** What was found
- **Proposed fix:** How to resolve

## Output

Pass to Step 4: Findings list sorted by layer, then severity.

## AST Limitations

Some rules use heuristics (grep, name matching). These get WARN or INFO severity:
- Inline comments (stripped by parser)
- Section headers (`# ===`)
- "Domain vocabulary" quality
- "One operation per method" (subjective)

**See:** `[[check-5-layer/references/ast-checks]]` for full implementation details.
