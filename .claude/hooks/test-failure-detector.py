#!/usr/bin/env python3
"""
Test Failure Detector - PostToolUse hook that sets needs_learn after test failures.

Triggers on: Bash commands that look like test runs with non-zero exit code.
Sets: needs_learn: true, needs_learn_reason: "test_failure"

This enforces the learn-after-fix loop in the kernel.
"""

import json
import sys
from pathlib import Path

STATE_DIR = Path('.claude/state')
SESSION_STATE = STATE_DIR / 'session_state.json'

# Patterns that indicate a test command
TEST_COMMAND_PATTERNS = (
    'pytest',
    'python -m pytest',
    'npm test',
    'npm run test',
    'yarn test',
    'jest',
    'mocha',
    'cargo test',
    'go test',
    'dotnet test',
    'mvn test',
    'gradle test',
    'playwright test',
    'npx playwright',
)


def read_state(state_file: Path) -> dict:
    if not state_file.exists():
        return {}
    try:
        return json.loads(state_file.read_text())
    except:
        return {}


def write_state(state_file: Path, state: dict):
    """Write state back to file."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    try:
        state_file.write_text(json.dumps(state, indent=2))
    except:
        pass  # Best effort


def is_test_command(command: str) -> bool:
    """Check if command looks like a test run."""
    cmd = command.strip().lower()
    for pattern in TEST_COMMAND_PATTERNS:
        if pattern.lower() in cmd:
            return True
    return False


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool_name = data.get('tool_name', '')

    # Only check Bash commands
    if tool_name != 'Bash':
        sys.exit(0)

    tool_input = data.get('tool_input', {})
    tool_result = data.get('tool_result', {})

    command = tool_input.get('command', '')

    # Only check test commands
    if not is_test_command(command):
        sys.exit(0)

    # Check exit code (non-zero = failure)
    # PostToolUse receives the result, which includes exit code for Bash
    # Fallback: check stdout/stderr for failure patterns if exit_code not available
    exit_code = tool_result.get('exit_code')

    # If exit_code not in tool_result, try to detect failure from output
    if exit_code is None:
        stdout = tool_result.get('stdout', '') or ''
        stderr = tool_result.get('stderr', '') or ''
        output = (stdout + stderr).lower()

        # Common test failure patterns
        failure_patterns = [
            'failed', 'failure', 'error', 'exception',
            'assert', 'traceback', 'exit code 1', 'exit code 2',
            'tests failed', 'test failed', '1 failed', '2 failed',
        ]

        # Check if any failure pattern is in output
        has_failure = any(pattern in output for pattern in failure_patterns)
        exit_code = 1 if has_failure else 0

    if exit_code != 0:
        # Test failed - set needs_learn
        session_state = read_state(SESSION_STATE)
        session_state['needs_learn'] = True
        session_state['needs_learn_reason'] = 'test_failure'
        write_state(SESSION_STATE, session_state)

        # Inform the agent (this goes to stderr, visible to agent)
        sys.stderr.write(f"""
TEST FAILURE DETECTED

Exit code: {exit_code}
Command: {command}

You must invoke /kernel/learn after fixing this failure.
Next write will be blocked until lesson is recorded.
""")

    sys.exit(0)


if __name__ == '__main__':
    main()
