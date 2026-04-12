# CP2 — Data Model + Auth + Permissions

**Muc tieu:** Dung xong core data model va business guardrails cho backend
**Requires:** CP1 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-data-auth-permissions/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP2 — Data Model + Auth + Permissions",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Implement schema va models

Can cu:

- `implementation/07-database-schema.md` muc `2.1` -> `2.11`
- `implementation/04-implementation-directives.md` muc `3.2`, `3.3`, `3.4`, `3.7`

Tao:

- Alembic migration core
- Models: `Organization`, `User`, `Project`, `DesignVersion`, `AuditLog`
- Enum cho `VersionStatus`, khong dung string tu do

## Buoc 2 — Auth va permission

Implement:

- `POST /auth/register`
- `POST /auth/login`
- `POST /auth/refresh`
- `ROLE_PERMISSIONS`
- `transition_version(...)` + audit log bat buoc

```bash
cd ../ai-architect-api
alembic upgrade head
pytest tests/integration/test_auth.py -q
pytest tests/unit/test_state_machine.py tests/unit/test_permissions.py tests/unit/test_audit.py -q
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp2-data-auth-permissions/result.json`.

```json
{
  "cp": "cp2-data-auth-permissions",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Core schema, auth flow, permissions, state machine va audit trail da xong.",
  "artifacts": [
    {"file": "../ai-architect-api/alembic/versions", "action": "updated"},
    {"file": "../ai-architect-api/app/models", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1/auth.py", "action": "created"},
    {"file": "../ai-architect-api/app/permissions/roles.py", "action": "created"}
  ],
  "issues": [],
  "notes": "Neu co seed data, chi can them sau khi tests on dinh."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp2-data-auth-permissions \
  --role implementer \
  --status READY \
  --summary "Schema core, auth, permissions va state machine da san sang." \
  --result-file docs/phases/phase-1/checkpoints/cp2-data-auth-permissions/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp2-data-auth-permissions/result.json
```
