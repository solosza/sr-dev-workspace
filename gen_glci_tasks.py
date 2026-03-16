#!/usr/bin/env python3
"""Generate 67 task files for gitlab-ci-spec validation."""
import os

OUTPUT_DIR = "D:/my_ai_projects/project_test_repos/test-glci-validation/tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

gates = [
    ("DISC-01", "Root config file scanning", "grep step-01.md for .gitlab-ci.yml AND root", "Root config file path and scan target documented"),
    ("DISC-02", "YAML parsing instructions", "grep step-01.md for YAML AND parse AND valid", "YAML parse with error handling documented"),
    ("DISC-03", "Include resolution", "grep step-01.md for include AND local AND remote AND template", "All include types documented"),
    ("DISC-04", "Stage graph construction", "grep step-01.md for stage_graph AND stages AND DAG", "Stage ordering and DAG construction documented"),
    ("DISC-05", "Job inventory extraction", "grep step-01.md for stage AND needs AND script", "Jobs extracted with stage, needs, and script metadata"),
    ("DISC-06", "Variable catalog", "grep step-01.md for variable_catalog AND global AND job", "Variable inventory at global and job levels documented"),
    ("DISC-07", "Include tree construction", "grep step-01.md for include_tree AND depth AND merge", "Include resolution tree with merge order documented"),
    ("DISC-08", "Trigger job detection", "grep step-01.md for trigger AND downstream AND child", "Bridge jobs for child and downstream pipelines detected"),
    ("STRUCT-01", "YAML schema validation", "grep step-02.md for YAML AND schema AND top-level", "YAML schema with valid top-level keys documented"),
    ("STRUCT-02", "Duplicate key detection", "grep step-02.md for duplicate keys AND well-formed", "Duplicate key detection and YAML well-formedness"),
    ("STRUCT-03", "Needs DAG cycle detection", "grep step-02.md for needs AND cycle AND circular AND DAG", "Circular dependency detection in needs graph"),
    ("STRUCT-04", "Rules logic validation", "grep step-02.md for rules AND only AND except AND merge_request_event", "Rules/only/except consistency and MR event handling"),
    ("STRUCT-05", "Extends chain validation", "grep step-02.md for extends AND hidden AND chain", "Extends inheritance chain resolution and circular detection"),
    ("STRUCT-06", "Anchor and alias resolution", "grep step-02.md for anchor AND alias AND scope", "YAML anchor scope and alias resolution validated"),
    ("STRUCT-07", "Stage ordering validation", "grep step-02.md for stage AND declared AND job", "Job stage assignments checked against declared stages"),
    ("STRUCT-08", "Script keyword validation", "grep step-02.md for script AND run AND keyword", "Script vs run keyword usage and unknown keywords flagged"),
    ("STRUCT-09", "Only/except deprecation", "grep step-02.md for only AND except AND legacy AND migrate", "Legacy only/except detected with migration guidance"),
    ("STRUCT-10", "Workflow rules validation", "grep step-02.md for workflow AND rules AND pipeline", "Workflow-level rules checked for pipeline creation logic"),
    ("SEC-01", "Variable masking audit", "grep step-03.md for masked AND variable AND sensitive", "CI/CD variables checked for masking of sensitive values"),
    ("SEC-02", "Variable protection audit", "grep step-03.md for protected AND variable AND branch", "Protected variable scoping to protected branches validated"),
    ("SEC-03", "Runner scope analysis", "grep step-03.md for Runner AND shared AND scope", "Runner scope matched to job sensitivity"),
    ("SEC-04", "Hardcoded credential detection", "grep step-03.md for hardcoded AND credential AND glpat", "Credential patterns scanned"),
    ("SEC-05", "Container image pinning", "grep step-03.md for image AND digest AND pin AND tag", "Image references checked for digest pinning vs mutable tags"),
    ("SEC-06", "Script injection detection", "grep step-03.md for script injection AND CI_COMMIT AND variable", "User-controlled CI variable injection in script blocks detected"),
    ("SEC-07", "Service container security", "grep step-03.md for service AND image AND alias", "Service container image pinning and alias conflicts checked"),
    ("SEC-08", "Runner tag validation", "grep step-03.md for Runner AND tag AND docker", "Runner tag specificity and matching validated"),
    ("SEC-09", "Credential pattern scanning", "grep step-03.md for token AND credential AND CRITICAL", "Hardcoded tokens and credentials flagged as CRITICAL"),
    ("SEC-10", "File type variable check", "grep step-03.md for variable AND file AND protected AND masked", "File-type CI/CD variables checked for protection attributes"),
    ("DEPLOY-01", "Environment declaration", "grep step-04.md for environment AND protection AND deploy", "Environment declarations validated with protection rules"),
    ("DEPLOY-02", "Auto-stop configuration", "grep step-04.md for auto_stop_in AND resource AND on_stop", "Review environment auto-stop and stop action validated"),
    ("DEPLOY-03", "Resource group serialization", "grep step-04.md for resource_group AND serialization AND parallel", "Production deployment serialization via resource_group"),
    ("DEPLOY-04", "Cache key strategy", "grep step-04.md for cache AND key AND policy AND fallback", "Cache key effectiveness, policy, and fallback validated"),
    ("DEPLOY-05", "Timeout configuration", "grep step-04.md for timeout AND retry AND runner_system_failure", "Job timeout and retry with failure-type targeting"),
    ("DEPLOY-06", "Artifact management", "grep step-04.md for artifact AND expire_in AND paths", "Artifact paths and expiration validated"),
    ("DEPLOY-07", "Interruptible validation", "grep step-04.md for interruptible AND deploy AND cancel", "Interruptible flag checked against job criticality"),
    ("DEPLOY-08", "Allow failure validation", "grep step-04.md for allow_failure AND critical AND pipeline", "Allow failure on critical jobs flagged"),
    ("REG-01", "MR pipeline consistency", "grep step-05.md for merge_request AND branch AND pipeline AND consistency", "MR vs branch pipeline parity validated"),
    ("REG-02", "Compliance pipeline check", "grep step-05.md for compliance AND pipeline AND audit", "Compliance pipeline configuration and audit trail checked"),
    ("REG-03", "Pipeline execution policies", "grep step-05.md for policy AND branch AND pipeline", "Protected branch and pipeline execution policies validated"),
    ("REG-04", "Coverage matrix", "grep step-05.md for coverage AND matrix AND category AND threshold", "Coverage matrix per validation category with threshold"),
    ("REG-05", "Readiness recommendation", "grep step-05.md for READY AND NOT READY AND CONDITIONAL AND RECOMMENDATION", "3 readiness levels defined"),
    ("REG-06", "Remediation priority", "grep step-05.md for remediation AND priority AND critical AND finding", "Remediation list prioritized by severity"),
    ("SPEC-01", "SKILL.md exists with frontmatter", "grep SKILL.md for name: AND type: AND domain:", "Frontmatter has name, type, domain"),
    ("SPEC-02", "Workflow contains 5-step index", "grep workflow.md for Step 1 AND Step 5 AND Step Index", "All 5 steps listed"),
    ("SPEC-03", "Workflow contains data flow", "grep workflow.md for pipeline_inventory AND structure_results AND security_results AND deployment_results", "Data flow variables documented"),
    ("SPEC-04", "Workflow contains category mapping", "grep workflow.md for Categories Covered AND DISC AND SEC AND DEPLOY", "Categories mapped to steps"),
    ("SPEC-05", "Workflow references state location", "grep workflow.md for pipeline_state.json AND tests/_state", "State file path documented"),
    ("SPEC-06", "All 5 step files exist", "file_exists steps/step-01.md through steps/step-05.md", "All step files present"),
    ("SPEC-07", "Gate-contract contains all categories", "grep gate-contract.md for DISC AND STRUCT AND SEC AND DEPLOY AND REG", "All 9 categories in index"),
    ("LES-01", "Lessons index exists", "file_exists lessons/lessons.md", "Index file present"),
    ("LES-02", "Lessons index has Quick Reference", "grep lessons.md for Quick Reference AND validate before merge", "Quick Reference section present"),
    ("LES-03", "Security lessons file exists", "file_exists lessons/gitlab-ci/security.md", "Security topic file present"),
    ("LES-04", "Security covers variables and images", "grep security.md for masked AND protected AND image AND digest", "Key security topics covered"),
    ("LES-05", "Structure lessons file exists", "file_exists lessons/gitlab-ci/structure.md", "Structure topic file present"),
    ("LES-06", "Structure covers includes, rules, needs", "grep structure.md for include AND rules AND needs", "3 key structure topics covered"),
    ("LES-07", "Deployment covers environments, caching, resource groups", "grep deployment.md for environment AND cache AND resource_group", "3 key deployment topics covered"),
    ("CHK-01", "Pre-construction checkpoint exists", "file_exists checkpoints/pre-construction.md", "File exists"),
    ("CHK-02", "Forbidden patterns documented", "grep pre-construction.md for FORBIDDEN AND execute AND mutable tag", "Forbidden patterns listed"),
    ("CHK-03", "Mandatory reads enforced", "grep pre-construction.md for READ AND CI configuration AND lessons", "Mandatory reads before validation"),
    ("CHK-04", "On-failure checkpoint exists", "file_exists checkpoints/on-failure.md", "File exists"),
    ("CHK-05", "HITL protocol in on-failure", "grep on-failure.md for STOP AND REPORT AND WAIT AND HOW SHOULD WE PROCEED", "HITL triage options presented"),
    ("CHK-06", "Error reporting format", "grep on-failure.md for SEVERITY AND FINDING AND REMEDIATION", "Structured error report format"),
    ("CONTR-01", "HITL Protocol defined", "grep gate-contract.md for HITL Protocol AND MANDATORY AND STOP IMMEDIATELY", "HITL section present"),
    ("CONTR-02", "Severity classification defined", "grep gate-contract.md for Severity Classification AND CRITICAL AND HIGH AND MEDIUM AND LOW", "4-level severity defined"),
    ("CONTR-03", "Learning Cycle described", "grep gate-contract.md for Learning Cycle AND VALIDATE AND TEACH AND LEARN", "Learning cycle documented"),
    ("CONTR-04", "State Persistence specified", "grep gate-contract.md for State Persistence AND pipeline_state.json", "State location documented"),
    ("CONTR-05", "Teaching Pattern defined", "grep gate-contract.md for Teaching Pattern AND signal AND outcome AND insight", "Teaching pattern documented"),
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
Gate contract: `.claude/skills/gitlab-ci-testing/gate-contract.md`
"""
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {OUTPUT_DIR}")
