# Repo Inventory — Current Kernel Features

## Status
NEW — populated from scan

## Tier 1: Recent Kernel (closest to master)

### domain-spec-factory
- **Commands:** spec-factory-build, spec-factory-run, spec-factory-score
- **Skills:** audit-workflow, autonomous-cycling, execute-pipeline, kernel-domain-setup, prod-test, spec-factory, task-builder
- **Hooks:** actions-log-appender, auto-approve-claude-writes, code-quality-enforcer, test-failure-detector, universal-gate-enforcer
- **Protocol:** spec_factory-protocol.md
- **Missing from master:** anchor, attest, backlog, complete, domain-setup, fix, learn, reset, scan-bookmarks, session-start, task-builder (as command), agent-inline-execution-blocker hook

### hmsa-healthcare-qa
- **Commands:** create-ado-test-cases, create-sql-dump, qa-onboard, qa-review, qa-test
- **Skills:** autonomous-cycling, execute-pipeline, healthcare-qa, kernel-domain-setup, task-builder
- **Hooks:** actions-log-appender, test-failure-detector, universal-gate-enforcer
- **Protocol:** hmsa_healthcare_qa-protocol.md
- **Missing from master:** anchor, attest, audit-workflow, backlog, complete, domain-setup, fix, learn, reset, scan-bookmarks, session-start, task-builder (command), auto-approve hook, agent-inline-execution-blocker hook, prod-test skill, audit-workflow skill

## Tier 2: Medium Kernel (some features)

### game-dev / game-engine-master (identical)
- **Commands:** game-build, game-create
- **Skills:** game-engine
- **Hooks:** actions-log-appender, auto-approve-claude-writes, code-quality-enforcer, test-failure-detector, universal-gate-enforcer
- **Protocol:** game-engine-protocol.md
- **Missing from master:** All 15 kernel commands, 6 kernel skills, agent-inline-execution-blocker hook

### healthcare-qa-spec-master
- **Commands:** qa-onboard, qa-review, qa-test
- **Skills:** healthcare-qa
- **Hooks:** actions-log-appender, auto-approve-claude-writes, code-quality-enforcer, test-failure-detector, universal-gate-enforcer
- **Protocol:** healthcare_qa-protocol.md
- **Missing from master:** All 15 kernel commands, 6 kernel skills, agent-inline-execution-blocker hook

### platform-deepeval
- **Commands:** eval-dev, eval-workflow
- **Skills:** audit-workflow, autonomous-cycling, deepeval-management-layer, kernel-domain-setup, prod-test, task-builder
- **Hooks:** actions-log-appender, auto-approve-claude-writes, test-failure-detector, universal-gate-enforcer
- **Protocol:** None
- **Missing from master:** All 15 kernel commands, execute-pipeline skill, agent-inline-execution-blocker hook

## Tier 3: Old Kernel (minimal features)

### cognitive-agent
- **Commands:** image-on-failure, image-pre-construction, image-propose-fix, image-reuse-check, image-workflow, image-workflow-dev, pr, run-test
- **Skills:** autonomous-cycling, image-testing-guidance, kernel-domain-setup
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Protocol:** image_testing-protocol.md
- **Missing from master:** All 15 kernel commands, 5 kernel skills, 4 hooks

### isagawa-qa-zentyant
- **Commands:** pr, qa-on-failure, qa-pre-construction, qa-propose-fix, qa-reuse-check, qa-workflow, qa-workflow-dev, run-test
- **Skills:** kernel-domain-setup, qa-management-layer
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Protocol:** qa-protocol.md
- **Missing from master:** All 15 kernel commands, 5 kernel skills, 4 hooks

### platform-playwright / platform-selenium (similar)
- **Commands:** pr, qa-on-failure, qa-pre-construction, qa-propose-fix, qa-reuse-check, qa-workflow, qa-workflow-dev, run-test
- **Skills:** autonomous-cycling, kernel-domain-setup, qa-management-layer
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Protocol:** None
- **Missing from master:** All 15 kernel commands, 4 kernel skills, 4 hooks

### test-content-production
- **Commands:** content-calendar, content-produce, content-repurpose
- **Skills:** content-production
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Protocol:** None
- **Missing from master:** All 15 kernel commands, 6 kernel skills, 4 hooks, CLAUDE.md

### test-kernel-bootstrap
- **Commands:** kernel-build, kernel-build-dev, kernel-on-failure, kernel-pre-build-check, qa-on-failure, qa-pre-construction, qa-propose-fix, qa-workflow, qa-workflow-dev
- **Skills:** autonomous-cycling, kernel-domain-setup, kernel-governance, qa-management-layer
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Protocol:** qa-management-layer-protocol.md
- **Missing from master:** All 15 kernel commands (as kernel/ prefixed), 4 kernel skills, 4 hooks

### test-platform-deepeval
- **Commands:** None
- **Skills:** autonomous-cycling, deepeval-management-layer, kernel-domain-setup
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Protocol:** deepeval-protocol.md
- **Missing from master:** All 15 kernel commands, 4 kernel skills, 4 hooks

## Tier 4: Legacy Kernel (pre-standard)

### isagawa-kernel
- **Commands:** None
- **Skills:** autonomous-cycling, kernel-domain-setup
- **Hooks:** test-failure-detector, universal-gate-enforcer
- **Missing from master:** All 15 commands, 5 skills, 4 hooks

### isagawa-kernel-a / isagawa-kernel-b
- **Commands:** (b has playwright-anchor, playwright-learn, playwright-validate)
- **Skills:** None
- **Hooks:** playwright-gate-enforcer, universal-gate-enforcer (+ test-failure-detector in b)
- **Missing from master:** Nearly everything

### py_sel_framework_mcp / qa_kernel_test (identical)
- **Commands:** 4d, cleanup, elegant, fix, grill, intel, pr, prove, qa-workflow, qa-workflow-dev, reset-kernel-test, run-test, sync-to-isagawa-qa
- **Skills:** create-vertical-validation-agents, design-decisions, design-execution-engine, dialogue-engine, documentation, execute-from-step1, fix-workflow, qa-management-layer, rag-learning, testing
- **Hooks:** audit-trail-writer, qa-gate-enforcer (+ test-failure-detector, universal-gate-enforcer in qa_kernel_test)
- **Protocol:** None
- **Missing from master:** All 15 kernel commands (completely different command set), all 7 kernel skills, 4+ hooks
