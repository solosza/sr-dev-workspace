"""Integration L3: Workspace isolation — hooks don't interfere across workspaces.

Verifies:
1. Triggering a violation in sr_dev does not affect hmsa/gamedev/ssh
2. Each workspace hook runs independently with its own state
3. Violation in one workspace, clean pass in another — simultaneously
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
    tmp_dir = tempfile.mkdtemp(prefix="integration_l3_")
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


SECRET_PAYLOAD = {
    "tool_name": "Write",
    "tool_input": {
        "file_path": "src/config.py",
        "content": "api_key = \"sk_live_12345\"\n",
    },
}

CLEAN_PAYLOAD = {
    "tool_name": "Write",
    "tool_input": {
        "file_path": "src/calc.py",
        "content": "def add(a, b):\n    return a + b\n",
    },
}


def test_violation_in_sr_dev_does_not_affect_others():
    """Trigger secret violation in sr_dev; verify hmsa, gamedev, ssh pass clean code."""
    cwd = make_valid_cwd()
    try:
        # sr_dev blocks the secret
        sr_result = run_hook(HOOKS["sr_dev"], SECRET_PAYLOAD, cwd=cwd)
        assert sr_result.returncode == 2, \
            f"sr_dev should block secret (got {sr_result.returncode})"

        # Other hooks pass clean code (unaffected by sr_dev's violation)
        for name in ["hmsa", "gamedev", "ssh"]:
            result = run_hook(HOOKS[name], CLEAN_PAYLOAD, cwd=cwd)
            assert result.returncode == 0, \
                f"{name} was affected by sr_dev violation (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_violation_in_gamedev_does_not_affect_others():
    """Trigger secret violation in gamedev; verify sr_dev, hmsa, ssh pass clean code."""
    cwd = make_valid_cwd()
    try:
        gd_result = run_hook(HOOKS["gamedev"], SECRET_PAYLOAD, cwd=cwd)
        assert gd_result.returncode == 2, \
            f"gamedev should block secret (got {gd_result.returncode})"

        for name in ["sr_dev", "hmsa", "ssh"]:
            result = run_hook(HOOKS[name], CLEAN_PAYLOAD, cwd=cwd)
            assert result.returncode == 0, \
                f"{name} was affected by gamedev violation (exit {result.returncode}): {result.stderr}"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


def test_independent_state_per_workspace():
    """Each workspace's cwd is independent — temp dirs don't share state."""
    cwd_a = make_valid_cwd()
    cwd_b = make_valid_cwd()
    try:
        # Run violation in cwd_a with sr_dev
        res_a = run_hook(HOOKS["sr_dev"], SECRET_PAYLOAD, cwd=cwd_a)
        assert res_a.returncode == 2, "sr_dev should block in cwd_a"

        # Run clean code in cwd_b with sr_dev — different cwd, same hook
        res_b = run_hook(HOOKS["sr_dev"], CLEAN_PAYLOAD, cwd=cwd_b)
        assert res_b.returncode == 0, \
            f"sr_dev in cwd_b affected by cwd_a (exit {res_b.returncode}): {res_b.stderr}"
    finally:
        shutil.rmtree(cwd_a, ignore_errors=True)
        shutil.rmtree(cwd_b, ignore_errors=True)


def test_all_four_hooks_independent_simultaneous():
    """Run all 4 hooks with mixed payloads — each operates independently."""
    cwd = make_valid_cwd()
    try:
        # sr_dev and gamedev get violations, hmsa and ssh get clean code
        sr_res = run_hook(HOOKS["sr_dev"], SECRET_PAYLOAD, cwd=cwd)
        hmsa_res = run_hook(HOOKS["hmsa"], CLEAN_PAYLOAD, cwd=cwd)
        gd_res = run_hook(HOOKS["gamedev"], SECRET_PAYLOAD, cwd=cwd)
        ssh_res = run_hook(HOOKS["ssh"], CLEAN_PAYLOAD, cwd=cwd)

        assert sr_res.returncode == 2, f"sr_dev should block (got {sr_res.returncode})"
        assert hmsa_res.returncode == 0, f"hmsa should pass (got {hmsa_res.returncode})"
        assert gd_res.returncode == 2, f"gamedev should block (got {gd_res.returncode})"
        assert ssh_res.returncode == 0, f"ssh should pass (got {ssh_res.returncode})"
    finally:
        shutil.rmtree(cwd, ignore_errors=True)


if __name__ == "__main__":
    tests = [
        test_violation_in_sr_dev_does_not_affect_others,
        test_violation_in_gamedev_does_not_affect_others,
        test_independent_state_per_workspace,
        test_all_four_hooks_independent_simultaneous,
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
