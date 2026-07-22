"""AST-based verification: stdlib-only imports + single-output-path law for render runtime."""
import ast
import sys

RENDER_SERVER = r"D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\skills\render\lib\render_server.py"
GENERATE = r"D:\my_ai_projects\project_test_repos\sr_dev_workspace\.claude\skills\render\templates\review-board\generate.py"

SERVER_ALLOWLIST = frozenset({
    "http", "socketserver", "json", "os", "sys",
    "tempfile", "pathlib", "datetime", "urllib",
})

failures = []


def fail(msg):
    failures.append(msg)
    print(f"  FAIL: {msg}")


def collect_docstring_ids(tree):
    ids = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if (node.body
                    and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Constant)
                    and isinstance(node.body[0].value.value, str)):
                ids.add(id(node.body[0].value))
    return ids


def check_imports(tree, allowlist, label):
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top = alias.name.split(".")[0]
                if top not in allowlist:
                    fail(f"{label}:{node.lineno} — import '{alias.name}' (top-level '{top}') not in allowlist")
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                top = node.module.split(".")[0]
                if top not in allowlist:
                    fail(f"{label}:{node.lineno} — from '{node.module}' (top-level '{top}') not in allowlist")


def check_no_state_refs(tree, label):
    docstring_ids = collect_docstring_ids(tree)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if id(node) in docstring_ids:
                continue
            if ".claude/state" in node.value or ".claude\\state" in node.value:
                fail(f"{label}:{node.lineno} — string references .claude/state: {node.value!r:.80}")


def find_open_writes(tree):
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not (isinstance(func, ast.Name) and func.id == "open"):
            continue
        mode = None
        if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
            mode = node.args[1].value
        for kw in node.keywords:
            if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                mode = kw.value.value
        if mode and isinstance(mode, str) and any(c in mode for c in ("w", "a", "x", "+")):
            results.append((node.lineno, mode))
    return results


def find_os_replace(tree):
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if (isinstance(func, ast.Attribute)
                and func.attr == "replace"
                and isinstance(func.value, ast.Name)
                and func.value.id == "os"):
            results.append(node.lineno)
    return results


def find_path_writes(tree):
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if isinstance(func, ast.Attribute) and func.attr.startswith("write_"):
            results.append((node.lineno, func.attr))
    return results


def find_tempfile_usage(tree):
    results = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if (isinstance(func, ast.Attribute)
                and isinstance(func.value, ast.Name)
                and func.value.id == "tempfile"):
            results.append((node.lineno, func.attr))
    return results


def verify_join_derives_session_dir(tree, varnames):
    found = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not (len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)):
            continue
        name = node.targets[0].id
        if name not in varnames:
            continue
        val = node.value
        if not (isinstance(val, ast.Call)
                and isinstance(val.func, ast.Attribute)
                and val.func.attr == "join"
                and val.args):
            continue
        first = val.args[0]
        if isinstance(first, ast.Attribute) and first.attr == "session_dir":
            found.add(name)
        elif isinstance(first, ast.Name) and first.id == "session_dir":
            found.add(name)
    return found


def check_server_writes(tree, label):
    writes = find_open_writes(tree)
    replaces = find_os_replace(tree)
    path_writes = find_path_writes(tree)
    tempfile_calls = find_tempfile_usage(tree)

    print(f"  open(write): {len(writes)} {writes}")
    print(f"  os.replace:  {len(replaces)} lines={replaces}")
    print(f"  Path.write_*: {len(path_writes)}")
    print(f"  tempfile.*:  {len(tempfile_calls)}")

    if len(writes) != 1:
        fail(f"{label}: expected 1 open-for-write, got {len(writes)}")
    if len(replaces) != 1:
        fail(f"{label}: expected 1 os.replace, got {len(replaces)}")
    if path_writes:
        fail(f"{label}: unexpected Path.write_* at {[l for l, _ in path_writes]}")
    if tempfile_calls:
        fail(f"{label}: unexpected tempfile.* at {[l for l, _ in tempfile_calls]}")

    derived = verify_join_derives_session_dir(tree, {"tmp_path", "annotations_path"})
    if "tmp_path" not in derived:
        fail(f"{label}: tmp_path not derived from session_dir via os.path.join")
    if "annotations_path" not in derived:
        fail(f"{label}: annotations_path not derived from session_dir via os.path.join")


def check_generate_writes(tree, label):
    writes = find_open_writes(tree)
    replaces = find_os_replace(tree)
    path_writes = find_path_writes(tree)

    print(f"  open(write): {len(writes)} {writes}")
    print(f"  os.replace:  {len(replaces)} lines={replaces}")
    print(f"  Path.write_*: {len(path_writes)}")

    if len(writes) != 1:
        fail(f"{label}: expected 1 open-for-write, got {len(writes)}")
    if replaces:
        fail(f"{label}: unexpected os.replace at lines {replaces}")
    if path_writes:
        fail(f"{label}: unexpected Path.write_* at {[l for l, _ in path_writes]}")

    found = False
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if not (len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == "out_path"):
            continue
        val = node.value
        if (isinstance(val, ast.Call)
                and isinstance(val.func, ast.Attribute)
                and val.func.attr == "join"
                and len(val.args) >= 2
                and isinstance(val.args[0], ast.Name) and val.args[0].id == "session_dir"
                and isinstance(val.args[1], ast.Constant) and val.args[1].value == "page.html"):
            found = True
    if not found:
        fail(f"{label}: out_path not set to os.path.join(session_dir, 'page.html')")


print("=" * 60)
print("Task 006: AST Semantics — Single-Output-Path + stdlib-only")
print("=" * 60)

print("\n--- render_server.py ---")
with open(RENDER_SERVER, "r", encoding="utf-8") as f:
    server_tree = ast.parse(f.read(), filename="render_server.py")

print("1. Import allowlist check:")
check_imports(server_tree, SERVER_ALLOWLIST, "render_server.py")
print("  OK" if not failures else "")

before = len(failures)
print("2. Write-target analysis:")
check_server_writes(server_tree, "render_server.py")
if len(failures) == before:
    print("  OK")

before = len(failures)
print("3. No .claude/state string refs:")
check_no_state_refs(server_tree, "render_server.py")
if len(failures) == before:
    print("  OK")

print("\n--- generate.py ---")
with open(GENERATE, "r", encoding="utf-8") as f:
    gen_tree = ast.parse(f.read(), filename="generate.py")

try:
    stdlib_names = sys.stdlib_module_names
except AttributeError:
    stdlib_names = SERVER_ALLOWLIST | frozenset({
        "html", "string", "re", "io", "collections", "itertools",
        "functools", "typing", "abc", "math", "decimal", "fractions",
        "random", "statistics", "struct", "codecs", "unicodedata",
        "textwrap", "enum", "numbers", "array", "copy", "pprint",
        "reprlib", "dataclasses", "contextlib", "operator",
    })

before = len(failures)
print("4. Stdlib-only import check:")
check_imports(gen_tree, stdlib_names, "generate.py")
if len(failures) == before:
    print("  OK")

before = len(failures)
print("5. Write-target analysis:")
check_generate_writes(gen_tree, "generate.py")
if len(failures) == before:
    print("  OK")

before = len(failures)
print("6. No .claude/state string refs:")
check_no_state_refs(gen_tree, "generate.py")
if len(failures) == before:
    print("  OK")

print(f"\n{'=' * 60}")
if failures:
    print(f"FAILED: {len(failures)} violation(s)")
    for v in failures:
        print(f"  - {v}")
    sys.exit(1)
else:
    print("PASSED: All 6 checks green")
    print("  stdlib-only imports, single-output-path, no .claude/state refs")
    sys.exit(0)
