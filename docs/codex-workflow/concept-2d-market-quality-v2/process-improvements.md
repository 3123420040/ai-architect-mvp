# Concept 2D Market Quality V2 Process Improvements

Status: ready for bootstrap

## Rules To Keep

1. Sync with local `main` before declaring a blocker.
2. Worker evidence is advisory; integrated `main` evidence is final.
3. Keep one integrator thread and paste every final report back there.
4. Use rework prompts as artifacts.
5. Separate local-env blockers from product blockers.
6. Keep browser/full-generation lanes serialized.

## New Rules For This Phase

1. Do not let technical gates hide weak design quality.
2. Every market-quality PASS must include artifact evidence, not only unit tests.
3. Keep concept-only safety language visible in every artifact.
4. Treat homeowner readability as a first-class acceptance dimension.
5. Treat architect plausibility as a first-class acceptance dimension.
6. If AI-inferred assumptions are needed, record provenance and confidence instead of presenting them as facts.
7. If the AI cannot infer safely, ask a friendly nontechnical confirmation question.
8. Do not add broad UI redesign unless a narrow review/delivery exposure is required.
9. Do not weaken existing Sprint 2/Sprint 3 or Professional Deliverables gates.
10. Do not introduce heavy rendering into synchronous FastAPI requests.

## Evidence Standard

Each implementation session should return:

- files changed;
- commands run;
- focused tests;
- relevant generated artifacts;
- visual/manual notes if available;
- known market-quality gaps;
- explicit scope-compliance statement.
