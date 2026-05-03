"""Isagawa Kernel — Lessons subsystem.

Provides structured lesson recording with pattern-key fingerprinting,
recurrence detection, alert/escalation, tiered memory decay, and
skill extraction capabilities.
"""

from lessons.schema import LessonRecord, generate_fingerprint
from lessons.recurrence import RecurrenceTracker
from lessons.alerts import check_threshold, escalate, get_escalation_report
from lessons.tiers import MemoryTier, TieredLesson, assign_tier
from lessons.decay import DecayEngine
from lessons.promotion import evaluate_promotion, run_promotion_check
from lessons.archival import archive_cold, get_archived, restore_from_archive
from lessons.maturity import evaluate_maturity, calculate_fix_consistency
from lessons.draft_generator import generate_draft, suggest_command_name
from lessons.approval import request_approval, record_decision, get_decision
from lessons.promotion_tracker import track_promotion, is_promoted, get_promotions

__all__ = [
    # 008 — Recurrence Detection
    "LessonRecord",
    "generate_fingerprint",
    "RecurrenceTracker",
    "check_threshold",
    "escalate",
    "get_escalation_report",
    # 006 — Tiered Memory Decay
    "MemoryTier",
    "TieredLesson",
    "assign_tier",
    "DecayEngine",
    "evaluate_promotion",
    "run_promotion_check",
    "archive_cold",
    "get_archived",
    "restore_from_archive",
    # 007 — Skill Extraction
    "evaluate_maturity",
    "calculate_fix_consistency",
    "generate_draft",
    "suggest_command_name",
    "request_approval",
    "record_decision",
    "get_decision",
    "track_promotion",
    "is_promoted",
    "get_promotions",
]
