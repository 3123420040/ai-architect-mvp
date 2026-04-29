# Concept 2D Live Product Integration Operating Model

Status: ready for integrator launch

## Core Principle

Worktree evidence is advisory. Only the integrator can accept a slice, merge it
into local `main`, and decide when the next dependent session may start.

The local Docker review/professional-deliverables run is a serialized lane. Only
one session may mutate or rely on the shared local Docker stack and project
`56e4c77f-5f46-4506-af8c-df88362aad34` at a time.

## Session Model

| Session | Title | Branch | Worktree | Main purpose |
|---|---|---|---|---|
| C2DL0 | Bootstrap/Worktrees | docs main | `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp` | Create and verify API/Web worktrees |
| C2DL1 | Product Contract Adapter | `codex/concept-2d-live-contract` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-contract` | Map live versions to concept source/package contract |
| C2DL2 | Professional Deliverables Wiring | `codex/concept-2d-live-deliverables` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-deliverables` | Use concept package in live 2D export |
| C2DL3 | Review and Delivery UI Exposure | `codex/concept-2d-live-ui` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-live-ui` | Show readiness and sheet links |
| C2DL4 | Evidence and Backward Compatibility | `codex/concept-2d-live-evidence` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-evidence` | Prove regression/backcompat with tests and artifacts |
| C2DL5 | Closeout Acceptance | `codex/concept-2d-live-closeout` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-closeout` | Merge accepted slices and rerun integrated evidence |

## Launch Order

1. Start `C2DL0`.
2. After `CONCEPT_2D_LIVE_WORKTREES_READY`, start `C2DL1`.
3. Integrator reviews and merges `C2DL1`.
4. Start `C2DL2` and `C2DL3` in parallel after `C2DL1` lands.
5. Integrator reviews and merges `C2DL2`, then `C2DL3`.
6. Start `C2DL4` after API/Web slices are integrated.
7. Start `C2DL5` only after `C2DL4` passes or any rework is merged.

## Merge Model

Preferred merge order:

1. `C2DL1` API contract adapter
2. `C2DL2` API professional-deliverables wiring
3. `C2DL3` Web review/delivery exposure
4. `C2DL4` evidence/backcompat
5. `C2DL5` closeout docs/evidence

Do not merge UI work that depends on fields not present in the integrated API
contract. Do not run the final local Docker project `56e4...` acceptance from a
worker worktree.

## Integrated-Main Rerun Gate

API:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q
make sprint3-ci-linux
```

Web:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Docker/manual:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp
docker compose -f docker-compose.local.yml up -d --build
```

Manual evidence must verify the review URL for project
`56e4c77f-5f46-4506-af8c-df88362aad34`, the selected locked version, and the
generated Professional Deliverables bundle.
