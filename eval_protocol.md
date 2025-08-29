# Evaluation Protocol — Helix Anomalous Math Training

This document describes the evaluation methodology for benchmarking models on the **Helix Anomalous Math Training** dataset.  
The goal is to provide **transparent, reproducible, and extensible** evaluation criteria.

---

## 1. Objectives

- Measure **accuracy** and **robustness** of language models on **non-standard math problems**.  
- Highlight performance gaps in:
  - Creative reasoning
  - Logical consistency
  - Handling of ambiguous or adversarial problem statements  
- Provide a **shared baseline** for researchers and practitioners.

---

## 2. Dataset Splits

- **Train Set** (`train.jsonl`)  
  Used for model fine-tuning or supervised training.  

- **Validation Set** (optional, can be split from train)  
  Used for hyperparameter tuning and early stopping.  

- **Test Set** (`test.jsonl`)  
  Used **only** for final evaluation and benchmarking.

---

## 3. Evaluation Metrics

### 3.1 Exact Match (EM)
- A prediction is correct if it **exactly matches** the ground-truth `solution` field.

### 3.2 Normalized Accuracy
- For numeric outputs: predictions are normalized (strip whitespace, remove formatting) before comparison.  
- For symbolic expressions: compare canonicalized forms (e.g., simplify algebra with `sympy`).

### 3.3 Partial Credit
- Some problems allow **multi-step reasoning**.  
- Credit may be awarded if intermediate steps are correct, even if final answer diverges.  

### 3.4 Robustness Score
- Evaluate how models respond to **trick questions** (tagged as `paradox`, `trick`, `adversarial`).  
- Score = % of cases where the model avoids “false confidence” (e.g., returns "undefined" when appropriate).

---

## 4. Baselines

- **Naive Baseline**: Random guessing or rule-based parsing.  
- **LLM Zero-Shot**: Direct prompting without fine-tuning.  
- **LLM Few-Shot**: Few in-context examples provided.  
- **Fine-Tuned Models**: Models trained directly on `train.jsonl`.

---

## 5. Reporting

When publishing results:  

1. **Report per-category accuracy** (`arithmetic`, `geometry`, `anomaly`, `creative`, etc.).  
2. **Include confidence calibration** — measure log-probability vs correctness.  
3. **Disclose evaluation setup**: model version, temperature, prompt template.  
4. **Release code + seeds** for reproducibility.

---

## 6. Example Evaluation Script

See [`loader.py`](loader.py) for data access.  
Evaluation scripts should:

```bash
python evaluate.py --model gpt-4 --test_file data/test.jsonl
