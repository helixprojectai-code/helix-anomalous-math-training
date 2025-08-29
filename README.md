# Helix Anomalous Math Training

An open dataset of **anomalous math problems** and **creative challenge cases**, developed under the Helix Project.  
Designed for training, benchmarking, and red-teaming large language models.  
Licensed under the Apache 2.0 License.

---

## Overview

Most math datasets focus on standard problem types (algebra, geometry, calculus, etc.).  
This repository explores the *edges* — problems that introduce twists, ambiguity, paradoxes, or symbolic anomalies.

The goal is twofold:
1. Provide **training material** that forces models to generalize beyond standard math drills.  
2. Offer **red-teaming challenges** to expose brittle reasoning or unexpected failure modes in language models.

---

## Structure

- `data/train/` → Training set (annotated anomalies, ~70%)  
- `data/val/` → Validation set (~15%)  
- `data/test/` → Held-out test set (~15%)  
- `schema/` → JSON/YAML schemas defining anomaly categories  
- `docs/` → Supporting documentation and taxonomy  

Each problem is stored as JSON with the following schema:

```json
{
  "id": "uuid",
  "type": "algebraic paradox",
  "problem": "If 1 = 2, what is 3?",
  "solution": "Undefined under standard arithmetic; anomaly case.",
  "tags": ["paradox", "logic", "consistency"]
}
```

---

## Anomaly Categories

The dataset includes (non-exhaustive):  
- Paradoxical equations  
- Infinite regressions  
- Category boundary violations  
- Creative twists (e.g., playful or metaphorical framing)  
- Symbolic confusions (glyph logic, ambiguous operators)  
- Cross-domain blends (math + language, math + physics)  

---

## Usage

### Training
```bash
git clone https://github.com/helixprojectai-code/helix-anomalous-math-training.git
cd helix-anomalous-math-training
python scripts/loader.py --split train
```

### Evaluation
```bash
python scripts/eval.py --model gpt-4o --split test
```

### Red-Teaming
Use `data/challenge/` to stress-test reasoning under ambiguous or adversarial cases.

---

## License

This project is licensed under the **Apache License 2.0**.  
See [LICENSE](./LICENSE) for details.  

---

## Contributing

Contributions are welcome!  
You can:  
- Suggest new anomaly types  
- Expand evaluation examples  
- Report issues via GitHub Issues  
- Submit PRs (target `dev` branch first)
