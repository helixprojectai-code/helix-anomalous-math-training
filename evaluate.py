# evaluate.py
import argparse
import re
from loader import AnomalousMathDataset
from typing import Dict, Any
try:
    import sympy
except ImportError:
    sympy = None  # Fallback to string comparison if sympy unavailable

def normalize_text(text: str) -> str:
    """Normalize text by stripping whitespace and converting to lowercase."""
    return re.sub(r'\s+', ' ', text.strip()).lower()

def is_symbolic_equivalent(pred: str, sol: str) -> bool:
    """Check if two expressions are symbolically equivalent using sympy."""
    if not sympy:
        return normalize_text(pred) == normalize_text(sol)
    try:
        pred_expr = sympy.sympify(pred)
        sol_expr = sympy.sympify(sol)
        return sympy.simplify(pred_expr - sol_expr) == 0
    except (sympy.SympifyError, TypeError):
        return normalize_text(pred) == normalize_text(sol)

def has_key_steps(pred: str, sol: str) -> float:
    """Check if prediction contains key steps from solution (basic regex-based)."""
    key_phrases = re.findall(r'[a-zA-Z0-9\s\-\+\*\/=]+', sol)
    matches = sum(1 for phrase in key_phrases if phrase in pred)
    return min(matches / max(len(key_phrases), 1), 1.0)

def evaluate_model(model, dataset: AnomalousMathDataset) -> Dict[str, Any]:
    if len(dataset) == 0:
        raise ValueError("Dataset is empty")
    
    results = {
        "exact_match": 0,
        "normalized_accuracy": 0,
        "partial_credit": 0,
        "robustness_score": 0,
        "by_category": {}
    }
    robust_count = 0
    
    for sample in dataset:
        category = sample["category"]
        results["by_category"].setdefault(category, {"correct": 0, "total": 0, "partial": 0})
        
        try:
            prediction = model.predict(sample["problem"])  # Placeholder for LLM call (e.g., xAI Grok API)
            solution = sample["solution"]
            
            # Exact Match
            if prediction == solution:
                results["exact_match"] += 1
                results["by_category"][category]["correct"] += 1
            
            # Normalized Accuracy
            if is_symbolic_equivalent(str(prediction), str(solution)):
                results["normalized_accuracy"] += 1
            
            # Partial Credit
            partial_score = has_key_steps(str(prediction), solution)
            results["partial_credit"] += partial_score
            results["by_category"][category]["partial"] += partial_score
            
            # Robustness Score (for paradox/trick questions)
            if any(tag in ["paradox", "trick"] for tag in sample["tags"]):
                robust_count += 1
                if "error" not in str(prediction).lower() and partial_score > 0.5:
                    results["robustness_score"] += 1
            
            results["by_category"][category]["total"] += 1
        
        except Exception as e:
            print(f"Error processing sample {sample['id']}: {e}")
            continue
    
    # Normalize results
    total_samples = len(dataset)
    results["exact_match"] /= total_samples
    results["normalized_accuracy"] /= total_samples
    results["partial_credit"] /= total_samples
    results["robustness_score"] /= max(robust_count, 1)  # Avoid division by zero
    for cat in results["by_category"]:
        results["by_category"][cat]["exact_match"] = results["by_category"][cat]["correct"] / results["by_category"][cat]["total"]
        results["by_category"][cat]["partial_credit"] = results["by_category"][cat]["partial"] / results["by_category"][cat]["total"]
    
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate model on Helix dataset")
    parser.add_argument("--model", help="Model name (e.g., grok-4)")
    parser.add_argument("--test_file", help="Path to test.jsonl")
    args = parser.parse_args()
    
    # Placeholder for LLM initialization (e.g., from xai_grok_api import GrokClient)
    model = None  # Replace with: model = GrokClient(model_name=args.model)
    if model is None:
        raise ValueError("Model not initialized. Please provide a valid model implementation.")
    
    dataset = AnomalousMathDataset(args.test_file)
    results = evaluate_model(model, dataset)
    print(f"Results: {results}")
