"""L2 Functional Tests: sr_dev-gate-enforcer.py

Pipes JSON to the hook via subprocess and verifies:
- Violations exit with code 2 (blocked)
- Clean input exits with code 0 (allowed)

Tests: debug statements, secrets, wildcard imports, bash cd, anchor ceremony.
"""

import json
import subprocess
import sys

HOOK_PATH = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py"
CWD = "D:/my_ai_projects/project_test_repos/sr_dev_workspace"


def run_hook(payload: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, HOOK_PATH],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=CWD,
    )


def test_clean_write_allowed():
    """Clean Python file should pass (exit 0)."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/utils.py",
            "content": "def add(a, b):\n    return a + b\n",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


def test_debug_statement_blocked():
    """Python print() should be blocked (exit 2)."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/app.py",
            "content": "x = 1\nprint('debug output')\n",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
    assert "Debug statement" in result.stderr


def test_secret_blocked():
    """Hardcoded password should be blocked (exit 2)."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/config.py",
            "content": "password = 'supersecret123'\n",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
    assert "secret" in result.stderr.lower()


def test_wildcard_import_blocked():
    """Wildcard import should be blocked (exit 2)."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/models.py",
            "content": "from os import *\n",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
    assert "Wildcard" in result.stderr


def test_bash_cd_blocked():
    """Bash cd command should be blocked (exit 2)."""
    result = run_hook({
        "tool_name": "Bash",
        "tool_input": {
            "command": "cd /tmp && ls",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
    assert "cd" in result.stderr.lower()


def test_bash_clean_allowed():
    """Clean bash command should pass (exit 0)."""
    result = run_hook({
        "tool_name": "Bash",
        "tool_input": {
            "command": "ls -la /tmp",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


def test_bash_cd_in_string_allowed():
    """cd inside a quoted string should not trigger block."""
    result = run_hook({
        "tool_name": "Bash",
        "tool_input": {
            "command": "echo 'cd /tmp is not a real cd'",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


def test_edit_with_debug_blocked():
    """Edit tool with debug statement in new_string should be blocked."""
    result = run_hook({
        "tool_name": "Edit",
        "tool_input": {
            "file_path": "src/handler.py",
            "old_string": "pass",
            "new_string": "print('debug')\npass",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"


def test_skipped_file_allowed():
    """Files matching skip patterns (.claude/) should pass regardless of content."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": ".claude/hooks/my_hook.py",
            "content": "print('this is fine in hook files')\n",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


def test_anchor_ceremony_valid():
    """Write/Edit with valid anchor ceremony in session state should pass."""
    # This test verifies the hook reads session_state.json and finds valid ceremony
    # The current session_state.json has valid ceremony fields from the anchor
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/clean.py",
            "content": "x = 1\n",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


def test_api_key_secret_blocked():
    """api_key assignment should be blocked."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/client.py",
            "content": "api_key = 'sk-abc123def456'\n",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"


def test_js_console_log_blocked():
    """console.log in .js file should be blocked."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/app.js",
            "content": "const x = 1;\nconsole.log(x);\n",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"


if __name__ == "__main__":
    tests = [
        test_clean_write_allowed,
        test_debug_statement_blocked,
        test_secret_blocked,
        test_wildcard_import_blocked,
        test_bash_cd_blocked,
        test_bash_clean_allowed,
        test_bash_cd_in_string_allowed,
        test_edit_with_debug_blocked,
        test_skipped_file_allowed,
        test_anchor_ceremony_valid,
        test_api_key_secret_blocked,
        test_js_console_log_blocked,
    ]

    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            print(f"  PASS: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL: {test.__name__} — {e}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed, {len(tests)} total")
    sys.exit(1 if failed else 0)
