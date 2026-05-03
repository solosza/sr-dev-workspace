"""Factory task type — parses and executes factory-mode tasks.

When a task has `## Execution: factory`, this module extracts the
delegation parameters and runs the task in the target repo.
"""

import re
from typing import Optional

from delegation.schema import DelegationRequest, DelegationResult
from delegation.engine import DelegationEngine


def is_factory_task(task_content: str) -> bool:
    """Check if a task file has factory execution mode.

    Args:
        task_content: Full markdown content of the task file.

    Returns:
        True if task has `## Execution` section with `factory`.
    """
    # Look for ## Execution section with "factory"
    pattern = r'##\s+Execution\s*\n\s*factory'
    return bool(re.search(pattern, task_content, re.IGNORECASE))


def parse_factory_section(task_content: str) -> Optional[DelegationRequest]:
    """Extract delegation parameters from a factory task's ## Factory section.

    Expected format in task markdown:
    ```
    ## Factory
    - target_repo: /path/to/repo
    - command: some command to run
    - expected_output: description of expected output
    ```

    Args:
        task_content: Full markdown content of the task file.

    Returns:
        DelegationRequest if factory section found, None otherwise.
    """
    # Find ## Factory section
    factory_match = re.search(
        r'##\s+Factory\s*\n(.*?)(?=\n##|\Z)',
        task_content,
        re.DOTALL | re.IGNORECASE,
    )

    if not factory_match:
        return None

    section = factory_match.group(1)

    # Extract fields
    target_repo = _extract_field(section, "target_repo")
    command = _extract_field(section, "command")
    expected_output = _extract_field(section, "expected_output") or ""

    if not target_repo or not command:
        return None

    return DelegationRequest(
        target_repo=target_repo,
        command=command,
        expected_output=expected_output,
    )


def _extract_field(text: str, field_name: str) -> Optional[str]:
    r"""Extract a field value from markdown list format.

    Matches: ``- field_name: value`` or ``- field_name: `value` ``
    """
    pattern = rf'-\s+{field_name}:\s*`?([^`\n]+)`?'
    match = re.search(pattern, text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None


def run_factory_task(
    task_content: str,
    engine: Optional[DelegationEngine] = None,
) -> Optional[DelegationResult]:
    """Parse and execute a factory task.

    Args:
        task_content: Full markdown content of the task file.
        engine: DelegationEngine instance. Creates one if not provided.

    Returns:
        DelegationResult, or None if not a valid factory task.
    """
    if not is_factory_task(task_content):
        return None

    request = parse_factory_section(task_content)
    if request is None:
        return None

    if engine is None:
        engine = DelegationEngine()

    if not engine.validate_target(request.target_repo):
        return DelegationResult(
            success=False,
            exit_code=-3,
            stderr=f"Target repo not found or not a git repo: {request.target_repo}",
            target_repo=request.target_repo,
        )

    return engine.execute(request)
