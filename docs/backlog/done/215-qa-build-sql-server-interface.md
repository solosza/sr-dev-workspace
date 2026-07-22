# SqlServerInterface [V3]

## Status
Open

## Priority
High — strictest clean-room item

## Summary
Build Layer 1 SqlServerInterface FROM SCRATCH on mssql-python per the 1.3 design doc. IP-critical: v2 OracleInterface had 80% similarity to the old concept — zero code reuse.

## Requirements
- execute_query/_query_one/_scalar/_non_query/_many/_sproc; ? parameterization; catch-log-reraise
- SDK: mssql-python (NOT pyodbc); hmsa-healthcare-qa is concept-only

## References
- projects/hmsa-qa-platform/01-interface-design/sql-server-interface.md
- projects/hmsa-qa-platform/02-reference-patterns/5-layer-contract.md (governing contract; compliance tables are gate sources)
- ANTI-PATTERN ONLY: v2 oracle_interface.py (never open for code)

## Task Builder Input
- **Deliverable:** framework/interfaces/sql_server_interface.py, from scratch, L1-L3 tested vs Orderly DB. L3 (e2e) requires the Orderly harness slice for this vertical to be running and reachable; if unreachable, report L3-BLOCKED and STOP for user decision — never fake an e2e pass.
- **Location:** new-repo:D:\my_ai_projects\project_test_repos\hmsa-qa-platform
- **Scope:** BUILD
- **Constraints:** V3 DB — blocked until V2 (209-213) is fully built and tested (213 accepted). STRICT vertical order within the slice — each item waits on the previous item's acceptance. Write ONLY on target-repo feature branch build/215-qa-build-sql-server-interface; merge via /kernel/review-queue accept, never direct to main. Clean-room: v2 legacy is anti-pattern/architecture reference only. DEMO DOMAIN IS GENERIC COMMERCE (Orderly orders app) — NO HMSA/healthcare vocabulary in any shipped code. Plan L1/L2/L3 test tasks during atomization.
