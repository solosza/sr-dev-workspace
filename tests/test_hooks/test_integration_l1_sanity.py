"""Integration L1 Sanity: All 4 refactored hooks load and run without errors.

Verifies that all 4 platform hooks (sr_dev, hmsa, gamedev, ssh) can:
1. Compile without syntax errors
2. Accept valid input and exit 0
3. Import shared validators from isagawa-kernel/lib/validators/
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

VALID_WRITE_PAYLOAD = {
    "tool_name": "Write",
    "tool_input": {
        "file_path": "src/clean.py",
        "content": "def add(a, b):\n    return a + b\n",
    },
}

VALID_BASH_PAYLOAD = {
    "tool_name": "Bash",
    "tool_input": {
        "command": "ls -la /tmp",
    },
}


def make_valid_cwd():
    """Create a temp dir with valid session_state.json (anchor_ceremony present)."""
    tmp_dir = tempfile.mkdtemp(prefix="integration_l1_")
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


# === L1: All hooks compile ===

def test_all_hooks_syntax_valid():
    """All 4 hook files compile without syntax errors."""
    for name, path in HOOKS.items():
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", path],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"{name} syntax error: {result.stderr}"


# === L1: All hooks accept valid Write and exit 0 ===

def test_all_hooks_valid_write_exits_0():
    """All 4 hooks accept clean Python write and exit 0."""
    cwd = make_valid_cwd()
    try:
        for name, path in HOOKS.items():
            result = run_hook(path, VALID_WRITE_PAYLOAD, cwd=cwd)
            assert result.returncode == 0, \
                f"{name} rejected valid write (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L1: All hooks accept valid Bash and exit 0 ===

def test_all_hooks_valid_bash_exits_0():
    """All 4 hooks accept clean bash command and exit 0."""
    for name, path in HOOKS.items():
        result = run_hook(path, VALID_BASH_PAYLOAD)
        assert result.returncode == 0, \
            f"{name} rejected valid bash (exit {result.returncode}): {result.stderr}"


# === L1: All hooks block debug statements ===

def test_all_hooks_block_debug():
    """All 4 hooks block print('debug') in Python files."""
    cwd = make_valid_cwd()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/debug.py",
                "content": "print('debug output')\n",
            },
        }
        for name, path in HOOKS.items():
            result = run_hook(path, payload, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} allowed debug statement (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


# === L1: All hooks block cd in bash ===

def test_all_hooks_block_bash_cd():
    """All 4 hooks block cd commands in Bash."""
    payload = {
        "tool_name": "Bash",
        "tool_input": {
            "command": "cd /tmp && ls",
        },
    }
    for name, path in HOOKS.items():
        result = run_hook(path, payload)
        assert result.returncode == 2, \
            f"{name} allowed cd in bash (exit {result.returncode}): {result.stderr}"


# === L1: All hooks skip .claude/ files ===

def test_all_hooks_skip_claude_files():
    """All 4 hooks allow writes to .claude/ paths."""
    payload = {
        "tool_name": "Write",
        "tool_input": {
            "file_path": ".claude/hooks/test_hook.py",
            "content": "print('allowed in .claude/')\n",
        },
    }
    for name, path in HOOKS.items():
        result = run_hook(path, payload)
        assert result.returncode == 0, \
            f"{name} blocked .claude/ write (exit {result.returncode}): {result.stderr}"


if __name__ == "__main__":
    tests = [
        test_all_hooks_syntax_valid,
        test_all_hooks_valid_write_exits_0,
        test_all_hooks_valid_bash_exits_0,
        test_all_hooks_block_debug,
        test_all_hooks_block_bash_cd,
        test_all_hooks_skip_claude_files,
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
