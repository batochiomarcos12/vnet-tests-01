"""
An example of a test module in pytest
"""

from vnet_tests_01 import total

def test_total_empty() -> None:
    """Total of empty list should be 0.0"""
    assert total([]) == 0.0

def test_total_single_item() -> None:
    """Total of a single item list should be the first item's value."""
    assert total([110.0]) == 110.0

def test_total_many_items() -> None:
    """Total of a list with many items should be their sum."""
    assert total([1.0, 2.0, 3.0]) == 6.0

