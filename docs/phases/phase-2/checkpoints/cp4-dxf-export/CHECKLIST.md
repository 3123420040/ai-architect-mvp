# CP4 Validation Checklist — DXF Export

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify DXF package ton tai va co sheet/layout structure dung.

## Danh sách kiểm tra

### CHECK-01: DXF export test passes

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && pytest -q
```

**Expected:** test suite pass  
**Fail if:** DXF export tests fail

### CHECK-02: DXF bytes are produced

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_dxf_bytes
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
payload = build_dxf_bytes("Demo", 2, geom)
assert payload[:4] == b'  0\\n' or payload.startswith(b'999') or len(payload) > 1000
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** DXF bytes empty

### CHECK-03: Export manifest references DXF

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_sheet_bundle
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
bundle = build_sheet_bundle("Demo", 2, geom)
assert "dxf" in bundle["top_level_exports"]
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** DXF khong duoc expose trong export bundle

