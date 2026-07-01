# Task 003: Refactor index.html Self-Extension Cards

## Status
Open

## Description
Update the Self-Extension section card descriptions. Two changes: clarify HITL capability and remove "sentence" language.

## Deliverable
Updated `D:/my_ai_projects/isagawa-co.github.io/index.html` with self-extension changes committed to `feature/spec-driven-framework-messaging` branch.

## Specification

### Change 1: Self-Extension Card 1 Description (Line 135)
**Current:**
```html
<p>Every capability begins as a sentence. The backlog captures raw conversational intent and structures it for execution. 130+ items logged, each one a starting point for autonomous production.</p>
```

**Replace with:**
```html
<p>Every capability begins as intent. The backlog captures intent and structures it for execution. 130+ items logged, each one a starting point for autonomous production.</p>
```

### Change 2: Self-Extension Card 2 Description (Line 141)
**Current:**
```html
<p>One command decomposes intent into tasks and executes them. 90+ completed pipelines across 50+ repos. No human intervention between start and finish.</p>
```

**Replace with:**
```html
<p>One command decomposes intent into tasks and executes them. 90+ completed pipelines across 50+ repos. Autonomous for deterministic execution; HITL for approvals, failures, and judgment points.</p>
```

## Acceptance Criteria
- Card 1 says "Every capability begins as intent" (not "sentence")
- Card 2 clarifies HITL: "Autonomous for deterministic execution; HITL for approvals, failures, and judgment points"
- No absolute claims about "no human intervention"
- HTML syntax valid
- Changes on feature branch only

## Gates
- BUILD-005: Self-extension card 1 updated ✓
- BUILD-006: Self-extension card 2 updated ✓
