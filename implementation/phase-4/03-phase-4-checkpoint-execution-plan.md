# Phase 4 Checkpoint Execution Plan

## CP-4.0 Phase Audit and Scope Reset

Goal:

- audit true status of Phase 2, Phase 3, and Phase 4,
- separate shipped reality from roadmap intent,
- freeze the branch and document strategy.

## CP-4.1 Research and Requirement Contract

Goal:

- complete market research outputs,
- lock the product requirement contract,
- define artifact set and design-board standard.

DoD:

- docs `21`, `22`, `23` created,
- Phase 4 implementation docs created,
- checkpoint breakdown locked.

## CP-4.2 Clarification Engine

Goal:

- upgrade brief parsing,
- add clarification state,
- improve AI follow-up behavior,
- improve production fallback safety.

DoD:

- chat, brief, and project responses expose clarification state,
- tests cover the new contract.

## CP-4.3 Intake UX Revamp

Goal:

- redesign the intake page into a guided workspace,
- localize labels to Vietnamese with diacritics,
- reduce raw JSON prominence.

DoD:

- web build passes,
- intake shows progress, missing items, and design-direction board.

## CP-4.4 Phase 3 Compatibility Validation

Goal:

- verify that Phase 4 brief changes do not break Phase 3 downstream generation and export.

DoD:

- end-to-end tests pass,
- deploy candidate remains package-flow compatible.

## CP-4.5 Production Deploy and Loop

Goal:

- deploy Phase 4 to production,
- run production loops,
- fix regressions or stability issues found from production truth.

DoD:

- production deploy succeeds,
- production loops complete,
- follow-up fixes are redeployed and revalidated.
