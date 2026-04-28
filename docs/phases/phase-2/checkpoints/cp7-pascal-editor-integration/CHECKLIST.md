# CP7 Validation Checklist — Pascal Editor Integration

**Danh cho:** Validator Agent
**Doc truoc:** `docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/result.json`
**Muc tieu:** Xac nhan Pascal editor da tich hop lam viewer + edit surface, khong regression viewer cu, round-trip geometry on.

---

## Buoc 0 — Bao bat dau

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7-pascal-editor-integration/status" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "validator",
    "status": "VALIDATING",
    "summary": "Bat dau validate CP7 Pascal editor integration",
    "readyForNextTrigger": false
  }' || true
```

---

## CHECK-01: Package build va typecheck

```bash
cd ../ai-architect-web
pnpm install
pnpm build
pnpm tsc --noEmit
```

**Expected:** Build thanh cong, khong tsc error tu `packages/pascal-editor` hoac `src/lib/pascal/*`.
**Fail if:** Bat ky build/type error nao.

---

## CHECK-02: Geometry adapter round-trip

```bash
cd ../ai-architect-web
pnpm test src/lib/pascal/geometry-adapter.test.ts
```

**Expected:**

- 3 fixture (simple/medium/complex) deep-equal sau round-trip tren canonical keys: `levels`, `walls`, `openings`, `rooms`, `slabs`, `items`.
- Field Pascal khong ho tro (grids, dimensions) duoc preserve qua `geometry_v2_extra`.

**Fail if:** Mat thong tin geometry, diff khong rong ngoai metadata cho phep.

---

## CHECK-03: Pascal viewer E2E

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_VIEWER=true pnpm exec playwright test e2e/pascal-viewer.spec.ts
```

**Expected:**

- Viewer page load scene cua version that.
- Orbit + zoom + level toggle (stacked/exploded/solo) khong crash.
- Console khong co error WebGPU fatal.

**Fail if:** Viewer trang, scene empty, hoac console error blocking.

---

## CHECK-04: KTS edit → revision bypass GPU

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_EDIT=true pnpm exec playwright test e2e/pascal-edit.spec.ts

cd ../ai-architect-api
pytest tests/integration/test_revise_from_scene.py -q
```

**Expected:**

- E2E: user di chuyen 1 wall, bam save → version moi xuat hien trong lineage, parent dung.
- Backend test: `POST /versions/{id}/revise-from-scene` tao version moi voi `generation_source = "pascal_edit"`, KHONG goi GPU pipeline (assert mock GPU not called).
- Version moi validate duoc qua canonical Layer 2 validator.

**Fail if:** GPU bi goi, validation fail, hoac lineage sai.

---

## CHECK-05: Fallback khi flag off (no regression CP12)

```bash
cd ../ai-architect-web
NEXT_PUBLIC_FF_PASCAL_VIEWER=false NEXT_PUBLIC_FF_PASCAL_EDIT=false pnpm exec playwright test e2e/viewer-3d.spec.ts
```

**Expected:** Viewer three.js GLTF cu van hoat dong nhu CP12.
**Fail if:** Bat ky regression nao so voi CP12 baseline.

---

## CHECK-06 (warning): License compliance

```bash
test -f ../ai-architect-web/packages/pascal-editor/LICENSE
grep -q "pascal" ../ai-architect-web/NOTICE 2>/dev/null || echo "NOTICE missing entry"
```

**Expected:** File `LICENSE` tu upstream ton tai, `NOTICE` cap nhat attribution.
**Warning if:** Thieu (khong block PASS nhung phai log).

---

## Ghi ket qua

**Blocker checks:** `CHECK-01`, `CHECK-02`, `CHECK-03`, `CHECK-04`, `CHECK-05`
**Warning checks:** `CHECK-06`

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7-pascal-editor-integration \
  --role validator \
  --status PASS \
  --summary "Pascal integration hop le, san sang rollout sau staging soak" \
  --result-file docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/validation.json

python3 docs/phases/phase-2/checkpoints/post-status.py \
  --result-file docs/phases/phase-2/checkpoints/cp7-pascal-editor-integration/validation.json
```
