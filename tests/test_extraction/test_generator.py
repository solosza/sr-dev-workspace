"""Tests for lessons.draft_generator — draft command generation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.draft_generator import generate_draft, suggest_command_name


def test_generate_draft_structure():
    draft = generate_draft(
        pattern_key="abc123",
        issue="Hook bypass via state edit",
        fix="Add PROTECTED_PATHS check",
        tags=["hook", "enforcement"],
    )
    assert "command_name" in draft
    assert "command_path" in draft
    assert "content" in draft
    assert "source_pattern" in draft
    assert draft["source_pattern"] == "abc123"


def test_suggest_command_name():
    name = suggest_command_name("Hook bypass via direct state edit", ["hook"])
    assert "-" in name
    assert name.startswith("check-")
    assert " " not in name


def test_draft_content_format():
    draft = generate_draft(
        pattern_key="abc123",
        issue="Test failure not detected",
        fix="Add test pattern to detector",
        tags=["testing"],
    )
    content = draft["content"]
    assert "# /kernel/" in content
    assert "## Instructions" in content
    assert "## When to Invoke" in content
    assert "## Source" in content


def test_draft_includes_source():
    draft = generate_draft(
        pattern_key="xyz789", issue="Config drift",
        fix="Re-anchor protocol", tags=["protocol"],
    )
    assert "xyz789" in draft["content"]
    assert draft["command_path"].startswith(".claude/commands/kernel/")
