# Enforcement Loop Diagram

## Status
NEW — needs design

## Location
docs/architecture-diagrams/enforcement-loop.svg

## What it shows
The core enforcement pattern:
```
Domain Spec → Implementation Code → Hook Triggers →
Verification Rules → Gate Pass/Fail → Action (Continue/Block)
```

## Key elements to visualize
1. Domain spec as source of truth
2. Hook insertion points in execution pipeline
3. Verification logic (protocol checks, state validation)
4. Gate contract execution
5. Pass path (continue work)
6. Fail path (block + remediation guidance)

## Dependencies
Depends on: diagram-specifications.md
