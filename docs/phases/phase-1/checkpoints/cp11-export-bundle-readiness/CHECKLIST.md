# CP11 Validation Checklist — Export + Bundle + Readiness

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp11-export-bundle-readiness/result.json`
**Muc tieu:** Xac nhan lop export va delivery co the chay duoc tren locked version

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp11-export-bundle-readiness/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP11 — Export + Bundle + Readiness",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Integration tests cho export API va file manifest pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_exports_api.py tests/integration/test_export_files_manifest.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Export API sai contract hoac manifest thieu file

---

### CHECK-02: Handoff readiness checks block dung cac version chua du dieu kien

```bash
cd ../ai-architect-api && pytest tests/unit/test_handoff_readiness.py tests/integration/test_handoff_api.py -q
```

**Expected:** Version khong dat readiness bi chan dung
**Fail if:** Handoff duoc tao khi version chua lock/chua approved/chua co export

---

### CHECK-03: PDF/SVG export va handoff bundle smoke test pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_export_pipeline_smoke.py -q
```

**Expected:** Tao duoc PDF/SVG va bundle
**Fail if:** Job fail hoac file output sai

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp11-export-bundle-readiness \
  --role validator \
  --status PASS \
  --summary "Export va handoff readiness hop le, co the sang CP12." \
  --result-file docs/phases/phase-1/checkpoints/cp11-export-bundle-readiness/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp11-export-bundle-readiness/validation.json
```
