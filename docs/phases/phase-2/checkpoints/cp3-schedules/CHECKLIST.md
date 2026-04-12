# CP3 Validation Checklist — Schedules

**Dành cho:** Validator Agent  
**Mục tiêu:** Verify schedule data va exports duoc generate dung.

## Danh sách kiểm tra

### CHECK-01: CSV exports exist

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && pytest -q
```

**Expected:** test suite pass  
**Fail if:** schedule export tests fail

### CHECK-02: Schedule helpers return all 3 tables

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_schedule_csvs
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
payload = build_schedule_csvs(geom)
assert set(payload) == {"door", "window", "room"}
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** thieu CSV schedule

### CHECK-03: Room schedule has totals

```bash
cd /Users/nguyenquocthong/project/ai-architect-api && python3 - <<'PY'
from app.services.geometry import build_geometry_v2
from app.services.exporter import build_schedule_rows
geom = build_geometry_v2({"lot": {"width_m": 5, "depth_m": 20}, "floors": 4}, option_index=0)
rows = build_schedule_rows(geom)["room"]
assert any(row.get("row_type") == "level_total" for row in rows)
assert any(row.get("row_type") == "building_total" for row in rows)
print("ok")
PY
```

**Expected:** in `ok`  
**Fail if:** khong co subtotal / total

