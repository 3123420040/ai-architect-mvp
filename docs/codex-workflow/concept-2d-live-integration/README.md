# Concept 2D Live Product Integration

Status: ready for integrator launch

This folder is the docs-first control plane for the next AI Architect phase:
wire the completed CP8-CP14 Concept 2D market-quality package into the live
product review and professional-deliverables path.

## Current Finding

Local Docker evidence on `2026-04-29` showed that
`http://localhost:3000/projects/56e4c77f-5f46-4506-af8c-df88362aad34/review`
can create a Professional Deliverables job, but that job still uses the old 2D
path:

```text
geometry_to_drawing_project(...)
  -> generate_project_2d_bundle(...)
```

The generated PDF/DXF receives the earlier 2D technical uplift, but not the full
CP8-CP14 Concept 2D package:

- PDF has 7 pages, not the full concept package sheet set.
- DXF has 7 sheets: site, floor plans, elevation, section.
- Missing physical concept sheets/tokens include `A-000`, `A-601`, `A-602`,
  `A-901`, `Professional Concept 2D Package`, room/area schedule, door/window
  schedule, assumptions, and style notes.

This phase closes that product integration gap.

## Repos

- Docs/orchestration: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`
- API main: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- Web main: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web`
- API worktrees: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/`
- Web worktrees: `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/`

## Files

- `plan.md`: phase goal, slices, non-goals, and exit gate.
- `operating-model.md`: launch order, worktree map, integration rules, and
  integrated-main rerun gate.
- `process-improvements.md`: controls to preserve while fixing the live product
  gap.
- `ledger.md`: canonical intake and decision log for the integrator thread.
- `prompt-index.md`: canonical worker prompts and rework prompt naming.
- `session-prompts/`: launch prompts.
- `rework-prompts/`: artifact location for rework prompts created by the
  integrator.

## Sessions

| Session | Title | Branch | Worktree |
|---|---|---|---|
| C2DL0 | Bootstrap/Worktrees | docs main | `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp` |
| C2DL1 | Product Contract Adapter | `codex/concept-2d-live-contract` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-contract` |
| C2DL2 | Professional Deliverables Wiring | `codex/concept-2d-live-deliverables` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-deliverables` |
| C2DL3 | Review and Delivery UI Exposure | `codex/concept-2d-live-ui` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-live-ui` |
| C2DL4 | Evidence and Backward Compatibility | `codex/concept-2d-live-evidence` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-evidence` |
| C2DL5 | Closeout Acceptance | `codex/concept-2d-live-closeout` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-closeout` |

## Operating Rule

One integrator thread receives every final report, updates `ledger.md`, decides
merge versus rework, and decides when closeout may start. Worker evidence is
advisory only. Final acceptance must be rerun from integrated API/Web `main`.

## Next Step

Start `C2DL0` first. After it reports `CONCEPT_2D_LIVE_WORKTREES_READY`, launch
`C2DL1`. Do not launch `C2DL2` or `C2DL3` until the integrator accepts and merges
`C2DL1`, because both depend on the live concept source contract.

## Integrated-Main Rerun Gate

Closeout reruns from integrated local `main`, not from a worker worktree:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q
make sprint3-ci-linux

cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Docker/manual evidence must prove the review flow for project
`56e4c77f-5f46-4506-af8c-df88362aad34` produces and exposes the full Concept 2D
package for the selected locked version.
