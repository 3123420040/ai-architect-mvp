# CP10 Validation Checklist — Share Link + Feedback + Revision

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp10-share-feedback-revision/result.json`
**Muc tieu:** Xac nhan vong lap feedback -> revision giu dung lineage va quyen truy cap

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp10-share-feedback-revision/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP10 — Share Link + Feedback + Revision",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Share link va feedback integration tests pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_share_api.py tests/integration/test_feedback_api.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Token auth sai hoac feedback khong luu duoc

---

### CHECK-02: Revision flow tao version moi dung `parent_version_id`

```bash
cd ../ai-architect-api && pytest tests/integration/test_revision_flow.py -q
```

**Expected:** Version moi duoc tao, parent chain dung
**Fail if:** Mutate version cu hoac lineage sai

---

### CHECK-03: E2E flow `share -> feedback -> revise -> new version` pass

```bash
cd ../ai-architect-web && pnpm exec playwright test e2e/share-feedback-revision.spec.ts
```

**Expected:** End-to-end pass
**Fail if:** Biet dong khong thong suot

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp10-share-feedback-revision \
  --role validator \
  --status PASS \
  --summary "Share va revision flow hop le, co the sang CP11." \
  --result-file docs/phases/phase-1/checkpoints/cp10-share-feedback-revision/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp10-share-feedback-revision/validation.json
```
