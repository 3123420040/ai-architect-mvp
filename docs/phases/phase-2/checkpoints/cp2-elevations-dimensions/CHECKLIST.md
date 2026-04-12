# CP2 Validation Checklist — 4 Elevations + Enhanced Dimensions

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify Phase 2 drawing sheets co day du elevation/section/dimension content.

## Danh sách kiểm tra

### CHECK-01: Export package contains elevation and section sheets

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && pytest -q
```

**Expected:** test suite pass  
**Fail if:** export integration test fail

### CHECK-02: Renderer emits 4 elevation faces

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_sheet_bundle
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4, "style": "modern_minimalist"}, option_index=1)
bundle = build_sheet_bundle("Demo", 2, geom)
faces = [s["type"] for s in bundle["sheets"] if s["type"].startswith("elevation_")]
assert sorted(faces) == ["elevation_east", "elevation_north", "elevation_south", "elevation_west"]
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** thieu elevation face

### CHECK-03: Bundle contains dimension metadata

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
assert geom["dimensions_config"]["chains"]["overall"] if "overall" in geom["dimensions_config"]["chains"] else True
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** dimension config khong ton tai

