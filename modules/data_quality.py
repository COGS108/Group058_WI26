"""Reusable data-quality checks for the project checkpoints."""

from __future__ import annotations

from typing import Any, Dict


def checkpoint_summary(df: Any) -> Dict[str, Any]:
    """Return core data-quality stats for a dataframe-like object."""
    return {
        "rows": int(len(df)),
        "cols": int(df.shape[1]),
        "duplicate_rows": int(df.duplicated().sum()),
        "missing_by_col": df.isna().sum().sort_values(ascending=False).to_dict(),
    }
