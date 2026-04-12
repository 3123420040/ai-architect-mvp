# CP0 — Environment Setup

**Muc tieu:** Tao mat bang workspace va local setup thong nhat cho 3 repos
**Requires:** Khong

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-environment-setup/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "implementer",
    "status": "IN_PROGRESS",
    "summary": "Bat dau implement CP0 — Environment Setup",
    "readyForNextTrigger": false
  }' || true
```

## Buoc 1 — Chot workspace va dependency local

- Clone hoac tao 3 repos song song voi repo docs nay:
  - `../ai-architect-web`
  - `../ai-architect-api`
  - `../ai-architect-gpu`
- Ap dung phan `implementation/08-deployment-guide.md` muc `2.1` va `2.5`
- Tao `.env.example` cho tung repo theo muc `3.1`, `3.2`, `3.3`

```bash
test -d ../ai-architect-web
test -d ../ai-architect-api
test -d ../ai-architect-gpu
```

## Buoc 2 — Tao local compose va script can thiet

- Dat `docker-compose.yml` trong `../ai-architect-api`
- Dam bao file compose co `postgres`, `redis`, `minio`
- Kiem tra parse thanh cong

```bash
docker compose -f ../ai-architect-api/docker-compose.yml config >/dev/null
```

## Buoc 3 — Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp0-environment-setup/result.json`:

```json
{
  "cp": "cp0-environment-setup",
  "role": "implementer",
  "status": "READY",
  "timestamp": "<ISO8601>",
  "summary": "Workspace 3 repos, env templates va local compose da san sang.",
  "artifacts": [
    {"file": "../ai-architect-api/.env.example", "action": "created"},
    {"file": "../ai-architect-web/.env.example", "action": "created"},
    {"file": "../ai-architect-gpu/.env.example", "action": "created"},
    {"file": "../ai-architect-api/docker-compose.yml", "action": "created"}
  ],
  "issues": [],
  "notes": "Neu chua co GPU local, chi can chot env va service skeleton."
}
```

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp0-environment-setup \
  --role implementer \
  --status READY \
  --summary "Workspace va local dev dependencies da san sang." \
  --result-file docs/phases/phase-1/checkpoints/cp0-environment-setup/result.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp0-environment-setup/result.json
```
