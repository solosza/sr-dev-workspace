"""Delegation engine — spawns sub-processes in target repos.

Manages lifecycle: validate target, execute command, collect results.
"""

import os
import subprocess
import time
from pathlib import Path
from typing import Optional

from delegation.schema import DelegationRequest, DelegationResult


class DelegationEngine:
    """Executes commands in target repositories.

    Spawns subprocess with cwd set to target_repo, captures output,
    and returns structured results.
    """

    def validate_target(self, target_repo: str) -> bool:
        """Check if target repo exists and is a git repository.

        Args:
            target_repo: Absolute path to the repository.

        Returns:
            True if valid git repo exists at path.
        """
        repo_path = Path(target_repo)
        if not repo_path.exists():
            return False
        if not repo_path.is_dir():
            return False
        git_dir = repo_path / ".git"
        return git_dir.exists()

    def execute(self, request: DelegationRequest) -> DelegationResult:
        """Execute a command synchronously in the target repo.

        Args:
            request: The delegation request.

        Returns:
            DelegationResult with execution outcome.
        """
        env = os.environ.copy()
        env.update(request.env_vars)

        start_time = time.time()
        try:
            result = subprocess.run(
                request.command,
                shell=True,
                cwd=request.target_repo,
                capture_output=True,
                text=True,
                timeout=request.timeout_seconds,
                env=env,
            )
            duration = time.time() - start_time

            return DelegationResult(
                success=(result.returncode == 0),
                exit_code=result.returncode,
                stdout=result.stdout,
                stderr=result.stderr,
                duration_seconds=round(duration, 2),
                target_repo=request.target_repo,
            )
        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            return DelegationResult(
                success=False,
                exit_code=-1,
                stdout="",
                stderr=f"Command timed out after {request.timeout_seconds} seconds",
                duration_seconds=round(duration, 2),
                target_repo=request.target_repo,
            )
        except Exception as e:
            duration = time.time() - start_time
            return DelegationResult(
                success=False,
                exit_code=-2,
                stdout="",
                stderr=str(e),
                duration_seconds=round(duration, 2),
                target_repo=request.target_repo,
            )

    def execute_async(self, request: DelegationRequest) -> subprocess.Popen:
        """Execute a command asynchronously in the target repo.

        Args:
            request: The delegation request.

        Returns:
            Popen process handle for later collection.
        """
        env = os.environ.copy()
        env.update(request.env_vars)

        return subprocess.Popen(
            request.command,
            shell=True,
            cwd=request.target_repo,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
