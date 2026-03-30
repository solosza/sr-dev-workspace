# SSH Platform Production Test — Task Index

## Goal

Full production test of the SSH image testing platform. Set up master repo with kernel, run domain-setup, copy to test repo, stand up Docker target, run L1/L2/L3 tests inside test repo via inner run-task.sh.

## Repos

- **Master repo:** `C:/Users/solos/my_ai_projects/platform-ssh-master` (golden copy — kernel + domain spec + framework + scripts)
- **Test repo:** `C:/Users/solos/my_ai_projects/platform-ssh-test` (disposable copy where tests run)
- **Source framework:** `C:/Users/solos/my_ai_projects/platform-ssh-verify` (existing platform code)
- **Kernel source:** `C:/Users/solos/my_ai_projects/run-task-resume-master` (shell scripts)

## Execution

```bash
# Outer orchestration from sr-dev-workspace
./run-task.sh . 25 ssh-prod-test
```

All outer tasks executed by **spawned agents** via `run-task.sh` in sr-dev-workspace.
Inner test tasks executed by **spawned agents** via `run-task.sh` inside the test repo.

## Tasks

### MASTER Phase — Build golden master repo

| # | Task | Type | Executor | Phase |
|---|------|------|----------|-------|
| 001 | [[001-create-master-repo]] | BUILD | outer spawned agent | MASTER |
| 002 | [[002-copy-framework-to-master]] | BUILD | outer spawned agent | MASTER |
| 003 | [[003-copy-domain-spec-to-master]] | BUILD | outer spawned agent | MASTER |
| 004 | [[004-copy-kernel-to-master]] | BUILD | outer spawned agent | MASTER |
| 005 | [[005-copy-shell-scripts-to-master]] | BUILD | outer spawned agent | MASTER |
| 006 | [[006-write-master-claude-md]] | BUILD | outer spawned agent | MASTER |

### VALIDATE Phase — Domain setup + verify

| # | Task | Type | Executor | Phase |
|---|------|------|----------|-------|
| 007 | [[007-run-domain-setup-in-master]] | BUILD | outer spawned agent | VALIDATE |
| 008 | [[008-verify-protocol-created]] | TEST | outer spawned agent | VALIDATE |
| 009 | [[009-verify-hooks-registered]] | TEST | outer spawned agent | VALIDATE |
| 010 | [[010-verify-commands-exist]] | TEST | outer spawned agent | VALIDATE |

### COPY Phase — Master → test repo

| # | Task | Type | Executor | Phase |
|---|------|------|----------|-------|
| 011 | [[011-copy-master-to-test-repo]] | BUILD | outer spawned agent | COPY |

### INFRA Phase — Docker target setup (in test repo)

| # | Task | Type | Executor | Phase |
|---|------|------|----------|-------|
| 012 | [[012-write-dockerfile]] | BUILD | outer spawned agent | INFRA |
| 013 | [[013-generate-ssh-key-pair]] | BUILD | outer spawned agent | INFRA |
| 014 | [[014-write-docker-compose]] | BUILD | outer spawned agent | INFRA |
| 015 | [[015-build-start-container]] | BUILD | outer spawned agent | INFRA |
| 016 | [[016-verify-ssh-connectivity]] | TEST | outer spawned agent | INFRA |
| 017 | [[017-install-python-deps]] | BUILD | outer spawned agent | INFRA |

### TEST Phase — Write inner test tasks + run via inner run-task.sh

| # | Task | Type | Executor | Phase |
|---|------|------|----------|-------|
| 018 | [[018-write-inner-test-tasks]] | BUILD | outer spawned agent | TEST |
| 019 | [[019-run-inner-test-batch]] | TEST | outer spawned agent (runs inner run-task.sh) | TEST |

### REPORT + CLEANUP Phase

| # | Task | Type | Executor | Phase |
|---|------|------|----------|-------|
| 020 | [[020-collect-validation-report]] | BUILD | outer spawned agent | REPORT |
| 021 | [[021-teardown-docker]] | BUILD | outer spawned agent | CLEANUP |

## Phases

```
MASTER → VALIDATE → COPY → INFRA → TEST → REPORT → CLEANUP
```

## Baseline

→ `docs/research/qa-platform-prod-test-baseline.md`
