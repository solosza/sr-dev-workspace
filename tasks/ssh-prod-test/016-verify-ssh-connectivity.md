# Verify SSH connectivity to container

## Type
TEST

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
ssh -i C:/Users/solos/my_ai_projects/platform-ssh-test/_test/docker/test_key -p 2222 -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@localhost whoami
```

## Acceptance Criteria
- [ ] Command exits 0
- [ ] Output contains `root`
