# Research: SSH Compliance Spec Decomposition

## Context

The SSH testing platform (`platform-ssh-test`) now has 13 validators and 88 compliance rules across 8 frameworks. The domain spec (`platform-ssh`) only has the original 4 validators (config, package, service, kernel). This document proposes how to integrate the compliance layer into the domain spec.

## Current State

### platform-ssh (domain spec)
```
.claude/skills/ssh-management-layer/
├── SKILL.md
├── workflow.md          ← 5-step: Input → Preflight → Plan → Execute → Report
├── gate-contract.md     ← 23 gates (expects 4 validators)
└── references/
    ├── step-01.md through step-05.md

framework/_reference/
├── ssh_interface.py
├── validators/          ← 4 files: config, package, service, kernel
├── fixtures/            ← host_configs.json only
├── roles/               ← ssh_batch_executor.py
├── tasks/               ← run_ssh_command.py
└── tests/               ← conftest.py, test_ssh_batch.py
```

### platform-ssh-test (what we built)
```
framework/_reference/
├── ssh_interface.py
├── validators/          ← 13 files: 4 original + compliance_validator.py + 8 frameworks
├── fixtures/            ← host_configs.json + 8 framework rule JSONs
├── roles/               ← ssh_batch_executor.py (enhanced with by_framework)
└── tests/               ← conftest.py + test_ssh_batch.py + 9 test files
```

### platform-selenium (reference for spec patterns)
```
.claude/skills/qa-management-layer/
├── SKILL.md
├── workflow.md          ← 5-step with data flow diagram
├── gate-contract.md
├── checkpoints/         ← on-failure.md, pre-construction.md, propose-fix.md
└── steps/               ← step-01 through step-05

framework/_reference/
├── pages/               ← POM pattern (login_page.py, employees_page.py, tasks_page.py)
├── roles/               ← orchestrators (employee_manager.py, task_manager.py)
├── tasks/               ← domain tasks (employee_management_tasks.py, etc.)
└── tests/               ← e2e tests
```

## Analysis

### How Selenium Handles Multiple Components

The selenium spec uses the **POM (Page Object Model) pattern** — each page gets its own file in `pages/`, each business flow gets a role in `roles/`, and tasks compose page actions. The spec's reference files are the **templates** the agent reads before writing new code (see step-04.md: "READ reference files before writing code").

**Key insight:** The selenium spec doesn't enumerate every page in the spec itself. It provides the *pattern* (one reference page, one reference role, one reference test) and teaches the agent to follow the pattern for new components.

### How SSH Should Handle Compliance Frameworks

The compliance frameworks follow a **data-driven inheritance pattern**: one base class (`ComplianceValidator`) with framework-specific subclasses that only override `default_rules()` to load a JSON fixture. This is simpler than the POM pattern — the agent doesn't need to discover UI elements or generate BDD scenarios. It just needs:

1. The base class (ComplianceValidator)
2. One example framework validator (e.g., STIG)
3. One example fixture JSON
4. The pattern rule: "for each new framework, create a subclass + fixture"

## Proposed Spec Architecture

### Option A: Fixtures-as-Reference (Recommended)

Include all fixture JSONs and the base class in `_reference/`. Include ONE example framework validator. The spec teaches the pattern; the agent generates new frameworks from fixtures.

```
framework/_reference/
├── ssh_interface.py
├── validators/
│   ├── config_validator.py      ← original
│   ├── package_validator.py     ← original
│   ├── service_validator.py     ← original (with pgrep fallback)
│   ├── kernel_validator.py      ← original
│   ├── compliance_validator.py  ← NEW: base class
│   └── stig_validator.py        ← NEW: one example framework validator
├── fixtures/
│   ├── host_configs.json        ← enhanced with frameworks field
│   └── stig_rules.json          ← one example fixture
├── roles/
│   └── ssh_batch_executor.py    ← enhanced with by_framework
├── tasks/
│   └── run_ssh_command.py
└── tests/
    ├── conftest.py
    ├── test_ssh_batch.py
    └── test_stig_validator.py   ← one example test
```

**Workflow change:** Add a new step or sub-step to Step 3 (Plan):

```
Step 3: Plan
  3a. Select core validators (package, kernel, service, config)
  3b. Select compliance frameworks from host config's `frameworks` field
  3c. For each selected framework:
      - If validator exists: use it
      - If fixture exists but no validator: generate validator from pattern
      - If neither: skip (framework not available)
```

**Pros:**
- Minimal spec size — only one example of each artifact type
- Agent learns the pattern and generates the rest
- New frameworks can be added by just dropping a fixture JSON
- Aligns with how selenium spec works (reference files as templates)

**Cons:**
- Agent must generate framework validators on first run (one-time cost)
- Generated code must match the reference pattern exactly

### Option B: All-Inclusive Reference

Include ALL 8 framework validators, ALL 8 fixture JSONs, and ALL tests in `_reference/`.

```
framework/_reference/
├── validators/          ← 13 files (all included)
├── fixtures/            ← 9 files (host_configs + 8 frameworks)
└── tests/               ← 11 files (all included)
```

**Pros:**
- Zero generation needed — everything ships pre-built
- Prod-tested code, no risk of generation errors

**Cons:**
- Spec bloat — 32 additional files in reference
- Doesn't teach the agent the pattern — it just copies
- Adding a new framework requires updating the spec itself

### Option C: Hybrid — Fixtures Ship, Validators Generated

Ship all fixture JSONs (they're data, not code) but only one example validator. Agent generates the rest from the pattern.

```
framework/_reference/
├── validators/
│   ├── compliance_validator.py  ← base class
│   └── stig_validator.py        ← one example
├── fixtures/
│   ├── host_configs.json
│   ├── stig_rules.json
│   ├── cis_l1_rules.json
│   ├── nist_rules.json
│   ├── fips_rules.json
│   ├── pci_dss_rules.json
│   ├── hipaa_rules.json
│   ├── soc2_rules.json
│   └── iso27001_rules.json
└── tests/
    └── test_stig_validator.py   ← one example test
```

**Pros:**
- Rules are data — correct to ship as-is (88 rules, no generation risk)
- Validators are trivial (10 lines each) — safe to generate from pattern
- Tests follow identical pattern — safe to generate
- Best of both worlds: data accuracy + pattern teaching

**Cons:**
- Agent must generate 7 validators + 7 test files on first run

## Recommendation: Option C (Hybrid)

**Ship fixtures as data, generate validators from pattern.**

Rationale:
1. **Fixture JSON files are data, not code.** They contain specific STIG/CIS/NIST rule numbers, severity levels, and remediation text that the agent shouldn't be generating from memory. These are authoritative compliance rules — they should ship pre-built.
2. **Validators are trivial code.** Each is 10 lines: set `FRAMEWORK`, `FRAMEWORK_ID`, override `default_rules()` to load the fixture. The pattern is mechanical — safe to generate.
3. **The test pattern is identical across all 8.** Four assertions: attributes, rule count, prefix, validate returns results. Safe to generate.
4. **This teaches the agent the architecture.** When a customer wants to add a 9th framework (e.g., CMMC), they create a fixture JSON and the agent generates the validator from the pattern. No spec update needed.

## Spec Changes Required

### 1. New Reference Files

| File | Type | Source |
|------|------|--------|
| `validators/compliance_validator.py` | Code | Copy from test repo |
| `validators/stig_validator.py` | Code | Copy from test repo (example) |
| `fixtures/stig_rules.json` | Data | Copy from test repo |
| `fixtures/cis_l1_rules.json` | Data | Copy from test repo |
| `fixtures/nist_rules.json` | Data | Copy from test repo |
| `fixtures/fips_rules.json` | Data | Copy from test repo |
| `fixtures/pci_dss_rules.json` | Data | Copy from test repo |
| `fixtures/hipaa_rules.json` | Data | Copy from test repo |
| `fixtures/soc2_rules.json` | Data | Copy from test repo |
| `fixtures/iso27001_rules.json` | Data | Copy from test repo |
| `tests/test_stig_validator.py` | Code | Copy from test repo (example) |

### 2. Updated Reference Files

| File | Change |
|------|--------|
| `validators/service_validator.py` | Add pgrep fallback |
| `roles/ssh_batch_executor.py` | Add `by_framework` grouping in `get_results()` |
| `fixtures/host_configs.json` | Add `frameworks` array to each host entry |

### 3. Workflow Changes

**workflow.md** — Update Key Classes section:
```markdown
## Key Classes

- **SSHInterface** — Layer 1, paramiko wrapper
- **PackageValidator, KernelValidator, ServiceValidator, ConfigValidator** — Layer 2 (core)
- **ComplianceValidator** — Layer 2.5 (base class for compliance frameworks)
- **STIGValidator, CISValidator, NISTValidator, ...** — Layer 2.5 (compliance frameworks)
- **run_ssh_command** — Layer 3, atomic execution
- **SSHBatchExecutor** — Layer 4, orchestrator (with by_framework grouping)
```

**step-03.md** — Add compliance framework selection:
```markdown
## Compliance Framework Selection

Based on host config `frameworks` field:
1. Read frameworks array from host config
2. For each framework ID (e.g., "stig", "cis_l1"):
   - Check if validator exists at validators/{framework_id}_validator.py
   - If not: read compliance_validator.py + stig_validator.py as pattern
   - Generate new validator + test from pattern
3. Add compliance validators to execution plan
```

**step-04.md** — Add compliance execution:
```markdown
## Compliance Execution

After core validators:
1. Initialize compliance validators for selected frameworks
2. Execute via SSHBatchExecutor (same pipeline)
3. Results automatically grouped by framework via by_framework
```

**step-05.md** — Add compliance reporting:
```markdown
## Compliance Report Section

Include per-framework breakdown:
- Framework name + ID
- Rules total / passed / failed
- High-severity failures highlighted
- Remediation steps for each failure
```

### 4. Gate Contract Changes

Add gates for compliance infrastructure:

```markdown
| BUILD-13 | compliance_validator.py | file_exists | base class present | Create |
| BUILD-14 | ≥1 framework fixture | file_exists | stig_rules.json present | Create |
| BUILD-15 | host_configs has frameworks | grep | frameworks array present | Add |
| FUNC-06 | ComplianceValidator imports | run_code | import succeeds | Fix |
| FUNC-07 | Framework fixture valid JSON | json_valid | parses without error | Fix |
```

### 5. SKILL.md Changes

Add to the file index:
```markdown
## Compliance Frameworks

Data-driven compliance validation. Base class dispatches checks by rule type.

| Component | Location |
|-----------|----------|
| Base class | `validators/compliance_validator.py` |
| Example validator | `validators/stig_validator.py` |
| Rule fixtures | `fixtures/*_rules.json` |
| Pattern: add framework | Read base + example, create subclass + fixture |
```

## Migration Plan

### Phase 1: Update platform-ssh spec (backlog item)
1. Copy compliance_validator.py, stig_validator.py, test_stig_validator.py to spec's `_reference/`
2. Copy all 8 fixture JSONs to spec's `_reference/fixtures/`
3. Update service_validator.py with pgrep fallback
4. Update ssh_batch_executor.py with by_framework grouping
5. Update host_configs.json with frameworks field
6. Update workflow.md, step-03.md, step-04.md, step-05.md
7. Update gate-contract.md with new gates
8. Update SKILL.md with compliance section

### Phase 2: Validate via prod-test
1. Run `/kernel/prod-test` against updated platform-ssh
2. Verify domain-setup produces correct protocol
3. Verify L1/L2/L3 gates pass with compliance infrastructure
4. Verify agent can generate remaining 7 validators from pattern

### Phase 3: Sync to platform-ssh-test
1. Copy updated spec from platform-ssh to platform-ssh-test
2. Verify existing tests still pass
3. Verify new gates pass

## Open Questions

1. **Should the spec ship a "compliance audit" command?** A `/compliance-audit` command that runs all frameworks for a host and produces a compliance report. This would be a new command in the spec, not just a workflow step. Decision: defer to Phase 2.

2. **Should fixtures be versioned?** STIG rules change with each STIG release. Should the fixture include a version field (e.g., `"stig_version": "V3R5"`)? Decision: yes, add a `version` field to each fixture in Phase 1.

3. **Should the spec support custom frameworks?** A user drops a `custom_rules.json` in fixtures/ and the agent generates a validator. The pattern already supports this — no spec change needed. Document it in SKILL.md.
