"""Tests for delegation.schema."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from delegation.schema import DelegationRequest, DelegationResult


def test_request_creation():
    req = DelegationRequest(target_repo="/tmp/test-repo", command="echo hello", expected_output="hello")
    assert req.target_repo == "/tmp/test-repo"
    assert req.command == "echo hello"
    assert req.timeout_seconds == 300


def test_result_creation():
    res = DelegationResult(success=True, exit_code=0, stdout="hello\n")
    assert res.success is True
    assert res.exit_code == 0


def test_request_serialization():
    req = DelegationRequest(target_repo="/tmp/repo", command="ls", env_vars={"FOO": "bar"})
    data = req.to_dict()
    restored = DelegationRequest.from_dict(data)
    assert restored.target_repo == req.target_repo
    assert restored.env_vars == {"FOO": "bar"}


def test_result_serialization():
    res = DelegationResult(success=False, exit_code=1, stderr="error", duration_seconds=1.5)
    data = res.to_dict()
    restored = DelegationResult.from_dict(data)
    assert restored.success is False
    assert restored.duration_seconds == 1.5


def test_request_defaults():
    req = DelegationRequest(target_repo="/tmp", command="pwd")
    assert req.expected_output == ""
    assert req.env_vars == {}
