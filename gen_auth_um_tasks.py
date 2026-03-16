#!/usr/bin/env python3
"""Generate 67 task files for auth-um-spec validation."""

import os

OUTPUT_DIR = "D:/my_ai_projects/project_test_repos/test-auth-um-validation/tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

gates = [
    # AUTH gates (Step 1)
    ("AUTH-01", "Service type configuration", "grep step-01.md for service_types AND inpatient_medical AND outpatient_surgery", "Service types list with medical/surgical categories documented"),
    ("AUTH-02", "Clinical criteria mapping", "grep step-01.md for criteria_map AND interqual AND mcg", "Criteria mapping to InterQual and MCG sources documented"),
    ("AUTH-03", "Provider network rules", "grep step-01.md for provider_network AND gold_card_eligible", "Provider network config with gold carding rules documented"),
    ("AUTH-04", "Auto-authorization rules", "grep step-01.md for auto_approve AND always_pend AND always_deny", "Auth rule categories (auto-approve, pend, deny) documented"),
    ("AUTH-05", "TAT requirements configuration", "grep step-01.md for tat_requirements AND urgent AND standard AND concurrent", "Turnaround time requirements by urgency level documented"),
    ("AUTH-06", "Regulatory TAT hours", "grep step-01.md for regulatory_max_hours AND payer_sla_hours", "Both regulatory and payer SLA hour thresholds defined"),
    ("AUTH-07", "Advanced imaging service types", "grep step-01.md for advanced_imaging AND specialty_drugs AND dme", "Specialty service types requiring auth documented"),
    ("AUTH-08", "State override handling", "grep step-01.md for state_override_hours AND retrospective", "State-specific TAT overrides and retrospective review documented"),

    # REQ gates (Step 2)
    ("REQ-01", "X12 278 submission testing", "grep step-02.md for x12_278 AND BHT01 AND BHT02", "X12 278 transaction structure with BHT segment documented"),
    ("REQ-02", "X12 278 loop structure", "grep step-02.md for Loop 2000A AND Loop 2000E AND UM01", "Auth request loop hierarchy and UM segment documented"),
    ("REQ-03", "FHIR PAS API submission", "grep step-02.md for fhir_api AND preauthorization AND ClaimResponse", "FHIR PAS submission with Claim.use and response documented"),
    ("REQ-04", "Provider portal channel", "grep step-02.md for portal AND channels_tested", "Portal submission channel included in test coverage"),
    ("REQ-05", "HCR action codes", "grep step-02.md for HCR AND A1 AND A2 AND A6", "Health Care Services Review action codes documented"),
    ("REQ-06", "Clinical documentation requirements", "grep step-02.md for clinical_doc AND PWK", "Clinical documentation attachment via PWK segment documented"),
    ("REQ-07", "Request validation segment", "grep step-02.md for AAA AND rejection_reasons", "AAA segment for rejection handling documented"),
    ("REQ-08", "FHIR review action values", "grep step-02.md for reviewAction AND approved AND denied AND pended", "FHIR reviewAction extension values documented"),
    ("REQ-09", "Test data structure", "grep step-02.md for test_members.json AND test_providers.json", "Test data file references documented"),

    # CLIN gates (Step 3)
    ("CLIN-01", "Auto-auth outcome tracking", "grep step-03.md for auto_auth_results AND correctly_auto_approved AND false_auto_approvals", "Auto-auth validation metrics documented"),
    ("CLIN-02", "InterQual criteria testing", "grep step-03.md for interqual_tested AND interqual_correct", "InterQual criteria application verification documented"),
    ("CLIN-03", "MCG criteria testing", "grep step-03.md for mcg_tested AND mcg_correct AND mcg_discrepancies", "MCG criteria application verification documented"),
    ("CLIN-04", "Peer-to-peer review", "grep step-03.md for p2p_requested AND p2p_completed AND overturned", "P2P review metrics with overturn tracking documented"),
    ("CLIN-05", "Urgent TAT compliance", "grep step-03.md for urgent_tested AND urgent_compliant AND 72", "Urgent/expedited 72-hour TAT testing documented"),
    ("CLIN-06", "Standard TAT compliance", "grep step-03.md for standard_tested AND standard_compliant AND standard_violations", "Standard TAT testing with violation tracking documented"),
    ("CLIN-07", "Gold card rules", "grep step-03.md for gold_card AND gold_card_threshold", "Gold carding provider exemption rules documented"),
    ("CLIN-08", "Criteria consistency validation", "grep step-03.md for criteria_consistency AND consistency_sets_tested AND all_consistent", "Same-profile consistency testing documented"),
    ("CLIN-09", "Emergency services never-deny", "grep step-03.md for emergency_services AND stabilization_services", "Emergency/stabilization never-deny rules documented"),

    # NOTIF gates (Step 4)
    ("NOTIF-01", "Determination letter validation", "grep step-04.md for approval_letters_accurate AND denial_letters_accurate", "Letter accuracy metrics for approvals and denials documented"),
    ("NOTIF-02", "Denial letter required elements", "grep step-04.md for specific_reason_for_denial AND clinical_criteria_reference AND reviewer_name_and_credentials", "Required denial letter elements documented"),
    ("NOTIF-03", "Appeal rights completeness", "grep step-04.md for appeal_rights_complete AND internal_appeal_right AND expedited_appeal_right", "Appeal rights elements including expedited documented"),
    ("NOTIF-04", "Appeal timeframes by LOB", "grep step-04.md for Medicare Advantage AND Medicaid AND ERISA", "Appeal filing timeframes by line of business documented"),
    ("NOTIF-05", "External review process", "grep step-04.md for IRO AND external_review", "Independent Review Organization external appeal documented"),
    ("NOTIF-06", "Language accessibility", "grep step-04.md for ACA Section 1557 AND threshold languages", "ACA Section 1557 language access requirements documented"),
    ("NOTIF-07", "Multi-channel delivery", "grep step-04.md for x12_278_response AND fhir_claimresponse AND provider_portal_notification", "Electronic notification channels documented"),
    ("NOTIF-08", "Appeal conflict of interest", "grep step-04.md for reviewer_did_not_make_original_decision", "Appeal reviewer conflict of interest check documented"),

    # CMS gates (Step 5)
    ("CMS-01", "FHIR PAS $submit operation", "grep step-05.md for $submit AND POST AND Claim", "PAS $submit endpoint and operation documented"),
    ("CMS-02", "FHIR PAS $inquire operation", "grep step-05.md for $inquire AND Bundle", "PAS $inquire endpoint and format documented"),
    ("CMS-03", "PARDD requirements discovery", "grep step-05.md for pa-requirements AND Coverage AND service-code", "PARDD endpoint with parameters documented"),
    ("CMS-04", "Patient Access API", "grep step-05.md for Patient Access API AND patient/ClaimResponse.read", "Patient Access API with SMART scope documented"),
    ("CMS-05", "Provider Access API", "grep step-05.md for Provider Access API AND attribution", "Provider Access API with attribution enforcement documented"),
    ("CMS-06", "OAuth2 security testing", "grep step-05.md for OAuth2 AND scope enforcement AND SMART on FHIR", "OAuth2/SMART security testing documented"),
    ("CMS-07", "Annual metrics reporting", "grep step-05.md for annual metrics AND percentage approved AND percentage denied", "Public metrics reporting requirements documented"),
    ("CMS-08", "42 CFR Part 2 sensitive data", "grep step-05.md for 42 CFR Part 2 AND sensitive AND substance abuse", "Substance abuse data protection documented"),

    # SPEC gates
    ("SPEC-01", "SKILL.md exists with frontmatter", "grep SKILL.md for name: AND type: AND domain:", "Frontmatter contains name, type, domain fields"),
    ("SPEC-02", "Workflow contains 5-step index", "grep workflow.md for step_count: 5 AND service_types AND pas_api_conformance", "Step count and first/last step outputs documented"),
    ("SPEC-03", "Workflow contains data flow", "grep workflow.md for x12_278_results AND clinical_review_outcomes AND determination_letters", "Data flow shows output variables from each step"),
    ("SPEC-04", "Workflow references state location", "grep workflow.md for workflow_state.json AND state_file", "State file path documented"),
    ("SPEC-05", "All 5 step files exist", "file_exists steps/step-01.md through steps/step-05.md", "All step reference files present"),
    ("SPEC-06", "Gate-contract contains all categories", "grep gate-contract.md for AUTH AND REQ AND CLIN AND NOTIF AND CMS", "All 9 gate categories present in index"),

    # LES gates
    ("LES-01", "Lessons index exists", "file_exists lessons/lessons.md", "Index file with topic table"),
    ("LES-02", "Auth configuration lessons", "grep lessons file for auto-auth AND criteria mapping", "Auto-auth and criteria mapping anti-patterns documented"),
    ("LES-03", "Clinical review lessons", "grep lessons file for TAT violation AND InterQual", "TAT compliance and criteria application lessons documented"),
    ("LES-04", "Notification lessons", "grep lessons file for denial letter AND appeal rights", "Denial content and appeal rights lessons documented"),
    ("LES-05", "Compliance lessons", "grep lessons file for CMS-0057-F AND FHIR", "CMS compliance and FHIR API lessons documented"),
    ("LES-06", "Quick reference top rules", "grep lessons.md for HITL is mandatory AND Quick Reference", "Top rules quick-reference in lessons index"),

    # CHK gates
    ("CHK-01", "Pre-construction checkpoint exists", "file_exists checkpoints/pre-construction.md", "File exists with trigger: before-test-build"),
    ("CHK-02", "Configuration verification", "grep pre-construction.md for service_types AND criteria_map AND auth_rules", "Required config fields verified before testing"),
    ("CHK-03", "Forbidden patterns defined", "grep pre-construction.md for hardcoded clinical criteria AND hardcoded waits", "Forbidden coding patterns documented"),
    ("CHK-04", "On-failure checkpoint exists", "file_exists checkpoints/on-failure.md", "File exists with trigger: test-failure"),
    ("CHK-05", "HITL triage in on-failure", "grep on-failure.md for FAILURE DETECTED AND AI Proposes Fix AND Stop Workflow", "HITL triage options presented on failure"),
    ("CHK-06", "Severity classification", "grep on-failure.md for Critical AND High AND Medium AND Low", "4-tier severity classification documented"),

    # CONTR gates
    ("CONTR-01", "HITL protocol defined", "grep gate-contract.md for HITL Protocol AND MANDATORY AND STOP IMMEDIATELY", "HITL section present with mandatory stop-and-ask behavior"),
    ("CONTR-02", "AuthInterface Methods First", "grep gate-contract.md for AuthInterface Methods First AND MANDATORY AND Forbidden Patterns", "AuthInterface-first mandate with forbidden patterns documented"),
    ("CONTR-03", "TAT compliance gate", "grep gate-contract.md for Turnaround Time AND TAT AND regulatory_max", "TAT compliance validation gate documented"),
    ("CONTR-04", "Denial completeness gate", "grep gate-contract.md for Denial Reason Completeness AND INCOMPLETE DENIAL", "Denial element completeness validation documented"),
    ("CONTR-05", "Criteria consistency gate", "grep gate-contract.md for Criteria Consistency AND CRITERIA INCONSISTENCY", "Same-profile consistency gate documented"),
    ("CONTR-06", "Teaching pattern defined", "grep gate-contract.md for Teaching Pattern AND signal AND outcome AND insight AND regulatory_impact", "Lesson template with regulatory_impact field"),
    ("CONTR-07", "State persistence specified", "grep gate-contract.md for State Persistence AND workflow_state.json AND compliance_flags", "State location with compliance flags documented"),
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
Gate contract: `.claude/skills/auth-um-testing/gate-contract.md`
"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {OUTPUT_DIR}")
