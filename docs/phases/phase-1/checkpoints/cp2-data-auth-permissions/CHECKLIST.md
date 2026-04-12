# CP2 Validation Checklist — Data Model + Auth + Permissions

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp2-data-auth-permissions/result.json`
**Muc tieu:** Xac nhan schema core, auth flow va business guards da dung

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp2-data-auth-permissions/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP2 — Data Model + Auth + Permissions",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: `alembic upgrade head` chay duoc va tao core schema

```bash
cd ../ai-architect-api && alembic upgrade head
```

**Expected:** Lenh exit `0`
**Fail if:** Migration fail hoac schema conflict

---

### CHECK-02: Integration test cho auth flow pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_auth.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Co test fail hoac thieu endpoint

---

### CHECK-03: Unit tests cho state machine, permissions va audit trail pass

```bash
cd ../ai-architect-api && \
pytest tests/unit/test_state_machine.py tests/unit/test_permissions.py tests/unit/test_audit.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Co bat ky test fail nao

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp2-data-auth-permissions \
  --role validator \
  --status PASS \
  --summary "Schema va guardrails core hop le, co the sang CP3." \
  --result-file docs/phases/phase-1/checkpoints/cp2-data-auth-permissions/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp2-data-auth-permissions/validation.json
```
