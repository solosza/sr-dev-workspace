"""Integration L2 Consistency: All 4 hooks block identical violations identically.

Feeds the same violation inputs to all 4 platform hooks and verifies:
1. All block secrets consistently (exit 2)
2. All block wildcard imports consistently (exit 2)
3. All block skipped tests in spec files consistently (exit 2)
4. All skip test_ prefixed files by design (exit 0)
5. All pass valid code consistently (exit 0)
6. Error messages mention the violation type
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
    tmp_dir = tempfile.mkdtemp(prefix="integration_l2_")
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


# === L2: All hooks block hardcoded secrets ===

def test_all_hooks_block_secret():
    """All 4 hooks block api_key = 'sk_live_12345' consistently."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/config.py",
                "content": "import os\napi_key = \"sk_live_12345\"\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} did not block secret (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_all_hooks_secret_message_mentions_secret():
    """All 4 hooks mention 'secret' in their blocking message."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/config.py",
                "content": "password = \"hunter2\"\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} did not block secret (exit {result.returncode})"
            output = (result.stdout + result.stderr).lower()
            assert "secret" in output, \
                f"{name} blocked but message doesn't mention 'secret': {result.stdout}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: All hooks block wildcard imports ===

def test_all_hooks_block_wildcard_import():
    """All 4 hooks block 'from os import *' consistently."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/utils.py",
                "content": "from os import *\nresult = path.exists('/tmp')\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} did not block wildcard import (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_all_hooks_wildcard_message_mentions_wildcard():
    """All 4 hooks mention 'wildcard' in their blocking message."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/utils.py",
                "content": "from pathlib import *\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} did not block wildcard (exit {result.returncode})"
            output = (result.stdout + result.stderr).lower()
            assert "wildcard" in output, \
                f"{name} blocked but message doesn't mention 'wildcard': {result.stdout}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: All hooks block skipped tests in spec files ===
# Note: test_ prefixed files are skipped by common.should_skip() by design
# (to avoid false positives on debug print() in tests). Skipped test detection
# works on spec files which also match the test/spec path check in code_quality.

def test_all_hooks_block_skipped_test_in_spec():
    """All 4 hooks block @pytest.mark.skip in spec files (not skipped by should_skip)."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "specs/feature_spec.py",
                "content": "import pytest\n\n@pytest.mark.skip\ndef test_broken():\n    assert False\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} did not block skipped test in spec (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_all_hooks_skip_test_files_intentionally():
    """All 4 hooks intentionally skip test_ prefixed files (no validation runs)."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "tests/test_feature.py",
                "content": "print('debug in test')\n@pytest.mark.skip\ndef test_todo():\n    pass\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 0, \
                f"{name} should skip test_ files but blocked (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L2: All hooks pass clean code ===

def test_all_hooks_pass_clean_python():
    """All 4 hooks accept clean Python code (no violations)."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/calculator.py",
                "content": "def add(a: int, b: int) -> int:\n    return a + b\n\n\ndef multiply(a: int, b: int) -> int:\n    return a * b\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 0, \
                f"{name} rejected clean code (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_all_hooks_pass_clean_bash():
    """All 4 hooks accept clean bash commands (no cd)."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {
            "command": "git status && ls -la",
        },
    }
    for name, path in HOOKS.items():
        result = run_hook(path, payload)
        assert result.returncode == 0, \
            f"{name} rejected clean bash (exit {result.returncode}): {result.stderr}"


if __name__ == "__main__":
    tests = [
        test_all_hooks_block_secret,
        test_all_hooks_secret_message_mentions_secret,
        test_all_hooks_block_wildcard_import,
        test_all_hooks_wildcard_message_mentions_wildcard,
        test_all_hooks_block_skipped_test_in_spec,
        test_all_hooks_skip_test_files_intentionally,
        test_all_hooks_pass_clean_python,
        test_all_hooks_pass_clean_bash,
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
