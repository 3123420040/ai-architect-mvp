# CP1 — Backend Bootstrap

**Code:** cp1-backend-bootstrap
**Order:** 1
**Depends On:** cp0-environment-setup
**Estimated Effort:** 0.5-1 ngay

## Muc tieu

Dung skeleton FastAPI theo `implementation/03-architecture-blueprint.md`, expose duoc `/health` va `/api/v1/openapi.json`, dong thoi co Celery va service wrappers o muc importable.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/app/main.py` | created | FastAPI app entry |
| `../ai-architect-api/app/api/v1/` | created | Router layer v1 |
| `../ai-architect-api/app/tasks/` | created | Celery app va task base |
| `../ai-architect-api/app/services/file_storage.py` | created | S3/MinIO wrapper skeleton |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Backend boot duoc va `/health` tra `200` | ✓ |
| CHECK-02 | `/api/v1/openapi.json` truy cap duoc | ✓ |
| CHECK-03 | Celery app va service wrappers import duoc khong loi | ✓ |
