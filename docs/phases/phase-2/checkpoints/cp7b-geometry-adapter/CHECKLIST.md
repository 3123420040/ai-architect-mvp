# CP7.B — Validation Checklist

## CHECK-01: Round-trip tests PASS

```bash
cd ../ai-architect-web
pnpm test src/lib/pascal/geometry-adapter.test.ts --run
```

**Expected:** 3/3 test PASS (simple/medium/complex).
**Fail if:** Bat ky test fail.

## CHECK-02: Complex fixture bao toan hinh dang

Ngoai deep-equal, validator load fixture complex, chay adapter, kiem tra manual:

- So luong walls bang nhau.
- Mitering angles preserve (sample 2 wall join).
- Opening positions khong doi > 1e-6 m.

**Fail if:** Mat info hinh dang.

## CHECK-03: `geometry_v2_extra` preserved

Test them:

```ts
test("extra preserved", () => {
  const withGrids = { ...simple, grids: [{ id: "g1", spacing: 1000 }] };
  const scene = geometryJsonToPascalScene(withGrids as any);
  const back = pascalSceneToGeometryJson(scene);
  expect(back.grids).toEqual(withGrids.grids);
});
```

**Fail if:** Grids / dimensions / annotations mat sau round-trip.

## CHECK-04: Design doc approved

Kiem `docs/phase-1/24-pascal-integration-design.md` co mapping table + coordinate convention + units + error handling section.
**Expected:** Document day du, da co review comment approved.
**Fail if:** Thieu muc chinh.

## CHECK-05 (warning): Type source

Adapter `import type { GeometryV2 } from "@/types/api"` — khong duplicate manual shape.
**Warning if:** Manual shape redeclare (tech debt).

## Blocker

CHECK-01, CHECK-02, CHECK-03, CHECK-04 → all PASS → trigger CP7.C.
