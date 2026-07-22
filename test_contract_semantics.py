"""
Contract semantics verification for _reference pages.

PAG-03: Every data-testid exists in templates
PAG-04: No try/except in page files (L2 never catches)
PAG-05: No decorators, no screenshots, no waits inside action methods
PAG-06: Atomic methods return self; state-checks return bool/primitive
"""
import ast
import os
import re
import sys

PAGES_DIR = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/pages"
TEMPLATES_DIR = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/templates"

violations = []


def check_file(filepath, filename):
    with open(filepath) as f:
        source = f.read()
    tree = ast.parse(source)

    for node in ast.walk(tree):
        # PAG-04: No try/except
        if isinstance(node, (ast.Try, ast.ExceptHandler)):
            violations.append(f"{filename}: try/except found at line {node.lineno}")

        # PAG-05: No decorators
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in node.decorator_list:
                violations.append(f"{filename}: decorator on {node.name} at line {node.lineno}")

    # PAG-05: No screenshots
    if "screenshot" in source.lower():
        for i, line in enumerate(source.split("\n"), 1):
            if "screenshot" in line.lower() and not line.strip().startswith("#") and not line.strip().startswith('"""') and "conftest" in line.lower():
                continue
            if "screenshot" in line.lower() and not line.strip().startswith("#") and not line.strip().startswith('"""') and "No screenshots" not in line:
                violations.append(f"{filename}: 'screenshot' reference at line {i}: {line.strip()}")

    # PAG-05: No waits inside action methods (wait methods are their own methods)
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_name = item.name
                    if method_name.startswith("wait_") or method_name.startswith("__"):
                        continue
                    if method_name.startswith("is_") or method_name.startswith("has_") or method_name.startswith("get_"):
                        continue
                    # Action method — check for wait calls inside
                    for subnode in ast.walk(item):
                        if isinstance(subnode, ast.Call):
                            if isinstance(subnode.func, ast.Attribute):
                                if "wait" in subnode.func.attr.lower():
                                    violations.append(
                                        f"{filename}: wait call inside action method '{method_name}' at line {subnode.lineno}"
                                    )

    # PAG-06: Check return types
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name != "__init__":
                    method_name = item.name
                    if method_name.startswith("is_") or method_name.startswith("has_"):
                        # Must return bool — check annotation
                        if item.returns:
                            ret = ast.dump(item.returns)
                            if "bool" not in ret.lower():
                                violations.append(
                                    f"{filename}: state-check '{method_name}' should return bool, got {ast.unparse(item.returns)}"
                                )
                    elif method_name.startswith("get_"):
                        # Must return primitive (str, int, float, list)
                        if item.returns:
                            ret = ast.unparse(item.returns)
                            if ret not in ("str", "int", "float", "list", "bool"):
                                violations.append(
                                    f"{filename}: state-check '{method_name}' should return primitive, got {ret}"
                                )
                    elif method_name.startswith("wait_") or method_name.startswith("navigate") or method_name.startswith("click_") or method_name.startswith("enter_") or method_name.startswith("select_"):
                        # Atomic methods must return self (check return annotation)
                        if item.returns:
                            ret = ast.unparse(item.returns)
                            if class_name not in ret and "self" not in ret.lower():
                                violations.append(
                                    f"{filename}: atomic method '{method_name}' should return self/{class_name}, got {ret}"
                                )


# PAG-03: data-testid verification
template_testids = set()
for fname in os.listdir(TEMPLATES_DIR):
    if fname.endswith(".html"):
        with open(os.path.join(TEMPLATES_DIR, fname)) as f:
            content = f.read()
        for m in re.finditer(r'data-testid=["\']([^"\'{}]+)["\']', content):
            template_testids.add(m.group(1))
        # Dynamic testids
        for m in re.finditer(r'data-testid=["\']([^"\']+)["\']', content):
            val = m.group(1)
            if "{{" in val:
                prefix = re.sub(r"\{\{.*?\}\}", "", val).strip().rstrip("-")
                template_testids.add(prefix + "-*")

page_files = [f for f in os.listdir(PAGES_DIR) if f.endswith(".py") and f != "__init__.py"]

for fname in page_files:
    filepath = os.path.join(PAGES_DIR, fname)
    with open(filepath) as f:
        content = f.read()

    # Static testids
    for m in re.finditer(r"data-testid='([^'{]+)'", content):
        tid = m.group(1)
        if tid not in template_testids:
            violations.append(f"{fname}: testid '{tid}' not found in templates")

    # Prefix selectors
    for m in re.finditer(r"data-testid\^='([^']+)'", content):
        prefix = m.group(1)
        found = any(t.startswith(prefix) for t in template_testids) or (prefix + "*") in template_testids
        if not found:
            violations.append(f"{fname}: prefix testid '{prefix}*' not found in templates")

# Run structural checks on each file
for fname in page_files:
    filepath = os.path.join(PAGES_DIR, fname)
    print(f"Checking {fname}...")
    check_file(filepath, fname)

# Report
print()
if violations:
    print(f"FAIL: {len(violations)} violation(s):")
    for v in violations:
        print(f"  - {v}")
    sys.exit(1)
else:
    print("PASS: All contract semantics gates satisfied (PAG-03/04/05/06)")
    sys.exit(0)
