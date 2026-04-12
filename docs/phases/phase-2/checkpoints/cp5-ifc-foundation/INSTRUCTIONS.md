# CP5 — IFC Foundation

**Mục tiêu:** Them BIM-oriented foundation export ma khong tach khoi canonical geometry.  
**Requires:** `cp4-dxf-export` PASS.

## Bước 1 — Define IFC scope

Phase 2 IFC scope is foundation-only:

- project hierarchy,
- storeys,
- walls,
- openings,
- spaces,
- basic metadata.

## Bước 2 — Export and manifest

Generate `.ifc` output and add it to top-level exports plus handoff bundle manifest.

## Bước 3 — Keep graceful fallback

If a richer IFC library is unavailable, the exporter must still produce a deterministic, documented IFC foundation artifact instead of crashing the export lane.

