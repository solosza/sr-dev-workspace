"""End-to-end test for cross-repo delegation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from delegation.schema import DelegationRequest
from delegation.engine import DelegationEngine
from delegation.collector import format_report, all_succeeded
from delegation.factory import is_factory_task, parse_factory_section


def test_full_delegation_flow(tmp_path):
    target = tmp_path / "target-repo"
    target.mkdir()
    (target / ".git").mkdir()
    (target / "test.txt").write_text("hello from target")

    engine = DelegationEngine()
    assert engine.validate_target(str(target)) is True

    request = DelegationRequest(target_repo=str(target), command="echo delegation_test_success")
    result = engine.execute(request)

    assert result.success is True
    assert "delegation_test_success" in result.stdout

    report = format_report([result])
    assert "PASS" in report
    assert all_succeeded([result]) is True


def test_factory_task_parsing():
    task_md = """# Test Factory Task

## Type
BUILD

## Execution
factory

## Factory
- target_repo: /tmp/test-repo
- command: echo hello
- expected_output: hello printed

## Acceptance Criteria
- [ ] Command executed
"""
    assert is_factory_task(task_md) is True
    request = parse_factory_section(task_md)
    assert request is not None
    assert request.target_repo == "/tmp/test-repo"
    assert request.command == "echo hello"
    assert request.expected_output == "hello printed"


def test_non_factory_task():
    task_md = """# Regular Task

## Execution
inline

## Requirements
- Do something
"""
    assert is_factory_task(task_md) is False
