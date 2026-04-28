# CP7.D — Instructions

## Buoc 0 — Notify

```bash
curl -s -X POST "http://localhost:3000/api/projects/ai-architect-mvp/checkpoints/cp7d-pascal-edit-mode/status" \
  -H "Content-Type: application/json" \
  -d '{"role":"implementer","status":"IN_PROGRESS","summary":"CP7.D start","readyForNextTrigger":false}' || true
```

## Buoc 1 — Backend: migration + enum

`ai-architect-api/app/models/version.py`:

```python
class GenerationSource(str, Enum):
    AI_GENERATED = "ai_generated"
    MANUAL = "manual"
    PASCAL_EDIT = "pascal_edit"
```

Alembic:

```bash
cd ../ai-architect-api
alembic revision --autogenerate -m "add pascal_edit generation_source"
# edit migration: ALTER TYPE generationsource ADD VALUE 'pascal_edit';
alembic upgrade head
```

Test migration tren staging DB dump.

## Buoc 2 — Backend: endpoint

`ai-architect-api/app/api/v1/versions.py`:

```python
@router.post("/{version_id}/revise-from-scene", response_model=VersionDetail)
async def revise_from_scene(
    version_id: UUID,
    body: ReviseFromSceneRequest,
    db: Session = Depends(get_db),
    user: User = Depends(require_role("editor","kts")),
):
    parent = get_version_or_404(db, version_id)
    if parent.status not in {VersionStatus.UNDER_REVIEW, VersionStatus.GENERATED}:
        raise HTTPException(409, "parent not in reviewable state")
    geometry = body.geometry_json  # client-first adapter
    geometry_service.validate_layer2(geometry)  # raises 422
    new_version = version_service.create_revision(
        parent=parent,
        geometry_json=geometry,
        generation_source=GenerationSource.PASCAL_EDIT,
        note=body.note,
        model_url=None,
    )
    # NO celery dispatch
    emit_ws("version.created", new_version)
    return new_version
```

Schema:

```python
class ReviseFromSceneRequest(BaseModel):
    geometry_json: GeometryV2
    note: str | None = None
```

## Buoc 3 — Backend: integration tests

`ai-architect-api/tests/integration/test_revise_from_scene.py`:

```python
def test_revise_from_scene_no_gpu(client, db, mock_celery):
    parent = create_version(db, status="under_review", generation_source="ai_generated")
    resp = client.post(f"/api/v1/versions/{parent.id}/revise-from-scene",
                       json={"geometry_json": fixture_geometry_simple(), "note":"move wall"})
    assert resp.status_code == 200
    v = resp.json()
    assert v["parent_version_id"] == str(parent.id)
    assert v["generation_source"] == "pascal_edit"
    assert v["model_url"] is None
    mock_celery.assert_not_called()

def test_revise_from_scene_invalid(client, db):
    parent = create_version(db, status="under_review")
    resp = client.post(f"/api/v1/versions/{parent.id}/revise-from-scene",
                       json={"geometry_json": {"levels":[]}})  # missing walls, rooms
    assert resp.status_code == 422

def test_revise_from_scene_locked_parent(client, db):
    parent = create_version(db, status="locked")
    resp = client.post(...)
    assert resp.status_code == 409
```

Run:

```bash
cd ../ai-architect-api && pytest tests/integration/test_revise_from_scene.py -q
```

## Buoc 4 — Readiness rule update

CP11 readiness logic: version co `generation_source = pascal_edit` → bat buoc lock + `model_url != null` moi duoc vao export bundle. Test positive + negative.

## Buoc 5 — Frontend: edit surface

`src/components/review/pascal-edit-surface.tsx`:

```tsx
"use client";
import dynamic from "next/dynamic";
import { geometryJsonToPascalScene, pascalSceneToGeometryJson } from "@/lib/pascal/geometry-adapter";
import type { VersionDetail } from "@/types/api";

const PascalRuntime = dynamic(() => import("pascal-editor").then(m => m.Editor), { ssr: false });

export function PascalEditSurface({ version, onSaved }: Props) {
  const initialScene = useMemo(() => geometryJsonToPascalScene(version.geometry_json), [version]);
  async function handleSave(scene) {
    const geometry = pascalSceneToGeometryJson(scene);
    const res = await api.post(`/versions/${version.id}/revise-from-scene`,
                               { geometry_json: geometry, note: /*from UI*/ "" });
    onSaved(res.data);
  }
  return <PascalRuntime scene={initialScene} onSave={handleSave} />;
}
```

## Buoc 6 — Wire vao review workspace

`src/components/review-client.tsx`: them tab "Chinh sua 3D":

```tsx
{process.env.NEXT_PUBLIC_FF_PASCAL_EDIT === "true" && version.geometry_json ? (
  <Tab title="Chinh sua 3D"><PascalEditSurface version={version} onSaved={refetch} /></Tab>
) : null}
```

## Buoc 7 — E2E

`e2e/pascal-edit.spec.ts`:

```ts
test("edit -> save -> new revision", async ({ page }) => {
  await page.goto("/projects/demo/review?ff_pascal_edit=1");
  await page.getByRole("tab", { name: /Chinh sua 3D/i }).click();
  await expect(page.locator("canvas")).toBeVisible();
  // di chuyen 1 wall qua window.__pascal API hoac keyboard
  await page.evaluate(() => window.__pascal.moveWall("wall-1", { dx: 100 }));
  await page.getByRole("button", { name: /Save/i }).click();
  await expect(page.getByText(/Version V\d+/i)).toBeVisible();
  // assert lineage parent hien thi
});
```

## Buoc 8 — Analytics

Emit event `revision.created` voi `generation_source`. Update dashboard tile hien breakdown.

## Buoc 9 — Result

```json
{
  "cp":"cp7d-pascal-edit-mode",
  "role":"implementer",
  "status":"READY",
  "summary":"Edit mode + revise-from-scene API, no GPU path",
  "artifacts":[
    {"file":"../ai-architect-web/src/components/review/pascal-edit-surface.tsx","action":"created"},
    {"file":"../ai-architect-web/src/components/review-client.tsx","action":"updated"},
    {"file":"../ai-architect-api/app/api/v1/versions.py","action":"updated"},
    {"file":"../ai-architect-api/alembic/versions/<hash>_add_pascal_edit.py","action":"created"}
  ]
}
```

```bash
uv run python docs/phases/phase-2/checkpoints/notify.py \
  --cp cp7d-pascal-edit-mode --role implementer --status READY \
  --summary "Edit mode done" \
  --result-file docs/phases/phase-2/checkpoints/cp7d-pascal-edit-mode/result.json
```
