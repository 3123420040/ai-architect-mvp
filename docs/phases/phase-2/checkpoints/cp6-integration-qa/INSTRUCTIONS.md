# CP6 — Integration + QA

**Mục tiêu:** Khoa Phase 2 bang verification that tren production lane.  
**Requires:** `cp5-ifc-foundation` PASS.

## Bước 1 — Regression and package verification

Run API tests, web build, and export verification against the final Phase 2 package.

## Bước 2 — Production deployment

Use the existing Docker-first production path from `ai-architect-mvp` to rebuild and redeploy the stack.

## Bước 3 — Production loops

Run the production loop script for 2 rounds and persist the artifact under `artifacts/production-checks/`.

