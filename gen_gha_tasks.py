#!/usr/bin/env python3
"""Generate 67 task files for github-actions-spec validation."""
import os

OUTPUT_DIR = "D:/my_ai_projects/project_test_repos/test-gha-validation/tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

gates = [
    ("DISC-01","Workflow file scanning","grep step-01.md for .github/workflows AND *.yml","Scan path and file patterns documented"),
    ("DISC-02","YAML parsing instructions","grep step-01.md for YAML AND parse AND valid","YAML parse with error handling documented"),
    ("DISC-03","Trigger cataloging","grep step-01.md for trigger AND push AND pull_request AND schedule","All major trigger types listed"),
    ("DISC-04","Job inventory extraction","grep step-01.md for job AND runs-on AND inventory","Jobs extracted with runner info"),
    ("DISC-05","Action usage cataloging","grep step-01.md for uses: AND action AND catalog","Third-party action references cataloged"),
    ("DISC-06","Dependency graph construction","grep step-01.md for needs AND dependency_graph AND DAG","Job dependency graph built"),
    ("DISC-07","Reusable workflow detection","grep step-01.md for reusable workflow AND workflow_call","Reusable workflow callers identified"),
    ("DISC-08","Composite action detection","grep step-01.md for composite action AND action.yml","Composite actions detected"),
    ("STRUCT-01","YAML syntax validation","grep step-02.md for YAML syntax AND duplicate keys AND well-formed","YAML well-formedness validated"),
    ("STRUCT-02","Top-level key validation","grep step-02.md for name AND on AND jobs AND top-level","Required top-level keys validated"),
    ("STRUCT-03","Trigger configuration validation","grep step-02.md for trigger AND branches AND tags AND paths AND filter","Trigger filters validated"),
    ("STRUCT-04","Needs DAG validation","grep step-02.md for needs AND cycle AND circular AND DAG","Circular dependency detection"),
    ("STRUCT-05","Matrix strategy validation","grep step-02.md for matrix AND include AND exclude AND fail-fast","Matrix combinations validated"),
    ("STRUCT-06","Step structure validation","grep step-02.md for uses AND run AND mutually exclusive AND step","Steps uses XOR run validated"),
    ("STRUCT-07","Runner label validation","grep step-02.md for runs-on AND ubuntu-latest AND runner label","Runner labels validated"),
    ("STRUCT-08","Expression syntax validation","grep step-02.md for expression AND context","Expression syntax validated"),
    ("STRUCT-09","Reusable workflow input validation","grep step-02.md for workflow_call AND inputs AND callee","Workflow call inputs match callee"),
    ("STRUCT-10","Concurrency configuration","grep step-02.md for concurrency AND cancel-in-progress AND group","Concurrency settings validated"),
    ("SEC-01","Permissions audit","grep step-03.md for permissions AND least privilege AND GITHUB_TOKEN","Least privilege permissions checked"),
    ("SEC-02","Script injection detection","grep step-03.md for script injection AND run:","Script injection in run blocks detected"),
    ("SEC-03","Pull request target risks","grep step-03.md for pull_request_target AND checkout AND CRITICAL","pull_request_target risks flagged"),
    ("SEC-04","Action pinning by SHA","grep step-03.md for pin AND SHA AND tag AND supply chain","SHA pinning vs mutable tags checked"),
    ("SEC-05","Hardcoded credentials","grep step-03.md for hardcoded AND credential AND token","Embedded credentials scanned"),
    ("SEC-06","Secret usage in conditions","grep step-03.md for secrets AND if: AND log","Secrets in conditions flagged"),
    ("SEC-07","OIDC configuration","grep step-03.md for OIDC AND id-token AND cloud provider","OIDC setup validated"),
    ("SEC-08","Environment variable safety","grep step-03.md for environment variable AND env: AND interpolation","Env vars over direct interpolation"),
    ("SEC-09","Persist credentials check","grep step-03.md for persist-credentials AND false AND checkout","Checkout persist-credentials checked"),
    ("SEC-10","Self-hosted runner hardening","grep step-03.md for self-hosted AND hardening AND ephemeral","Self-hosted runner security documented"),
    ("DEPLOY-01","Environment configuration","grep step-04.md for environment: AND protection AND reviewers","Environment protection rules validated"),
    ("DEPLOY-02","Approval gate validation","grep step-04.md for approval AND wait timer AND required reviewers","Approval gates checked"),
    ("DEPLOY-03","Rollback strategy","grep step-04.md for rollback AND workflow_dispatch AND previous","Rollback mechanism documented"),
    ("DEPLOY-04","Artifact management","grep step-04.md for artifact AND upload AND download AND retention","Artifact patterns validated"),
    ("DEPLOY-05","Caching strategy","grep step-04.md for caching AND cache AND restore-keys AND hashFiles","Cache keys and paths validated"),
    ("DEPLOY-06","Concurrency controls","grep step-04.md for concurrency AND deployment AND parallel","Deployment concurrency controls"),
    ("DEPLOY-07","Conditional deployment","grep step-04.md for if: AND github.ref AND deploy AND conditional","Deployment guarded by conditions"),
    ("DEPLOY-08","Timeout and resource limits","grep step-04.md for timeout-minutes AND continue-on-error AND resource","Timeouts and limits configured"),
    ("REG-01","Workflow change tracking","grep step-05.md for baseline AND diff AND change tracking","Workflow diffs against baseline"),
    ("REG-02","Required status checks","grep step-05.md for required status checks AND branch protection","Status checks aligned with jobs"),
    ("REG-03","Branch protection compliance","grep step-05.md for branch protection AND force push AND review","Branch protection rules validated"),
    ("REG-04","Coverage matrix","grep step-05.md for coverage AND matrix AND category AND threshold","Coverage matrix with threshold"),
    ("REG-05","Readiness recommendation","grep step-05.md for READY AND NOT READY AND CONDITIONAL AND RECOMMENDATION","3 readiness levels defined"),
    ("REG-06","Remediation priority","grep step-05.md for remediation AND priority AND critical AND finding","Remediation prioritized by severity"),
    ("SPEC-01","SKILL.md exists with frontmatter","grep SKILL.md for name: AND type: AND domain:","Frontmatter has name, type, domain"),
    ("SPEC-02","Workflow contains 5-step index","grep workflow.md for Step 1 AND Step 5 AND Step Index","All 5 steps listed"),
    ("SPEC-03","Workflow contains data flow","grep workflow.md for workflow_inventory AND structure_results AND security_results AND deployment_results","Data flow variables documented"),
    ("SPEC-04","Workflow contains category mapping","grep workflow.md for Categories Covered AND DISC AND SEC AND DEPLOY","Categories mapped to steps"),
    ("SPEC-05","Workflow references state location","grep workflow.md for workflow_state.json AND tests/_state","State file path documented"),
    ("SPEC-06","All 5 step files exist","file_exists steps/step-01.md through steps/step-05.md","All step files present"),
    ("SPEC-07","Gate-contract contains all categories","grep gate-contract.md for DISC AND STRUCT AND SEC AND DEPLOY AND REG","All 9 categories in index"),
    ("LES-01","Lessons index exists","file_exists lessons/lessons.md","Index file present"),
    ("LES-02","Lessons index has Quick Reference","grep lessons.md for Quick Reference AND validate before merge","Quick Reference section present"),
    ("LES-03","Security lessons file exists","file_exists lessons/github-actions/security.md","Security topic file present"),
    ("LES-04","Security covers injection and permissions","grep security.md for script injection AND permissions AND pin actions","3 key security topics covered"),
    ("LES-05","Structure lessons file exists","file_exists lessons/github-actions/structure.md","Structure topic file present"),
    ("LES-06","Structure covers needs, matrix, triggers","grep structure.md for needs AND matrix AND triggers","3 key structure topics covered"),
    ("LES-07","Deployment covers environments, rollback, caching","grep deployment.md for environments AND rollback AND caching","3 key deployment topics covered"),
    ("CHK-01","Pre-construction checkpoint exists","file_exists checkpoints/pre-construction.md","File exists"),
    ("CHK-02","Forbidden patterns documented","grep pre-construction.md for FORBIDDEN AND execute workflows AND mutable tag","Forbidden patterns listed"),
    ("CHK-03","Mandatory reads enforced","grep pre-construction.md for READ AND workflow files AND lessons","Mandatory reads before validation"),
    ("CHK-04","On-failure checkpoint exists","file_exists checkpoints/on-failure.md","File exists"),
    ("CHK-05","HITL protocol in on-failure","grep on-failure.md for STOP AND REPORT AND WAIT AND HOW SHOULD WE PROCEED","HITL triage options presented"),
    ("CHK-06","Error reporting format","grep on-failure.md for WORKFLOW AND SEVERITY AND FINDING AND REMEDIATION","Structured error report format"),
    ("CONTR-01","HITL Protocol defined","grep gate-contract.md for HITL Protocol AND MANDATORY AND STOP IMMEDIATELY","HITL section present"),
    ("CONTR-02","Severity classification defined","grep gate-contract.md for Severity Classification AND CRITICAL AND HIGH AND MEDIUM AND LOW","4-level severity defined"),
    ("CONTR-03","Learning Cycle described","grep gate-contract.md for Learning Cycle AND VALIDATE AND TEACH AND LEARN","Learning cycle documented"),
    ("CONTR-04","State Persistence specified","grep gate-contract.md for State Persistence AND workflow_state.json","State location documented"),
    ("CONTR-05","Teaching Pattern defined","grep gate-contract.md for Teaching Pattern AND signal AND outcome AND insight","Teaching pattern documented"),
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
Gate contract: `.claude/skills/github-actions-testing/gate-contract.md`
"""
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {OUTPUT_DIR}")
