"""Tests for lessons.maturity — maturity evaluation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.maturity import evaluate_maturity, calculate_fix_consistency


def test_immature_lesson():
    result = evaluate_maturity(2)
    assert result["is_mature"] is False
    assert result["recommendation"] == "too_early"


def test_mature_lesson():
    result = evaluate_maturity(7, fix_consistency=1.0)
    assert result["is_mature"] is True
    assert result["recommendation"] == "extract"
    assert result["score"] > 0.9


def test_inconsistent_fixes():
    result = evaluate_maturity(10, fix_consistency=0.3)
    assert result["is_mature"] is False
    assert result["recommendation"] == "monitor"


def test_fix_consistency_all_same():
    fixes = ["Added check", "Added check", "Added check"]
    assert calculate_fix_consistency(fixes) == 1.0


def test_fix_consistency_mixed():
    fixes = ["Added check", "Added check", "Different fix", "Added check"]
    consistency = calculate_fix_consistency(fixes)
    assert consistency == 0.75


def test_fix_consistency_empty():
    assert calculate_fix_consistency([]) == 0.0


def test_maturity_boundary():
    result = evaluate_maturity(5, fix_consistency=0.8)
    assert result["is_mature"] is True
    assert result["recommendation"] == "extract"
