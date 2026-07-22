# Task 002: Write SQL Server Compose File

**Type:** BUILD | **Gates:** DB-02

## Action
Write `D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/docker/sqlserver-compose.yml` (ONE file).

## Spec
- Image `mcr.microsoft.com/mssql/server:2022-latest`; container_name `orderly-sqlserver`
- `ACCEPT_EULA=Y`, `MSSQL_SA_PASSWORD=${MSSQL_SA_PASSWORD:-Orderly!Dev2026}` (env-overridable dev default)
- Check host port first (`netstat` or python socket bind on 1433); map 1433 or the first free of 14330-14339 — record the chosen port IN the compose file comment and use it consistently in later tasks via env `ORDERLY_MSSQL_PORT`
- healthcheck: `/opt/mssql-tools18/bin/sqlcmd -C -S localhost -U sa -P $$MSSQL_SA_PASSWORD -Q "SELECT 1"` interval 10s retries 10

## Acceptance
`docker compose -f <file> config` parses clean; greps per DB-02.
