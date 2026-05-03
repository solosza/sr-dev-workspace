"""End-to-end test for skill extraction flow."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from lessons.maturity import evaluate_maturity, calculate_fix_consistency
from lessons.draft_generator import generate_draft
from lessons.approval import request_approval, record_decision, get_decision
from lessons.promotion_tracker import track_promotion, is_promoted, get_promotions
from lessons.integrations import notify_skill_extraction, INTEGRATION_READY


def test_full_extraction_flow(tmp_path):
    approval_registry = tmp_path / "approvals.json"
    promotion_registry = tmp_path / "promotions.json"

    fixes = ["Add PROTECTED_PATHS check"] * 6
    consistency = calculate_fix_consistency(fixes)
    assessment = evaluate_maturity(6, fix_consistency=consistency)
    assert assessment["is_mature"] is True
    assert assessment["recommendation"] == "extract"

    draft = generate_draft(
        pattern_key="abc123",
        issue="Hook bypass via direct state edit",
        fix="Add PROTECTED_PATHS check",
        tags=["hook", "enforcement"],
    )
    assert draft["command_name"] != ""

    prompt = request_approval(draft)
    assert "Approve" in prompt

    record_decision("abc123", True, draft["command_name"], registry_path=approval_registry)
    decision = get_decision("abc123", registry_path=approval_registry)
    assert decision["approved"] is True

    track_promotion("abc123", draft["command_name"], draft["command_path"], registry_path=promotion_registry)
    assert is_promoted("abc123", registry_path=promotion_registry) is True

    promotions = get_promotions(registry_path=promotion_registry)
    assert len(promotions) == 1
    assert promotions[0]["pattern_key"] == "abc123"


def test_integration_readiness():
    assert INTEGRATION_READY["skill_extraction"] is True


def test_notify_skill_extraction():
    result = notify_skill_extraction("abc", 7, "test issue", "test fix")
    assert "is_mature" in result
    assert "recommendation" in result
    assert result["is_mature"] is True
