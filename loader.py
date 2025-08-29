#!/usr/bin/env python3
"""
Loader for the Helix Anomalous Math Training dataset.
Reads JSONL files (train/test), validates structure, and provides iteration utilities.

License: Apache 2.0
"""

import json
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional
from argparse import ArgumentParser

class AnomalousMathDataset:
    REQUIRED_FIELDS = {"id", "category", "problem", "solution", "tags", "difficulty"}

    def __init__(self, file_path: str) -> None:
        self.file_path = Path(file_path)
        self.samples: List[Dict[str, Any]] = []
        self._load()

    def _load(self) -> None:
        if not self.file_path.exists():
            raise FileNotFoundError(f"Dataset file {self.file_path} not found")
        with self.file_path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    missing = self.REQUIRED_FIELDS - set(obj.keys())
                    if missing:
                        raise ValueError(f"Missing fields {missing} in {self.file_path}, line {line_no}")
                    self.samples.append(obj)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON at line {line_no}: {e}") from e

    def __len__(self) -> int:
        return len(self.samples)

    def __getitem__(self, idx: int) -> Dict[str, Any]:
        return self.samples[idx]

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        return iter(self.samples)

    def stats(self) -> Dict[str, Any]:
        """Return dataset statistics (category and difficulty counts)."""
        categories = {}
        difficulties = {}
        for sample in self.samples:
            cat = sample["category"]
            diff = sample["difficulty"]
            categories[cat] = categories.get(cat, 0) + 1
            difficulties[diff] = difficulties.get(diff, 0) + 1
        return {"categories": categories, "difficulties": difficulties}

    def filter_by_category(self, category: str) -> "AnomalousMathDataset":
        new_dataset = AnomalousMathDataset.__new__(AnomalousMathDataset)
        new_dataset.file_path = self.file_path
        new_dataset.samples = [s for s in self.samples if s["category"] == category]
        return new_dataset

def main():
    parser = ArgumentParser(description="Inspect Helix anomalous math dataset")
    parser.add_argument("file_path", help="Path to JSONL dataset file")
    parser.add_argument("--category", help="Filter by category")
    args = parser.parse_args()

    dataset = AnomalousMathDataset(args.file_path)
    if args.category:
        dataset = dataset.filter_by_category(args.category)
    print(f"Dataset: {args.file_path}")
    print(f"Number of samples: {len(dataset)}")
    print(f"Stats: {dataset.stats()}")

if __name__ == "__main__":
    main()
