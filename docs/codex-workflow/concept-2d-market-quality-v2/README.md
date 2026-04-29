# Concept 2D Market Quality V2

Status: ready for bootstrap

This workflow starts after the live Concept 2D integration passed technical full-flow acceptance.

The previous phase proved:

- the live product path can generate Concept 2D PDF/DXF from the selected version;
- Review and Delivery expose the Concept 2D package correctly;
- the 5m x 20m live case no longer leaks stale 5m x 15m dimensions;
- PDF/DXF artifacts are technically valid and concept-only.

This phase is different. Its goal is market/customer/architect acceptance:

```text
Can a low-communication homeowner review the generated 2D concept package and give useful feedback,
and would an architect consider the package a credible first-pass concept drawing set?
```

## Required Reading

- Shared contract: `context-and-acceptance-contract.md`
- Latest full-flow pass: `../concept-2d-live-integration/fresh-full-flow-acceptance.md`
- Previous closeout: `../concept-2d-live-integration/closeout-report.md`
- Browser audit findings: `../../../output/concept-2d-acceptance-audit/10-loop-findings.md`

## Sessions

| Session | Title | Purpose |
|---|---|---|
| C2DQ0 | Bootstrap/Worktrees | Create and verify dedicated API/Web/Docs worktrees for market-quality slices |
| C2DQ1 | Acceptance Rubric And Case Matrix | Convert browser audit findings into a market/customer/architect acceptance rubric and 20-case fixture matrix |
| C2DQ2 | Spatial Planning Quality | Improve concept layouts so room programs, circulation, stairs, wet cores, storage, openings, and furniture read plausibly for customer review |
| C2DQ3 | Drawing Craft And Readability | Improve PDF/DXF sheet composition, viewport scale, label density, dimensions, line hierarchy, legends, and visual non-overlap |
| C2DQ4 | Style And Facade Expression | Make style-specific facade/elevation/section/material notes visibly meaningful without construction-ready claims |
| C2DQ5 | Client Revision Truth Loop | Exercise upload-descriptor and natural-language feedback loops, preserving original requirements while regenerating better concept sheets |
| C2DQ6 | Integrated Closeout Acceptance | Run fresh browser full-flow acceptance on integrated main, inspect artifacts, and write final market-quality decision |

## Launch Order

1. Run `C2DQ0`.
2. Run `C2DQ1`.
3. After `C2DQ1` is accepted and merged, run `C2DQ2`, `C2DQ3`, and `C2DQ4` in parallel.
4. Merge accepted API slices in this order: `C2DQ2`, `C2DQ3`, `C2DQ4`.
5. Run `C2DQ5` after the accepted API slices are integrated.
6. Run `C2DQ6` only after `C2DQ1`-`C2DQ5` are accepted and merged.

## Integrated-Main Rerun Gate

The integrator must rerun from integrated `main`, not worker worktrees:

```bash
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api
PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. .venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py tests/test_briefing.py -q
make sprint3-ci-linux

cd /Users/nguyenquocthong/project/ai-architect/ai-architect-web
pnpm lint
pnpm build
```

Closeout must also run fresh browser flows and inspect generated PDF/DXF artifacts for the accepted case matrix.
