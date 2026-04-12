# CP13 Validation Checklist — Hardening + Staging + Launch

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp13-hardening-staging-launch/result.json`
**Muc tieu:** Xac nhan MVP co the demo tren staging va dat quality gate truoc launch

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp13-hardening-staging-launch/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP13 — Hardening + Staging + Launch",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Full test suite va CI gate pass

```bash
cd ../ai-architect-api && pytest tests/ -q --cov=app && \
test -f .github/workflows/ci.yml && test -f .github/workflows/deploy.yml
```

**Expected:** Full suite pass va workflows ton tai
**Fail if:** Test fail hoac thieu CI/CD files

---

### CHECK-02: Staging environment, monitoring va health checks san sang

```bash
curl -fsS https://api-staging.aiarchitect.vn/health
```

**Expected:** Health endpoint tra `200`
**Fail if:** Staging chua song hoac health fail

---

### CHECK-03: Launch checklist security/performance/backup duoc danh dau dat

```bash
test -f ../ai-architect-api/docs/launch-checklist.md && \
! rg -n '\\[ \\]' ../ai-architect-api/docs/launch-checklist.md
```

**Expected:** Launch checklist file ton tai va khong con muc `[ ]`
**Fail if:** Chua tao runbook hoac con launch blocker mo

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp13-hardening-staging-launch \
  --role validator \
  --status PASS \
  --summary "Launch gates da dat, phase 1 co the close." \
  --result-file docs/phases/phase-1/checkpoints/cp13-hardening-staging-launch/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp13-hardening-staging-launch/validation.json
```
