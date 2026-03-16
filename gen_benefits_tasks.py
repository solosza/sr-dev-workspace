#!/usr/bin/env python3
"""Generate 63 task files for benefits-config-spec validation."""

import os

OUTPUT_DIR = "D:/my_ai_projects/project_test_repos/test-benefits-validation/tasks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

gates = [
    # PLAN gates (Step 1)
    ("PLAN-01", "Plan hierarchy defined", "grep step-01.md for plan_id AND benefit_package AND network_config", "Plan config output contains plan ID, benefit package, and network"),
    ("PLAN-02", "SBC loading logic", "grep step-01.md for SBC AND source of truth", "SBC document loaded and referenced as validation source"),
    ("PLAN-03", "Core admin platform references", "grep step-01.md for Facets AND QNXT AND HealthEdge", "Major platform options documented"),
    ("PLAN-04", "Metal tier handling", "grep step-01.md for metal_tier AND Bronze AND Gold", "ACA metal tiers referenced in plan setup"),
    ("PLAN-05", "Network configuration", "grep step-01.md for network AND in-network AND out-of-network", "Network tier types documented"),
    ("PLAN-06", "Rider handling", "grep step-01.md for rider AND fertility", "Optional rider add-ons documented"),
    ("PLAN-07", "Plan year definition", "grep step-01.md for plan_year AND start AND end", "Plan year dates captured for accumulator boundaries"),

    # COST gates (Step 2)
    ("COST-01", "Copay validation rules", "grep step-02.md for copay AND PCP AND specialist AND ER", "Copay amounts validated for major service categories"),
    ("COST-02", "Coinsurance rules", "grep step-02.md for coinsurance AND in_network AND out_of_network", "Coinsurance percentages by network tier documented"),
    ("COST-03", "Deductible application logic", "grep step-02.md for deductible AND not met AND fully met", "Deductible states (not met, partially met, fully met) tested"),
    ("COST-04", "Preventive care $0 rule", "grep step-02.md for preventive AND $0", "Preventive care always $0 per ACA"),
    ("COST-05", "ER copay waiver on admission", "grep step-02.md for ER AND admission AND waiver", "ER copay waived when admitted documented"),
    ("COST-06", "Place of service rules", "grep step-02.md for place of service OR Place of Service", "Place of service impacts on cost-sharing documented"),
    ("COST-07", "Pharmacy tier cost-sharing", "grep step-02.md for pharmacy AND tier AND generic AND brand", "Pharmacy tiers (generic, preferred brand, non-preferred, specialty)"),
    ("COST-08", "Out-of-network allowed amount", "grep step-02.md for out-of-network AND allowed amount", "OON allowed amount calculation documented"),
    ("COST-09", "Service category test matrix", "grep step-02.md for Service Category AND deductible AND scenario", "Service types x deductible states test matrix defined"),

    # ACCUM gates (Step 3)
    ("ACCUM-01", "Individual deductible tracking", "grep step-03.md for individual deductible AND accumulated AND remaining", "Individual deductible accumulator with limit, accumulated, remaining"),
    ("ACCUM-02", "Family embedded vs aggregate", "grep step-03.md for embedded AND aggregate AND family", "Both family deductible types (embedded cap, aggregate) documented"),
    ("ACCUM-03", "OOP max tracking", "grep step-03.md for OOP AND max AND individual AND family", "Individual and family OOP max accumulators tracked"),
    ("ACCUM-04", "Dollar tolerance rule", "grep step-03.md for $0.01 OR tolerance", "Dollar tolerance for monetary accumulator comparisons"),
    ("ACCUM-05", "Plan year rollover", "grep step-03.md for rollover AND plan year", "Accumulator reset on plan year boundary documented"),
    ("ACCUM-06", "Claim reversal handling", "grep step-03.md for reversal AND decrement", "Claim reversals must decrement accumulators"),
    ("ACCUM-07", "Mid-year plan change", "grep step-03.md for mid-year AND transfer", "Accumulator transfer on mid-year plan changes"),
    ("ACCUM-08", "Pre/post claim state capture", "grep step-03.md for pre-claim AND post-claim", "Accumulator state captured before AND after every claim"),

    # COB gates (Step 4)
    ("COB-01", "Payer order determination", "grep step-04.md for payer order AND primary AND secondary", "Standard COB order determination rules documented"),
    ("COB-02", "Birthday rule", "grep step-04.md for birthday rule AND month AND day", "Birthday rule uses month/day only (not year)"),
    ("COB-03", "Medicare primary/secondary", "grep step-04.md for Medicare AND employer size", "Medicare payer order based on employer size (20+ employees)"),
    ("COB-04", "COBRA scenarios", "grep step-04.md for COBRA AND secondary", "COBRA becomes secondary with new coverage"),
    ("COB-05", "COB methods", "grep step-04.md for standard COB AND non-duplication", "Standard COB, maintenance of benefits, non-duplication methods"),
    ("COB-06", "ESRD transition", "grep step-04.md for ESRD AND 30-month", "ESRD 30-month coordination period documented"),
    ("COB-07", "Court order override", "grep step-04.md for court order", "Court order overrides standard COB rules"),

    # COMP gates (Step 5)
    ("COMP-01", "ACA essential health benefits", "grep step-05.md for Essential Health Benefits AND EHB", "10 EHB categories verified"),
    ("COMP-02", "MHPAEA parity", "grep step-05.md for MHPAEA AND parity AND QTL", "Mental health parity quantitative treatment limits tested"),
    ("COMP-03", "OOP max ACA limit", "grep step-05.md for ACA AND OOP AND limit", "OOP max within ACA annual limit verified"),
    ("COMP-04", "State mandate rules", "grep step-05.md for state mandate AND fully-insured", "State mandates apply to fully-insured only (not self-funded)"),
    ("COMP-05", "Actuarial value metal tier", "grep step-05.md for actuarial value AND metal tier", "AV within allowed range for metal tier"),
    ("COMP-06", "Regression suite", "grep step-05.md for regression AND scenario", "Core regression scenarios defined (20+ scenarios)"),
    ("COMP-07", "Preventive care USPSTF", "grep step-05.md for preventive AND USPSTF OR A/B", "USPSTF A/B recommendations covered at $0"),

    # SPEC gates
    ("SPEC-01", "SKILL.md exists with frontmatter", "grep SKILL.md for name: AND type: AND domain:", "Frontmatter contains name, type, domain fields"),
    ("SPEC-02", "Workflow contains 5-step index", "grep workflow.md for Step 1 AND Step 5 AND Step Index", "All 5 steps listed with purpose, input, output, reference"),
    ("SPEC-03", "Workflow contains data flow", "grep workflow.md for plan_id AND cost_sharing_rules AND accumulator_state AND cob_rules", "Data flow shows output variables from each step"),
    ("SPEC-04", "Workflow references state location", "grep workflow.md for workflow_state.json AND tests/_state", "State file path and format documented"),
    ("SPEC-05", "All 5 step files exist", "file_exists steps/step-01.md through steps/step-05.md", "All step reference files present"),
    ("SPEC-06", "Gate-contract contains all categories", "grep gate-contract.md for PLAN AND COST AND ACCUM AND COB AND COMP", "All 9 gate categories present in index"),

    # LES gates
    ("LES-01", "Lessons index exists", "file_exists lessons/lessons.md", "Index file with topic table"),
    ("LES-02", "Accumulator lessons present", "grep accumulators.md for Embedded vs Aggregate AND OOP Max Excludes", "Key accumulator anti-patterns documented"),
    ("LES-03", "Cost-sharing lessons present", "grep cost-sharing.md for Copay Before vs After Deductible AND Preventive vs Diagnostic", "Key cost-sharing edge cases documented"),
    ("LES-04", "COB lessons present", "grep cob.md for Birthday rule AND Medicare primary", "Key COB determination lessons documented"),
    ("LES-05", "Compliance lessons present", "grep compliance.md for ACA preventive AND MHPAEA", "Key compliance testing lessons documented"),
    ("LES-06", "Quick reference top rules", "grep lessons.md for SBC is always the source of truth AND Quick Reference", "Top 10 rules quick-reference in lessons index"),

    # CHK gates
    ("CHK-01", "Pre-construction checkpoint exists", "file_exists checkpoints/pre-construction.md", "File exists with trigger: before-test-execution"),
    ("CHK-02", "SBC verification in pre-construction", "grep pre-construction.md for SBC AND VERIFY", "SBC loaded and validated before any testing"),
    ("CHK-03", "Mandatory reads enforced", "grep pre-construction.md for READ AND lessons.md", "Lessons must be read before test execution"),
    ("CHK-04", "On-failure checkpoint exists", "file_exists checkpoints/on-failure.md", "File exists with trigger: test-failure"),
    ("CHK-05", "HITL protocol in on-failure", "grep on-failure.md for STOP AND REPORT AND WAIT AND Enter choice", "5 user options presented on any failure"),
    ("CHK-06", "Severity classification", "grep on-failure.md for CRITICAL AND HIGH AND MEDIUM AND LOW", "4-tier severity classification documented"),

    # CONTR gates
    ("CONTR-01", "HITL protocol defined", "grep gate-contract.md for HITL Protocol AND MANDATORY AND STOP IMMEDIATELY", "HITL section present with mandatory stop-and-ask behavior"),
    ("CONTR-02", "SBC-First validation mandate", "grep gate-contract.md for SBC-First Validation AND MANDATORY AND Forbidden Patterns", "SBC-first validation with forbidden patterns documented"),
    ("CONTR-03", "Accumulator validation rules", "grep gate-contract.md for Accumulator Validation AND pre-claim AND post-claim AND $0.01", "Pre/post claim capture with $0.01 tolerance"),
    ("CONTR-04", "COB validation rules", "grep gate-contract.md for COB Validation AND payer order AND non-duplication", "COB determination and non-duplication rules"),
    ("CONTR-05", "Severity classification", "grep gate-contract.md for Severity Classification AND CRITICAL AND HIGH", "4-tier severity with examples"),
    ("CONTR-06", "Teaching pattern defined", "grep gate-contract.md for Teaching Pattern AND signal AND outcome AND insight", "Lesson template with plan_context field"),
    ("CONTR-07", "State persistence specified", "grep gate-contract.md for State Persistence AND workflow_state.json", "State location and format documented"),
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
Gate contract: `.claude/skills/benefits-config-testing/gate-contract.md`
"""
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {OUTPUT_DIR}")
