# C2DQ6 Prompt - Integrated Closeout Acceptance

Copy everything below into a new Codex session only after C2DQ1-C2DQ5 are accepted and merged into local `main`.

```text
You are the C2DQ6 Integrated Closeout Acceptance Agent for AI Architect Concept 2D Market Quality V2.

Worktree path:
/Users/nguyenquocthong/project/ai-architect/ai-architect-api/.worktrees/concept-2d-market-closeout

Main project path:
/Users/nguyenquocthong/project/ai-architect

Repos:
- API: /Users/nguyenquocthong/project/ai-architect/ai-architect-api
- Web: /Users/nguyenquocthong/project/ai-architect/ai-architect-web
- Docs: /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp

Required docs to read first:
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/context-and-acceptance-contract.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/market-quality-rubric.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/20-case-matrix.md
- /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/ledger.md

Primary objective:
Run final integrated-main acceptance for Concept 2D market quality and write the closeout decision.

Hard constraints:
- Do not start if C2DQ1-C2DQ5 accepted slices are not merged.
- Do not implement broad product fixes in closeout.
- Do not overstate market quality.
- Do not claim construction/permit/MEP/legal readiness.
- Do not push unless the integrator explicitly requests it after PASS.

Tasks:
1. Inspect API/Web/Docs git status.
2. Merge current local `main` into this closeout worktree.
3. Confirm C2DQ1-C2DQ5 are accepted and merged from the ledger.
4. If not merged, stop and report:
   - Decision: BLOCKED
   - Known issues: BLOCKED_BY_PENDING_C2DQ_SLICES
5. Run integrated verification:
   - API professional deliverables tests.
   - API foundation/flows/briefing tests.
   - `make sprint3-ci-linux`.
   - Web lint/build if Web changed in the phase.
6. Rebuild Docker local:
   - `docker compose -f docker-compose.local.yml up -d --build`
7. Run fresh browser full-flow acceptance from intake to delivery.
8. Generate artifacts for the 20-case matrix or a justified representative subset plus the required full live flow.
9. Download/render PDFs and inspect at least 5 generated packages as homeowner and architect.
10. Open DXFs with `ezdxf`.
11. Check Review/Delivery console and network.
12. Write closeout report:
   - /Users/nguyenquocthong/project/ai-architect/ai-architect-mvp/docs/codex-workflow/concept-2d-market-quality-v2/closeout-report.md
13. Commit closeout report locally:
   - Suggested message: docs(concept-2d): close market quality v2 acceptance

Expected PASS:
- selected-version geometry preserved;
- Concept 2D package ready;
- 20-case matrix evidence exists or justified subset is approved by integrator;
- at least 5 PDFs manually inspected;
- Review/Delivery expose correct package state and links;
- no console/network failures in final flows;
- no unsafe readiness claims;
- technical tests pass.

Expected NEEDS_REVIEW:
- market-quality output is useful but one non-critical visual quality issue remains.

Expected BLOCKED:
- integrated flow fails;
- pending slices are missing;
- product needs an architecture/design decision before safe implementation.

Final report format:
Decision: PASS | NEEDS_REVIEW | BLOCKED

Scope:
- Session: C2DQ6 Integrated Closeout Acceptance
- API branch/commit:
- Web branch/commit:
- Docs branch/commit:
- Owned files changed:
- Shared files changed:

Integrated state:
- C2DQ1 merge present:
- C2DQ2 merge present:
- C2DQ3 merge present:
- C2DQ4 merge present:
- C2DQ5 merge present:

Verification:
- API tests:
- Web lint/build:
- sprint3-ci-linux:
- Docker rebuild:
- Browser full-flow:
- Artifact evidence:

Market-quality decision:
- Homeowner readability:
- Architect plausibility:
- Spatial planning:
- Drawing craft:
- Style expression:
- Revision usefulness:
- Concept-only safety:

Residual risk:
- Flakes:
- Known gaps:

Contract compliance:
- No push:
- No PR:
- No unsafe readiness claims:
- Worker evidence not used as final truth:

Known issues:
-
```
