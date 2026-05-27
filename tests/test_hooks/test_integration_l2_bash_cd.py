"""Integration L2: All 4 hooks block bash cd commands identically.

Feeds bash commands containing 'cd' to all 4 platform hooks and verifies:
1. All block 'cd /some/path && git log' (exit 2)
2. All mention 'cd' in their blocking message
3. All allow bash commands that contain 'cd' in strings (no false positive)
"""

import json
import subprocess
import sys

HOOKS = {
    "sr_dev": "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py",
    "hmsa": "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/hooks/hmsa_healthcare_qa-gate-enforcer.py",
    "gamedev": "D:/my_ai_projects/project_test_repos/game-dev/.claude/hooks/game_engine-gate-enforcer.py",
    "ssh": "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/.claude/hooks/ssh-gate-enforcer.py",
}


def run_hook(hook_path, payload):
    return subprocess.run(
        [sys.executable, hook_path],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
    )


def test_all_hooks_block_cd_command():
    """All 4 hooks block 'cd /some/path && git log' consistently."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {
            "command": "cd /some/path && git log",
        },
    }
    for name, path in HOOKS.items():
        result = run_hook(path, payload)
        assert result.returncode == 2, \
            f"{name} did not block cd (exit {result.returncode}): {result.stderr}"


def test_all_hooks_cd_message_mentions_cd():
    """All 4 hooks mention 'cd' in their blocking message."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {
            "command": "cd /tmp && ls",
        },
    }
    for name, path in HOOKS.items():
        result = run_hook(path, payload)
        assert result.returncode == 2, \
            f"{name} did not block cd (exit {result.returncode})"
        output = (result.stdout + result.stderr).lower()
        assert "cd" in output, \
            f"{name} blocked but message doesn't mention 'cd': {result.stdout}"


def test_all_hooks_allow_cd_in_string():
    """All 4 hooks allow bash with 'cd' inside a quoted string (no false positive)."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {
            "command": "echo 'cd implementation notes'",
        },
    }
    for name, path in HOOKS.items():
        result = run_hook(path, payload)
        assert result.returncode == 0, \
            f"{name} false-positive blocked 'cd' in string (exit {result.returncode}): {result.stderr}"


if __name__ == "__main__":
    tests = [
        test_all_hooks_block_cd_command,
        test_all_hooks_cd_message_mentions_cd,
        test_all_hooks_allow_cd_in_string,
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
