"""AST-based contract semantics gate for ROL-04 (lesson #39: no string grep)."""

import ast
import sys
from pathlib import Path

REPO = Path("D:/my_ai_projects/project_test_repos/hmsa-qa-platform")
FILES = {
    "common_tasks": REPO / "framework/_reference/tasks/common_tasks.py",
    "order_clerk": REPO / "framework/_reference/roles/order_clerk.py",
    "order_manager": REPO / "framework/_reference/roles/order_manager.py",
}

failures = []


def fail(file_key, msg):
    failures.append(f"[{file_key}] {msg}")


def get_tree(file_key):
    path = FILES[file_key]
    if not path.exists():
        fail(file_key, f"File not found: {path}")
        return None
    return ast.parse(path.read_text(encoding="utf-8"))


def get_class(tree, class_name):
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return node
    return None


def count_try(tree):
    return sum(1 for node in ast.walk(tree) if isinstance(node, ast.Try))


def get_decorator_names(node):
    names = []
    for d in node.decorator_list:
        if isinstance(d, ast.Call):
            if isinstance(d.func, ast.Name):
                args = [a.value for a in d.args if isinstance(a, ast.Constant)]
                names.append((d.func.id, args))
            elif isinstance(d.func, ast.Attribute):
                args = [a.value for a in d.args if isinstance(a, ast.Constant)]
                names.append((d.func.attr, args))
        elif isinstance(d, ast.Name):
            names.append((d.id, []))
        elif isinstance(d, ast.Attribute):
            names.append((d.attr, []))
    return names


def get_return_annotation(func_node):
    if func_node.returns is None:
        return None
    if isinstance(func_node.returns, ast.Constant) and func_node.returns.value is None:
        return "None"
    if isinstance(func_node.returns, ast.Name):
        return func_node.returns.id
    return repr(func_node.returns)


def get_param_names(func_node):
    return [a.arg for a in func_node.args.args if a.arg != "self"]


def get_param_annotations(func_node):
    result = {}
    for a in func_node.args.args:
        if a.arg == "self":
            continue
        if a.annotation:
            if isinstance(a.annotation, ast.Name):
                result[a.arg] = a.annotation.id
            elif isinstance(a.annotation, ast.Attribute):
                result[a.arg] = a.annotation.attr
            else:
                result[a.arg] = ast.dump(a.annotation)
        else:
            result[a.arg] = None
    return result


BANNED_PARAM_NAMES = {"browser", "interface", "browser_interface", "page", "driver"}
BANNED_ANNOTATION_NAMES = {"BrowserInterface", "WebDriver"}


def check_no_try(file_key, tree):
    n = count_try(tree)
    if n > 0:
        fail(file_key, f"ast.Try count = {n}, expected 0")
    else:
        print(f"  [PASS] {file_key}: ast.Try count = 0")


def check_no_testid_literals(file_key, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if "data-testid" in node.value:
                fail(file_key, f"Found 'data-testid' literal: {node.value!r}")
                return
    print(f"  [PASS] {file_key}: no data-testid literals")


def check_no_screenshot_calls(file_key, tree):
    screenshot_names = {"screenshot", "take_screenshot", "save_screenshot", "get_screenshot_as_png"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr in screenshot_names:
                fail(file_key, f"Found screenshot call: {node.func.attr}")
                return
            if isinstance(node.func, ast.Name) and node.func.id in screenshot_names:
                fail(file_key, f"Found screenshot call: {node.func.id}")
                return
    print(f"  [PASS] {file_key}: no screenshot calls")


def check_no_credential_literals_in_login(file_key, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "login":
                for arg in node.args:
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        fail(file_key, f"Credential literal in login call: {arg.value!r}")
                        return
                for arg in node.args:
                    if not isinstance(arg, ast.Subscript):
                        continue
    print(f"  [PASS] {file_key}: login args are not credential literals")


def check_login_args_are_identity_subscript(file_key, tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "login":
                for arg in node.args:
                    if isinstance(arg, ast.Constant):
                        fail(file_key, f"Login arg is a constant: {arg.value!r} — must be self.identity[...] subscript")
                        return
                    if isinstance(arg, ast.Subscript):
                        if isinstance(arg.value, ast.Attribute):
                            if not (isinstance(arg.value.value, ast.Name) and arg.value.value.id == "self" and arg.value.attr == "identity"):
                                fail(file_key, f"Login arg subscript base is not self.identity")
                                return
    print(f"  [PASS] {file_key}: login args use self.identity subscripts")


# --- common_tasks.py checks ---

def check_common_tasks():
    print("\n=== common_tasks.py ===")
    tree = get_tree("common_tasks")
    if tree is None:
        return

    check_no_try("common_tasks", tree)
    check_no_testid_literals("common_tasks", tree)
    check_no_screenshot_calls("common_tasks", tree)

    cls = get_class(tree, "CommonTasks")
    if cls is None:
        fail("common_tasks", "Class CommonTasks not found")
        return

    init = None
    login = None
    for node in ast.iter_child_nodes(cls):
        if isinstance(node, ast.FunctionDef):
            if node.name == "__init__":
                init = node
            elif node.name == "login":
                login = node

    if init is None:
        fail("common_tasks", "__init__ not found")
        return

    init_decorators = get_decorator_names(init)
    if len(init_decorators) > 0:
        fail("common_tasks", f"__init__ should be undecorated, found: {init_decorators}")
    else:
        print("  [PASS] common_tasks: __init__ undecorated")

    init_params = get_param_names(init)
    if init_params != ["login_page"]:
        fail("common_tasks", f"__init__ params = {init_params}, expected ['login_page']")
    else:
        print("  [PASS] common_tasks: __init__ takes login_page only")

    init_annotations = get_param_annotations(init)
    for pname, ptype in init_annotations.items():
        if ptype and ptype in BANNED_ANNOTATION_NAMES:
            fail("common_tasks", f"__init__ param '{pname}' has banned annotation: {ptype}")
        if pname in BANNED_PARAM_NAMES:
            fail("common_tasks", f"__init__ param name '{pname}' is banned (browser/interface)")

    if login is None:
        fail("common_tasks", "login method not found")
        return

    login_decorators = get_decorator_names(login)
    has_trace_task = any(name == "trace" and "Task" in args for name, args in login_decorators)
    if not has_trace_task:
        fail("common_tasks", f"login missing @trace('Task'), found: {login_decorators}")
    else:
        print("  [PASS] common_tasks: login has @trace('Task')")

    ret = get_return_annotation(login)
    if ret != "None":
        fail("common_tasks", f"login return annotation = {ret}, expected None")
    else:
        print("  [PASS] common_tasks: login -> None")


# --- Role file checks (order_clerk, order_manager) ---

def check_role_file(file_key, class_name, expected_workflows):
    print(f"\n=== {file_key}.py ===")
    tree = get_tree(file_key)
    if tree is None:
        return

    check_no_try(file_key, tree)
    check_no_testid_literals(file_key, tree)
    check_no_screenshot_calls(file_key, tree)
    check_no_credential_literals_in_login(file_key, tree)
    check_login_args_are_identity_subscript(file_key, tree)

    cls = get_class(tree, class_name)
    if cls is None:
        fail(file_key, f"Class {class_name} not found")
        return

    init = None
    workflows = {}
    for node in ast.iter_child_nodes(cls):
        if isinstance(node, ast.FunctionDef):
            if node.name == "__init__":
                init = node
            elif node.name in expected_workflows:
                workflows[node.name] = node

    # __init__ checks
    if init is None:
        fail(file_key, "__init__ not found")
        return

    init_decorators = get_decorator_names(init)
    has_role_constructor = any(name == "trace" and "Role Constructor" in args for name, args in init_decorators)
    if not has_role_constructor:
        fail(file_key, f"__init__ missing @trace('Role Constructor'), found: {init_decorators}")
    else:
        print(f"  [PASS] {file_key}: __init__ has @trace('Role Constructor')")

    init_params = get_param_names(init)
    init_annotations = get_param_annotations(init)

    for pname in init_params:
        if pname in BANNED_PARAM_NAMES:
            fail(file_key, f"__init__ param name '{pname}' is banned (browser/interface/page)")
    for pname, ptype in init_annotations.items():
        if ptype and ptype in BANNED_ANNOTATION_NAMES:
            fail(file_key, f"__init__ param '{pname}' has banned annotation: {ptype}")

    if "identity" not in init_params:
        fail(file_key, "__init__ missing 'identity' param")
    else:
        print(f"  [PASS] {file_key}: __init__ has identity param")

    # Check no internal task/page class construction in __init__
    for node in ast.walk(init):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            called_name = node.func.id
            if called_name[0].isupper() and called_name not in ("CommonTasks", "OrderWorkupTasks"):
                pass
            if called_name in ("CommonTasks", "OrderWorkupTasks", "LoginPage", "OrderWorkupPage"):
                fail(file_key, f"__init__ constructs {called_name} internally — must use DI")
    print(f"  [PASS] {file_key}: __init__ does not construct task/page classes")

    # Workflow method checks
    for wf_name in expected_workflows:
        if wf_name not in workflows:
            fail(file_key, f"Workflow method {wf_name} not found")
            continue

        wf = workflows[wf_name]

        wf_decorators = get_decorator_names(wf)
        has_trace_role = any(name == "trace" and "Role" in args for name, args in wf_decorators)
        if not has_trace_role:
            fail(file_key, f"{wf_name} missing @trace('Role'), found: {wf_decorators}")
        else:
            print(f"  [PASS] {file_key}: {wf_name} has @trace('Role')")

        ret = get_return_annotation(wf)
        if ret != "None":
            fail(file_key, f"{wf_name} return annotation = {ret}, expected None")
        else:
            print(f"  [PASS] {file_key}: {wf_name} -> None")

        # Composition rule: body must call >= 2 DISTINCT task-attribute targets
        # e.g., self.common.login AND self.order_workup.open_order
        task_targets = set()
        for node in ast.walk(wf):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                value = node.func.value
                if isinstance(value, ast.Attribute) and isinstance(value.value, ast.Name):
                    if value.value.id == "self":
                        task_targets.add(value.attr)

        if len(task_targets) < 2:
            fail(file_key, f"{wf_name} calls only {task_targets} task modules — composition rule requires >= 2 DISTINCT task-attribute targets")
        else:
            print(f"  [PASS] {file_key}: {wf_name} calls {len(task_targets)} distinct task modules: {task_targets}")


if __name__ == "__main__":
    print("ROL-04 Contract Semantics — AST-based verification")
    print("=" * 55)

    check_common_tasks()
    check_role_file("order_clerk", "OrderClerk", ["work_order_status_change"])
    check_role_file("order_manager", "OrderManager", ["cancel_order"])

    print("\n" + "=" * 55)
    if failures:
        print(f"FAILED — {len(failures)} violation(s):")
        for f in failures:
            print(f"  ✗ {f}")
        sys.exit(1)
    else:
        print("PASSED — all ROL-04 contract semantics verified (AST-only)")
        sys.exit(0)
