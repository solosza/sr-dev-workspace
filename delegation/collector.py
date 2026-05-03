"""Result collector — parses and aggregates sub-agent results.

Supports waiting for async operations and formatting results.
"""

import subprocess
import time
from typing import List

from delegation.schema import DelegationRequest, DelegationResult


def collect_result(
    process: subprocess.Popen,
    request: DelegationRequest,
    start_time: float = 0.0,
) -> DelegationResult:
    """Wait for an async process and collect its result.

    Args:
        process: The Popen handle from execute_async.
        request: The original delegation request.
        start_time: When execution started (for duration calc).

    Returns:
        DelegationResult with execution outcome.
    """
    if start_time == 0.0:
        start_time = time.time()

    try:
        stdout, stderr = process.communicate(timeout=request.timeout_seconds)
        duration = time.time() - start_time

        return DelegationResult(
            success=(process.returncode == 0),
            exit_code=process.returncode,
            stdout=stdout or "",
            stderr=stderr or "",
            duration_seconds=round(duration, 2),
            target_repo=request.target_repo,
        )
    except subprocess.TimeoutExpired:
        process.kill()
        duration = time.time() - start_time
        return DelegationResult(
            success=False,
            exit_code=-1,
            stdout="",
            stderr=f"Timed out after {request.timeout_seconds}s",
            duration_seconds=round(duration, 2),
            target_repo=request.target_repo,
        )


def format_report(results: List[DelegationResult]) -> str:
    """Format a human-readable summary of delegation results.

    Args:
        results: List of DelegationResult instances.

    Returns:
        Formatted report string.
    """
    lines = ["DELEGATION REPORT", "=" * 50]
    for i, result in enumerate(results, 1):
        status = "PASS" if result.success else "FAIL"
        lines.append(f"\n[{i}] {status} — {result.target_repo}")
        lines.append(f"    Exit code: {result.exit_code}")
        lines.append(f"    Duration:  {result.duration_seconds}s")
        if result.stderr and not result.success:
            lines.append(f"    Error:     {result.stderr[:200]}")

    total = len(results)
    passed = sum(1 for r in results if r.success)
    lines.append(f"\nSummary: {passed}/{total} passed")
    return "\n".join(lines)


def all_succeeded(results: List[DelegationResult]) -> bool:
    """Check if all delegation results were successful.

    Args:
        results: List of DelegationResult instances.

    Returns:
        True if all results have success=True.
    """
    return all(r.success for r in results)
