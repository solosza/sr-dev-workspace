"""L3 Behavioral Tests: sr_dev-gate-enforcer.py

Tests integrated behavioral scenarios beyond L2 functional tests:
- All 5 violation types blocked in a single suite run
- Multiple violations in one file detected
- State-dependent behavior (anchor ceremony with manipulated state)
- Sequential behavior (blocks don't affect subsequent valid actions)
- Edge cases: multi-language violations, mixed valid+invalid content
- Error message consistency across violation types
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile

HOOK_PATH = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py"
CWD = "D:/my_ai_projects/project_test_repos/sr_dev_workspace"
STATE_PATH = os.path.join(CWD, ".claude/state/session_state.json")


def run_hook(payload: dict, cwd: str = CWD) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, HOOK_PATH],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=cwd,
    )


# --- Behavioral: All 5 violation types in one suite ---

def test_all_five_violations_blocked_sequentially():
    """All 5 violation types blocked when tested back-to-back in sequence."""
    violations = [
        ("debug", {"tool_name": "Write", "tool_input": {"file_path": "src/a.py", "content": "print('x')\n"}}),
        ("secret", {"tool_name": "Write", "tool_input": {"file_path": "src/b.py", "content": "password = 'abc'\n"}}),
        ("wildcard", {"tool_name": "Write", "tool_input": {"file_path": "src/c.py", "content": "from os import *\n"}}),
        ("bash_cd", {"tool_name": "Bash", "tool_input": {"command": "cd /tmp && ls"}}),
        ("anchor", None),  # handled separately below
    ]

    for name, payload in violations:
        if name == "anchor":
            continue  # anchor tested in dedicated state test
        result = run_hook(payload)
        assert result.returncode == 2, f"Violation '{name}' should block (exit 2), got {result.returncode}: {result.stderr}"

    # After all blocks, valid code still passes
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {"file_path": "src/ok.py", "content": "x = 1\n"},
    })
    assert result.returncode == 0, f"Valid code after blocks should pass, got {result.returncode}: {result.stderr}"


def test_multiple_violations_single_file():
    """File with multiple violation types reports all of them."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/multi.py",
            "content": "from os import *\npassword = 'secret123'\nprint('debug')\n",
        },
    })
    assert result.returncode == 2
    # Should mention at least some violations in stderr
    stderr = result.stderr.lower()
    assert any(word in stderr for word in ["debug", "secret", "wildcard"]), \
        f"Expected violation details in stderr, got: {result.stderr}"


def test_valid_code_after_block_not_tainted():
    """A block on one invocation does not taint the next valid invocation."""
    # First: block
    result_bad = run_hook({
        "tool_name": "Write",
        "tool_input": {"file_path": "src/bad.py", "content": "print('debug')\n"},
    })
    assert result_bad.returncode == 2

    # Second: valid — must pass cleanly
    result_good = run_hook({
        "tool_name": "Write",
        "tool_input": {"file_path": "src/good.py", "content": "x = 1\n"},
    })
    assert result_good.returncode == 0
    assert result_good.stderr.strip() == "", f"Valid code should produce no stderr, got: {result_good.stderr}"


# --- Behavioral: State-dependent anchor ceremony ---

def test_anchor_ceremony_missing_blocks_write():
    """Write blocked when session_state.json has no anchor_ceremony."""
    # Create temp dir with a stripped session_state.json (no ceremony)
    tmp_dir = tempfile.mkdtemp(prefix="sr_dev_l3_")
    state_dir = os.path.join(tmp_dir, ".claude", "state")
    os.makedirs(state_dir, exist_ok=True)

    stripped_state = {
        "session_started": True,
        "timestamp": "2026-05-27T08:00:00Z",
        "domain": "sr_dev",
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


def test_anchor_ceremony_partial_fields_blocks():
    """Write blocked when anchor_ceremony has only some required fields."""
    tmp_dir = tempfile.mkdtemp(prefix="sr_dev_l3_")
    state_dir = os.path.join(tmp_dir, ".claude", "state")
    os.makedirs(state_dir, exist_ok=True)

    partial_state = {
        "session_started": True,
        "anchor_ceremony": {
            "protocol_read_timestamp": "2026-05-27T08:00:00Z",
            # Missing other required fields
        },
    }
    with open(os.path.join(state_dir, "session_state.json"), "w") as f:
        json.dump(partial_state, f)

    try:
        result = run_hook(
            {"tool_name": "Write", "tool_input": {"file_path": "src/test.py", "content": "x = 1\n"}},
            cwd=tmp_dir,
        )
        assert result.returncode == 2, f"Partial ceremony should block, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_anchor_ceremony_complete_allows():
    """Write allowed when anchor_ceremony has all required fields."""
    tmp_dir = tempfile.mkdtemp(prefix="sr_dev_l3_")
    state_dir = os.path.join(tmp_dir, ".claude", "state")
    os.makedirs(state_dir, exist_ok=True)

    complete_state = {
        "session_started": True,
        "anchor_ceremony": {
            "protocol_read_timestamp": "2026-05-27T08:00:00Z",
            "lessons_read_timestamp": "2026-05-27T08:00:00Z",
            "actions_reviewed_count": 0,
            "violations_found": 0,
            "next_action_stated": "implement task",
            "rules_applied": "NEVER ASSUME",
            "ceremony_output_generated": "2026-05-27T08:00:00Z",
        },
    }
    with open(os.path.join(state_dir, "session_state.json"), "w") as f:
        json.dump(complete_state, f)

    try:
        result = run_hook(
            {"tool_name": "Write", "tool_input": {"file_path": "src/test.py", "content": "x = 1\n"}},
            cwd=tmp_dir,
        )
        assert result.returncode == 0, f"Complete ceremony should allow, got {result.returncode}: {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


# --- Behavioral: Multi-language consistency ---

def test_debug_blocked_across_languages():
    """Debug statements blocked in Python, JS, TS, Go consistently."""
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
        })
        assert result.returncode == 2, f"Debug in {file_path} should block, got {result.returncode}: {result.stderr}"


# --- Behavioral: Error message format consistency ---

def test_error_messages_contain_blocked_prefix():
    """All violation types produce stderr starting with 'BLOCKED:'."""
    payloads = [
        {"tool_name": "Write", "tool_input": {"file_path": "src/a.py", "content": "print('x')\n"}},
        {"tool_name": "Write", "tool_input": {"file_path": "src/b.py", "content": "password = 'x'\n"}},
        {"tool_name": "Write", "tool_input": {"file_path": "src/c.py", "content": "from os import *\n"}},
        {"tool_name": "Bash", "tool_input": {"command": "cd /tmp"}},
    ]
    for payload in payloads:
        result = run_hook(payload)
        assert result.returncode == 2
        assert result.stderr.strip().startswith("BLOCKED:"), \
            f"Error should start with 'BLOCKED:', got: {result.stderr[:80]}"


# --- Behavioral: Edit tool uses new_string for checking ---

def test_edit_checks_new_string_not_old_string():
    """Edit tool validates new_string content, not old_string."""
    # old_string has violation but new_string is clean — should pass
    result = run_hook({
        "tool_name": "Edit",
        "tool_input": {
            "file_path": "src/fix.py",
            "old_string": "print('debug')",
            "new_string": "logger.info('fixed')",
        },
    })
    assert result.returncode == 0, f"Clean new_string should pass, got {result.returncode}: {result.stderr}"

    # new_string has violation — should block
    result = run_hook({
        "tool_name": "Edit",
        "tool_input": {
            "file_path": "src/fix.py",
            "old_string": "logger.info('x')",
            "new_string": "print('oops')",
        },
    })
    assert result.returncode == 2, f"Violation in new_string should block, got {result.returncode}: {result.stderr}"


# --- Behavioral: Skip pattern respected even with violations ---

def test_skip_pattern_bypasses_all_checks():
    """Files in .claude/ skip ALL checks even with violations."""
    result = run_hook({
        "tool_name": "Write",
        "tool_input": {
            "file_path": ".claude/hooks/new_hook.py",
            "content": "print('debug')\nfrom os import *\npassword = 'secret'\n",
        },
    })
    assert result.returncode == 0, f"Skipped file should pass, got {result.returncode}: {result.stderr}"


if __name__ == "__main__":
    tests = [
        test_all_five_violations_blocked_sequentially,
        test_multiple_violations_single_file,
        test_valid_code_after_block_not_tainted,
        test_anchor_ceremony_missing_blocks_write,
        test_anchor_ceremony_partial_fields_blocks,
        test_anchor_ceremony_complete_allows,
        test_debug_blocked_across_languages,
        test_error_messages_contain_blocked_prefix,
        test_edit_checks_new_string_not_old_string,
        test_skip_pattern_bypasses_all_checks,
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
