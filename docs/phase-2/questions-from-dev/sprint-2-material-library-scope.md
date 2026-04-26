---
title: Sprint 2 Question — Material Library Scope
phase: 2
status: open
date: 2026-04-27
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

