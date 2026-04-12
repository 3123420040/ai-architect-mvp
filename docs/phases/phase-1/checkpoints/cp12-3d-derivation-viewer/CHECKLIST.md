# CP12 Validation Checklist — 3D Derivation + Viewer

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-1/checkpoints/cp12-3d-derivation-viewer/result.json`
**Muc tieu:** Xac nhan lop 3D duoc derive tu locked version va viewer co the su dung

---

## Buoc 0 — Bao bat dau validate

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp12-3d-derivation-viewer/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP12 — 3D Derivation + Viewer",
    "readyForNextTrigger": false
  }' || true
```

## Danh sach kiem tra

### CHECK-01: Derivation chi cho phep tren locked version va integration tests pass

```bash
cd ../ai-architect-api && pytest tests/integration/test_derive_3d_api.py -q
```

**Expected:** Tat ca test pass; version chua lock bi `409`
**Fail if:** Derive duoc tu version khong hop le

---

### CHECK-02: GPU smoke test tao duoc model_url/render_urls

```bash
cd ../ai-architect-gpu && python -m pytest tests/test_blender_pipeline.py tests/test_render_outputs.py -q
```

**Expected:** Tat ca test pass
**Fail if:** Khong tao duoc output assets

---

### CHECK-03: Viewer page load duoc GLTF khi feature flag bat

```bash
cd ../ai-architect-web && NEXT_PUBLIC_FF_VIEWER_3D=true pnpm exec playwright test e2e/viewer-3d.spec.ts
```

**Expected:** Viewer load model, orbit/zoom co the thao tac
**Fail if:** Viewer khong load duoc model

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`
**Warning checks:** none

```bash
uv run python docs/phases/phase-1/checkpoints/notify.py \
  --cp cp12-3d-derivation-viewer \
  --role validator \
  --status PASS \
  --summary "3D derivation va viewer hop le, co the sang CP13." \
  --result-file docs/phases/phase-1/checkpoints/cp12-3d-derivation-viewer/validation.json

python3 docs/phases/phase-1/checkpoints/post-status.py \
  --result-file docs/phases/phase-1/checkpoints/cp12-3d-derivation-viewer/validation.json
```
