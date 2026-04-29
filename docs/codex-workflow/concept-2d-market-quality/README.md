# AI Concept 2D Market-Quality Hardening

Status: ready for integrator launch

This folder is the docs-first control plane for the next AI Concept 2D phase:
move the existing concept package pipeline from functional CP8-CP14 output to
market-quality homeowner deliverables.

## Repos

- Docs/orchestration: `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp`
- API integration main: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api`
- API worker worktrees: `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/`

## Files

- `plan.md`: phase goal, workstreams, non-goals, and exit gate.
- `operating-model.md`: launch order, worktree map, integrator rules, and main rerun gate.
- `process-improvements.md`: reusable controls to preserve during the phase.
- `ledger.md`: canonical intake and decision log for the integrator thread.
- `prompt-index.md`: canonical worker prompts and rework prompt naming.
- `session-prompts/`: initial launch prompts.
- `rework-prompts/`: artifact location for rework prompts created by the integrator.

## Sessions

| Session | Title | Branch | Worktree |
|---|---|---|---|
| C2D0 | Bootstrap/Worktrees | docs main | `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp` |
| C2D1 | Input Style Contract | `codex/concept-2d-input-style` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-input-style` |
| C2D2 | Spatial Layout Quality | `codex/concept-2d-layout-quality` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-layout-quality` |
| C2D3 | Drawing Craft Render QA | `codex/concept-2d-render-qa` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-render-qa` |
| C2D4 | Client Review Revision Loop | `codex/concept-2d-review-loop` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-review-loop` |
| C2D5 | Closeout Acceptance | `codex/concept-2d-closeout` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-closeout` |

## Operating Rule

One integrator thread receives every final report, updates `ledger.md`, decides
merge versus rework, and decides when closeout can start. Worker evidence is
advisory only. Workers do not self-certify integration success.

## Closeout Gate

Closeout reruns from integrated API `main`, not from a worker worktree:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q
make sprint3-ci-linux
```

Manual render evidence must also exist for at least:

- `7x25 modern tropical`
- `5x20 minimal warm`
- `apartment indochine with reference-image descriptors`
