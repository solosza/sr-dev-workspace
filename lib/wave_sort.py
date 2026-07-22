"""Wave sorting via Kahn's algorithm for DAG-based task dispatch.

Implements topological sort to extract execution waves from task dependencies.
Detects cycles and errors before any spawning occurs.
"""

import re
from typing import Dict, List, Set, Tuple


def parse_index_dependencies(index_path: str) -> Dict[int, List[int]]:
    """Parse 000-index.md to extract task dependencies.

    Looks for markdown table with format:
    | # | Task | Type | Dependencies | ... |
    | 001 | ... | BUILD | none | ... |
    | 002 | ... | BUILD | 001 | ... |
    | 005 | ... | TEST | 002, 003, 004 | ... |

    Returns: {task_number: [dependency_numbers]}
    Raises: ValueError if parsing fails or dependencies reference non-existent tasks
    """
    adjacency = {}
    all_tasks = set()

    try:
        with open(index_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        raise ValueError(f"Index file not found: {index_path}")

    # Extract table rows: | NNN | ... | ... | dependencies? |
    # Handles both 3-column (no deps) and 4+ column (with deps) tables

    # Try: 4+ columns with Dependencies column (columns: #, Task, Type, Dependencies)
    rows_4col = re.findall(r'\|\s*(\d{3})\s*\|[^|]*\|[^|]*\|([^|]*?)\|', content)

    # Check if we have valid 4-column data (dependencies column should have content or "none")
    has_deps_column = False
    if rows_4col:
        # Filter for rows that have actual dependency content (not just whitespace/newlines)
        valid_rows = [
            (task_str, deps_str) for task_str, deps_str in rows_4col
            if deps_str.strip() and deps_str.strip() not in ['\n', '\r']
        ]
        has_deps_column = len(valid_rows) > 0

    if has_deps_column and rows_4col:
        # 4+ column table with Dependencies column found
        for task_str, deps_str in rows_4col:
            task_num = int(task_str)
            all_tasks.add(task_num)

            # Parse dependencies
            deps_str = deps_str.strip().lower()
            if deps_str == 'none' or deps_str == '':
                adjacency[task_num] = []
            else:
                # Split on comma, extract numbers
                deps = []
                for dep_str in deps_str.split(','):
                    dep_str = dep_str.strip()
                    if dep_str and dep_str != 'none':
                        try:
                            dep_num = int(''.join(c for c in dep_str if c.isdigit()))
                            deps.append(dep_num)
                        except ValueError:
                            pass
                adjacency[task_num] = deps
    else:
        # Fall back to 3-column table (no Dependencies column)
        rows_3col = re.findall(r'\|\s*(\d{3})\s*\|[^|]*\|[^|]*\|', content)
        if rows_3col:
            for task_str in rows_3col:
                task_num = int(task_str)
                all_tasks.add(task_num)
                adjacency[task_num] = []

    if not adjacency:
        raise ValueError(f"No task table found in {index_path}")

    # Validate: all referenced dependencies exist
    for task_num, deps in adjacency.items():
        for dep in deps:
            if dep not in all_tasks:
                raise ValueError(
                    f"Task {task_num} depends on {dep}, but task {dep} not found in index"
                )

    return adjacency


def topological_sort_waves(adjacency: Dict[int, List[int]]) -> Tuple[List[List[int]], str]:
    """Sort tasks into waves using Kahn's algorithm (BFS-based).

    Detects cycles and errors before returning.

    Args:
        adjacency: {task_number: [dependency_numbers]}

    Returns:
        (waves, error_msg) where:
        - waves: List of waves, each wave is a list of task numbers
        - error_msg: Empty string if successful, error message if cycle detected

    Example:
        Input: {1: [], 2: [1], 3: [1], 4: [1], 5: [2, 3, 4]}
        Output: ([[1], [2, 3, 4], [5]], "")
    """
    if not adjacency:
        return ([], "")

    # Build reverse adjacency (task -> list of tasks that depend on it)
    reverse_adj = {task: [] for task in adjacency}
    in_degree = {task: 0 for task in adjacency}

    for task, deps in adjacency.items():
        in_degree[task] = len(deps)
        for dep in deps:
            reverse_adj[dep].append(task)

    # Kahn's algorithm: extract waves
    waves = []
    remaining = set(adjacency.keys())

    while remaining:
        # Find all tasks with in-degree 0 (ready tasks)
        wave = [task for task in remaining if in_degree[task] == 0]

        if not wave:
            # Cycle detected: tasks remain but none are ready
            cycle_tasks = sorted(remaining)
            error_msg = f"ERROR: Circular dependency detected. Tasks in cycle: {cycle_tasks}"
            return ([], error_msg)

        waves.append(sorted(wave))

        # Remove this wave's tasks and decrement dependents' in-degree
        for task in wave:
            remaining.discard(task)
            for dependent in reverse_adj[task]:
                in_degree[dependent] -= 1

    return (waves, "")


def get_waves(index_path: str) -> Tuple[List[List[int]], str]:
    """Main entry point: parse index and return execution waves.

    Args:
        index_path: Path to 000-index.md

    Returns:
        (waves, error_msg) where:
        - waves: List of waves if successful, empty list if error
        - error_msg: Empty string if successful, error message if any failure
    """
    try:
        adjacency = parse_index_dependencies(index_path)
        return topological_sort_waves(adjacency)
    except ValueError as e:
        return ([], str(e))
