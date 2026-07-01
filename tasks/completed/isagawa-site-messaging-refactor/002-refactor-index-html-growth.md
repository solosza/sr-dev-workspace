# Task 002: Refactor index.html Growth Section

## Status
Open

## Description
Update the Growth section (Section 02) of index.html. Two changes: subtitle and narrative text removal of "natural language" claims.

## Deliverable
Updated `D:/my_ai_projects/isagawa-co.github.io/index.html` with growth section changes committed to `feature/spec-driven-framework-messaging` branch.

## Specification

### Change 1: Growth Subtitle (Line 98)
**Current:**
```html
<p class="anchor-section__subtitle reveal">The kernel produced everything it now uses to operate: agent harnesses, a factory, workspaces.</p>
```

**Replace with:**
```html
<p class="anchor-section__subtitle reveal">SDD architecture: the kernel governs execution, the domain-spec factory compiles specifications into harnesses, and together they bootstrap each new capability.</p>
```

### Change 2: Growth Narrative (Line 99)
**Current:**
```html
<p class="anchor-section__narrative reveal"><strong>None of this was hand-coded</strong>. The kernel managed conversations that produced AI agents. Those agents taught the system new fields. A factory pipeline emerged to <strong>compile natural language into structured agents automatically</strong>. Workspaces followed. Complete development environments that inherit kernel management from birth.</p>
```

**Replace with:**
```html
<p class="anchor-section__narrative reveal"><strong>None of this was hand-coded</strong>. The kernel managed conversations that produced AI agents. Those agents taught the system new fields. A factory pipeline emerged to compile specifications into structured agents. Workspaces followed. Complete development environments that inherit kernel management from birth.</p>
```

## Acceptance Criteria
- Subtitle mentions "SDD architecture"
- Narrative no longer contains "natural language" claims
- "compile specifications into structured agents" language used
- HTML syntax valid
- Changes on feature branch only

## Gates
- BUILD-003: Growth subtitle updated ✓
- BUILD-004: Growth narrative updated ✓
