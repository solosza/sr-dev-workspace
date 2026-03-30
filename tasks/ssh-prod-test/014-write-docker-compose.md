# Write docker-compose.yml in test repo

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
Write `C:/Users/solos/my_ai_projects/platform-ssh-test/_test/docker/docker-compose.yml`:

- Service: `rocky-ssh`
- Build from local Dockerfile
- Map port 22 → 2222
- Container name: `ssh-prod-test`

## Acceptance Criteria
- [ ] File exists
- [ ] Contains `2222:22`
- [ ] Contains `rocky-ssh`
