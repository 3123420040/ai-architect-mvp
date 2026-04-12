# CP1 Validation Checklist — Backend Bootstrap

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/result.json`
**Muc tieu:** Xac nhan FastAPI skeleton boot duoc va cac thanh phan nen import on dinh

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-backend-bootstrap/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP1 — Backend Bootstrap",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Backend boot duoc va `/health` tra `200`

```bash
curl -fsS http://localhost:8000/health
```

**Expected:** JSON health response
**Fail if:** HTTP khac `200` hoac connection fail

---

### CHECK-02: `/api/v1/openapi.json` truy cap duoc

```bash
curl -fsS http://localhost:8000/api/v1/openapi.json | jq '.openapi'
```

**Expected:** In ra version OpenAPI
**Fail if:** Endpoint khong ton tai hoac JSON loi

---

### CHECK-03: Celery app va service wrappers import duoc khong loi

```bash
cd ../ai-architect-api && \
python -c "from app.tasks.base import celery_app; from app.services.file_storage import FileStorageService"
```

**Expected:** Lenh exit `0`
**Fail if:** Import error

## Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/validation.json`.

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp1-backend-bootstrap \
  --role validator \
  --status PASS \
  --summary "Backend bootstrap hop le, co the sang CP2." \
  --result-file docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/validation.json
```
