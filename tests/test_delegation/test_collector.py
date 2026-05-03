"""Tests for delegation.collector."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from delegation.schema import DelegationResult
from delegation.collector import format_report, all_succeeded


def test_all_succeeded_true():
    results = [DelegationResult(success=True, exit_code=0), DelegationResult(success=True, exit_code=0)]
    assert all_succeeded(results) is True


def test_all_succeeded_false():
    results = [DelegationResult(success=True, exit_code=0), DelegationResult(success=False, exit_code=1)]
    assert all_succeeded(results) is False


def test_format_report_content():
    results = [
        DelegationResult(success=True, exit_code=0, target_repo="/tmp/a", duration_seconds=1.0),
        DelegationResult(success=False, exit_code=1, target_repo="/tmp/b", stderr="error", duration_seconds=2.0),
    ]
    report = format_report(results)
    assert "PASS" in report
    assert "FAIL" in report
    assert "1/2 passed" in report


def test_format_report_empty():
    report = format_report([])
    assert "0/0 passed" in report
