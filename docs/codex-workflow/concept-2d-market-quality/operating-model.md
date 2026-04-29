# AI Concept 2D Market-Quality Hardening Operating Model

Status: ready

## Core Principle

This workflow has one canonical integrator thread. The integrator receives all
worker final reports, updates the ledger, reviews diffs, decides merge versus
rework, and starts closeout only after accepted branches are integrated into
API `main`.

Worker reports and worktree test results are evidence, not acceptance. No
worker self-certifies integration success.

## Session Model

| Session | Lane | Branch | Worktree | Ownership |
|---|---|---|---|---|
| C2D0 | Bootstrap | docs main | `/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp` | Workflow docs and worktree verification only |
| C2D1 | Parallel worker | `codex/concept-2d-input-style` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-input-style` | Homeowner extraction, style inference, style knowledge, assumptions, provenance |
| C2D2 | Parallel worker | `codex/concept-2d-layout-quality` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-layout-quality` | Spatial planning, adjacency, stairs, openings, furniture, layout constraints |
| C2D3 | Parallel worker | `codex/concept-2d-render-qa` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-render-qa` | PDF/DXF drawing craft, sheet composition, labels, line hierarchy, schedules, render QA |
| C2D4 | Parallel worker | `codex/concept-2d-review-loop` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-review-loop` | Homeowner feedback interpretation, revision operations, reference-image descriptor revisions |
| C2D5 | Serialized closeout | `codex/concept-2d-closeout` | `/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-closeout` | Acceptance report only; final gate runs from integrated API `main` |

## Launch Order

1. Complete `C2D0` bootstrap and verify docs plus worktrees.
2. Launch `C2D1`, `C2D2`, `C2D3`, and `C2D4` after the integrator confirms the worktrees are current with local API `main`.
3. Paste every worker final report back into the integrator thread. Workers do not edit the ledger directly unless the integrator asks.
4. Integrator reviews and merges in dependency order: `C2D1`, `C2D2`, `C2D3`, then `C2D4`, with rework prompts created for any rejected or incomplete slice.
5. Launch `C2D5` only after the integrator has an integrated API `main` containing all accepted slices.

## Rework Model

Rework is always a prompt artifact, not an informal chat correction. The
integrator writes rework prompts under:

```text
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/rework-prompts/
```

Use this naming pattern:

```text
c2d<N>-rework-YYYYMMDD-<short-reason>.prompt.md
```

Each rework prompt must state the source session, branch/worktree, accepted
parts, rejected parts, exact requested changes, verification evidence required,
and final report format.

## Merge Model

- All implementation branches originate from local API `main` at bootstrap.
- The integrator may merge only after reading the final report and reviewing the branch diff.
- Conflicts, failing focused tests, missing evidence, or unclear ownership become rework, not acceptance.
- C2D3 render artifacts produced in a worker worktree are useful but advisory.
- C2D5 is the only closeout lane and must rerun from integrated API `main`.

## Integrated-Main Rerun Gate

Run exactly from:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q
make sprint3-ci-linux
```

Manual render evidence must cover at least:

- `7x25 modern tropical`
- `5x20 minimal warm`
- `apartment indochine with reference-image descriptors`

Closeout fails if any command fails, any required manual render case is missing,
or the evidence was produced from a worker worktree instead of integrated API
`main`.
