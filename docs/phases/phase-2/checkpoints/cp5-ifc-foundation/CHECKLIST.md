# CP5 Validation Checklist — IFC Foundation

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify IFC foundation artifact ton tai va duoc bind vao package.

## Danh sách kiểm tra

### CHECK-01: IFC export path passes tests

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && pytest -q
```

**Expected:** test suite pass  
**Fail if:** IFC export tests fail

### CHECK-02: IFC bytes are produced

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_ifc_bytes
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
payload = build_ifc_bytes("Demo", 2, geom)
assert payload.startswith(b"ISO-10303-21;")
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** IFC bytes empty hoac sai header

### CHECK-03: Export bundle exposes IFC

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_sheet_bundle
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
bundle = build_sheet_bundle("Demo", 2, geom)
assert "ifc" in bundle["top_level_exports"]
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** IFC khong duoc expose

