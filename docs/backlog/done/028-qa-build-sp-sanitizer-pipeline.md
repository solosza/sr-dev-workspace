# SP Sanitizer Pipeline — Safe SQL Sharing for AI-Assisted QA

## Status
Done

## Priority
High — enables AI agents to analyze production stored procedures without exposing real schema names, table structures, or sensitive identifiers. Direct blocker for AI-assisted SP validation on 30-Day Readmissions and future QNXT projects.

## Summary
Build a modular Python pipeline that sanitizes SQL Server stored procedures for safe sharing with AI agents. The tool replaces real database identifiers (tables, columns, schemas, SP names) with consistent synthetic names, guarantees zero leakage via a heuristic leak detector, and supports reverse mapping to translate AI recommendations back to real names. Designed for QA analysts who need AI help understanding SP logic without exposing proprietary schema.

## Context
- No direct database access — only SP source code as input
- T-SQL (SQL Server) specific — HMSA/QNXT healthcare claims environment
- Must handle dynamic SQL (EXEC, sp_executesql), comments, string literals, four-part names, delimited identifiers
- 95% sanitization is worse than 0% — partial leaks create false confidence
- The tester learns from sanitized output, so accuracy of structure/logic preservation is critical

## Architecture (Grilled + Elegant Rethink)

### Design: Aggressive Replace + Heuristic Leak Detector

Original 7-module pipeline was grilled and found to have a fatal flaw: no safety net for missed identifiers. Reworked to a 2-phase + refinement design:

```
Phase 1: extract + aggressive replace (catalog_replace.py)
  - Extract identifiers from SP text itself (no DB access needed)
  - Global find/replace: every real name → synthetic name
  - Intentionally aggressive — catches dynamic SQL, comments, strings
  - Persistent mapping store for cross-file consistency

Phase 2: leak detector (leak_detector.py)
  - Scan output for anything that LOOKS real but wasn't mapped
  - Heuristics: unrecognized PascalCase/snake_case tokens not in T-SQL keyword list
  - Pattern checks: dbo.X, schema.X, tokens after FROM/JOIN/INTO/UPDATE/EXEC
  - Binary output: CLEAN or FLAGGED (with locations)

Phase 3 (optional): refinement (refine.py)
  - Context-aware pass to reduce false positives in comments/strings
  - Only place that needs actual T-SQL parsing — and it's optional

Plus:
  - reverse.py — translate sanitized names back to real names
  - runner.py — orchestrator, data contracts between phases
```

### Key Design Decisions
- **Aggressive over surgical**: Replace everything, verify after — not parse perfectly, replace carefully
- **Heuristic leak detection without DB access**: T-SQL keyword whitelist + mapping store = anything unrecognized is suspect
- **SRP modules with data contracts**: Pydantic models or JSON schemas between steps for testability
- **Persistent mapping store**: Cross-file consistency, gitignored, treated as secret
- **Position-based replacement dropped**: Global text replacement is simpler and catches dynamic SQL for free

### Grill Findings Addressed
| Grill Finding | How Addressed |
|---------------|---------------|
| No safety net for missed identifiers | Leak detector (Phase 2) |
| Dynamic SQL black hole | Aggressive global replace catches all occurrences |
| Comments/string literals leaking | Same — aggressive replace hits everything |
| Mapping store is the secret | Gitignore, treat as sensitive, document handling |
| Partial sanitization worse than none | Leak detector gives binary CLEAN/FLAGGED |
| No "good enough" definition | Zero leaks or fail — leak detector is the gate |
| SQL dialect specificity | T-SQL keyword whitelist, SQL Server delimited identifier handling |

## Requirements
- Python 3.10+ with no heavy dependencies (stdlib + Pydantic for contracts)
- Input: raw `.sql` files (one or more SPs)
- Output: sanitized `.sql` files + mapping file + leak report
- Mapping store must be persistent across runs for cross-SP consistency
- Mapping store must be gitignored and documented as sensitive
- Leak detector must flag ANY unrecognized non-keyword token in identifier positions
- Must handle: `[delimited identifiers]`, four-part names, `#temp` tables, `@table` variables, CTEs, MERGE, CROSS APPLY, OUTPUT clauses
- Reverse mapping must be 1:1 and invertible
- Each module independently testable via data contracts

## References
- 30-Day Readmissions project: `projects/30-day-readmissions/`
- Phase 2 execution plan: `projects/30-day-readmissions/phase2-execution-plan.md`
- Grill command used for adversarial review: `.claude/commands/grill.md`
- Elegant rethink triggered by grill verdict: `.claude/commands/elegant.md`

## Task Builder Input
- **Deliverable:** Python package (`sp_sanitizer/`) with 5 modules (catalog_replace, leak_detector, refine, reverse, runner), Pydantic data contracts, T-SQL keyword whitelist, CLI entry point, and test suite
- **Scope:** BUILD
- **Constraints:**
  - No database access — schema catalog derived from SP text only
  - T-SQL specific (SQL Server syntax, `[]` delimiters, four-part names)
  - Mapping store is sensitive — must be gitignored, never committed
  - Leak detector is the quality gate — pipeline fails if any leak detected
  - Must be testable with sample SP fixtures (synthetic SPs that mimic real patterns)
  - Target repo TBD — likely standalone or under `tools/` in this workspace
