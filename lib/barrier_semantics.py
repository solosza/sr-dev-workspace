"""Wave barrier logic with failure decision table implementation.

Handles wave transitions, failure classification, and partial dispatch semantics.
"""

from typing import Dict, List, Set, Tuple
from enum import Enum


class AgentStatus(Enum):
    """Agent outcome states."""
    COMPLETE = "complete"
    FAILED = "failed"
    SKIPPED = "skipped"
    TIMED_OUT = "timed_out"
    RUNNING = "running"
    BLOCKED = "blocked"


def classify_agent_outcome(agent_state: Dict) -> AgentStatus:
    """Classify an agent's outcome from its state file.

    Reads the agent's final status and maps to AgentStatus enum.
    """
    status = agent_state.get("status", "running").lower()

    if status == "complete":
        return AgentStatus.COMPLETE
    elif status == "failed":
        return AgentStatus.FAILED
    elif status == "skipped":
        return AgentStatus.SKIPPED
    elif status == "timed_out":
        return AgentStatus.TIMED_OUT
    elif status == "running":
        return AgentStatus.RUNNING
    elif status == "blocked":
        return AgentStatus.BLOCKED
    else:
        return AgentStatus.RUNNING


def get_blocking_agents(wave_outcomes: Dict[int, AgentStatus]) -> Set[int]:
    """Extract agents that should block downstream dependents.

    Args:
        wave_outcomes: {agent_id: AgentStatus} for current completed wave

    Returns:
        Set of agent IDs with FAILED/SKIPPED/TIMED_OUT status
    """
    return {
        agent_id for agent_id, status in wave_outcomes.items()
        if status in (AgentStatus.FAILED, AgentStatus.SKIPPED, AgentStatus.TIMED_OUT)
    }


def apply_partial_dispatch_policy(
    next_wave_plan: List[Dict],
    current_wave_outcomes: Dict[int, AgentStatus],
    all_wave_dependencies: Dict[int, List[int]]
) -> Tuple[List[Dict], List[Dict]]:
    """Apply partial dispatch policy to determine which agents in next wave can run.

    Partial dispatch: Only agents that depend on failed/skipped/timed-out agents are blocked.
    Independent agents proceed even if others in the same wave failed.

    Args:
        next_wave_plan: [{backlog: N, tasks: [...]}, ...] for next wave
        current_wave_outcomes: {agent_id: AgentStatus} from current completed wave
        all_wave_dependencies: {task_id: [dependency_task_ids]} across all waves

    Returns:
        (dispatched_agents, blocked_agents)
        - dispatched_agents: can run in next wave
        - blocked_agents: should not run (dependency failed/skipped/timed_out)
    """
    blocking_agents = get_blocking_agents(current_wave_outcomes)
    dispatched = []
    blocked = []

    for agent_entry in next_wave_plan:
        backlog_id = agent_entry["backlog"]

        # Get this agent's dependencies
        dependencies = all_wave_dependencies.get(backlog_id, [])

        # Check if ANY dependency is blocking
        has_blocking_dep = any(dep in blocking_agents for dep in dependencies)

        if has_blocking_dep:
            # This agent is blocked
            agent_entry["status"] = AgentStatus.BLOCKED.value
            blocked.append(agent_entry)
        else:
            # This agent can dispatch
            dispatched.append(agent_entry)

    return (dispatched, blocked)


def detect_orphaned_wave(dispatched_agents: List[Dict]) -> bool:
    """Detect if next wave is entirely blocked (no tasks to dispatch).

    Args:
        dispatched_agents: Result of apply_partial_dispatch_policy

    Returns:
        True if no agents can dispatch
    """
    return len(dispatched_agents) == 0


def update_manifest_wave_transition(
    manifest: Dict,
    next_wave_id: int,
    dispatched_agents: List[Dict],
    blocked_agents: List[Dict]
) -> Dict:
    """Update manifest after wave transition decision.

    Records:
    - Which wave is now active (current_wave)
    - Which agents in next wave can dispatch
    - Which agents are blocked (and why)

    Args:
        manifest: Current manifest
        next_wave_id: Wave ID to transition to
        dispatched_agents: Agents that will dispatch
        blocked_agents: Agents that are blocked

    Returns:
        Updated manifest
    """
    # Mark current wave as complete
    current_wave_id = manifest.get("current_wave", 0)

    # Update waves_completed list
    if "waves_completed" not in manifest:
        manifest["waves_completed"] = []
    manifest["waves_completed"].append(current_wave_id)

    # Set new current wave
    manifest["current_wave"] = next_wave_id

    # Record blocked agents in manifest for diagnostics
    if not blocked_agents:
        manifest["blocked_agents"] = {}
    else:
        if "blocked_agents" not in manifest:
            manifest["blocked_agents"] = {}
        manifest["blocked_agents"][next_wave_id] = [
            a["backlog"] for a in blocked_agents
        ]

    # Update active_agents with new wave's dispatched set
    if "active_agents" not in manifest:
        manifest["active_agents"] = []

    # Keep completed/blocked agents in history, add new dispatched agents
    new_active = [
        a for a in manifest["active_agents"]
        if a.get("wave_id", 0) < next_wave_id
    ]

    # Add dispatched agents from next wave
    for agent in dispatched_agents:
        new_active.append({
            "backlog": agent["backlog"],
            "wave_id": next_wave_id,
            "status": "running",
            "spawned_at": None,  # Will be set by step-03
            "last_update": None,
            "progress": "0/? tasks"
        })

    manifest["active_agents"] = new_active

    return manifest
