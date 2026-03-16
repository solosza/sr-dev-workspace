#!/usr/bin/env python3
"""Generate 67 task files for azure-devops-spec validation."""
import os

OUTPUT_DIR = "D:/my_ai_projects/project_test_repos/test-azdo-validation/tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

gates = [
    ("DISC-01", "Pipeline file scanning", "grep step-01.md for azure-pipelines.yml AND *.yml", "Scan path and file patterns documented"),
    ("DISC-02", "YAML parsing instructions", "grep step-01.md for YAML AND parse AND valid", "YAML parse with error handling documented"),
    ("DISC-03", "Trigger cataloging", "grep step-01.md for trigger AND pr AND schedules AND resources", "All major trigger types listed"),
    ("DISC-04", "Stage/job/step hierarchy", "grep step-01.md for Stage AND Job AND Step AND hierarchy", "Jobs extracted with hierarchy info"),
    ("DISC-05", "Template reference resolution", "grep step-01.md for extends AND template AND template_graph", "Template references resolved"),
    ("DISC-06", "Variable group inventory", "grep step-01.md for Variable group AND Key Vault AND service connection", "Variable groups and service connections inventoried"),
    ("DISC-07", "Resource cataloging", "grep step-01.md for resources.repositories AND resources.pipelines AND resources.containers", "External resource dependencies cataloged"),
    ("DISC-08", "Parameter extraction", "grep step-01.md for parameters AND type AND default AND values", "Pipeline parameters extracted with types"),
    ("STRUCT-01", "YAML schema validation", "grep step-02.md for YAML Schema AND duplicate keys AND top-level", "YAML schema compliance checked"),
    ("STRUCT-02", "Top-level key validation", "grep step-02.md for trigger AND stages AND jobs AND steps AND Top-level", "Required top-level keys validated"),
    ("STRUCT-03", "Trigger configuration validation", "grep step-02.md for trigger AND branches AND paths AND filter", "Trigger filters validated"),
    ("STRUCT-04", "DependsOn DAG validation", "grep step-02.md for dependsOn AND cycle AND circular AND DAG", "Circular dependency detection"),
    ("STRUCT-05", "Template parameter contract", "grep step-02.md for parameter AND type AND required AND contract", "Template parameter types validated"),
    ("STRUCT-06", "Step structure validation", "grep step-02.md for task: AND script: AND mutually exclusive AND step", "Steps task XOR script validated"),
    ("STRUCT-07", "Pool and vmImage validation", "grep step-02.md for vmImage AND ubuntu-latest AND pool", "Runner labels validated"),
    ("STRUCT-08", "Condition expression validation", "grep step-02.md for condition AND succeeded() AND expression AND syntax", "Condition syntax validated"),
    ("STRUCT-09", "Schedule cron validation", "grep step-02.md for schedules AND Cron AND always", "Cron expressions validated"),
    ("STRUCT-10", "Concurrency and lock behavior", "grep step-02.md for lockBehavior AND pipeline", "Lock behavior validated"),
    ("SEC-01", "Service connection scope audit", "grep step-03.md for service connection AND scope AND subscription AND least privilege", "Service connections checked for least privilege"),
    ("SEC-02", "Variable group secret handling", "grep step-03.md for variable group AND Key Vault AND isSecret AND script", "Variable group secret expansion detected"),
    ("SEC-03", "Hardcoded credential scanning", "grep step-03.md for hardcoded AND credential AND API key", "Embedded credentials scanned"),
    ("SEC-04", "Agent pool security", "grep step-03.md for self-hosted AND ephemeral AND workspace AND clean", "Self-hosted agent hardening documented"),
    ("SEC-05", "Checkout credential persistence", "grep step-03.md for persistCredentials AND false AND checkout", "Checkout persist-credentials checked"),
    ("SEC-06", "Task version pinning", "grep step-03.md for task AND pin AND version AND deprecated", "Task versions verified"),
    ("SEC-07", "Extends template security", "grep step-03.md for extends AND required AND template AND security", "Template compliance checked"),
    ("SEC-08", "Secret in script expansion", "grep step-03.md for $(secretVariable) AND script AND leak AND log", "Secret variable expansion flagged"),
    ("SEC-09", "Service connection environment guard", "grep step-03.md for service connection AND environment AND approval", "Service connections within environment-protected stages"),
    ("SEC-10", "Custom task publisher verification", "grep step-03.md for marketplace AND publisher AND verified", "Unverified publisher tasks flagged"),
    ("DEPLOY-01", "Environment protection validation", "grep step-04.md for environment AND approval AND protection AND reviewers", "Environment protection rules validated"),
    ("DEPLOY-02", "Deployment strategy validation", "grep step-04.md for runOnce AND rolling AND canary AND strategy", "Deployment strategy validated"),
    ("DEPLOY-03", "Rollback mechanism check", "grep step-04.md for rollback AND on.failure AND failure", "Rollback mechanism documented"),
    ("DEPLOY-04", "Artifact management validation", "grep step-04.md for artifact AND publish AND download AND retention", "Artifact patterns validated"),
    ("DEPLOY-05", "Caching configuration check", "grep step-04.md for Cache AND restoreKeys AND lock file AND path", "Cache keys and paths validated"),
    ("DEPLOY-06", "Concurrency and lock controls", "grep step-04.md for lockBehavior AND exclusive lock AND parallel", "Deployment concurrency controls"),
    ("DEPLOY-07", "Conditional deployment guards", "grep step-04.md for condition AND Build.SourceBranch AND deploy AND conditional", "Deployment guarded by conditions"),
    ("DEPLOY-08", "Timeout and resource limits", "grep step-04.md for timeoutInMinutes AND continueOnError AND retryCountOnTaskFailure", "Timeouts and limits configured"),
    ("REG-01", "Pipeline change tracking", "grep step-05.md for baseline AND diff AND change tracking", "Pipeline diffs against baseline"),
    ("REG-02", "Branch policy alignment", "grep step-05.md for branch AND protection AND status check AND policy", "Branch policies validated"),
    ("REG-03", "Decorator compliance", "grep step-05.md for decorator AND organizational AND policy AND compliance", "Decorator compliance verified"),
    ("REG-04", "Coverage matrix", "grep step-05.md for coverage AND matrix AND category AND threshold", "Coverage matrix with threshold"),
    ("REG-05", "Readiness recommendation", "grep step-05.md for READY AND NOT READY AND CONDITIONAL AND RECOMMENDATION", "3 readiness levels defined"),
    ("REG-06", "Remediation priority", "grep step-05.md for remediation AND priority AND critical AND finding", "Remediation prioritized by severity"),
    ("SPEC-01", "SKILL.md exists with frontmatter", "grep SKILL.md for name: AND type: AND domain:", "Frontmatter has name, type, domain"),
    ("SPEC-02", "Workflow contains 5-step index", "grep workflow.md for Step 1 AND Step 5 AND Step Index", "All 5 steps listed"),
    ("SPEC-03", "Workflow contains data flow", "grep workflow.md for pipeline_inventory AND structure_results AND security_results AND deployment_results", "Data flow variables documented"),
    ("SPEC-04", "Workflow contains category mapping", "grep workflow.md for Categories Covered AND DISC AND SEC AND DEPLOY", "Categories mapped to steps"),
    ("SPEC-05", "Workflow references state location", "grep workflow.md for workflow_state.json AND tests/_state", "State file path documented"),
    ("SPEC-06", "All 5 step files exist", "file_exists steps/step-01.md through steps/step-05.md", "All step files present"),
    ("SPEC-07", "Gate-contract contains all categories", "grep gate-contract.md for DISC AND STRUCT AND SEC AND DEPLOY AND REG", "All 9 categories in index"),
    ("LES-01", "Lessons index exists", "file_exists lessons/lessons.md", "Index file present"),
    ("LES-02", "Lessons index has Quick Reference", "grep lessons.md for Quick Reference AND validate before merge", "Quick Reference section present"),
    ("LES-03", "Security lessons file exists", "file_exists lessons/azure-devops/security.md", "Security topic file present"),
    ("LES-04", "Security covers service connections and credentials", "grep security.md for service connection AND variable group AND credential", "Key security topics covered"),
    ("LES-05", "Structure lessons file exists", "file_exists lessons/azure-devops/structure.md", "Structure topic file present"),
    ("LES-06", "Structure covers dependsOn, templates, conditions", "grep structure.md for dependsOn AND template AND condition", "3 key structure topics covered"),
    ("LES-07", "Deployment covers environments, rollback, strategies", "grep deployment.md for environment AND rollback AND strategy", "3 key deployment topics covered"),
    ("CHK-01", "Pre-construction checkpoint exists", "file_exists checkpoints/pre-construction.md", "File exists"),
    ("CHK-02", "Forbidden patterns documented", "grep pre-construction.md for FORBIDDEN AND execute pipeline AND hardcoded credential", "Forbidden patterns listed"),
    ("CHK-03", "Mandatory reads enforced", "grep pre-construction.md for READ AND pipeline files AND lessons", "Mandatory reads before validation"),
    ("CHK-04", "On-failure checkpoint exists", "file_exists checkpoints/on-failure.md", "File exists"),
    ("CHK-05", "HITL protocol in on-failure", "grep on-failure.md for STOP AND REPORT AND WAIT AND HOW SHOULD WE PROCEED", "HITL triage options presented"),
    ("CHK-06", "Error reporting format", "grep on-failure.md for PIPELINE AND SEVERITY AND FINDING AND REMEDIATION", "Structured error report format"),
    ("CONTR-01", "HITL Protocol defined", "grep gate-contract.md for HITL Protocol AND MANDATORY AND STOP IMMEDIATELY", "HITL section present"),
    ("CONTR-02", "Severity classification defined", "grep gate-contract.md for Severity Classification AND CRITICAL AND HIGH AND MEDIUM AND LOW", "4-level severity defined"),
    ("CONTR-03", "Learning Cycle described", "grep gate-contract.md for Learning Cycle AND VALIDATE AND TEACH AND LEARN", "Learning cycle documented"),
    ("CONTR-04", "State Persistence specified", "grep gate-contract.md for State Persistence AND workflow_state.json", "State location documented"),
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
Gate contract: `.claude/skills/azure-devops-testing/gate-contract.md`
"""
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {OUTPUT_DIR}")
