# CP0 — Environment Setup

**Code:** cp0-environment-setup
**Order:** 0
**Depends On:** —
**Estimated Effort:** 0.5 ngay

## Muc tieu

Chot workspace layout, env templates, local dependencies va shared checkpoint scripts de tat ca team co the bat dau dev ma khong block nhau.

## Artifacts du kien

| File/Path | Action | Mo ta |
|-----------|--------|-------|
| `../ai-architect-api/.env.example` | created | Env template cho backend |
| `../ai-architect-web/.env.example` | created | Env template cho frontend |
| `../ai-architect-gpu/.env.example` | created | Env template cho GPU service |
| `../ai-architect-api/docker-compose.yml` | created | Postgres + Redis + MinIO cho local dev |

## Checklist Validator

| ID | Mo ta | Blocker |
|----|-------|---------|
| CHECK-01 | Ba repo muc tieu ton tai dung ten va co README/co cau truc toi thieu | ✓ |
| CHECK-02 | `docker-compose.yml` cua backend parse duoc va khai bao Postgres, Redis, MinIO | ✓ |
| CHECK-03 | Ca 3 repo deu co `.env.example` khop implementation package | ✓ |
