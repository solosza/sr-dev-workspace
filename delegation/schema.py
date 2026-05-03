"""Data models for cross-repo delegation.

Defines what gets sent to a sub-agent (DelegationRequest)
and what comes back (DelegationResult).
"""

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class DelegationRequest:
    """Request to delegate work to another repo.

    Attributes:
        target_repo: Absolute path to the target repository.
        command: Shell command to execute in the target repo.
        expected_output: Description of expected successful output.
        timeout_seconds: Max execution time. Default 300 (5 min).
        env_vars: Additional environment variables to set.
    """
    target_repo: str
    command: str
    expected_output: str = ""
    timeout_seconds: int = 300
    env_vars: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "target_repo": self.target_repo,
            "command": self.command,
            "expected_output": self.expected_output,
            "timeout_seconds": self.timeout_seconds,
            "env_vars": self.env_vars,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "DelegationRequest":
        return cls(
            target_repo=data["target_repo"],
            command=data["command"],
            expected_output=data.get("expected_output", ""),
            timeout_seconds=data.get("timeout_seconds", 300),
            env_vars=data.get("env_vars", {}),
        )


@dataclass
class DelegationResult:
    """Result from a delegated sub-agent execution.

    Attributes:
        success: Whether the command succeeded (exit code 0).
        exit_code: Process exit code.
        stdout: Standard output.
        stderr: Standard error.
        duration_seconds: Execution time in seconds.
        target_repo: The repo this was executed in.
    """
    success: bool
    exit_code: int
    stdout: str = ""
    stderr: str = ""
    duration_seconds: float = 0.0
    target_repo: str = ""

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "exit_code": self.exit_code,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "duration_seconds": self.duration_seconds,
            "target_repo": self.target_repo,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "DelegationResult":
        return cls(
            success=data["success"],
            exit_code=data["exit_code"],
            stdout=data.get("stdout", ""),
            stderr=data.get("stderr", ""),
            duration_seconds=data.get("duration_seconds", 0.0),
            target_repo=data.get("target_repo", ""),
        )
