# AI Concept 2D Market-Quality Hardening Plan

Status: ready

## Decision

CP8-CP14 established the AI Concept 2D package pipeline. This phase hardens
that pipeline for market-quality homeowner output by improving input
understanding, spatial planning, drawing craft, revision handling, and rendered
evidence under a worktree-isolated integrator workflow.

## Goal

At the end of this phase, the API `main` checkout should generate concept 2D
packages that are credible for homeowner review across narrow houses,
apartment cases, style-driven briefs, and reference-image revision loops.

## Non-Goals

- Do not push branches during bootstrap.
- Do not start implementation in `C2D0`.
- Do not let a worker session certify integration or closeout.
- Do not accept worktree-only evidence as final closeout evidence.

## Workstreams

| Session | Outcome |
|---|---|
| C2D0 Bootstrap/Worktrees | Workflow docs tailored, worktrees created, launch order and closeout gate clear |
| C2D1 Input Style Contract | Homeowner conversation extraction, style knowledge, assumptions, and provenance are stronger and covered by tests |
| C2D2 Spatial Layout Quality | Room planning, adjacency, stairs, openings, furniture, and constraints produce more plausible plans |
| C2D3 Drawing Craft Render QA | PDF/DXF sheet composition, labels, line hierarchy, schedules, and visual QA meet a stronger craft bar |
| C2D4 Client Review Revision Loop | Homeowner feedback and reference-image descriptors produce traceable, bounded revisions |
| C2D5 Closeout Acceptance | Integrated API `main` passes the required tests, Docker parity, and manual render evidence gate |

## Exit Gate

From integrated API `main`:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q
make sprint3-ci-linux
```

Manual render evidence must include artifact paths and reviewer notes for:

- `7x25 modern tropical`
- `5x20 minimal warm`
- `apartment indochine with reference-image descriptors`

Closeout is blocked by failing commands, missing render evidence, unmerged
accepted branches, unresolved rework prompts, or evidence generated only from a
worker worktree.
