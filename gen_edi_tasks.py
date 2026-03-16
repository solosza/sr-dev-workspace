import os

tasks_dir = "D:/my_ai_projects/project_test_repos/test-edi-validation/tasks"
os.makedirs(tasks_dir, exist_ok=True)

gates = [
    ("001", "ENV-01", "Verify step-01.md contains transaction type options", "grep step-01.md for 837P, 835, 270, 834. All major X12 healthcare transaction codes must be present."),
    ("002", "ENV-02", "Verify step-01.md contains IG version mapping", "grep step-01.md for 005010X222A2, 005010X221A1. Each transaction type maps to correct IG version."),
    ("003", "ENV-03", "Verify step-01.md contains ISA parsing instructions", "grep step-01.md for 106 characters and fixed-length. ISA fixed-length parsing documented with position map."),
    ("004", "ENV-04", "Verify step-01.md contains delimiter extraction", "grep step-01.md for element separator, sub-element separator, segment terminator. All 3 delimiter types extracted from ISA positions."),
    ("005", "ENV-05", "Verify step-01.md contains companion guide loading", "grep step-01.md for companion guide and SNIP Type 7. Companion guide path handling with fallback when absent."),
    ("006", "ENV-06", "Verify step-01.md contains sample file validation", "grep step-01.md for sample_files and ISA parseable. At least 1 file required, ISA must parse successfully."),
    ("007", "ENV-07", "Verify step-01.md contains harness config output", "grep step-01.md for harness_config and element_separator. Config object contains transaction_type, ig_version, delimiters."),
    ("008", "SYN-01", "Verify step-02.md covers ISA/IEA pairing", "grep step-02.md for ISA/IEA and ISA13 must equal IEA02. Envelope pairing with control number matching documented."),
    ("009", "SYN-02", "Verify step-02.md covers GS/GE pairing", "grep step-02.md for GS/GE and GS06 must equal GE02. Functional group pairing with control number matching."),
    ("010", "SYN-03", "Verify step-02.md covers ST/SE pairing", "grep step-02.md for ST/SE and SE01 must equal count. Transaction set pairing with inclusive segment count."),
    ("011", "SYN-04", "Verify step-02.md covers segment ID validation", "grep step-02.md for segment ID and valid X12 segment identifier. All segment IDs checked against X12 standard."),
    ("012", "SYN-05", "Verify step-02.md covers element type validation", "grep step-02.md for AN and DT and TM and numeric. All 7 element types covered."),
    ("013", "SYN-06", "Verify step-02.md covers element length validation", "grep step-02.md for min/max length and fixed-length. Min/max length checks per IG definition."),
    ("014", "SYN-07", "Verify step-02.md covers segment order", "grep step-02.md for SEGMENT ORDER and order defined by the IG. 837P, 835, 270/271 segment orders documented."),
    ("015", "SYN-08", "Verify step-02.md covers required segment check", "grep step-02.md for Required and Situational and Not Used. R/S/N designation per IG enforced."),
    ("016", "SYN-09", "Verify step-02.md covers loop/HL structure", "grep step-02.md for HL01 and HL02 and parent-child. HL hierarchy chain validation with level codes."),
    ("017", "SYN-10", "Verify step-02.md covers qualifier/code validation", "grep step-02.md for NM1*85 and REF*D9 and DTP*472. Segment qualifier values checked against IG definitions."),
    ("018", "BAL-01", "Verify step-03.md covers claim charge balancing", "grep step-03.md for SV1*02 and CLM02 and total claim charge. Sum of line charges must equal claim total."),
    ("019", "BAL-02", "Verify step-03.md covers 835 payment balancing", "grep step-03.md for CLP04 and CLP03 and BPR02. Claim payment, service payment, and transaction-level balance."),
    ("020", "BAL-03", "Verify step-03.md covers segment count revalidation", "grep step-03.md for SE01 and GE01 and IEA01. All 3 envelope counts revalidated at semantic level."),
    ("021", "ISEG-01", "Verify step-03.md covers subscriber vs patient hierarchy", "grep step-03.md for 2000C and PAT and subscriber. Patient loop required when subscriber != patient."),
    ("022", "ISEG-02", "Verify step-03.md covers rendering provider requirement", "grep step-03.md for NM1*82 and rendering provider. NM1*82 required when billing != rendering."),
    ("023", "ISEG-03", "Verify step-03.md covers COB rules", "grep step-03.md for SBR01 and 2320 and COB. 2320 loop required when payer sequence != primary."),
    ("024", "ISEG-04", "Verify step-03.md covers diagnosis pointer linkage", "grep step-03.md for SV107 and HI and diagnosis pointer. SV107 references must point to valid HI positions."),
    ("025", "ISEG-05", "Verify step-03.md covers date consistency rules", "grep step-03.md for DTP*472 and future and admission date. Service dates not future, within coverage period."),
    ("026", "ISEG-06", "Verify step-03.md covers claim frequency/type codes", "grep step-03.md for CLM05-3 and REF*F8 and replacement. Replacement/void claims require original reference number."),
    ("027", "CODE-01", "Verify step-03.md covers ICD-10 code validation", "grep step-03.md for ICD-10-CM and HI segment and October 1. ICD-10 codes validated with date-sensitive code set."),
    ("028", "CODE-02", "Verify step-03.md covers CPT/HCPCS code validation", "grep step-03.md for CPT and HCPCS and SV101. Procedure codes validated against current code set."),
    ("029", "CODE-03", "Verify step-03.md covers Place of Service codes", "grep step-03.md for Place of Service and SV105. POS codes validated against CMS code set."),
    ("030", "CODE-04", "Verify step-03.md covers Revenue codes", "grep step-03.md for Revenue and SV201 and UB-04. Revenue codes validated against NUBC list."),
    ("031", "CODE-05", "Verify step-03.md covers Taxonomy codes", "grep step-03.md for Taxonomy and PRV03 and NUCC. Provider taxonomy validated against NUCC."),
    ("032", "CODE-06", "Verify step-03.md covers CARC/RARC codes", "grep step-03.md for CARC and RARC and CAQH CORE. Adjustment codes validated with combination rules."),
    ("033", "CODE-07", "Verify step-03.md covers NDC codes", "grep step-03.md for NDC and LIN segment and FDA. National Drug Codes validated against FDA directory."),
    ("034", "PROD-01", "Verify step-03.md covers professional 837P rules", "grep step-03.md for SV1 segment required and SV105 and Place of Service. 837P uses SV1, CPT/HCPCS, POS codes."),
    ("035", "PROD-02", "Verify step-03.md covers institutional 837I rules", "grep step-03.md for SV2 segment required and Revenue Code and Type of Bill. 837I uses SV2, revenue codes, UB-04."),
    ("036", "PROD-03", "Verify step-03.md covers dental 837D rules", "grep step-03.md for SV3 segment required and ADA CDT and TOO segment. 837D uses SV3, CDT codes, tooth info."),
    ("037", "TP-01", "Verify step-04.md covers companion guide analysis", "grep step-04.md for Companion Guide Analysis and ISA/GS requirements. Extraction of ISA, GS, content, submission, ack requirements."),
    ("038", "TP-02", "Verify step-04.md covers ISA qualifier validation", "grep step-04.md for ISA05 and ISA07 and companion guide required qualifier. Envelope qualifiers checked against partner requirements."),
    ("039", "TP-03", "Verify step-04.md covers application code validation", "grep step-04.md for GS02 and GS03 and application sender. GS application codes per companion guide."),
    ("040", "TP-04", "Verify step-04.md covers CAQH CORE operating rules", "grep step-04.md for CAQH CORE and Connectivity Rule and operating rules. CORE rules for eligibility, claims, payment, prior auth."),
    ("041", "TP-05", "Verify step-04.md covers TA1 acknowledgment generation", "grep step-04.md for TA1 and Acknowledgment Code and Interchange Note Code. TA1 generation with A/E/R codes."),
    ("042", "TP-06", "Verify step-04.md covers 999 acknowledgment generation", "grep step-04.md for 999 and AK1 and IK3 and IK5. 999 generation with full structure."),
    ("043", "TP-07", "Verify step-04.md covers 999 error codes", "grep step-04.md for IK3 and IK4 error codes. IK3 segment error codes (1-8) and IK4 element error codes (1-10)."),
    ("044", "TP-08", "Verify step-04.md covers clearinghouse considerations", "grep step-04.md for clearinghouse and translation. Clearinghouse routing, translation, and test endpoint handling."),
    ("045", "REG-01", "Verify step-05.md covers regression suite construction", "grep step-05.md for regression and test_snip and conftest. Test files organized by SNIP level with fixtures."),
    ("046", "REG-02", "Verify step-05.md covers regression comparison", "grep step-05.md for baseline and Previously-passing and regression. Baseline comparison with regression detection."),
    ("047", "REG-03", "Verify step-05.md covers coverage assessment", "grep step-05.md for Coverage and Min Tests and 80%. Coverage matrix per transaction type with threshold."),
    ("048", "REG-04", "Verify step-05.md covers production readiness report", "grep step-05.md for READY and NOT READY and CONDITIONAL. Report with SNIP results, ack status, coverage."),
    ("049", "REG-05", "Verify step-05.md covers readiness recommendation levels", "grep step-05.md for RECOMMENDATION and regressions and coverage. 3 levels with criteria."),
    ("050", "SPEC-01", "Verify SKILL.md exists with frontmatter", "grep SKILL.md for name: and type: and domain:. Frontmatter contains name, type, domain fields."),
    ("051", "SPEC-02", "Verify workflow contains 5-step index", "grep workflow.md for Step 1 and Step 5 and Step Index. All 5 steps listed with purpose, input, output, reference."),
    ("052", "SPEC-03", "Verify workflow contains data flow", "grep workflow.md for transaction_type and syntax_results and semantic_results and partner_results. Data flow shows output variables."),
    ("053", "SPEC-04", "Verify workflow contains SNIP mapping", "grep workflow.md for SNIP Types Covered and Type 1 and Type 7. SNIP types 1-7 mapped to workflow steps."),
    ("054", "SPEC-05", "Verify workflow references state location", "grep workflow.md for workflow_state.json and tests/_state. State file path and format documented."),
    ("055", "SPEC-06", "Verify all 5 step files exist", "file_exists steps/step-01.md through steps/step-05.md. All step reference files present."),
    ("056", "SPEC-07", "Verify gate-contract contains all categories", "grep gate-contract.md for ENV, SYN, BAL, ISEG, CODE, PROD, TP, REG. All 12 gate categories present in index."),
    ("057", "LES-01", "Verify lessons index exists", "file_exists lessons/lessons.md. Index file with topic table."),
    ("058", "LES-02", "Verify ISA fixed-length lesson", "grep common-mistakes.md for 106 characters and positional parsing. ISA fixed-length parsing pattern documented."),
    ("059", "LES-03", "Verify delimiter detection lesson", "grep common-mistakes.md for segment terminator and position 106. Dynamic delimiter detection from ISA documented."),
    ("060", "LES-04", "Verify SE01 count lesson", "grep common-mistakes.md for SE01 and ST and SE and inclusive. Inclusive segment count rule documented."),
    ("061", "LES-05", "Verify implicit decimal lesson", "grep common-mistakes.md for N2 and implied decimal and R. N0/N2/R decimal handling documented."),
    ("062", "LES-06", "Verify code set date sensitivity lesson", "grep common-mistakes.md for October 1 and January 1 and date of service. Date-aware code set validation documented."),
    ("063", "CHK-01", "Verify pre-construction checkpoint exists", "file_exists checkpoints/pre-construction.md. File exists with trigger: before-build."),
    ("064", "CHK-02", "Verify forbidden patterns documented", "grep pre-construction.md for FORBIDDEN and Hardcoded delimiters and Hardcoded code set. At least 4 forbidden patterns with correct alternatives."),
    ("065", "CHK-03", "Verify mandatory reads enforced", "grep pre-construction.md for READ and Implementation Guide and companion guide. IG read, companion guide read, lessons read before tests."),
    ("066", "CHK-04", "Verify on-failure checkpoint exists", "file_exists checkpoints/on-failure.md. File exists with trigger: validation-failure."),
    ("067", "CHK-05", "Verify HITL protocol in on-failure", "grep on-failure.md for STOP and REPORT and WAIT and HOW SHOULD WE PROCEED. 5 user options presented on any failure."),
    ("068", "CHK-06", "Verify error reporting format", "grep on-failure.md for SEGMENT and ELEMENT and IG REFERENCE and EXPECTED and ACTUAL. Structured error report."),
    ("069", "CONTR-01", "Verify HITL protocol defined in gate-contract", "grep gate-contract.md for HITL Protocol and MANDATORY and STOP IMMEDIATELY. HITL section present with mandatory stop-and-ask."),
    ("070", "CONTR-02", "Verify auto-fixable errors list", "grep gate-contract.md for Auto-Fixable and SE01 count and control number mismatch. Explicit list of mechanically fixable errors."),
    ("071", "CONTR-03", "Verify learning cycle described", "grep gate-contract.md for Learning Cycle and VALIDATE and TEACH and LEARN. Gate execution flow documented."),
    ("072", "CONTR-04", "Verify state persistence specified", "grep gate-contract.md for State Persistence and workflow_state.json. State location and format documented."),
    ("073", "CONTR-05", "Verify teaching pattern defined", "grep gate-contract.md for Teaching Pattern and signal and outcome and insight. Lesson template documented."),
]

for num, gate_id, title, criteria in gates:
    content = f"""# Task {num}: {title}

**Gate:** {gate_id}
**Type:** verification
**Status:** pending

## Acceptance Criteria

{criteria}

## Verification

1. Read the source file referenced in the gate
2. Search for the required patterns
3. Confirm pass criteria are met
4. Report PASS or FAIL with evidence
"""
    filepath = os.path.join(tasks_dir, f"{num}-verify-{gate_id.lower().replace('-', '_')}.md")
    with open(filepath, "w") as f:
        f.write(content)

print(f"Generated {len(gates)} task files in {tasks_dir}")
