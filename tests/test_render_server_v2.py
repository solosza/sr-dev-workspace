"""Tests for render_server.py v2 — v1 regression + /status + AST law.

Task 005 of backlog 233 (render-reply-channel).
Gates: RC-01, RC-02.
"""

import ast
import json
import os
import signal
import subprocess
import sys
import tempfile
import time
import urllib.request
import urllib.error

SERVER_SCRIPT = os.path.join(
    os.path.dirname(__file__),
    os.pardir,
    ".claude",
    "skills",
    "render",
    "lib",
    "render_server.py",
)
SERVER_SCRIPT = os.path.normpath(SERVER_SCRIPT)

STDLIB_MODULES = frozenset([
    "http", "http.server", "json", "os", "socketserver", "sys",
    "pathlib", "io", "threading", "signal", "time", "tempfile",
    "shutil", "hashlib", "re", "functools", "typing", "collections",
    "abc", "contextlib", "copy", "datetime", "enum", "itertools",
    "logging", "math", "operator", "string", "struct", "textwrap",
    "traceback", "unittest", "uuid", "warnings", "xml", "html",
    "socket", "select", "selectors", "subprocess", "urllib",
])


def _start_server(session_dir):
    proc = subprocess.Popen(
        [sys.executable, SERVER_SCRIPT, session_dir],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    line = proc.stdout.readline().decode().strip()
    assert line.startswith("PORT="), f"Expected PORT=<n>, got: {line!r}"
    port = int(line.split("=", 1)[1])
    return proc, port


def _request(port, method, path, body=None, content_type="application/json"):
    url = f"http://127.0.0.1:{port}{path}"
    data = body.encode() if isinstance(body, str) else body
    req = urllib.request.Request(url, data=data, method=method)
    if content_type and data is not None:
        req.add_header("Content-Type", content_type)
    try:
        resp = urllib.request.urlopen(req, timeout=5)
        return resp.status, resp.read(), dict(resp.headers)
    except urllib.error.HTTPError as e:
        return e.code, e.read(), dict(e.headers)


# ── v1 regression tests ──────────────────────────────────────────────

def test_get_root_serves_page():
    with tempfile.TemporaryDirectory() as td:
        html = b"<html><body>hello</body></html>"
        with open(os.path.join(td, "page.html"), "wb") as f:
            f.write(html)
        proc, port = _start_server(td)
        try:
            status, body, headers = _request(port, "GET", "/")
            assert status == 200
            assert body == html
            assert "text/html" in headers.get("Content-Type", "")
        finally:
            proc.kill()
            proc.wait()


def test_get_root_404_when_no_page():
    with tempfile.TemporaryDirectory() as td:
        proc, port = _start_server(td)
        try:
            status, _, _ = _request(port, "GET", "/")
            assert status == 404
        finally:
            proc.kill()
            proc.wait()


def test_post_annotate_valid():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            annotation = {
                "target": "card-1",
                "action": "reject",
                "raw_words": "not relevant",
                "at": "2026-07-15T00:00:00Z",
            }
            status, body, _ = _request(port, "POST", "/annotate", json.dumps(annotation))
            assert status == 200
            result = json.loads(body)
            assert result == {"ok": True}

            ann_path = os.path.join(td, "annotations.json")
            assert os.path.isfile(ann_path)
            with open(ann_path, "r") as f:
                saved = json.loads(f.read())
            assert len(saved) == 1
            assert saved[0]["target"] == "card-1"
            assert saved[0]["raw_words"] == "not relevant"
        finally:
            proc.kill()
            proc.wait()


def test_post_annotate_malformed_json():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            status, _, _ = _request(port, "POST", "/annotate", "not json{{{")
            assert status == 400
        finally:
            proc.kill()
            proc.wait()


def test_post_annotate_missing_fields():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            status, _, _ = _request(
                port, "POST", "/annotate", json.dumps({"target": "x"})
            )
            assert status == 400
        finally:
            proc.kill()
            proc.wait()


def test_post_annotate_empty_body():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            status, _, _ = _request(port, "POST", "/annotate", "")
            assert status in (400, 411)
        finally:
            proc.kill()
            proc.wait()


def test_post_annotate_not_object():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            status, _, _ = _request(port, "POST", "/annotate", json.dumps([1, 2, 3]))
            assert status == 400
        finally:
            proc.kill()
            proc.wait()


def test_atomicity_multiple_annotations():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            for i in range(5):
                annotation = {
                    "target": f"card-{i}",
                    "action": "accept",
                    "raw_words": f"note {i}",
                    "at": f"2026-07-15T00:0{i}:00Z",
                }
                status, _, _ = _request(port, "POST", "/annotate", json.dumps(annotation))
                assert status == 200

            ann_path = os.path.join(td, "annotations.json")
            with open(ann_path, "r") as f:
                saved = json.loads(f.read())
            assert len(saved) == 5
            targets = {a["target"] for a in saved}
            assert targets == {f"card-{i}" for i in range(5)}
        finally:
            proc.kill()
            proc.wait()


def test_localhost_only_binding():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            source = open(SERVER_SCRIPT, "r").read()
            assert '("127.0.0.1"' in source or "('127.0.0.1'" in source
        finally:
            proc.kill()
            proc.wait()


def test_unknown_path_404():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            status, _, _ = _request(port, "GET", "/nonexistent")
            assert status == 404
        finally:
            proc.kill()
            proc.wait()


# ── /status route tests ──────────────────────────────────────────────

def test_status_absent_reply_file():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        try:
            status, body, headers = _request(port, "GET", "/status")
            assert status == 200
            data = json.loads(body)
            assert data == {"status": "idle"}
            assert "application/json" in headers.get("Content-Type", "")
        finally:
            proc.kill()
            proc.wait()


def test_status_present_reply_file():
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        reply_content = {
            "confirms": [
                {"target": "card-1", "question": "Accept this?", "options": ["yes", "no"]}
            ],
            "results": [],
        }
        reply_path = os.path.join(td, "session-reply.json")
        with open(reply_path, "w") as f:
            json.dump(reply_content, f)
        proc, port = _start_server(td)
        try:
            status, body, headers = _request(port, "GET", "/status")
            assert status == 200
            data = json.loads(body)
            assert data == reply_content
            assert "application/json" in headers.get("Content-Type", "")
        finally:
            proc.kill()
            proc.wait()


def test_status_serves_exact_bytes():
    """Reply file content served verbatim — byte-for-byte."""
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        raw_bytes = b'{"custom":  "spaced",\n  "key": 42}'
        reply_path = os.path.join(td, "session-reply.json")
        with open(reply_path, "wb") as f:
            f.write(raw_bytes)
        proc, port = _start_server(td)
        try:
            status, body, _ = _request(port, "GET", "/status")
            assert status == 200
            assert body == raw_bytes
        finally:
            proc.kill()
            proc.wait()


# ── AST law tests (lessons #39/#43) ──────────────────────────────────

def _parse_server():
    with open(SERVER_SCRIPT, "r") as f:
        return ast.parse(f.read(), filename=SERVER_SCRIPT)


def _get_function_body_calls(tree, class_name, method_name):
    """Get all ast.Call nodes from a method's BODY only (not decorators/annotations)."""
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name == method_name:
                        calls = []
                        for stmt in item.body:
                            for child in ast.walk(stmt):
                                if isinstance(child, ast.Call):
                                    calls.append(child)
                        return calls
    return []


def _extract_string_arg(call_node, arg_index=0):
    """Extract a string constant from a call's positional argument."""
    if len(call_node.args) > arg_index:
        arg = call_node.args[arg_index]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            return arg.value
    return None


def test_ast_write_targets_frozen():
    """Write targets == {tmp_path (.annotations.tmp), os.replace→annotations_path} exactly (SET comparison)."""
    tree = _parse_server()
    source = open(SERVER_SCRIPT, "r").read()

    write_filenames = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if isinstance(node, ast.FunctionDef) and node.name in ("__init__",):
            continue
        for stmt in node.body:
            for child in ast.walk(stmt):
                if not isinstance(child, ast.Call):
                    continue
                func = child.func
                if isinstance(func, ast.Name) and func.id == "open":
                    for kw in child.keywords:
                        if kw.arg == "mode":
                            if isinstance(kw.value, ast.Constant) and "w" in str(kw.value.value):
                                fname = _extract_string_arg(child, 0)
                                if fname:
                                    write_filenames.add(fname)
                    if len(child.args) >= 2:
                        mode_arg = child.args[1]
                        if isinstance(mode_arg, ast.Constant) and "w" in str(mode_arg.value):
                            fname = _extract_string_arg(child, 0)
                            if fname:
                                write_filenames.add(fname)

    open_write_calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for stmt in item.body:
                        for child in ast.walk(stmt):
                            if isinstance(child, ast.Call):
                                func = child.func
                                if isinstance(func, ast.Name) and func.id == "open":
                                    mode = None
                                    if len(child.args) >= 2:
                                        m = child.args[1]
                                        if isinstance(m, ast.Constant):
                                            mode = m.value
                                    for kw in child.keywords:
                                        if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                                            mode = kw.value.value
                                    if mode and "w" in mode:
                                        open_write_calls.append(child)

    os_replace_calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for stmt in item.body:
                        for child in ast.walk(stmt):
                            if isinstance(child, ast.Call):
                                func = child.func
                                if isinstance(func, ast.Attribute) and func.attr == "replace":
                                    if isinstance(func.value, ast.Name) and func.value.id == "os":
                                        os_replace_calls.append(child)

    assert len(open_write_calls) == 1, f"Expected exactly 1 open(write) call, got {len(open_write_calls)}"
    assert len(os_replace_calls) == 1, f"Expected exactly 1 os.replace call, got {len(os_replace_calls)}"

    write_call = open_write_calls[0]
    write_target = write_call.args[0]
    assert isinstance(write_target, ast.Name) and write_target.id == "tmp_path", \
        f"open(write) target should be tmp_path, got {ast.dump(write_target)}"

    replace_call = os_replace_calls[0]
    replace_dst = replace_call.args[1]
    assert isinstance(replace_dst, ast.Name) and replace_dst.id == "annotations_path", \
        f"os.replace dst should be annotations_path, got {ast.dump(replace_dst)}"


def test_ast_served_reads():
    """Served reads ⊆ {page.html, session-reply.json}."""
    tree = _parse_server()
    allowed_reads = {"page.html", "session-reply.json"}

    served_filenames = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "RenderHandler":
            for item in node.body:
                if isinstance(item, ast.FunctionDef) and item.name.startswith("do_GET"):
                    for stmt in item.body:
                        for child in ast.walk(stmt):
                            if isinstance(child, ast.Call):
                                func = child.func
                                if isinstance(func, ast.Attribute) and func.attr == "join":
                                    if len(child.args) >= 2:
                                        fname_arg = child.args[-1]
                                        if isinstance(fname_arg, ast.Constant) and isinstance(fname_arg.value, str):
                                            served_filenames.add(fname_arg.value)

    assert served_filenames, "Should find at least one served filename"
    assert served_filenames <= allowed_reads, \
        f"Served reads {served_filenames} not subset of {allowed_reads}"
    assert served_filenames == allowed_reads, \
        f"Expected exactly {allowed_reads}, got {served_filenames}"


def test_ast_imports_stdlib_only():
    """All imports must be stdlib-only."""
    tree = _parse_server()

    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported.add(node.module.split(".")[0])

    non_stdlib = imported - STDLIB_MODULES
    assert not non_stdlib, f"Non-stdlib imports found: {non_stdlib}"


def test_ast_no_file_writes_outside_do_post():
    """No open(write) or os.replace calls exist outside do_POST body (docstrings excluded)."""
    tree = _parse_server()

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "RenderHandler":
            for item in node.body:
                if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                if item.name == "do_POST":
                    continue
                for stmt in item.body:
                    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
                        continue
                    for child in ast.walk(stmt):
                        if isinstance(child, ast.Call):
                            func = child.func
                            if isinstance(func, ast.Name) and func.id == "open":
                                mode = None
                                if len(child.args) >= 2:
                                    m = child.args[1]
                                    if isinstance(m, ast.Constant):
                                        mode = m.value
                                for kw in child.keywords:
                                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                                        mode = kw.value.value
                                assert not (mode and "w" in mode), \
                                    f"open(write) found in {item.name}, not do_POST"
                            if isinstance(func, ast.Attribute) and func.attr == "replace":
                                if isinstance(func.value, ast.Name) and func.value.id == "os":
                                    assert False, f"os.replace found in {item.name}, not do_POST"

    for node in ast.iter_child_nodes(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name == "main":
                for stmt in node.body:
                    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
                        continue
                    for child in ast.walk(stmt):
                        if isinstance(child, ast.Call):
                            func = child.func
                            if isinstance(func, ast.Name) and func.id == "open":
                                mode = None
                                if len(child.args) >= 2:
                                    m = child.args[1]
                                    if isinstance(m, ast.Constant):
                                        mode = m.value
                                for kw in child.keywords:
                                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                                        mode = kw.value.value
                                assert not (mode and "w" in mode), \
                                    "open(write) found in main(), not do_POST"


# ── Kill by PID in finally (test infra) ──────────────────────────────

def test_server_kill_by_pid():
    """Server can be killed by PID; cleanup works."""
    with tempfile.TemporaryDirectory() as td:
        with open(os.path.join(td, "page.html"), "w") as f:
            f.write("<html></html>")
        proc, port = _start_server(td)
        pid = proc.pid
        try:
            status, _, _ = _request(port, "GET", "/")
            assert status == 200
        finally:
            proc.kill()
            proc.wait()
        assert proc.returncode is not None


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-v"]))
