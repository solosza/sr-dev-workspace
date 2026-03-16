#!/usr/bin/env python3
"""Generate validation task files from azure-devops-generator-spec gate-contract."""

import os

TASKS_DIR = "D:/my_ai_projects/project_test_repos/test-azdo-gen-validation/tasks"

# Gates extracted from gate-contract.md
GATES = [
    # SPEC Gates
    ("SPEC-01", "SKILL.md exists", "file_exists", ".claude/skills/azdo-generator/SKILL.md exists", "Create SKILL.md"),
    ("SPEC-02", "workflow.md exists", "file_exists", ".claude/skills/azdo-generator/workflow.md exists", "Create workflow.md"),
    ("SPEC-03", "gate-contract.md exists", "file_exists", ".claude/skills/azdo-generator/gate-contract.md exists", "Create gate-contract.md"),
    ("SPEC-04", "SKILL.md has YAML frontmatter", "grep", "SKILL.md contains `name: azdo-generator`", "Add frontmatter to SKILL.md"),
    ("SPEC-05", "SKILL.md has domain vocabulary table", "grep", "SKILL.md contains `Domain Vocabulary`", "Add vocabulary section"),
    # DISC Gates
    ("DISC-01", "Phase 1 file exists", "file_exists", "phases/phase-01-discovery.md exists", "Create phase-01-discovery.md"),
    ("DISC-02", "Opening question defined", "grep", "phase-01-discovery.md contains `What does your pipeline need`", "Add opening question"),
    ("DISC-03", "Follow-up strategy documented", "grep", "phase-01-discovery.md contains `Follow-Up Strategy`", "Add follow-up strategy section"),
    ("DISC-04", "Depth signals defined", "grep", "phase-01-discovery.md contains `Depth Signals`", "Add depth signals section"),
    ("DISC-05", "Pipeline profile output structure", "grep", "phase-01-discovery.md contains `Pipeline Profile Structure`", "Add profile output section"),
    # DEC Gates
    ("DEC-01", "Phase 2 file exists", "file_exists", "phases/phase-02-decisions.md exists", "Create phase-02-decisions.md"),
    ("DEC-02", "Decision tree references present", "grep", "phase-02-decisions.md contains `_decision-trees/`", "Add decision tree references"),
    ("DEC-03", "Deployment strategy tree exists", "file_exists", "_decision-trees/deployment-strategy.md exists", "Create deployment-strategy.md"),
    ("DEC-04", "Secret management tree exists", "file_exists", "_decision-trees/secret-management.md exists", "Create secret-management.md"),
    ("DEC-05", "Runner selection tree exists", "file_exists", "_decision-trees/runner-selection.md exists", "Create runner-selection.md"),
    ("DEC-06", "Caching strategy tree exists", "file_exists", "_decision-trees/caching-strategy.md exists", "Create caching-strategy.md"),
    # ARCH Gates
    ("ARCH-01", "Phase 3 file exists", "file_exists", "phases/phase-03-architecture.md exists", "Create phase-03-architecture.md"),
    ("ARCH-02", "Stage graph design documented", "grep", "phase-03-architecture.md contains `Stage Graph`", "Add stage graph section"),
    ("ARCH-03", "Environment configuration documented", "grep", "phase-03-architecture.md contains `Environment Configuration`", "Add environment config section"),
    # GEN Gates
    ("GEN-01", "Phase 4 file exists", "file_exists", "phases/phase-04-generate.md exists", "Create phase-04-generate.md"),
    ("GEN-02", "Security defaults section", "grep", "phase-04-generate.md contains `Security Defaults Checklist`", "Add security defaults"),
    ("GEN-03", "Task version pinning rule documented", "grep", "phase-04-generate.md contains `task version pinning`", "Add task pinning instructions"),
    ("GEN-04", "Condition expressions documented", "grep", "phase-04-generate.md contains `condition:`", "Add condition expression instructions"),
    ("GEN-05", "Exclusive lock rule documented", "grep", "phase-04-generate.md contains `lockBehavior`", "Add exclusive lock rule"),
    # ITER Gates
    ("ITER-01", "Phase 5 file exists", "file_exists", "phases/phase-05-iterate.md exists", "Create phase-05-iterate.md"),
    ("ITER-02", "Re-validation requirement documented", "grep", "phase-05-iterate.md contains `re-validate`", "Add re-validation section"),
    # CHK Gates
    ("CHK-01", "Requirements review checkpoint exists", "file_exists", "checkpoints/requirements-review.md exists", "Create checkpoint"),
    ("CHK-02", "Architecture review checkpoint exists", "file_exists", "checkpoints/architecture-review.md exists", "Create checkpoint"),
    ("CHK-03", "Pre-generate checkpoint exists", "file_exists", "checkpoints/pre-generate.md exists", "Create checkpoint"),
    ("CHK-04", "Generation complete checkpoint exists", "file_exists", "checkpoints/generation-complete.md exists", "Create checkpoint"),
    ("CHK-05", "On-failure checkpoint exists", "file_exists", "checkpoints/on-failure.md exists", "Create checkpoint"),
    # LES Gates
    ("LES-01", "Lesson index exists", "file_exists", "lessons/lessons.md exists", "Create lesson index"),
    ("LES-02", "Discovery lessons exist", "file_exists", "lessons/azdo-generator/discovery.md exists", "Create discovery lessons"),
    ("LES-03", "Generation lessons exist", "file_exists", "lessons/azdo-generator/generation.md exists", "Create generation lessons"),
    ("LES-04", "Security lessons exist", "file_exists", "lessons/azdo-generator/security-defaults.md exists", "Create security lessons"),
    # CONTR Gates
    ("CONTR-01", "All phase files reference correct templates", "manual", "Phase files reference `_templates/` for output artifacts", "Fix template references"),
    ("CONTR-02", "Security defaults appear in generation phase", "grep", "phase-04-generate.md contains `persistCredentials`", "Add persistCredentials generation"),
]


def generate_task(index: int, gate_id: str, check: str, method: str, pass_criteria: str, fail_action: str) -> str:
    """Generate a single task file content."""
    return f"""# Task {index:03d}: Validate Gate {gate_id}

## Gate
- **ID:** {gate_id}
- **Check:** {check}
- **Verification method:** `{method}`

## Acceptance Criteria
- {pass_criteria}

## Pass Criteria
{_method_instructions(method, pass_criteria)}

## On Failure
- {fail_action}
"""


def _method_instructions(method: str, pass_criteria: str) -> str:
    if method == "file_exists":
        path = pass_criteria.replace(" exists", "")
        return f"- File `{path}` must exist in the workspace under `.claude/skills/azdo-generator/`"
    elif method == "grep":
        return f"- Search the specified file for the pattern described: {pass_criteria}"
    elif method == "manual":
        return f"- Orchestrator reads the file and judges: {pass_criteria}"
    return f"- Verify: {pass_criteria}"


def main():
    os.makedirs(TASKS_DIR, exist_ok=True)
    for i, (gate_id, check, method, pass_criteria, fail_action) in enumerate(GATES, 1):
        content = generate_task(i, gate_id, check, method, pass_criteria, fail_action)
        filename = f"{i:03d}-gate-{gate_id}.md"
        filepath = os.path.join(TASKS_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {filename}")
    print(f"\nTotal: {len(GATES)} task files generated in {TASKS_DIR}")


if __name__ == "__main__":
    main()
