# Write Dockerfile in test repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Write `C:/Users/solos/my_ai_projects/platform-ssh-test/_test/docker/Dockerfile`:

- Base: `rockylinux:9`
- Install `openssh-server`
- Configure sshd: `PermitRootLogin yes`, `PubkeyAuthentication yes`
- Set up `/root/.ssh/authorized_keys`
- Expose port 22
- CMD: `/usr/sbin/sshd -D`

## Acceptance Criteria
- [ ] Dockerfile exists at the specified path
- [ ] Contains `rockylinux:9`
- [ ] Contains `openssh-server`
