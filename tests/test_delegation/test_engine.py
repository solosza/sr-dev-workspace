"""Tests for delegation.engine."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from delegation.schema import DelegationRequest
from delegation.engine import DelegationEngine


def test_validate_target_valid(tmp_path):
    (tmp_path / ".git").mkdir()
    engine = DelegationEngine()
    assert engine.validate_target(str(tmp_path)) is True


def test_validate_target_no_git(tmp_path):
    engine = DelegationEngine()
    assert engine.validate_target(str(tmp_path)) is False


def test_validate_target_nonexistent():
    engine = DelegationEngine()
    assert engine.validate_target("/nonexistent/path/123456") is False


def test_execute_echo(tmp_path):
    (tmp_path / ".git").mkdir()
    engine = DelegationEngine()
    request = DelegationRequest(target_repo=str(tmp_path), command="echo hello_world")
    result = engine.execute(request)
    assert result.success is True
    assert result.exit_code == 0
    assert "hello_world" in result.stdout


def test_execute_failure(tmp_path):
    (tmp_path / ".git").mkdir()
    engine = DelegationEngine()
    request = DelegationRequest(target_repo=str(tmp_path), command="exit 1")
    result = engine.execute(request)
    assert result.success is False
    assert result.exit_code == 1


def test_execute_captures_stderr(tmp_path):
    (tmp_path / ".git").mkdir()
    engine = DelegationEngine()
    request = DelegationRequest(target_repo=str(tmp_path), command="echo error_msg 1>&2")
    result = engine.execute(request)
    assert "error_msg" in result.stderr
