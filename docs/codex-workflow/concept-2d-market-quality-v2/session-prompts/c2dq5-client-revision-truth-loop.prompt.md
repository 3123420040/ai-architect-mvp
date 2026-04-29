# C2DQ5 Prompt - Client Revision Truth Loop

Copy everything below into a new Codex session only after C2DQ2-C2DQ4 are accepted and merged.

```text
You are the C2DQ5 Client Revision Truth Loop Agent for AI Architect Concept 2D Market Quality V2.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-revision

Optional Web companion path, only if a narrow UI exposure is required:
/Users/nguyenquocthong/project/ai-architect/ai-architect-web/.worktrees/concept-2d-market-review-ui

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/market-quality-rubric.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/20-case-matrix.md
- Latest C2DQ2-C2DQ4 reports from the ledger, if available.

Primary objective:
Validate and improve the homeowner feedback loop so natural-language and reference-descriptor feedback changes the right design assumptions and regenerates traceable concept packages.

Likely API files:
- app/services/design_intelligence/revision_interpreter.py
- app/services/design_intelligence/concept_revision.py
- app/services/design_intelligence/customer_understanding.py
- tests/test_concept_revision_loop.py
- tests/professional_deliverables/test_ai_concept_2d_e2e.py

Optional Web files, only if needed:
- src/components/review-client.tsx
- src/components/delivery-client.tsx
- src/lib/professional-deliverables.ts

In scope:
- homeowner-friendly clarification behavior;
- preserving original requirements;
- applying feedback to room priorities, style features, dislikes, storage/light/greenery/open-kitchen preferences;
- reference-image descriptors as non-measured style evidence;
- revision provenance and assumptions;
- tests proving before/after package metadata.

Out of scope:
- real image analysis;
- broad UI redesign;
- construction-ready revisions;
- automatic fixes that silently discard original brief facts.

Verification:
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_revision_loop.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/professional_deliverables/test_ai_concept_2d_e2e.py -q`
- `PYTHONPATH=. .venv/bin/python -m pytest tests/test_concept_model_contract.py tests/test_concept_layout_generator.py tests/professional_deliverables/test_concept_2d_package.py -q`
- Web touched only if needed: `pnpm lint && pnpm build`
- `git diff --check`

Commit locally:
- Suggested message: feat(concept-2d): improve market revision loop

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DQ5 Client Revision Truth Loop
- Branch/worktree:
- Owned files changed:
- Shared files changed:

Summary:
- Implemented:
- Not implemented:
- Deferred:

Revision coverage:
- Natural-language feedback:
- Reference descriptors:
- Original requirement preservation:
- Regeneration metadata:
- Ambiguity handling:
- Unsafe-scope handling:

Verification:
- Commands run:
- Focused tests:
- Web verification, if any:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No broad UI redesign:
- No real image analysis claim:
- No unsafe readiness claims:
- Any NEEDS_ARCHITECT_DECISION:

Known issues:
-
```
