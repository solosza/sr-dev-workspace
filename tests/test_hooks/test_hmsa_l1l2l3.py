"""L1/L2/L3 Tests: hmsa_healthcare_qa-gate-enforcer.py

L1: Syntax valid, shared validators import correctly
L2: Violations exit 2 (blocked), clean input exits 0 (allowed)
L3: Behavioral integration — sequential blocks, multi-violation, state-dependent, multi-language
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HOOK_PATH = "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/hooks/hmsa_healthcare_qa-gate-enforcer.py"


def make_valid_cwd():
    """Create a temp dir with valid session_state.json (anchor_ceremony present)."""
    tmp_dir = tempfile.mkdtemp(prefix="hmsa_test_")
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


def run_hook(payload: dict, cwd: str = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, HOOK_PATH],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=cwd,
    )


# === L1: Imports ===

def test_l1_syntax_valid():
    """Hook file compiles without syntax errors."""
    result = subprocess.run(
        [sys.executable, "-m", "py_compile", HOOK_PATH],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Syntax error: {result.stderr}"


def test_l1_shared_validators_import():
    """Shared validators import from isagawa-kernel/lib/validators/."""
    result = subprocess.run(
        [sys.executable, "-c",
         "import sys; from pathlib import Path; "
         f"sys.path.insert(0, str(Path(r'{HOOK_PATH}').resolve().parents[4] / 'isagawa-kernel')); "
         "from lib.validators import code_quality, state_validation, bash_validation, common; "
         "print('OK')"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Import failed: {result.stderr}"
    assert "OK" in result.stdout


# === L2: Functional ===

def test_l2_clean_write_allowed():
    """Clean Python file passes (exit 0)."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/utils.py",
                "content": "def add(a, b):\n    return a + b\n",
            },
        }, cwd=cwd)
        assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l2_debug_statement_blocked():
    """Python print() blocked (exit 2)."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/app.py",
                "content": "x = 1\nprint('debug output')\n",
            },
        }, cwd=cwd)
        assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
        assert "Debug statement" in result.stderr
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l2_secret_blocked():
    """Hardcoded password blocked (exit 2)."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/config.py",
                "content": "password = 'supersecret123'\n",
            },
        }, cwd=cwd)
        assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
        assert "secret" in result.stderr.lower()
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l2_wildcard_import_blocked():
    """Wildcard import blocked (exit 2)."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/models.py",
                "content": "from os import *\n",
            },
        }, cwd=cwd)
        assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
        assert "Wildcard" in result.stderr
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l2_bash_cd_blocked():
    """Bash cd command blocked (exit 2)."""
    result = run_hook({
        "tool_name": "Bash",
        "tool_input": {
            "command": "cd /tmp && ls",
        },
    })
    assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
    assert "cd" in result.stderr.lower()


def test_l2_bash_clean_allowed():
    """Clean bash command passes (exit 0)."""
    result = run_hook({
        "tool_name": "Bash",
        "tool_input": {
            "command": "ls -la /tmp",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


def test_l2_edit_debug_blocked():
    """Edit tool with debug in new_string blocked."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Edit",
            "tool_input": {
                "file_path": "src/handler.py",
                "old_string": "pass",
                "new_string": "print('debug')\npass",
            },
        }, cwd=cwd)
        assert result.returncode == 2, f"Expected 2, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l2_skipped_file_allowed():
    """Files in .claude/ skip all checks."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": ".claude/hooks/my_hook.py",
            "content": "print('this is fine in hook files')\n",
        },
    })
    assert result.returncode == 0, f"Expected 0, got {result.returncode}: {result.stderr}"


# === L3: Behavioral ===

def test_l3_all_violations_blocked_then_valid_passes():
    """All violation types blocked back-to-back, then valid code passes."""
    cwd = make_valid_cwd()
    try:
        violations = [
            ("debug", {"tool_name": "Write", "tool_input": {"file_path": "src/a.py", "content": "print('x')\n"}}),
            ("secret", {"tool_name": "Write", "tool_input": {"file_path": "src/b.py", "content": "password = 'abc'\n"}}),
            ("wildcard", {"tool_name": "Write", "tool_input": {"file_path": "src/c.py", "content": "from os import *\n"}}),
            ("bash_cd", {"tool_name": "Bash", "tool_input": {"command": "cd /tmp && ls"}}),
        ]

        for name, payload in violations:
            result = run_hook(payload, cwd=cwd)
            assert result.returncode == 2, f"Violation '{name}' should block, got {result.returncode}: {result.stderr}"

        result = run_hook({
            "tool_name": "Write",
            "tool_input": {"file_path": "src/ok.py", "content": "x = 1\n"},
        }, cwd=cwd)
        assert result.returncode == 0, f"Valid code after blocks should pass, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l3_multiple_violations_single_file():
    """File with multiple violations reports at least one."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/multi.py",
                "content": "from os import *\npassword = 'secret123'\nprint('debug')\n",
            },
        }, cwd=cwd)
        assert result.returncode == 2
        stderr = result.stderr.lower()
        assert any(word in stderr for word in ["debug", "secret", "wildcard"]), \
            f"Expected violation details in stderr, got: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l3_valid_code_after_block_not_tainted():
    """A block does not taint subsequent valid invocations."""
    cwd = make_valid_cwd()
    try:
        result_bad = run_hook({
            "tool_name": "Write",
            "tool_input": {"file_path": "src/bad.py", "content": "print('debug')\n"},
        }, cwd=cwd)
        assert result_bad.returncode == 2

        result_good = run_hook({
            "tool_name": "Write",
            "tool_input": {"file_path": "src/good.py", "content": "x = 1\n"},
        }, cwd=cwd)
        assert result_good.returncode == 0
        assert result_good.stderr.strip() == "", f"Valid code should produce no stderr, got: {result_good.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l3_anchor_ceremony_missing_blocks():
    """Write blocked when session_state.json has no anchor_ceremony."""
    tmp_dir = tempfile.mkdtemp(prefix="hmsa_l3_")
    state_dir = os.path.join(tmp_dir, ".claude", "state")
    os.makedirs(state_dir, exist_ok=True)

    stripped_state = {
        "session_started": True,
        "timestamp": "2026-05-27T08:00:00Z",
        "domain": "hmsa_healthcare_qa",
    }
    with open(os.path.join(state_dir, "session_state.json"), "w") as f:
        json.dump(stripped_state, f)

    try:
        result = run_hook(
            {"tool_name": "Write", "tool_input": {"file_path": "src/test.py", "content": "x = 1\n"}},
            cwd=tmp_dir,
        )
        assert result.returncode == 2, f"Missing ceremony should block, got {result.returncode}: {result.stderr}"
        assert "anchor" in result.stderr.lower() or "ceremony" in result.stderr.lower(), \
            f"Error should mention anchor/ceremony, got: {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_l3_anchor_ceremony_complete_allows():
    """Write allowed when anchor_ceremony has all required fields."""
    cwd = make_valid_cwd()
    try:
        result = run_hook(
            {"tool_name": "Write", "tool_input": {"file_path": "src/test.py", "content": "x = 1\n"}},
            cwd=cwd,
        )
        assert result.returncode == 0, f"Complete ceremony should allow, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l3_debug_blocked_across_languages():
    """Debug statements blocked in Python, JS, TS, Go consistently."""
    cwd = make_valid_cwd()
    try:
        cases = [
            ("src/a.py", "print('x')\n"),
            ("src/b.js", "console.log('x');\n"),
            ("src/c.ts", "console.debug('x');\n"),
            ("src/d.go", "fmt.Println(x)\n"),
        ]
        for file_path, content in cases:
            result = run_hook({
                "tool_name": "Write",
                "tool_input": {"file_path": file_path, "content": content},
            }, cwd=cwd)
            assert result.returncode == 2, f"Debug in {file_path} should block, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l3_error_messages_contain_blocked_prefix():
    """All violation types produce stderr starting with 'BLOCKED:'."""
    cwd = make_valid_cwd()
    try:
        payloads = [
            {"tool_name": "Write", "tool_input": {"file_path": "src/a.py", "content": "print('x')\n"}},
            {"tool_name": "Write", "tool_input": {"file_path": "src/b.py", "content": "password = 'x'\n"}},
            {"tool_name": "Write", "tool_input": {"file_path": "src/c.py", "content": "from os import *\n"}},
            {"tool_name": "Bash", "tool_input": {"command": "cd /tmp"}},
        ]
        for payload in payloads:
            result = run_hook(payload, cwd=cwd)
            assert result.returncode == 2
            assert result.stderr.strip().startswith("BLOCKED:"), \
                f"Error should start with 'BLOCKED:', got: {result.stderr[:80]}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_l3_edit_checks_new_string_not_old_string():
    """Edit validates new_string, not old_string."""
    cwd = make_valid_cwd()
    try:
        result = run_hook({
            "tool_name": "Edit",
            "tool_input": {
                "file_path": "src/fix.py",
                "old_string": "print('debug')",
                "new_string": "logger.info('fixed')",
            },
        }, cwd=cwd)
        assert result.returncode == 0, f"Clean new_string should pass, got {result.returncode}: {result.stderr}"

        result = run_hook({
            "tool_name": "Edit",
            "tool_input": {
                "file_path": "src/fix.py",
                "old_string": "logger.info('x')",
                "new_string": "print('oops')",
            },
        }, cwd=cwd)
        assert result.returncode == 2, f"Violation in new_string should block, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


if __name__ == "__main__":
    tests = [
        test_l1_syntax_valid,
        test_l1_shared_validators_import,
        test_l2_clean_write_allowed,
        test_l2_debug_statement_blocked,
        test_l2_secret_blocked,
        test_l2_wildcard_import_blocked,
        test_l2_bash_cd_blocked,
        test_l2_bash_clean_allowed,
        test_l2_edit_debug_blocked,
        test_l2_skipped_file_allowed,
        test_l3_all_violations_blocked_then_valid_passes,
        test_l3_multiple_violations_single_file,
        test_l3_valid_code_after_block_not_tainted,
        test_l3_anchor_ceremony_missing_blocks,
        test_l3_anchor_ceremony_complete_allows,
        test_l3_debug_blocked_across_languages,
        test_l3_error_messages_contain_blocked_prefix,
        test_l3_edit_checks_new_string_not_old_string,
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
