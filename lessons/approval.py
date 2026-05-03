"""User approval gate for generated commands.

Generated commands must not be auto-deployed. They require user approval
before being written to `.claude/commands/`.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional


DEFAULT_APPROVAL_REGISTRY = Path(".claude/state/skill_approvals.json")


def _load_registry(registry_path: Path) -> dict:
    """Load approval registry from disk."""
    if registry_path.exists():
        try:
            return json.loads(registry_path.read_text())
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def _save_registry(registry_path: Path, data: dict):
    """Save approval registry to disk."""
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(json.dumps(data, indent=2))


def format_approval_prompt(draft: dict) -> str:
    """Format a draft for human-readable review.

    Args:
        draft: The draft dict from generate_draft().

    Returns:
        Formatted string for display to user.
    """
    return (
        f"SKILL EXTRACTION — Approval Required\n"
        f"{'=' * 50}\n"
        f"\n"
        f"Command Name:  {draft['command_name']}\n"
        f"Target Path:   {draft['command_path']}\n"
        f"Source Pattern: {draft['source_pattern']}\n"
        f"\n"
        f"--- Proposed Content ---\n"
        f"{draft['content']}\n"
        f"--- End Content ---\n"
        f"\n"
        f"Approve this command? (yes/no)\n"
    )


def request_approval(draft: dict) -> str:
    """Format the draft for user review and return the approval prompt.

    Args:
        draft: The draft dict from generate_draft().

    Returns:
        Formatted approval request string.
    """
    return format_approval_prompt(draft)


def record_decision(
    pattern_key: str,
    approved: bool,
    command_name: str = "",
    registry_path: Optional[Path] = None,
) -> None:
    """Record an approval or rejection decision.

    Args:
        pattern_key: The lesson fingerprint.
        approved: Whether the command was approved.
        command_name: Name of the proposed command.
        registry_path: Path to approval registry.
    """
    if registry_path is None:
        registry_path = DEFAULT_APPROVAL_REGISTRY

    registry = _load_registry(registry_path)
    registry[pattern_key] = {
        "approved": approved,
        "timestamp": datetime.now().isoformat(),
        "command_name": command_name,
    }
    _save_registry(registry_path, registry)


def get_decision(
    pattern_key: str,
    registry_path: Optional[Path] = None,
) -> Optional[dict]:
    """Get the approval decision for a pattern.

    Args:
        pattern_key: The lesson fingerprint.
        registry_path: Path to approval registry.

    Returns:
        Decision dict or None if no decision recorded.
    """
    if registry_path is None:
        registry_path = DEFAULT_APPROVAL_REGISTRY

    registry = _load_registry(registry_path)
    return registry.get(pattern_key)
