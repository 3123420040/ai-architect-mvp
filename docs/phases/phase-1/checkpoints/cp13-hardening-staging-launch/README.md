# CP13 — Hardening + Staging + Launch

**Code:** cp13-hardening-staging-launch
**Order:** 13
**Depends On:** cp12-3d-derivation-viewer
**Estimated Effort:** 1 ngay

## Muc tieu

Dong full quality gate: CI/CD, staging, monitoring, backups, security/performance checklist va launch readiness cho Phase 1 MVP.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/.github/workflows/ci.yml` | created | CI pipeline |
| `../ai-architect-api/.github/workflows/deploy.yml` | created | Backend deploy pipeline |
| `../ai-architect-web/e2e/` | updated | E2E regression suite |
| `../ai-architect-api/scripts/backup.sh` | created | Backup automation hook |
| `../ai-architect-api/docs/launch-checklist.md` | created | Launch runbook da duoc danh dau |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Full test suite va CI gate pass | ✓ |
| CHECK-02 | Staging environment, monitoring va health checks san sang | ✓ |
| CHECK-03 | Launch checklist security/performance/backup duoc danh dau dat | ✓ |
