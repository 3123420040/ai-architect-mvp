# CP8 Validation Checklist — Generation Orchestration + Gallery Selection

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp8-generation-gallery-selection/result.json`
**Muc tieu:** Xac nhan full flow generation dau tien da thong suot

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp8-generation-gallery-selection/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP8 — Generation Orchestration + Gallery Selection",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Integration tests cho `POST /generate` va job tracking pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_generation_api.py tests/integration/test_generation_status.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Job khong tao, khong track duoc progress, hoac khong luu version

---

### CHECK-02: Full generation E2E `brief -> 3 options -> select` pass

```bash
cd ../ai-architect-web && pnpm exec playwright test e2e/generation-flow.spec.ts
```

**Expected:** Sinh duoc 3 option va select duoc 1 option
**Fail if:** Gallery khong hien, progress khong cap nhat, hoac selection fail

---

### CHECK-03: Generation progress va recovery UI hien dung state

```bash
cd ../ai-architect-web && pnpm test src/components/generation/__tests__/generation-progress.test.tsx
```

**Expected:** Progress/error/recovery states render dung
**Fail if:** State mapping sai

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp8-generation-gallery-selection \
  --role validator \
  --status PASS \
  --summary "Generation flow hop le, co the sang CP9." \
  --result-file docs/phases/phase-1/checkpoints/cp8-generation-gallery-selection/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp8-generation-gallery-selection/validation.json
```
