"""An example Python module."""

from typing import List

def total(values: List[float]) -> float:
    """Total returns the sum of values."""
    result: float = 0.0
    # For each x float in values, add it to result
    for item in values:
        result += item
    return result
