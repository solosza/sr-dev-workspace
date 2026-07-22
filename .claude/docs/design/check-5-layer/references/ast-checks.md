# AST Check Implementations

How each contract rule is verified using Python's `ast` module.

---

## Global Rule Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| #1 Module docstring | `ast.get_docstring(module)` is not None, contains layer name | FAIL |
| #2 Class docstring | `ast.get_docstring(class_node)` is not None, contains bullet points | FAIL |
| #3 Method docstrings | For each `FunctionDef` in class: `ast.get_docstring(node)` is not None | FAIL |
| #4 Inline comments | Not AST-checkable — skip (comments stripped by parser) | — |
| #5 Section headers | Grep for `# ===` pattern in raw source | WARN |
| #6 Composition | Class bases list contains only implicit `object` — no explicit inheritance | FAIL |
| #7 Import boundaries | Parse `Import`/`ImportFrom` nodes, verify source module is layer below or utilities | FAIL |
| #8 Logging | Layer-specific — Interface checks `self.logger`, others check decorator | WARN |
| #9 Constants | Class body has `Assign` nodes at class level (not inside methods) | WARN |
| #10 Type hints | `FunctionDef.args.args[n].annotation` is not None, `FunctionDef.returns` is not None | FAIL |

## Error Handling Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| #1 Interface catches/re-raises | Interface methods contain `try/except` blocks that call `self.logger` and end with `raise` | FAIL |
| #2 No try/except above Interface | Layer 2-5 files have zero `Try` nodes in AST | FAIL |

## Business Logic Boundary Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| Interface: no logic | No `if/for/while` beyond SDK error handling (`try/except`) | WARN |
| Component: no logic | No `if/for/while` beyond simple guard clauses | WARN |
| Test: AAA only | No `if/for/while` in test methods — only Arrange/Act/Assert | WARN |

**Note:** Task and Role ARE allowed business logic (operational and workflow respectively). These checks only apply to layers that should be logic-free.

## Method Scope Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| Interface: one SDK call | Method body has exactly one SDK method call (exclude logging) | WARN |
| Component: one operation | Method body has ≤2 non-return statements | WARN |
| Task: one domain op | Heuristic — method contains one Component method chain | INFO |
| Role: multi-Task | Workflow method calls ≥2 Task methods (from Role structural rule #3) | WARN |
| Role: cross-module | Workflow method calls Tasks from ≥2 different Task modules | INFO |

## Layer 1: Interface Checks

| Contract Rule | AST Check | Severity |
|--------------|-----------|----------|
| #1 Wraps SDK, no domain vocabulary | Scan method names and docstrings for domain terms (from Layer 2 class names) | WARN |
| #2 Constructor takes SDK+config+logger | `__init__` args include SDK-typed param + `config` + `logger` | FAIL |
| #3 Config-driven defaults | Constructor has default values or config-dict access for timeouts, dirs, flags | WARN |
| #4 SDK primitive returns | `FunctionDef.returns` is primitive type annotation (`bool`, `str`, `int`, `dict`, `list`, `WebElement`, etc.) | FAIL |
| #5 No upward knowledge | No imports from Layer 2+ directories | FAIL |

## Layer 2: Component Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| #1 Constructor takes Interface | `__init__` has exactly one typed param (Interface class), no class inheritance | FAIL |
| #2 No decorators | `FunctionDef.decorator_list` is empty for all methods | FAIL |
| #3 Class-level constants | Has `Assign` nodes at class body level | WARN |
| #4 Atomic methods | Method body calls Interface exactly once (excluding `return self`) | WARN |
| #5 Domain vocabulary | Method names contain domain terms, not generic SDK terms | INFO |
| #6 Import boundary | Imports only from `interfaces/` or `resources/` | FAIL |
| #7 No upward knowledge | No imports from `tasks/`, `roles/`, `tests/` | FAIL |
| Return: self | Non-state-check methods: last statement is `return self` | FAIL |
| Return: primitive | State-check methods (`is_*`, `get_*`, `has_*`): return annotation is `bool`/`str`/`float`/`int` | FAIL |

## Layer 3: Task Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| #1 Constructor creates Components | `__init__` body contains assignments that instantiate Layer 2 classes | FAIL |
| #2 Decorator on methods | Non-`__init__` methods have `@automation_logger("Task")` in decorator_list | FAIL |
| #2b No decorator on constructor | `__init__` decorator_list is empty | FAIL |
| #3 One operation per method | Heuristic: method calls ≤1 distinct Component method chain | INFO |
| #4 Fluent chaining | Method body contains parenthesized expression with chained `.method()` calls | INFO |
| #5 Domain parameters | Method args have simple type annotations (`str`, `int`, `float`, `bool`), not SDK types | WARN |
| #6 Import boundary | Imports from Layer 2 directories and `interfaces/` | FAIL |
| #7 No upward knowledge | No imports from `roles/`, `tests/` | FAIL |
| Return: None | `FunctionDef.returns` is `None` annotation, or method has no return statement | FAIL |

## Layer 4: Role Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| #1 Constructor params | `__init__` takes Interface + additional config params | FAIL |
| #2 Creates Tasks | `__init__` body instantiates Task classes | FAIL |
| #3 Multi-Task workflows | Workflow methods contain calls to ≥2 different Task methods | WARN |
| #4 Config on self | `__init__` has `self.x = x` assignments for config params | WARN |
| #5 Import boundary | Imports from `tasks/` only | FAIL |
| #6 No upward knowledge | No imports from `tests/` | FAIL |
| Decorator: constructor | `__init__` has `@automation_logger("Role Constructor")` | FAIL |
| Decorator: methods | Non-`__init__` methods have `@automation_logger("Role")` | FAIL |
| Return: None | Workflow methods return `None` | FAIL |

## Layer 5: Test Checks

| Rule | AST Check | Severity |
|------|-----------|----------|
| #1 Setup fixture | Has method named `setup` with `@pytest.fixture(autouse=True)` | FAIL |
| #2 Components on self | Setup method body has `self.x = ComponentClass(...)` assignments | FAIL |
| #3 Decorator | Test methods have `@automation_logger("Test")` | FAIL |
| #4 Pytest marks | Test methods have `@pytest.mark.*` decorators | WARN |
| #5 Role in Arrange | Test method body contains Role class instantiation | FAIL |
| #6 Role call in Act | Test method body calls a method on the Role instance | FAIL |
| #7 Assert via state-check | `assert` statements call Component state-check methods (`is_*`, `get_*`, `has_*`) | FAIL |
| #8 One AAA block | Test method has one logical scenario. Integration tests with causal phases (Phase 1 output = Phase 2 input) are valid — multiple Act/Assert blocks allowed when phases are causally dependent. | INFO |
| #9 No direct layer calls | Test method does not call Task or Component action methods directly | FAIL |

## Heuristic Severity Guide

- **FAIL** — mechanically verifiable via AST, contract says "must"
- **WARN** — AST can detect a signal but human judgment needed (e.g., "atomic" is subjective)
- **INFO** — pattern observed, worth noting, but not a violation (e.g., naming style)

## AST Limitations

Some rules cannot be fully verified via AST:
- Inline comments (stripped by parser) — use raw source grep
- Section header comments (`# ===`) — use raw source grep
- "Domain vocabulary" quality — heuristic name matching only
- "One operation per method" — heuristic, not mechanically provable

For these, use WARN or INFO severity and note the heuristic in the finding.
