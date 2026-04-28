---
title: Sprint 2 Question — Material Library Scope
phase: 2
status: ANSWERED
date: 2026-04-27
answered: 2026-04-27
from: Dev/Test Agent
to: PM/Architect Agent via PO
---

# Context

Sprint 2 scope requires GLB/FBX export and KTX2 texture outputs for the golden townhouse. The handoff also mentions Plan A material library bootstrap: curate ~50 starter materials from Quixel Megascans free tier + Polyhaven, Modern Minimalist + Tropical VN.

Curating, licensing, downloading, and committing a 50-material external asset library is materially larger than the golden fixture export gates. It may also introduce binary repo size and license tracking decisions that affect Sprint 4 manifest/file inventory.

# Precise Question

Is a full ~50 external material pack required for Sprint 2 acceptance, or can Sprint 2 ship a deterministic golden-fixture material registry with KTX2 textures and the schema/paths needed to expand to the ~50-material pack later?

# Answer Format Needed

Please answer with one of:

1. `Golden fixture material set`: Sprint 2 acceptance requires only the materials needed for the golden fixture, generated/deterministic and KTX2-compressed, with metadata compatible with later expansion.
2. `Full starter material pack`: Sprint 2 acceptance requires the curated ~50-material Modern Minimalist + Tropical VN pack; provide license/source policy and expected storage location.

# Fallback If Not Answered Within 24 Hours

I will implement option 1: golden fixture material set plus expandable material registry. I will not commit external Quixel/Polyhaven source assets until the PM/Architect agent confirms source/licensing/storage policy.

---

# Answer (PM/Architect Agent — 2026-04-27)

**Decision: Option 1 — Golden fixture material set.**

## Rationale
- Sprint 2's goal is **3D pipeline foundation** (GLB/FBX export, KTX2 encoding, validators, CI gates). Demonstrating that the pipeline produces valid, gate-passing outputs is the deliverable. The number of materials in flight does not change pipeline correctness.
- Curating 50 external materials = a parallel **asset curation + licensing workstream**, not engineering. Doing it inside Sprint 2 inflates scope and risks committing third-party binaries before the licensing policy is set.
- Quixel Megascans free tier and Polyhaven CC0 have very different obligations (subscription/attribution model vs. truly public domain). They warrant a deliberate policy decision, not a hurried Sprint 2 commit.
- Your fallback approach (deterministic registry + expandable schema) is exactly what the product needs at this point.

## What Sprint 2 must include
- A deterministic material registry sufficient for the golden townhouse (target: ~5–10 distinct materials covering walls, slabs, roof, openings/glass, doors, fixed fixtures, site/ground, vegetation placeholder).
- KTX2-encoded textures for each material, following the Sprint 2 metadata stub schema.
- Material registry shape forward-compatible with the future ~50-material pack — same fields, same naming convention `MAT_<asset>_<part>`, same texture slot layout.

## What Sprint 2 must NOT include
- No external Quixel/Polyhaven binaries committed to the repo.
- No public-asset attribution files committed yet (those land with the curated pack).
- No bespoke procedural generation (DEF-006, ROOM project's territory).

Synthetic/deterministic source maps (e.g. solid albedo with simple noise) for the golden fixture are acceptable in Sprint 2 — the goal is to prove the encoding/validation chain end-to-end, not to deliver photoreal renders. Photoreal-quality materials arrive with the 50-material pack.

## Curated 50-material pack — separate workstream

I have registered this as **DEF-007** in `docs/phase-2/04-deferred-roadmap.md`. It is a parallel asset/licensing workstream that may run concurrently with engineering sprints once a policy owner is assigned. It is **not** a Sprint 2/3/4 blocker.

**This unblocks the material scope question. Proceed with Sprint 2 implementation.**

