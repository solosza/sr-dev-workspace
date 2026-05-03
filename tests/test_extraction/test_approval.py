"""Tests for lessons.approval — approval gate."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.approval import request_approval, format_approval_prompt, record_decision, get_decision


def test_request_approval_format():
    draft = {
        "command_name": "check-hook-bypass",
        "command_path": ".claude/commands/kernel/check-hook-bypass.md",
        "content": "# /kernel/check-hook-bypass\n...",
        "source_pattern": "abc123",
    }
    result = request_approval(draft)
    assert isinstance(result, str)
    assert "check-hook-bypass" in result
    assert "abc123" in result


def test_record_approval(tmp_path):
    registry = tmp_path / "approvals.json"
    record_decision("abc123", True, "check-hook-bypass", registry_path=registry)
    decision = get_decision("abc123", registry_path=registry)
    assert decision is not None
    assert decision["approved"] is True
    assert "timestamp" in decision


def test_record_rejection(tmp_path):
    registry = tmp_path / "approvals.json"
    record_decision("xyz789", False, "check-drift", registry_path=registry)
    decision = get_decision("xyz789", registry_path=registry)
    assert decision is not None
    assert decision["approved"] is False


def test_format_approval_prompt():
    draft = {
        "command_name": "check-config-drift",
        "command_path": ".claude/commands/kernel/check-config-drift.md",
        "content": "# Content here",
        "source_pattern": "def456",
    }
    prompt = format_approval_prompt(draft)
    assert "check-config-drift" in prompt
    assert "def456" in prompt
    assert "Approve" in prompt
