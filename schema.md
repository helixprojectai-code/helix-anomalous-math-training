# Schema --- Helix Anomalous Math Training

This document defines the schema for the anomalous math dataset,
ensuring consistency across training, validation, and evaluation splits.

## File Structure

-   `train/` --- Training set (bulk examples for model learning)
-   `val/` --- Validation set (for tuning hyperparameters)
-   `test/` --- Test set (for final evaluation)
-   `challenge/` --- Special cases and adversarial anomalies
-   `docs/` --- Supporting documentation (schema, taxonomy, protocol,
    etc.)

## Data Format

Each example in the dataset is stored as a JSON object with the
following fields:

``` json
{
  "id": "unique_identifier",
  "type": "algebraic|geometric|logical|numeric|creative",
  "difficulty": "easy|medium|hard|extreme",
  "prompt": "Problem statement as plain text",
  "solution": "Expected solution in plain text or structured form",
  "tags": ["list", "of", "tags"],
  "metadata": {
    "source": "human|synthetic|mixed",
    "created_by": "author or system",
    "date": "YYYY-MM-DD"
  }
}
```

## Example Entry

``` json
{
  "id": "ex-001",
  "type": "algebraic",
  "difficulty": "medium",
  "prompt": "Solve for x: 3x + 7 = 19",
  "solution": "x = 4",
  "tags": ["linear", "equations"],
  "metadata": {
    "source": "human",
    "created_by": "Starvibe",
    "date": "2025-08-28"
  }
}
```

## Notes

-   All files should be UTF-8 encoded.
-   Each dataset split (`train.jsonl`, `val.jsonl`, etc.) is stored in
    **JSON Lines** format, one object per line.
-   Challenge cases may include ambiguous, paradoxical, or creative
    formulations that do not have a single "correct" solution.

------------------------------------------------------------------------

© 2025 Helix Project AI --- Released under the Apache 2.0 License
