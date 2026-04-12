# CP1 Validation Checklist — Geometry Layer 2

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify Layer 2 geometry contract ton tai va duoc persist dung cach.

## Danh sách kiểm tra

### CHECK-01: Tests cover Layer 2 geometry

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && pytest -q
```

**Expected:** test suite pass  
**Fail if:** co test fail lien quan generation/export flow

### CHECK-02: Generated versions include Layer 2 schema

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4, "style": "modern_minimalist"}, option_index=0)
assert geom["$schema"] == "ai-architect-geometry-v2"
for key in ("grids", "levels", "walls", "openings", "rooms"):
    assert key in geom and geom[key]
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** thieu key hoac schema sai

### CHECK-03: Geometry builder supports fallback

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import ensure_geometry_v2
geom = ensure_geometry_v2(None, {"lot": {"width_m": 5, "depth_m": 20}, "floors": 3, "style": "minimal"})
assert geom["version"] == "2.0"
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** brief-only fallback khong generate duoc geometry

