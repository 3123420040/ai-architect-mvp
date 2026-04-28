# CP7 — Pascal Editor Integration (Program Docs)

**Branch:** `cp7-pascal-editor-integration`
**Phase:** Phase 2
**Ngay tao:** 2026-04-19
**Trang thai:** planning

## Muc luc

| Doc | Noi dung |
|-----|----------|
| [00-context.md](00-context.md) | Boi canh, stakeholders, constraints, success metrics |
| [01-as-is.md](01-as-is.md) | AS-IS: hien trang viewer/review/geometry, evidence tu code |
| [02-to-be.md](02-to-be.md) | TO-BE: muc tieu kien truc voi Pascal |
| [03-gap-analysis.md](03-gap-analysis.md) | Gap AS-IS → TO-BE, work items |
| [04-checkpoint-breakdown.md](04-checkpoint-breakdown.md) | CP7 chia thanh 4 sub-CP (A/B/C/D), sequence va exit criteria |
| [05-rollout-plan.md](05-rollout-plan.md) | Feature flag matrix, staging soak, rollback |

## Checkpoint folders

- Umbrella: [`checkpoints/cp7-pascal-editor-integration/`](../checkpoints/cp7-pascal-editor-integration/)
- Sub-CP A — Spike + vendor: [`cp7a-pascal-spike/`](../checkpoints/cp7a-pascal-spike/)
- Sub-CP B — Geometry adapter: [`cp7b-geometry-adapter/`](../checkpoints/cp7b-geometry-adapter/)
- Sub-CP C — Viewer replacement: [`cp7c-pascal-viewer/`](../checkpoints/cp7c-pascal-viewer/)
- Sub-CP D — KTS edit mode: [`cp7d-pascal-edit-mode/`](../checkpoints/cp7d-pascal-edit-mode/)

## Nguyen tac lam viec

1. **Canonical-first:** moi edit phai round-trip qua `geometry_json` Layer 2 (khong anchor state vao scene graph Pascal).
2. **Feature-flag gated:** moi phase ship duoc duoi flag off tren production.
3. **Fallback bao toan:** `<model-viewer>` hien tai giu nguyen lam fallback, khong xoa den khi Pascal viewer on dinh tren staging ≥ 1 tuan.
4. **No GPU regression:** edit-derived revision KHONG goi GPU pipeline, phai danh dau `generation_source = "pascal_edit"`.
