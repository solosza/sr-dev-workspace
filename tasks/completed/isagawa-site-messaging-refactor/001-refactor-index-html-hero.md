# Task 001: Refactor index.html Hero Section

## Status
Open

## Description
Update the hero section of index.html with new SDD architecture messaging. Three specific line replacements from the change-map.

## Deliverable
Updated `D:/my_ai_projects/isagawa-co.github.io/index.html` with hero changes committed to `feature/spec-driven-framework-messaging` branch.

## Specification

### Change 1: Hero Title (Line 46)
**Current:**
```html
<h2>An agent harness factory.</h2>
```

**Replace with:**
```html
<h2>SDD architecture for governed agents.</h2>
```

### Change 2: Hero Subtitle (Line 47)
**Current:**
```html
<p>You describe intent in natural language. The factory produces agent harnesses - structured runtimes that govern what agents do, with the governance baked in.</p>
```

**Replace with:**
```html
<p>Isagawa turns repeatable workflows into governed agent harnesses. The kernel enforces execution, the domain-spec factory builds vertical packs, and the backlog pipeline turns intent into validated work.</p>
```

## Acceptance Criteria
- Hero title contains "SDD architecture for governed agents"
- Hero subtitle matches exact replacement text
- No "natural language" claims in hero section
- HTML syntax valid
- Changes on feature branch only

## Gates
- BUILD-001: Hero title updated ✓
- BUILD-002: Hero subtitle updated ✓
