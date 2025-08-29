# evaluate.py
import argparse
from loader import AnomalousMathDataset
from typing import Dict, Any

def evaluate_model(model, dataset: AnomalousMathDataset) -> Dict[str, float]:
    results = {"exact_match": 0, "normalized_accuracy": 0}
    for sample in dataset:
        prediction = model.predict(sample["problem"])  # Placeholder for LLM call
        if prediction == sample["solution"]:
            results["exact_match"] += 1
        # Add normalized accuracy, partial credit, robustness logic
    results["exact_match"] /= len(dataset)
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate model on Helix dataset")
    parser.add_argument("--model", help="Model name (e.g., grok-4)")
    parser.add_argument("--test_file", help="Path to test.jsonl")
    args = parser.parse_args()
    dataset = AnomalousMathDataset(args.test_file)
    results = evaluate_model(args.model, dataset)
    print(f"Results: {results}")
