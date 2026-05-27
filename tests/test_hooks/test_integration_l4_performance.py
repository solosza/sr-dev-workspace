"""Integration L4: Performance testing across all 4 workspace hooks.

Verifies:
1. All validators run in < 1 second per call
2. Multiple sequential calls don't degrade performance
3. Reports per-call timing for each workspace
"""

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

HOOKS = {
    "sr_dev": "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py",
    "hmsa": "D:/my_ai_projects/project_test_repos/hmsa-healthcare-qa/.claude/hooks/hmsa_healthcare_qa-gate-enforcer.py",
    "gamedev": "D:/my_ai_projects/project_test_repos/game-dev/.claude/hooks/game_engine-gate-enforcer.py",
    "ssh": "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/.claude/hooks/ssh-gate-enforcer.py",
}

THRESHOLD_SECONDS = 1.0


def make_valid_cwd():
    tmp_dir = tempfile.mkdtemp(prefix="integration_l4_")
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


def timed_hook(hook_path, payload, cwd=None):
    start = time.perf_counter()
    result = subprocess.run(
        [sys.executable, hook_path],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        cwd=cwd,
    )
    elapsed = time.perf_counter() - start
    return result, elapsed


WRITE_PAYLOAD = {
    "tool_name": "Write",
    "tool_input": {
        "file_path": "src/calc.py",
        "content": "def add(a, b):\n    return a + b\n\ndef multiply(a, b):\n    return a * b\n",
    },
}

BASH_PAYLOAD = {
    "tool_name": "Bash",
    "tool_input": {
        "command": "git status && ls -la",
    },
}

SECRET_PAYLOAD = {
    "tool_name": "Write",
    "tool_input": {
        "file_path": "src/config.py",
        "content": "api_key = \"sk_live_12345\"\n",
    },
}


def test_all_hooks_under_threshold_write():
    """All 4 hooks process a Write payload in < 1 second."""
    cwd = make_valid_cwd()
    try:
        for name, path in HOOKS.items():
            _, elapsed = timed_hook(path, WRITE_PAYLOAD, cwd=cwd)
            assert elapsed < THRESHOLD_SECONDS, \
                f"{name} Write took {elapsed:.3f}s (threshold: {THRESHOLD_SECONDS}s)"
            sys.stdout.write(f"    {name} Write: {elapsed:.3f}s\n")
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_all_hooks_under_threshold_bash():
    """All 4 hooks process a Bash payload in < 1 second."""
    for name, path in HOOKS.items():
        _, elapsed = timed_hook(path, BASH_PAYLOAD)
        assert elapsed < THRESHOLD_SECONDS, \
            f"{name} Bash took {elapsed:.3f}s (threshold: {THRESHOLD_SECONDS}s)"
        sys.stdout.write(f"    {name} Bash: {elapsed:.3f}s\n")


def test_all_hooks_under_threshold_violation():
    """All 4 hooks detect a violation in < 1 second."""
    cwd = make_valid_cwd()
    try:
        for name, path in HOOKS.items():
            result, elapsed = timed_hook(path, SECRET_PAYLOAD, cwd=cwd)
            assert result.returncode == 2, \
                f"{name} didn't block secret (exit {result.returncode})"
            assert elapsed < THRESHOLD_SECONDS, \
                f"{name} violation detection took {elapsed:.3f}s (threshold: {THRESHOLD_SECONDS}s)"
            sys.stdout.write(f"    {name} violation: {elapsed:.3f}s\n")
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_sequential_calls_no_degradation():
    """10 sequential calls per hook — no call exceeds threshold."""
    cwd = make_valid_cwd()
    try:
        for name, path in HOOKS.items():
            times = []
            for _ in range(10):
                _, elapsed = timed_hook(path, WRITE_PAYLOAD, cwd=cwd)
                times.append(elapsed)
                assert elapsed < THRESHOLD_SECONDS, \
                    f"{name} call took {elapsed:.3f}s on iteration (threshold: {THRESHOLD_SECONDS}s)"
            avg = sum(times) / len(times)
            sys.stdout.write(f"    {name} 10-call avg: {avg:.3f}s (max: {max(times):.3f}s)\n")
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


if __name__ == "__main__":
    tests = [
        test_all_hooks_under_threshold_write,
        test_all_hooks_under_threshold_bash,
        test_all_hooks_under_threshold_violation,
        test_sequential_calls_no_degradation,
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
