# C2D1 Prompt - Input Style Contract

Copy everything below into a new Codex chat session after the integrator
confirms this session may start.

```text
You are the Input Style Contract Agent for this repo.

Primary objective:
Improve homeowner conversation extraction, style knowledge, assumptions, and provenance.

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/README.md

Hard constraints:
- Work only in /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-input-style.
- Branch: codex/concept-2d-input-style.
- Preferred write scope: app/services/design_intelligence/customer_understanding.py, app/services/design_intelligence/style_inference.py, app/services/design_intelligence/provenance.py, app/services/professional_deliverables/style_knowledge.py, app/services/professional_deliverables/style_profiles/, and focused tests.
- Treat layout, PDF/DXF rendering, and revision-loop files as read-only unless a tiny contract change is unavoidable and called out.
- Do not edit the workflow ledger. Paste the final report back to the integrator.
- Do not push.

Acceptance criteria:
- Homeowner conversation extraction produces explicit requirements, assumptions, unknowns, and provenance.
- Style inference uses style knowledge consistently for modern tropical, minimal warm, and indochine cases.
- Tests cover successful extraction and ambiguity handling.
- Final report lists focused tests and any integration risks for downstream layout/render workers.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2D1 Input Style Contract
- Branch/worktree: codex/concept-2d-input-style at /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-input-style
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Verification:
- Commands run:
- Focused tests:
- Main rerun evidence, if applicable:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- Any product blockers:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
- 
```
