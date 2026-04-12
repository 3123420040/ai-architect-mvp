# CP2 — Data Model + Auth + Permissions

**Code:** cp2-data-auth-permissions
**Order:** 2
**Depends On:** cp1-backend-bootstrap
**Estimated Effort:** 1 ngay

## Muc tieu

Hoan tat migration nen, core tables, auth flow, role permissions, version state machine va audit trail theo `implementation/07-database-schema.md` va `implementation/04-implementation-directives.md`.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/alembic/versions/*_initial_core.py` | created | Migration cho org/user/project/version/audit |
| `../ai-architect-api/app/models/` | created | SQLAlchemy models core |
| `../ai-architect-api/app/api/v1/auth.py` | created | Register/login/refresh |
| `../ai-architect-api/app/permissions/roles.py` | created | Role matrix va permission checks |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | `alembic upgrade head` chay duoc va tao core schema | ✓ |
| CHECK-02 | Integration test cho auth flow pass | ✓ |
| CHECK-03 | Unit tests cho state machine, permissions va audit trail pass | ✓ |
