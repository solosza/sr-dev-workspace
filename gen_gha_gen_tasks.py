#!/usr/bin/env python3
"""Generate 35 task files for github-actions-generator-spec validation."""
import os

OUTPUT_DIR = "D:/my_ai_projects/project_test_repos/test-gha-gen-validation/tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

gates = [
    ("SPEC-01", "SKILL.md exists", "file_exists .claude/skills/gha-generator/SKILL.md", "SKILL.md exists"),
    ("SPEC-02", "workflow.md exists", "file_exists .claude/skills/gha-generator/workflow.md", "workflow.md exists"),
    ("SPEC-03", "gate-contract.md exists", "file_exists .claude/skills/gha-generator/gate-contract.md", "gate-contract.md exists"),
    ("SPEC-04", "SKILL.md has YAML frontmatter", "grep SKILL.md for name: gha-generator", "SKILL.md contains name: gha-generator"),
    ("SPEC-05", "SKILL.md has domain vocabulary", "grep SKILL.md for Domain Vocabulary", "SKILL.md contains Domain Vocabulary section"),
    ("DISC-01", "Phase 1 file exists", "file_exists phases/phase-01-discovery.md", "phase-01-discovery.md exists"),
    ("DISC-02", "Opening question defined", "grep phase-01-discovery.md for What does your pipeline need", "Opening question documented"),
    ("DISC-03", "Follow-up strategy documented", "grep phase-01-discovery.md for Follow-Up Strategy", "Follow-up strategy section present"),
    ("DISC-04", "Depth signals defined", "grep phase-01-discovery.md for Depth Signals", "Depth signals section present"),
    ("DISC-05", "Pipeline profile output structure", "grep phase-01-discovery.md for Pipeline Profile Structure", "Profile output section present"),
    ("DEC-01", "Phase 2 file exists", "file_exists phases/phase-02-decisions.md", "phase-02-decisions.md exists"),
    ("DEC-02", "Decision tree references present", "grep phase-02-decisions.md for _decision-trees/", "Decision tree references present"),
    ("DEC-03", "Deployment strategy tree exists", "file_exists _decision-trees/deployment-strategy.md", "deployment-strategy.md exists"),
    ("DEC-04", "Secret management tree exists", "file_exists _decision-trees/secret-management.md", "secret-management.md exists"),
    ("DEC-05", "Runner selection tree exists", "file_exists _decision-trees/runner-selection.md", "runner-selection.md exists"),
    ("DEC-06", "Caching strategy tree exists", "file_exists _decision-trees/caching-strategy.md", "caching-strategy.md exists"),
    ("ARCH-01", "Phase 3 file exists", "file_exists phases/phase-03-architecture.md", "phase-03-architecture.md exists"),
    ("ARCH-02", "Job graph design documented", "grep phase-03-architecture.md for Job Graph", "Job graph section present"),
    ("ARCH-03", "Environment configuration documented", "grep phase-03-architecture.md for Environment Configuration", "Environment config section present"),
    ("GEN-01", "Phase 4 file exists", "file_exists phases/phase-04-generate.md", "phase-04-generate.md exists"),
    ("GEN-02", "Security defaults section", "grep phase-04-generate.md for Security Defaults Checklist", "Security defaults section present"),
    ("GEN-03", "SHA pinning rule documented", "grep phase-04-generate.md for SHA pin", "SHA pinning instructions present"),
    ("GEN-04", "Permissions rule documented", "grep phase-04-generate.md for permissions:", "Permissions instructions present"),
    ("GEN-05", "persist-credentials rule documented", "grep phase-04-generate.md for persist-credentials: false", "persist-credentials rule present"),
    ("ITER-01", "Phase 5 file exists", "file_exists phases/phase-05-iterate.md", "phase-05-iterate.md exists"),
    ("ITER-02", "Re-validation requirement documented", "grep phase-05-iterate.md for re-validate", "Re-validation section present"),
    ("CHK-01", "Requirements review checkpoint exists", "file_exists checkpoints/requirements-review.md", "Checkpoint file exists"),
    ("CHK-02", "Architecture review checkpoint exists", "file_exists checkpoints/architecture-review.md", "Checkpoint file exists"),
    ("CHK-03", "Pre-generate checkpoint exists", "file_exists checkpoints/pre-generate.md", "Checkpoint file exists"),
    ("CHK-04", "Generation complete checkpoint exists", "file_exists checkpoints/generation-complete.md", "Checkpoint file exists"),
    ("CHK-05", "On-failure checkpoint exists", "file_exists checkpoints/on-failure.md", "Checkpoint file exists"),
    ("LES-01", "Lesson index exists", "file_exists lessons/lessons.md", "Lesson index exists"),
    ("LES-02", "Discovery lessons exist", "file_exists lessons/gha-generator/discovery.md", "Discovery lessons file exists"),
    ("LES-03", "Generation lessons exist", "file_exists lessons/gha-generator/generation.md", "Generation lessons file exists"),
    ("LES-04", "Security lessons exist", "file_exists lessons/gha-generator/security-defaults.md", "Security lessons file exists"),
]

for i, (gate_id, desc, verification, criteria) in enumerate(gates, 1):
    filename = f"{i:03d}-validate-{gate_id.lower()}.md"
    content = f"""# Task {i:03d}: Validate {gate_id}

## Gate
- **ID:** {gate_id}
- **Description:** {desc}

## Verification Method
{verification}

## Acceptance Criteria
- [ ] {criteria}

## Source
Gate contract: `.claude/skills/gha-generator/gate-contract.md`
"""
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {OUTPUT_DIR}")
