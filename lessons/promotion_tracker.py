"""Promotion tracker — records which lessons have been promoted to skills.

Prevents duplicate promotions and enables status queries.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional


DEFAULT_PROMOTIONS_REGISTRY = Path(".claude/state/promoted_lessons.json")


def _load_registry(registry_path: Path) -> dict:
    """Load promotions registry from disk."""
    if registry_path.exists():
        try:
            return json.loads(registry_path.read_text())
        except (json.JSONDecodeError, IOError):
            return {}
    return {}


def _save_registry(registry_path: Path, data: dict):
    """Save promotions registry to disk."""
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(json.dumps(data, indent=2))


def track_promotion(
    pattern_key: str,
    command_name: str,
    command_path: str,
    registry_path: Optional[Path] = None,
) -> None:
    """Record that a lesson was promoted to a skill/command.

    Args:
        pattern_key: The lesson fingerprint.
        command_name: Name of the generated command.
        command_path: File path of the generated command.
        registry_path: Path to promotions registry.
    """
    if registry_path is None:
        registry_path = DEFAULT_PROMOTIONS_REGISTRY

    registry = _load_registry(registry_path)
    registry[pattern_key] = {
        "command_name": command_name,
        "command_path": command_path,
        "promoted_at": datetime.now().isoformat(),
    }
    _save_registry(registry_path, registry)


def is_promoted(
    pattern_key: str,
    registry_path: Optional[Path] = None,
) -> bool:
    """Check if a lesson has already been promoted.

    Args:
        pattern_key: The lesson fingerprint.
        registry_path: Path to promotions registry.

    Returns:
        True if the lesson has been promoted.
    """
    if registry_path is None:
        registry_path = DEFAULT_PROMOTIONS_REGISTRY

    registry = _load_registry(registry_path)
    return pattern_key in registry


def get_promotions(
    registry_path: Optional[Path] = None,
) -> List[dict]:
    """Return all recorded promotions.

    Args:
        registry_path: Path to promotions registry.

    Returns:
        List of promotion records.
    """
    if registry_path is None:
        registry_path = DEFAULT_PROMOTIONS_REGISTRY

    registry = _load_registry(registry_path)
    result = []
    for key, data in registry.items():
        entry = dict(data)
        entry["pattern_key"] = key
        result.append(entry)
    return result
