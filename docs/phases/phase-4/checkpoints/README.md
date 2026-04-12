# Phase 4 Checkpoints

Phase 4 is locked to:

- `docs/phase-1/21-ai-needs-clarification-market-research-report.md`
- `docs/phase-1/22-ai-needs-clarification-product-requirements.md`
- `implementation/phase-4/02-phase-4-implementation-detailed.md`
- `implementation/phase-4/03-phase-4-checkpoint-execution-plan.md`

## Sequence

| Order | Code | Checkpoint | Depends On | Target |
|---|---|---|---|---|
| 0 | `cp-4.0-phase-audit` | Phase Audit and Scope Reset | — | Lock true status of Phase 3 and Phase 4 before new work |
| 1 | `cp-4.1-research-contract` | Research and Requirement Contract | `cp-4.0-phase-audit` | Market research, product requirements, references, and implementation contract |
| 2 | `cp-4.2-clarification-engine` | Clarification Engine | `cp-4.1-research-contract` | Richer brief parsing, clarification state, safer chat fallback |
| 3 | `cp-4.3-intake-ux` | Intake UX Revamp | `cp-4.2-clarification-engine` | Vietnamese-first guided AI clarification workspace |
| 4 | `cp-4.4-phase3-compat` | Phase 3 Compatibility Validation | `cp-4.3-intake-ux` | Verify Phase 4 handoff does not break Phase 3 export baseline |
| 5 | `cp-4.5-production-loop` | Production Deploy and Loop | `cp-4.4-phase3-compat` | Deploy, run loops, fix, and revalidate |

## Notes

- Phase 4 builds on top of the shipped Phase 3 package/export lane.
- Phase 4 does not replace the downstream review/export/handoff flow.
- Production truth remains the final gate for accepting Phase 4 changes.
