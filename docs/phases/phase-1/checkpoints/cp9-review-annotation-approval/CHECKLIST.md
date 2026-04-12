# CP9 Validation Checklist — Review + Annotation + Approval

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp9-review-annotation-approval/result.json`
**Muc tieu:** Xac nhan review workspace va lock flow cho KTS da dung

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp9-review-annotation-approval/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP9 — Review + Annotation + Approval",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Integration tests cho annotation CRUD va review endpoints pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_review_flow.py tests/integration/test_annotations_api.py -q
```

**Expected:** Tat ca test pass
**Fail if:** CRUD annotations hoac review endpoints sai contract

---

### CHECK-02: Review E2E `annotate -> approve -> locked` pass

```bash
cd ../ai-architect-web && pnpm exec playwright test e2e/review-flow.spec.ts
```

**Expected:** Sau approve status thanh `Locked`
**Fail if:** Annotation khong luu hoac version khong lock

---

### CHECK-03: Audit log duoc tao cho moi action review quan trong

```bash
cd ../ai-architect-api && pytest tests/unit/test_audit.py tests/integration/test_audit_review_events.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Thieu audit log cho approve/reject/annotate

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp9-review-annotation-approval \
  --role validator \
  --status PASS \
  --summary "Review va approval flow hop le, co the sang CP10." \
  --result-file docs/phases/phase-1/checkpoints/cp9-review-annotation-approval/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp9-review-annotation-approval/validation.json
```
