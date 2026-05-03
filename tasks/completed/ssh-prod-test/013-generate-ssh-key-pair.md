# Generate SSH test key pair in test repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
ssh-keygen -t ed25519 -f C:/Users/solos/my_ai_projects/platform-ssh-test/_test/docker/test_key -N "" -C "ssh-prod-test"
```

## Acceptance Criteria
- [ ] `_test/docker/test_key` exists (private key)
- [ ] `_test/docker/test_key.pub` exists (public key)
