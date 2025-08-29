# Schema --- Helix Anomalous Math Training

This document defines the schema for the anomalous math dataset, ensuring consistency across training, validation, and test splits.

## File Structure

- `train/` --- Training set (bulk examples for model learning)
- `val/` --- Validation set (for tuning hyperparameters)
- `test/` --- Test set (for final evaluation)
- `challenge/` --- Special cases and adversarial anomalies
- `docs/` --- Supporting documentation (schema, taxonomy, protocol, etc.)

## Data Format

Each example in the dataset is stored as a JSON object with the following fields:

```json
{
  "id": "unique_identifier",
  "category": "arithmetic|algebra|geometry|logic|probability|creative|meta-cognitive",
  "difficulty": "easy|medium|hard|challenge",
  "problem": "Problem statement as plain text",
  "solution": "Expected solution in plain text or structured form",
  "tags": ["list", "of", "tags"],
  "answer": "Optional final answer (numeric, string, or object)",
  "metadata": {
    "source": "Optional: human|synthetic|mixed",
    "created_by": "Optional: author or system",
    "date": "Optional: YYYY-MM-DD"
  }
}
