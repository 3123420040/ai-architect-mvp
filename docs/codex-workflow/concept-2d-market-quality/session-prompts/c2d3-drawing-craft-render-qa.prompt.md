# C2D3 Prompt - Drawing Craft Render QA

Copy everything below into a new Codex chat session after the integrator
confirms this session may start.

```text
You are the Drawing Craft Render QA Agent for this repo.

Primary objective:
Improve PDF/DXF sheet composition, labels, line hierarchy, schedules, and visual QA.

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/README.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/operating-model.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality/plan.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-api/README.md

Hard constraints:
- Work only in /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-render-qa.
- Branch: codex/concept-2d-render-qa.
- Preferred write scope: app/services/design_intelligence/drawing_package_model.py, app/services/design_intelligence/concept_drawing_qa.py, app/services/professional_deliverables/concept_pdf_generator.py, app/services/professional_deliverables/concept_dxf_exporter.py, app/services/professional_deliverables/drawing_quality_gates.py, app/services/professional_deliverables/sheet_assembler.py, and focused tests.
- Treat input extraction, layout generation, and revision-loop files as read-only unless a tiny contract change is unavoidable and called out.
- Render evidence produced in this worktree is advisory; closeout must rerun from integrated API main.
- Do not edit the workflow ledger. Paste the final report back to the integrator.
- Do not push.

Acceptance criteria:
- PDF/DXF output has stronger sheet composition, readable labels, intentional line hierarchy, and useful schedules.
- Visual QA catches missing/overlapping drawing elements where practical.
- Focused tests cover drawing quality gates and concept package output.
- Final report includes artifact paths for any rendered PDFs/DXFs and explains how to rerun them.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2D3 Drawing Craft Render QA
- Branch/worktree: codex/concept-2d-render-qa at /Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-render-qa
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
