# CP7.B — Instructions

## Buoc 0 — Notify

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7b-geometry-adapter/status" \
  -H "Content-Type: application/json" \
  -d '{"role":"implementer","status":"IN_PROGRESS","summary":"CP7.B start","readyForNextTrigger":false}' || true
```

## Buoc 1 — Import canonical schema

Lay Layer 2 types tu OpenAPI generated:

```bash
cd ../ai-architect-web
pnpm generate:api-types
```

Confirm `GeometryV2` type available. Khong redeclare shape — nhap truc tiep tu types generated.

## Buoc 2 — Design mapping

Tao `docs/phase-1/24-pascal-integration-design.md`:

- Copy mapping table tu `README.md` CP7.B.
- Them rule chi tiet:
  - Wall mitering: tu `walls[].joins[]` hoac infer tu adjacency (document cach infer).
  - Openings: `opening.wall_id` → tim wall, tao cutout tai offset `opening.position`.
  - Units: Layer 2 o met, Pascal cung co nen o met → khong conversion.
  - Coordinate system: confirm Y-up vs Z-up, ghi ro.
- Metadata preservation: Pascal scene carry truong `geometry_v2_extra: unknown` o root; adapter pass-through.

## Buoc 3 — Implement adapter

`src/lib/pascal/geometry-adapter.ts`:

```ts
import type { GeometryV2 } from "@/types/api";

export interface PascalScene {
  version: "pascal-scene-v1";
  levels: PascalLevel[];
  geometry_v2_extra: unknown;
}

export function geometryJsonToPascalScene(g: GeometryV2): PascalScene { /* ... */ }
export function pascalSceneToGeometryJson(s: PascalScene): GeometryV2 { /* ... */ }
```

Nguyen tac:

- Pure function, khong I/O.
- Deterministic ordering (sort by id) de deep-equal on dinh.
- Throw `AdapterError` neu shape invalid; khong silent drop.

## Buoc 4 — Fixtures

Tao 3 fixture json tai `src/lib/pascal/fixtures/`:

- `geometry-simple.json`: 1 level, 4 walls (hinh chu nhat), 1 room.
- `geometry-medium.json`: 2 levels, 12 walls (2 tang hinh chu L), 4 rooms, 2 door + 1 window, 2 slab.
- `geometry-complex.json`: 3 levels, wall mitering (tuong xien), 1 nested room (phong trong phong), 4 openings, furniture.

Nen lay fixture tu 1 project that tren staging qua `GET /api/v1/projects/{id}/geometry?version=latest` va redact.

## Buoc 5 — Round-trip tests

`src/lib/pascal/geometry-adapter.test.ts`:

```ts
import { test, expect } from "vitest";
import simple from "./fixtures/geometry-simple.json";
import medium from "./fixtures/geometry-medium.json";
import complex from "./fixtures/geometry-complex.json";
import { geometryJsonToPascalScene, pascalSceneToGeometryJson } from "./geometry-adapter";

const canonicalKeys = ["levels","walls","openings","rooms","slabs","items"] as const;

function canonicalize(g: any) {
  return canonicalKeys.reduce((acc, k) => ({ ...acc, [k]: g[k] ?? [] }), {});
}

for (const [name, g] of [["simple",simple],["medium",medium],["complex",complex]] as const) {
  test(`round-trip ${name}`, () => {
    const scene = geometryJsonToPascalScene(g as any);
    const roundtrip = pascalSceneToGeometryJson(scene);
    expect(canonicalize(roundtrip)).toEqual(canonicalize(g));
  });
}
```

Run:

```bash
pnpm test src/lib/pascal/geometry-adapter.test.ts
```

Fix cho den khi het 3 test PASS.

## Buoc 6 — Result

`result.json`:

```json
{
  "cp": "cp7b-geometry-adapter",
  "role": "implementer",
  "status": "READY",
  "summary": "Adapter round-trip PASS tren 3 fixtures, design doc approved",
  "artifacts": [
    {"file":"../ai-architect-web/src/lib/pascal/geometry-adapter.ts","action":"created"},
    {"file":"../ai-architect-web/src/lib/pascal/geometry-adapter.test.ts","action":"created"},
    {"file":"docs/phase-1/24-pascal-integration-design.md","action":"created"}
  ]
}
```

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7b-geometry-adapter --role implementer --status READY \
  --summary "Adapter done" \
  --result-file docs/phases/phase-2/checkpoints/cp7b-geometry-adapter/result.json
```
