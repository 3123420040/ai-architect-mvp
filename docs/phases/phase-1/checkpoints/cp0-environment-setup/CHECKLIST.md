# CP0 Validation Checklist — Environment Setup

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp0-environment-setup/result.json`
**Muc tieu:** Xac nhan workspace local co du 3 repos, compose va env templates

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp0-environment-setup/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP0 — Environment Setup",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Ba repo muc tieu ton tai dung ten va co cau truc toi thieu

```bash
test -d ../ai-architect-web && test -d ../ai-architect-api && test -d ../ai-architect-gpu
```

**Expected:** Lenh exit `0`
**Fail if:** Thieu bat ky repo nao

---

### CHECK-02: `docker-compose.yml` cua backend parse duoc va khai bao Postgres, Redis, MinIO

```bash
docker compose -f ../ai-architect-api/docker-compose.yml config | rg 'postgres|redis|minio'
```

**Expected:** Output co du `postgres`, `redis`, `minio`
**Fail if:** Parse loi hoac thieu service

---

### CHECK-03: Ca 3 repo deu co `.env.example` khop implementation package

```bash
test -f ../ai-architect-api/.env.example && \
test -f ../ai-architect-web/.env.example && \
test -f ../ai-architect-gpu/.env.example
```

**Expected:** Lenh exit `0`
**Fail if:** Thieu bat ky file env nao

## Ghi ket qua

Tao `docs/phases/phase-1/checkpoints/cp0-environment-setup/validation.json`:

```json
{
  "cp": "cp0-environment-setup",
  "role": "validator",
  "status": "PASS | FAIL | PARTIAL",
  "timestamp": "<ISO8601>",
  "summary": "<1-2 cau>",
  "checks": [],
  "issues": [],
  "ready_for_next_cp": true,
  "next_cp": "cp1-backend-bootstrap"
}
```

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp0-environment-setup \
  --role validator \
  --status PASS \
  --summary "Environment setup hop le, co the sang CP1." \
  --result-file docs/phases/phase-1/checkpoints/cp0-environment-setup/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp0-environment-setup/validation.json
```
