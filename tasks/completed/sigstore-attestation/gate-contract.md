# Gate Contract — Sigstore Attestation Pipeline

## Gate Contract

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Attestations directory exists | file_exists | `test -d .claude/state/attestations/` | Create directory |
| BUILD-02 | Schema module exists | file_exists | `test -f lib/attestation/schema.py` | Create file |
| BUILD-03 | Hash collector exists | file_exists | `test -f lib/attestation/collect.py` | Create file |
| BUILD-04 | Signing wrapper exists | file_exists | `test -f lib/attestation/sign.py` | Create file |
| BUILD-05 | Rekor logger exists | file_exists | `test -f lib/attestation/rekor.py` | Create file |
| BUILD-06 | Attest orchestrator exists | file_exists | `test -f lib/attestation/attest.py` | Create file |
| BUILD-07 | Attest command exists | file_exists | `test -f .claude/commands/kernel/attest.md` | Create file |
| BUILD-08 | Execute-pipeline step-05 updated | grep | `grep -q 'attestation' .claude/skills/execute-pipeline/references/step-05-validate-report.md` | Add attestation step |
| FUNC-01 | Hash collector produces SHA-256 | run_code | `python lib/attestation/collect.py --test` exits 0 with valid hash output | Fix collector |
| FUNC-02 | Schema validates bundle | run_code | `python lib/attestation/schema.py --validate` exits 0 | Fix schema |
| FUNC-03 | cosign CLI available | run_code | `cosign version` exits 0 | Install cosign |
| TEST-01 | Full attestation on test artifact | run_code | `python lib/attestation/attest.py --dry-run` exits 0 with bundle written | Fix pipeline |
| TEST-02 | Bundle has all required fields | run_code | Bundle JSON has predicateType, invocation, output, timestamp, metadata | Fix schema |
