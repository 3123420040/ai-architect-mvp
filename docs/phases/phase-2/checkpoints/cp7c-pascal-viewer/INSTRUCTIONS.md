# CP7.C — Instructions

## Buoc 0 — Notify

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7c-pascal-viewer/status" \
  -H "Content-Type: application/json" \
  -d '{"role":"implementer","status":"IN_PROGRESS","summary":"CP7.C start","readyForNextTrigger":false}' || true
```

## Buoc 1 — `PascalViewer` component

`src/components/viewer/pascal-viewer.tsx`:

```tsx
"use client";
import dynamic from "next/dynamic";
import { geometryJsonToPascalScene } from "@/lib/pascal/geometry-adapter";
import type { VersionDetail } from "@/types/api";

const PascalRuntime = dynamic(
  () => import("pascal-editor").then((m) => m.ReadonlyViewer),
  { ssr: false, loading: () => <ViewerSkeleton /> }
);

export function PascalViewer({ version }: { version: VersionDetail }) {
  if (!version.geometry_json) return <ViewerEmpty />;
  const scene = geometryJsonToPascalScene(version.geometry_json);
  return <PascalRuntime scene={scene} toolbar={{ levelMode: true, zones: true }} />;
}
```

Browser detect helper:

```ts
export function supportsWebGPU(): boolean {
  return typeof navigator !== "undefined" && "gpu" in navigator;
}
```

## Buoc 2 — Flag branch trong viewer-client

Sua block tai [viewer-client.tsx:416-443](../../../../../ai-architect-web/src/components/viewer-client.tsx):

```tsx
{sceneGlb ? (
  process.env.NEXT_PUBLIC_FF_PASCAL_VIEWER === "true" && supportsWebGPU()
    ? <PascalViewer version={selectedVersion} />
    : modelViewer
) : (
  <EmptyState />
)}
```

Giu `modelViewer` variable va `<model-viewer>` logic nguyen. Chi them branch.

## Buoc 3 — Toolbar

Trong `PascalViewer`, wire toolbar Pascal exposed (level stacked/exploded/solo, zones on/off, items on/off). Pascal co san qua zustand store — connect vao UI button.

## Buoc 4 — E2E test

`e2e/pascal-viewer.spec.ts`:

```ts
import { test, expect } from "@playwright/test";

test("pascal viewer orbit + level toggle", async ({ page }) => {
  await page.goto("/projects/demo/viewer?ff_pascal_viewer=1");
  await expect(page.locator("canvas")).toBeVisible();
  await page.getByRole("button", { name: /exploded/i }).click();
  // assert change (snapshot or zustand state via window.__pascal)
});
```

Update `e2e/viewer-3d.spec.ts`: test CP12 baseline flag off.

## Buoc 5 — Bundle check

```bash
cd ../ai-architect-web && pnpm build
# So sanh .next/analyze route /projects/[id]/viewer voi budget tu spike
```

Neu vuot: ap dung them route-level splitting hoac defer load zustand.

## Buoc 6 — Fallback WebGPU

Trong `viewer-client.tsx`:

```tsx
const useFallback = !supportsWebGPU();
// branch cho fallback irrespective of flag
```

Log event `pascal.webgpu.fallback` vao analytics.

## Buoc 7 — Result + notify

```json
{
  "cp":"cp7c-pascal-viewer",
  "role":"implementer",
  "status":"READY",
  "summary":"Pascal viewer active behind flag, fallback chain on",
  "artifacts":[
    {"file":"../ai-architect-web/src/components/viewer/pascal-viewer.tsx","action":"created"},
    {"file":"../ai-architect-web/src/components/viewer-client.tsx","action":"updated"},
    {"file":"../ai-architect-web/e2e/pascal-viewer.spec.ts","action":"created"}
  ]
}
```

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7c-pascal-viewer --role implementer --status READY \
  --summary "Viewer done" \
  --result-file docs/phases/phase-2/checkpoints/cp7c-pascal-viewer/result.json
```
