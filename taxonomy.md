# Taxonomy — Helix Anomalous Math Training

This document describes the taxonomy used to organize anomalous math problems and creative challenge cases in this dataset.

---

## 1. Core Categories

### A. Arithmetic Anomalies
- Misleading phrasing (e.g., “more than less than” constructs)
- Hidden operations (implicit multiplication/division)
- Boundary trick cases (0, 1, negative numbers, infinities)

### B. Algebraic Anomalies
- Variable traps (e.g., same symbol reused differently)
- Contradictory equations (unsolvable by design)
- Identity inversions (expressions that simplify in non-obvious ways)

### C. Geometric / Spatial Anomalies
- Impossible figures (non-Euclidean tricks, Penrose-like)
- Dimensional shifts (2D framed as 3D or higher)
- Overloaded diagrams (ambiguous labeling)

### D. Probabilistic Anomalies
- Confusing sample space framing
- Paradoxical events (Monty Hall, Bertrand box paradox variants)
- Hidden conditionality

### E. Combinatorial / Set Anomalies
- Overcounting / undercounting traps
- Non-standard groupings (nested sets, recursive partitions)
- Category overlap contradictions

### F. Meta-Cognitive Challenges
- Self-referential math (“this equation has no solution” type)
- Problems requiring reinterpretation of rules mid-way
- Trick linguistic framing

---

## 2. Difficulty Tiers

- **Tier 1 (Simple Twist):** Recognizable with minor misdirection
- **Tier 2 (Cognitive Trap):** Requires reframing or deeper parsing
- **Tier 3 (Paradoxical Core):** Appears unsolvable until perspective shift
- **Tier 4 (Research Edge):** Open-problem style, useful for stress-testing reasoning models

---

## 3. Metadata Tags

Each problem instance should be annotated with:
- `category` (from Core Categories above)
- `tier` (1–4)
- `source` (human-generated, model-generated, hybrid)
- `status` (train, val, test, challenge, eval)
- `notes` (optional human commentary)

---

## 4. Usage Notes

This taxonomy is meant to be **extensible**.  
New categories or tiers can be added as anomalies evolve.  
When in doubt: document the reasoning trap clearly and tag conservatively.

---

© 2025 Helix Project AI — Licensed under Apache 2.0
