#!/usr/bin/env python3
"""AST-based contract semantics checker for _reference UI tests (task 003).

Checks per lessons #38/#39/#43:
  (a) no try/except outside pytest.raises
  (b) one AAA block per test method
  (c) asserts carry failure messages
  (d) acts only through Task/Role — no page-action calls, no Interface calls, no locators
  (e) no screenshot calls in test bodies
  (f) same-instance assertion rule (fixture identity)

All body-scoped rules iterate fn.body per-statement (never ast.walk(fn)).
Docstrings excluded from all string checks.
"""
import ast
import sys
import os

TARGET_DIR = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/tests"

PAGE_FIXTURES = {"login_page", "orders_page", "detail_page"}
TASK_FIXTURES = {"common_tasks", "order_workup"}
ROLE_FIXTURES = {"order_clerk", "order_manager"}
INTERFACE_NAMES = {"browser", "driver"}

SCREENSHOT_METHODS = {"take_screenshot", "screenshot", "save_screenshot", "get_screenshot_as_png"}

errors = []


def get_body_statements(fn_node):
    """Yield all statements in fn.body, skipping the docstring."""
    body = fn_node.body
    start = 0
    if (body and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, (ast.Constant, ast.Str))):
        start = 1
    for stmt in body[start:]:
        yield stmt


def walk_body(fn_node):
    """Walk all AST nodes in fn.body only, excluding docstring and decorators."""
    for stmt in get_body_statements(fn_node):
        yield from ast.walk(stmt)


def is_test_method(node):
    return isinstance(node, ast.FunctionDef) and node.name.startswith("test_")


def get_method_params(fn_node):
    """Return set of parameter names (excluding self)."""
    params = set()
    for arg in fn_node.args.args:
        if arg.arg != "self":
            params.add(arg.arg)
    return params


def check_no_try_except(fn_node, filename):
    """(a) No try/except outside pytest.raises context managers."""
    for stmt in get_body_statements(fn_node):
        for node in ast.walk(stmt):
            if isinstance(node, ast.Try):
                errors.append(
                    f"{filename}:{node.lineno} {fn_node.name}: "
                    f"try/except block found — only pytest.raises is allowed"
                )
            if isinstance(node, ast.With):
                for item in node.items:
                    call = item.context_expr
                    if isinstance(call, ast.Call):
                        func = call.func
                        if (isinstance(func, ast.Attribute)
                                and func.attr == "raises"
                                and isinstance(func.value, ast.Name)
                                and func.value.id == "pytest"):
                            pass


def check_aaa_pattern(fn_node, filename):
    """(b) One AAA block per test method — verify Arrange/Act/Assert comments exist."""
    comments_source_lines = []
    try:
        with open(os.path.join(TARGET_DIR, filename), "r") as f:
            source_lines = f.readlines()
    except FileNotFoundError:
        errors.append(f"{filename}: could not open file for AAA check")
        return

    fn_start = fn_node.lineno - 1
    fn_end = fn_node.end_lineno
    fn_lines = source_lines[fn_start:fn_end]

    aaa_markers = []
    for line in fn_lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            lower = stripped.lower()
            for marker in ("arrange", "act", "assert"):
                if marker in lower:
                    aaa_markers.append(marker)

    act_count = sum(1 for m in aaa_markers if m == "act")
    assert_count = sum(1 for m in aaa_markers if m == "assert")

    if act_count == 0 and assert_count == 0:
        errors.append(
            f"{filename}:{fn_node.lineno} {fn_node.name}: "
            f"missing AAA block comments (Arrange/Act/Assert)"
        )

    if act_count > 2 or assert_count > 2:
        errors.append(
            f"{filename}:{fn_node.lineno} {fn_node.name}: "
            f"multiple AAA blocks detected (act={act_count}, assert={assert_count}) — "
            f"one scenario per test method"
        )


def check_assert_messages(fn_node, filename):
    """(c) Every assert carries a failure message."""
    for stmt in get_body_statements(fn_node):
        for node in ast.walk(stmt):
            if isinstance(node, ast.Assert):
                if node.msg is None:
                    errors.append(
                        f"{filename}:{node.lineno} {fn_node.name}: "
                        f"assert without failure message"
                    )


def check_acts_through_task_role(fn_node, filename):
    """(d) Acts only through Task/Role — no page-action calls, Interface calls, or locators."""
    params = get_method_params(fn_node)
    page_params = params & PAGE_FIXTURES
    interface_params = params & INTERFACE_NAMES

    for stmt in get_body_statements(fn_node):
        if isinstance(stmt, ast.Assert):
            continue

        for node in ast.walk(stmt):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                obj = node.func.value
                if isinstance(obj, ast.Name):
                    if obj.id in page_params:
                        errors.append(
                            f"{filename}:{node.lineno} {fn_node.name}: "
                            f"action call on page object '{obj.id}.{node.func.attr}' — "
                            f"acts must go through Task/Role layer"
                        )
                    if obj.id in interface_params:
                        errors.append(
                            f"{filename}:{node.lineno} {fn_node.name}: "
                            f"direct Interface call '{obj.id}.{node.func.attr}' — "
                            f"tests never call Interface methods"
                        )

    for node in walk_body(fn_node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            val = node.value
            if any(pattern in val for pattern in
                   ["xpath", "css_selector", "By.", "//", "[data-testid"]):
                errors.append(
                    f"{filename}:{node.lineno} {fn_node.name}: "
                    f"locator string in test body: '{val[:60]}'"
                )


def check_no_screenshots(fn_node, filename):
    """(e) No screenshot calls in test bodies."""
    for node in walk_body(fn_node):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr in SCREENSHOT_METHODS:
                errors.append(
                    f"{filename}:{node.lineno} {fn_node.name}: "
                    f"screenshot call '{node.func.attr}' in test body"
                )


def check_same_instance(conftest_tree, test_tree, conftest_file, test_file):
    """(f) Same-instance assertion rule — page fixtures in asserts must be the fixtures wired into Tasks."""
    task_page_wiring = {}

    for node in ast.walk(conftest_tree):
        if isinstance(node, ast.FunctionDef) and node.name in TASK_FIXTURES:
            params = {a.arg for a in node.args.args}
            wired_pages = params & PAGE_FIXTURES
            task_page_wiring[node.name] = wired_pages

    for node in ast.walk(test_tree):
        if not is_test_method(node):
            continue

        test_params = get_method_params(node)
        test_tasks = test_params & TASK_FIXTURES
        test_roles = test_params & ROLE_FIXTURES

        wired_pages_via_tasks = set()
        for task in test_tasks:
            wired_pages_via_tasks |= task_page_wiring.get(task, set())

        for role in test_roles:
            for conftest_node in ast.walk(conftest_tree):
                if isinstance(conftest_node, ast.FunctionDef) and conftest_node.name == role:
                    role_params = {a.arg for a in conftest_node.args.args}
                    role_tasks = role_params & TASK_FIXTURES
                    for rt in role_tasks:
                        wired_pages_via_tasks |= task_page_wiring.get(rt, set())

        test_page_params = test_params & PAGE_FIXTURES

        for page in test_page_params:
            if page not in wired_pages_via_tasks:
                errors.append(
                    f"{test_file}:{node.lineno} {node.name}: "
                    f"page fixture '{page}' used in test but not wired into any "
                    f"Task/Role consumed by this test — fixture identity violation"
                )


def main():
    conftest_path = os.path.join(TARGET_DIR, "conftest.py")
    test_path = os.path.join(TARGET_DIR, "test_order_workup.py")

    with open(conftest_path, "r") as f:
        conftest_tree = ast.parse(f.read(), conftest_path)

    with open(test_path, "r") as f:
        test_tree = ast.parse(f.read(), test_path)

    for node in ast.walk(test_tree):
        if not is_test_method(node):
            continue
        check_no_try_except(node, "test_order_workup.py")
        check_aaa_pattern(node, "test_order_workup.py")
        check_assert_messages(node, "test_order_workup.py")
        check_acts_through_task_role(node, "test_order_workup.py")
        check_no_screenshots(node, "test_order_workup.py")

    check_same_instance(conftest_tree, test_tree, "conftest.py", "test_order_workup.py")

    if errors:
        print(f"FAIL: {len(errors)} contract violation(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("PASS: all contract semantics checks passed")
        print("  (a) no try/except outside pytest.raises")
        print("  (b) AAA pattern present in each test")
        print("  (c) all asserts carry failure messages")
        print("  (d) acts only through Task/Role layer")
        print("  (e) no screenshot calls")
        print("  (f) same-instance fixture identity verified")
        sys.exit(0)


if __name__ == "__main__":
    main()
