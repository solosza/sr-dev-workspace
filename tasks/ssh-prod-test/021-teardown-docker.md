# Tear down Docker container

## Type
BUILD

## Executor
Outer spawned agent via `run-task.sh` in sr-dev-workspace

## Action
```bash
docker-compose -f C:/Users/solos/my_ai_projects/platform-ssh-test/_test/docker/docker-compose.yml down
```

## Acceptance Criteria
- [ ] `docker ps --filter name=ssh-prod-test` shows no running containers
