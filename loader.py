#!/usr/bin/env python3
"""
Loader for the Helix Anomalous Math Training dataset.
Reads JSONL files (train/test), validates structure, and provides iteration utilities.

License: Apache 2.0
"""

import json
from pathlib import Path
from typing import Dict, Iterator, List, Any


class AnomalousMathDataset:
    REQUIRED_FIELDS = {"id", "category", "problem", "solution", "tags", "difficulty"}

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"Dataset file not found: {self.file_path}")

        self.samples: List[Dict[str, Any]] = []
        self._load()

    def _load(self) -> None:
        """Load and validate dataset file."""
        with self.file_path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON at line {line_no}: {e}") from e

                missing = self.REQUIRED_FIELDS - set(obj.keys())
                if missing:
                    raise ValueError(
                        f"Missing fields {missing} in {self.file_path}, line {line_no}"
                    )

                self.samples.append(obj)

    def __len__(self) -> int:
        return len(self.samples)

    def __iter__(self) -> Iterator[Dict[str, Any]]:
        return iter(self.samples)

    def filter_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Return samples matching a given category."""
        return [s for s in self.samples if s.get("category") == category]

    def filter_by_tag(self, tag: str) -> List[Dict[str, Any]]:
        """Return samples containing a given tag."""
        return [s for s in self.samples if tag in s.get("tags", [])]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Load and inspect the Helix Anomalous Math dataset."
    )
    parser.add_argument("file", help="Path to dataset file (e.g., train.jsonl)")
    parser.add_argument("--category", help="Filter by category", default=None)
    parser.add_argument("--tag", help="Filter by tag", default=None)

    args = parser.parse_args()

    dataset = AnomalousMathDataset(args.file)
    print(f"Loaded {len(dataset)} samples from {args.file}")

    if args.category:
        filtered = dataset.filter_by_category(args.category)
        print(f"Found {len(filtered)} samples in category '{args.category}'")

    if args.tag:
        filtered = dataset.filter_by_tag(args.tag)
        print(f"Found {len(filtered)} samples with tag '{args.tag}'")

