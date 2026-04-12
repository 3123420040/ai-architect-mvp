# CP1 — Backend Bootstrap

**Muc tieu:** Khoi tao backend skeleton theo architecture blueprint
**Requires:** CP0 PASS

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp1-backend-bootstrap/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP1 — Backend Bootstrap",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Dung project skeleton

Can cu `implementation/03-architecture-blueprint.md` muc `5.3`, `9` va `implementation/02-tech-stack-decisions.md` muc `3`.

Tao toi thieu:

- `app/main.py`
- `app/api/v1/__init__.py`
- `app/core/config.py`
- `app/core/database.py`
- `app/tasks/base.py`
- `app/services/file_storage.py`

## Buoc 2 — Expose health va OpenAPI

```bash
cd ../ai-architect-api
python -m uvicorn app.main:app --reload --port 8000
curl -f http://localhost:8000/health
curl -f http://localhost:8000/api/v1/openapi.json
python -c "from app.tasks.base import celery_app; print(celery_app.main)"
python -c "from app.services.file_storage import FileStorageService; print(FileStorageService)"
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/result.json`:

```json
{
  "cp": "cp1-backend-bootstrap",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Backend skeleton, health, OpenAPI va Celery/file service wrappers da co.",
  "artifacts": [
    {"file": "../ai-architect-api/app/main.py", "action": "created"},
    {"file": "../ai-architect-api/app/api/v1", "action": "created"},
    {"file": "../ai-architect-api/app/tasks", "action": "created"},
    {"file": "../ai-architect-api/app/services/file_storage.py", "action": "created"}
  ],
  "issues": [],
  "notes": "Chua implement business logic o CP1."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp1-backend-bootstrap \
  --role implementer \
  --status READY \
  --summary "Backend skeleton va health routes da san sang." \
  --result-file docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp1-backend-bootstrap/result.json
```
