"""Backfill task_count and completed_count for May 27 attestation bundles.

These bundles had null task_count because:
1. Python dict.get("total_tasks", 0) returns None when the value is null (not 0)
2. Attestation ran after workflow state was reset (total_tasks: null, completed_tasks: [])

This script patches the LOCAL bundle JSON files only.
Do NOT run on .sigstore.json files — those are signed and must not be altered.
"""

import json
import os

ATT_DIR = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/.claude/state/attestations"
COMPLETED_DIR = "D:/my_ai_projects/project_test_repos/sr_dev_workspace/tasks/completed"

BACKFILL = {
    "087-20260527T103244Z.json": {"folder": "multi-model-routing", "task_count": 6},
    "088-20260527T103258Z.json": {"folder": "ssh-compliance-spec-migration", "task_count": 17},
    "089-20260527T103310Z.json": {"folder": "universal-hook-validator-system", "task_count": 36},
    "090-20260527T103323Z.json": {"folder": "fix-execute-pipeline-cycling", "task_count": 8},
    "091-20260527T103156Z.json": {"folder": "sync-model-router", "task_count": 5},
}


def count_tasks_in_folder(folder_path: str) -> int:
    """Count NNN-*.md files (excluding 000-index and gate-contract)."""
    import re
    if not os.path.isdir(folder_path):
        return 0
    count = 0
    for fname in os.listdir(folder_path):
        if not fname.endswith(".md"):
            continue
        if "gate-contract" in fname:
            continue
        if re.match(r"^\d{3,}-", fname) and fname != "000-index.md":
            count += 1
    return count


def main():
    errors = []

    for bundle_filename, info in BACKFILL.items():
        bundle_path = os.path.join(ATT_DIR, bundle_filename)
        folder_path = os.path.join(COMPLETED_DIR, info["folder"])

        if not os.path.isfile(bundle_path):
            print(f"SKIP: {bundle_filename} — file not found")
            continue

        # Verify against live folder count
        live_count = count_tasks_in_folder(folder_path)
        expected_count = info["task_count"]
        if live_count != expected_count:
            print(f"WARN: {bundle_filename}: live folder count {live_count} != expected {expected_count}")
            # Use live count as authoritative
            actual_count = live_count if live_count > 0 else expected_count
        else:
            actual_count = expected_count

        # Read bundle
        with open(bundle_path, "r") as f:
            bundle = json.load(f)

        # Patch metadata
        current_tc = bundle.get("predicate", {}).get("metadata", {}).get("task_count")
        current_cc = bundle.get("predicate", {}).get("metadata", {}).get("completed_count")

        bundle["predicate"]["metadata"]["task_count"] = actual_count
        bundle["predicate"]["metadata"]["completed_count"] = actual_count  # all tasks completed

        # Write back
        with open(bundle_path, "w") as f:
            json.dump(bundle, f, indent=2)

        print(f"OK: {bundle_filename}: task_count {current_tc} -> {actual_count}, completed_count {current_cc} -> {actual_count}")

    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("\nBackfill complete.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
