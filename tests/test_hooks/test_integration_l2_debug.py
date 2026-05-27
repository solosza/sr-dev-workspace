"""Integration L2 Debug: All 4 hooks block debug statements consistently.

Phase 6.2 gate: Feed debug code to all 4 workspaces, verify all 4 block
with consistent message and exit code 2.

Tests multiple debug patterns:
- print() basic call
- pprint() call
- Indented print (inside function)
- print with f-string
- Non-debug print in comments (should NOT trigger)
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HOOKS = {
    "sr_dev": "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py",
    "hmsa": "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/hooks/hmsa_healthcare_qa-gate-enforcer.py",
    "gamedev": "D:/my_ai_projects/project_test_repos/game-dev/.claude/hooks/game_engine-gate-enforcer.py",
    "ssh": "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/.claude/hooks/ssh-gate-enforcer.py",
}


def make_valid_cwd():
    """Create a temp dir with valid session_state.json (anchor_ceremony present)."""
    tmp_dir = tempfile.mkdtemp(prefix="integration_l2_debug_")
    state_dir = os.path.join(tmp_dir, ".claude", "state")
    os.makedirs(state_dir, exist_ok=True)
    state = {
        "session_started": True,
        "anchor_ceremony": {
            "protocol_read_timestamp": "2026-05-27T08:00:00Z",
            "lessons_read_timestamp": "2026-05-27T08:00:00Z",
            "actions_reviewed_count": 0,
            "violations_found": 0,
            "next_action_stated": "test",
            "rules_applied": "test",
            "ceremony_output_generated": "2026-05-27T08:00:00Z",
        },
    }
    with open(os.path.join(state_dir, "session_state.json"), "w") as f:
        json.dump(state, f)
    return tmp_dir


def run_hook(hook_path, payload, cwd=None):
    return subprocess.run(
        [sys.executable, hook_path],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=cwd,
    )


def make_write_payload(filename, content):
    return {
        "tool_name": "Write",
        "tool_input": {
            "file_path": filename,
            "content": content,
        },
    }


# === L2: Basic print() blocked in all 4 hooks ===

def test_basic_print_blocked():
    """All 4 hooks block basic print('hello') with exit 2."""
    cwd = make_valid_cwd()
    try:
        payload = make_write_payload("src/app.py", "x = 1\nprint('hello')\ny = 2\n")
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name}: expected exit 2, got {result.returncode}. stderr={result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: pprint() blocked in all 4 hooks ===

def test_pprint_blocked():
    """All 4 hooks block pprint(data) with exit 2."""
    cwd = make_valid_cwd()
    try:
        payload = make_write_payload("src/debug.py", "import pprint\npprint(data)\n")
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name}: expected exit 2 for pprint, got {result.returncode}. stderr={result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: Indented print() blocked ===

def test_indented_print_blocked():
    """All 4 hooks block indented print() inside a function."""
    cwd = make_valid_cwd()
    try:
        code = "def process(data):\n    result = transform(data)\n    print(result)\n    return result\n"
        payload = make_write_payload("src/processor.py", code)
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name}: expected exit 2 for indented print, got {result.returncode}. stderr={result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: print with f-string blocked ===

def test_fstring_print_blocked():
    """All 4 hooks block print(f'value: {x}') with exit 2."""
    cwd = make_valid_cwd()
    try:
        code = "x = 42\nprint(f'value: {x}')\n"
        payload = make_write_payload("src/output.py", code)
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name}: expected exit 2 for f-string print, got {result.returncode}. stderr={result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: All 4 hooks include "Debug" in blocking message ===

def test_blocking_message_mentions_debug():
    """All 4 hooks mention 'debug' or 'Debug' in stderr when blocking."""
    cwd = make_valid_cwd()
    try:
        payload = make_write_payload("src/app.py", "print('test')\n")
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name}: expected exit 2, got {result.returncode}"
            assert "debug" in result.stderr.lower() or "Debug" in result.stderr, \
                f"{name}: stderr missing 'debug' keyword: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: Comment containing print is NOT blocked ===

def test_comment_print_not_blocked():
    """All 4 hooks allow comments containing 'print' (no false positive)."""
    cwd = make_valid_cwd()
    try:
        code = "# print('this is a comment')\nx = 1\n"
        payload = make_write_payload("src/clean.py", code)
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 0, \
                f"{name}: blocked comment with print (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: Non-Python file with print is NOT blocked ===

def test_non_python_print_not_blocked():
    """All 4 hooks allow print() in .md files (not a code file)."""
    cwd = make_valid_cwd()
    try:
        payload = make_write_payload("docs/guide.md", "Use print() to output results.\n")
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 0, \
                f"{name}: blocked print in .md file (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


if __name__ == "__main__":
    tests = [
        test_basic_print_blocked,
        test_pprint_blocked,
        test_indented_print_blocked,
        test_fstring_print_blocked,
        test_blocking_message_mentions_debug,
        test_comment_print_not_blocked,
        test_non_python_print_not_blocked,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
            sys.stdout.write(f"  PASS: {test.__name__}\n")
        except AssertionError as e:
            failed += 1
            sys.stdout.write(f"  FAIL: {test.__name__} -- {e}\n")
        except Exception as e:
            failed += 1
            sys.stdout.write(f"  ERROR: {test.__name__} -- {type(e).__name__}: {e}\n")

    sys.stdout.write(f"\nResults: {passed} passed, {failed} failed, {len(tests)} total\n")
    sys.exit(1 if failed else 0)
