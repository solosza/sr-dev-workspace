#!/usr/bin/env python3
"""L2 Functional Tests for sr_dev-gate-enforcer.py hook."""

import subprocess
import json
import sys

HOOK = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py"

def run_hook(tool_name, tool_input):
    """Run the hook with given input, return (returncode, stderr)."""
    data = json.dumps({"tool_name": tool_name, "tool_input": tool_input})
    result = subprocess.run(
        ["python", HOOK],
        input=data,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stderr

def test_blocks_debug():
    rc, err = run_hook("Write", {"file_path": "src/app.py", "content": "print('hello')\nx = 1"})
    assert rc == 2, f"Expected exit 2, got {rc}"
    assert "Debug statement" in err
    print("PASS: Debug statement blocked")

def test_blocks_secret():
    rc, err = run_hook("Write", {"file_path": "src/config.py", "content": 'password = "supersecret123"'})
    assert rc == 2, f"Expected exit 2, got {rc}"
    assert "secret" in err.lower()
    print("PASS: Secret blocked")

def test_blocks_wildcard():
    rc, err = run_hook("Write", {"file_path": "src/utils.py", "content": "from os import *"})
    assert rc == 2, f"Expected exit 2, got {rc}"
    assert "Wildcard" in err
    print("PASS: Wildcard import blocked")

def test_blocks_bash_cd():
    rc, err = run_hook("Bash", {"command": "cd /tmp && ls"})
    assert rc == 2, f"Expected exit 2, got {rc}"
    assert "cd" in err.lower()
    print("PASS: Bash cd blocked")

def test_allows_clean_code():
    rc, err = run_hook("Write", {"file_path": "src/clean.py", "content": "import os\nx = 1"})
    if rc == 0:
        print("PASS: Clean code allowed")
    elif "Anchor ceremony" in err:
        print("PASS: Clean code blocked by anchor ceremony (state_validation works as expected)")
    else:
        print(f"FAIL: Unexpected block: {err}")
        sys.exit(1)

def test_skips_claude_files():
    rc, err = run_hook("Write", {"file_path": ".claude/hooks/test.py", "content": "print('debug')"})
    assert rc == 0, f"Expected exit 0 for .claude/ file, got {rc}: {err}"
    print("PASS: .claude/ file skipped")

def test_allows_safe_bash():
    rc, err = run_hook("Bash", {"command": "git log --oneline"})
    assert rc == 0, f"Expected exit 0, got {rc}: {err}"
    print("PASS: Safe bash allowed")

if __name__ == "__main__":
    passed = 0
    failed = 0
    tests = [
        test_blocks_debug,
        test_blocks_secret,
        test_blocks_wildcard,
        test_blocks_bash_cd,
        test_allows_clean_code,
        test_skips_claude_files,
        test_allows_safe_bash,
    ]
    for t in tests:
        try:
            t()
            passed += 1
        except AssertionError as e:
            print(f"FAIL ({t.__name__}): {e}")
            failed += 1
        except Exception as e:
            print(f"ERROR ({t.__name__}): {e}")
            failed += 1

    print(f"\n{passed}/{passed + failed} tests passed")
    sys.exit(1 if failed else 0)
