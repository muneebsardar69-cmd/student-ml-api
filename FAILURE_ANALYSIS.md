# Failure Analysis

## Failure 1: Broken Test
- Changed assertion to 'wrong' to demonstrate CI catches failures
- Error: AssertionError - expected 'healthy', got 'wrong'
- Fixed by reverting assertion to 'healthy'
- Learning: CI/CD pipeline automatically catches test failures

## Failure 2: Empty Dockerfile
- Dockerfile was empty, build failed
- Error: "failed to build: the Dockerfile cannot be empty"
- Fixed by writing complete Dockerfile with all layers
- Learning: Configuration errors caught by CI

## Failure 3: GHCR Permission Denied
- Release pipeline failed pushing to registry
- Error: "denied: installation not allowed to create organization package"
- Root cause: GitHub token had "read-only" permissions
- Fixed by changing to "read and write" permissions in Settings → Actions → General
- Learning: Security permissions must be explicitly granted
