# Failure Analysis

## Failure 1: Broken Test

**Evidence:** See `evidence/14-failure-broken-test.png`

Changed test assertion from 'healthy' to 'wrong' to demonstrate CI catches failures.

- **Error:** AssertionError - expected 'healthy', got 'wrong'
- **Fix:** Reverted assertion to 'healthy'
- **Result:** All 4 tests passed ✓
- **Learning:** CI/CD catches bugs automatically

---

## Failure 2: Empty Dockerfile

**Evidence:** See `evidence/15-failure-empty-dockerfile.png`

Dockerfile was created but not populated with content.

- **Error:** "failed to build: the Dockerfile cannot be empty"
- **Fix:** Wrote complete Dockerfile with all layers
- **Result:** Docker build succeeded ✓
- **Learning:** Configuration errors caught by CI

---

## Failure 3: GHCR Permission Denied

**Evidence:** See `evidence/16-failure-ghcr-permission.png`

GitHub Actions token had "read-only" permissions, couldn't push to registry.

- **Error:** "denied: installation not allowed to create organization package"
- **Root Cause:** Token permissions were insufficient
- **Fix:** Changed Settings → Actions → General to "Read and write permissions"
- **Result:** Docker image pushed successfully to GHCR ✓
- **Learning:** Security permissions must be explicitly granted

---

## Summary

| Failure | Caught By | Fixed | Time |
|---------|-----------|-------|------|
| Broken Test | CI Pipeline | Yes | 2 min |
| Empty Dockerfile | CI Pipeline | Yes | 5 min |
| GHCR Permission | Manual | Yes | 3 min |

**Key Learning:** Automated testing and CI/CD catch errors early!
