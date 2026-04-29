# C2DL4 Prompt - Evidence and Backward Compatibility

Copy everything below into a new Codex chat session only after the integrator
accepts and merges C2DL2 and C2DL3.

```text
You are the Evidence and Backward Compatibility Agent for AI Architect Concept 2D Live Product Integration.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-evidence

Main API path, read-only except local git merge from main:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api

Web path, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web

Docs path, read-only:
/Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-live-integration/ledger.md

Precondition:
- Merge current local API main first: `git merge --no-edit main`.
- Confirm C2DL2 code is present.
- Confirm C2DL3 has either landed in Web main or is explicitly deferred by the integrator.
- If not, stop with BLOCKED_BY_PENDING_C2DL_SLICES.

Primary objective:
Add regression/backward-compatibility evidence so the integrator can trust the live Concept 2D product path before closeout.

Owned files:
- tests/professional_deliverables/test_concept_2d_live_integration.py
- tests/professional_deliverables/test_product_e2e_bridge.py only if needed for product fixture reuse
- tests/professional_deliverables/fixtures/** only if an existing pattern supports fixtures
- No product code unless a narrow testability hook is required and documented

Hard constraints:
- Do not change Web.
- Avoid product code changes. If a product defect is found, capture evidence and return NEEDS_REWORK.
- Do not push or create PRs.
- Do not rely on worker-worktree evidence as final acceptance.
- Do not make construction/permit/MEP/legal-ready claims.

Required evidence:
1. Eligible live/product geometry produces a full concept package:
   - PDF contains `A-000`, `A-601`, `A-602`, `A-901` or equivalent package sheet titles;
   - PDF contains selected lot dimensions;
   - PDF does not contain stale golden dimensions;
   - DXF sheet files match the package model or unsupported sheet reasons are explicit;
   - quality report states readiness truthfully.
2. Legacy fallback remains supported:
   - unsupported/missing geometry does not crash silently;
   - fallback reason is machine-readable;
   - existing old geometry tests remain green.
3. Regression project behavior is reproducible:
   - project id `56e4c77f-5f46-4506-af8c-df88362aad34` is documented as the local live case;
   - if local DB does not contain it, create a deterministic test fixture equivalent: 5x20, 4 floors, rooms/walls/openings.

Verification commands:
cd /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-live-evidence
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/professional_deliverables/test_concept_2d_live_integration.py -q
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/professional_deliverables -q
PYTHONPATH=. /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.venv/bin/python -m pytest tests/test_foundation.py tests/test_flows.py -q

Optional Docker evidence:
Run only if the integrator explicitly allows using the shared local Docker lane in this session.

Commit locally if verification passes:
test(concept-2d): cover live package integration

Acceptance criteria:
- Tests fail against the old 7-page-only live path and pass against the integrated concept path.
- Backward compatibility/fallback is covered.
- Existing professional deliverables regressions pass.
- Worktree is clean after commit.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DL4 Evidence and Backward Compatibility
- Branch/worktree:
- Commit:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Evidence coverage:
- Full concept package:
- Selected geometry:
- DXF/sheet files:
- Quality report:
- Legacy fallback:
- Project 56e4 or equivalent fixture:

Verification:
- Commands run:
- Focused tests:
- Regression tests:
- Docker/manual evidence, if authorized:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No Web changes:
- Product code changes avoided or justified:
- No push/PR:
- No unsafe readiness claims:

Known issues:
-
```
