"""
AIF-03 Contract Semantics — AST-based validation.

Checks api_interface.py against the 5-layer contract:
1. Every except handler re-raises (or is a documented primitive-return state check)
2. No screenshot/save call names
3. No domain vocabulary (order/customer/patient/claim) in identifiers or string literals
4. Imports subset of stdlib + requests
5. Each verb method body includes a logging call (body-scoped, decorator-aware)

Lessons applied: #38 (AST-only), #39 (docstrings excluded), #43 (body-scoped walk, decorator-aware)
"""

import ast
import sys

TARGET = sys.argv[1] if len(sys.argv) > 1 else None
if not TARGET:
    print("FAIL: Usage: python check_contract_semantics.py <path_to_api_interface.py>")
    sys.exit(1)

with open(TARGET, 'r') as f:
    source = f.read()

tree = ast.parse(source)
failures = []
checks_run = 0

STDLIB_MODULES = {
    'logging', 'time', 'dataclasses', 'typing', 'os', 'sys', 'json',
    'pathlib', 'collections', 'abc', 'functools', 'contextlib',
    'enum', 'copy', 'inspect', 're', 'datetime', 'io', 'traceback',
}
ALLOWED_THIRD_PARTY = {'requests'}
ALLOWED_IMPORTS = STDLIB_MODULES | ALLOWED_THIRD_PARTY

DOMAIN_WORDS = {'order', 'orders', 'customer', 'customers', 'patient', 'patients', 'claim', 'claims'}
SCREENSHOT_WORDS = {'screenshot', 'save_screenshot', 'take_screenshot', 'capture_screenshot'}
VERB_METHODS = {'get', 'post', 'put', 'patch', 'delete'}


def is_docstring(node, body):
    """Check if a node is the docstring (first Expr(Constant(str)) in body)."""
    if not body:
        return False
    first = body[0]
    return (
        first is node
        and isinstance(first, ast.Expr)
        and isinstance(first.value, ast.Constant)
        and isinstance(first.value.value, str)
    )


def walk_body_statements(body):
    """Walk all nodes in body statements, excluding docstrings. Body-scoped only."""
    for i, stmt in enumerate(body):
        if i == 0 and isinstance(stmt, ast.Expr) and isinstance(getattr(stmt, 'value', None), ast.Constant) and isinstance(stmt.value.value, str):
            continue
        for node in ast.walk(stmt):
            yield node


# === CHECK 1: Except handlers re-raise ===
checks_run += 1
print("CHECK 1: except-handlers-reraise")
for node in ast.walk(tree):
    if isinstance(node, ast.Try):
        for handler in node.handlers:
            has_raise = False
            for child in ast.walk(handler):
                if isinstance(child, ast.Raise):
                    has_raise = True
                    break
            if not has_raise:
                lineno = handler.lineno
                handler_type = "bare except"
                if handler.type:
                    if isinstance(handler.type, ast.Name):
                        handler_type = handler.type.id
                    elif isinstance(handler.type, ast.Attribute):
                        handler_type = ast.dump(handler.type)
                failures.append(f"  LINE {lineno}: except {handler_type} — no re-raise found")

if not any("CHECK 1" in f for f in failures):
    print("  PASS: all except handlers re-raise")
else:
    for f in failures:
        if "LINE" in f:
            print(f)


# === CHECK 2: No screenshot/save call names ===
checks_run += 1
print("CHECK 2: no-screenshot-calls")
screenshot_violations = []
for node in ast.walk(tree):
    if isinstance(node, ast.Call):
        func = node.func
        name = None
        if isinstance(func, ast.Name):
            name = func.id
        elif isinstance(func, ast.Attribute):
            name = func.attr
        if name and name.lower() in SCREENSHOT_WORDS:
            screenshot_violations.append(f"  LINE {node.lineno}: call to '{name}'")

if screenshot_violations:
    failures.extend(screenshot_violations)
    for v in screenshot_violations:
        print(v)
else:
    print("  PASS: no screenshot/save calls found")


# === CHECK 3: No domain vocabulary ===
checks_run += 1
print("CHECK 3: no-domain-vocabulary")
domain_violations = []

for node in ast.walk(tree):
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        body = node.body
        for child in walk_body_statements(body):
            if isinstance(child, ast.Name) and child.id.lower() in DOMAIN_WORDS:
                domain_violations.append(f"  LINE {child.lineno}: identifier '{child.id}'")
            if isinstance(child, ast.Constant) and isinstance(child.value, str):
                val_lower = child.value.lower()
                for dw in DOMAIN_WORDS:
                    if dw in val_lower.split():
                        domain_violations.append(f"  LINE {child.lineno}: string literal contains '{dw}'")
                        break
            if isinstance(child, ast.Attribute) and child.attr.lower() in DOMAIN_WORDS:
                domain_violations.append(f"  LINE {child.lineno}: attribute '{child.attr}'")
        if node.name.lower() in DOMAIN_WORDS:
            domain_violations.append(f"  LINE {node.lineno}: definition name '{node.name}'")

# Also check module-level non-docstring strings
module_body = tree.body
for child in walk_body_statements(module_body):
    if isinstance(child, ast.Name) and child.id.lower() in DOMAIN_WORDS:
        domain_violations.append(f"  LINE {child.lineno}: module-level identifier '{child.id}'")
    if isinstance(child, ast.Constant) and isinstance(child.value, str):
        val_lower = child.value.lower()
        for dw in DOMAIN_WORDS:
            if dw in val_lower.split():
                domain_violations.append(f"  LINE {child.lineno}: module-level string contains '{dw}'")
                break

if domain_violations:
    unique = list(dict.fromkeys(domain_violations))
    failures.extend(unique)
    for v in unique:
        print(v)
else:
    print("  PASS: no domain vocabulary found")


# === CHECK 4: Imports subset of stdlib + requests ===
checks_run += 1
print("CHECK 4: imports-allowed")
import_violations = []

for node in ast.walk(tree):
    if isinstance(node, ast.Import):
        for alias in node.names:
            top = alias.name.split('.')[0]
            if top not in ALLOWED_IMPORTS:
                import_violations.append(f"  LINE {node.lineno}: import '{alias.name}' — not in allowed set")
    elif isinstance(node, ast.ImportFrom):
        if node.module:
            top = node.module.split('.')[0]
            if top not in ALLOWED_IMPORTS:
                import_violations.append(f"  LINE {node.lineno}: from '{node.module}' — not in allowed set")

if import_violations:
    failures.extend(import_violations)
    for v in import_violations:
        print(v)
else:
    print("  PASS: all imports within allowed set (stdlib + requests)")


# === CHECK 5: Verb methods have logging calls in body ===
checks_run += 1
print("CHECK 5: verb-methods-logging")
logging_violations = []

for node in ast.walk(tree):
    if isinstance(node, ast.ClassDef):
        for item in node.body:
            if isinstance(item, ast.FunctionDef) and item.name in VERB_METHODS:
                has_log = False
                for stmt in item.body:
                    if isinstance(stmt, ast.Expr) and isinstance(getattr(stmt, 'value', None), ast.Constant) and isinstance(stmt.value.value, str):
                        continue
                    for child in ast.walk(stmt):
                        if isinstance(child, ast.Call):
                            func = child.func
                            if isinstance(func, ast.Attribute):
                                if func.attr in ('info', 'debug', 'warning', 'error', 'critical', 'log'):
                                    has_log = True
                                    break
                    if has_log:
                        break
                if not has_log:
                    logging_violations.append(f"  LINE {item.lineno}: verb method '{item.name}' — no logging call in body")

if logging_violations:
    failures.extend(logging_violations)
    for v in logging_violations:
        print(v)
else:
    print("  PASS: all verb methods have logging calls")


# === SUMMARY ===
print(f"\n--- SUMMARY ---")
print(f"Checks run: {checks_run}")
print(f"Failures: {len(failures)}")

if failures:
    print("\nFAILED CHECKS:")
    for f in failures:
        print(f)
    sys.exit(1)
else:
    print("\nALL CHECKS PASSED — contract semantics verified via AST")
    sys.exit(0)
