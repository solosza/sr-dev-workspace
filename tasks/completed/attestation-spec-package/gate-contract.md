# Gate Contract — Attestation Domain Spec Package

| Gate ID | Task | Method | Check | Expected |
|---------|------|--------|-------|----------|
| BUILD-01 | 001 | file_exists | `D:\my_ai_projects\agent-attestation-spec\LICENSE` | exists |
| BUILD-01b | 001 | file_exists | `D:\my_ai_projects\agent-attestation-spec\.gitignore` | exists |
| BUILD-02 | 002 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\collect.py` | exists |
| BUILD-03 | 003 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\schema.py` | exists |
| BUILD-04 | 004 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\sign.py` | exists |
| BUILD-05 | 005 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\rekor.py` | exists |
| BUILD-06 | 006 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\intent.py` | exists |
| BUILD-07 | 007 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\attest.py` | exists |
| BUILD-07b | 007 | file_exists | `D:\my_ai_projects\agent-attestation-spec\lib\__init__.py` | exists |
| BUILD-08 | 008 | file_exists | `D:\my_ai_projects\agent-attestation-spec\SKILL.md` | exists |
| BUILD-09 | 009 | file_exists | `D:\my_ai_projects\agent-attestation-spec\references\step-01-prerequisites.md` | exists |
| BUILD-09b | 009 | file_exists | `D:\my_ai_projects\agent-attestation-spec\references\step-05-verify.md` | exists |
| BUILD-10 | 010 | file_exists | `D:\my_ai_projects\agent-attestation-spec\README.md` | exists |
| BUILD-10b | 010 | grep | `grep -c "quickstart\|Quickstart\|Quick Start" D:\my_ai_projects\agent-attestation-spec\README.md` | >= 1 |
| BUILD-11 | 011 | file_exists | `D:\my_ai_projects\agent-attestation-spec\docs\architecture.md` | exists |
| BUILD-12 | 012 | file_exists | `D:\my_ai_projects\agent-attestation-spec\examples\sample-bundle.json` | exists |
| TEST-13 | 013 | run_code | `cd D:\my_ai_projects\agent-attestation-spec && python lib\attest.py --dry-run` | exit 0 |
