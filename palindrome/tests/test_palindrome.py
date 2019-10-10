"""
Assignment 4: Palindrome Checker

The test module for the palindrome checker
"""

import pytest
from palindrome import is_palindrome

def test_is_string():
    """
    Test Requirement: `is_palindrome` raises a `ValueError` when not provided with a value
      that is  an instance of `str`.
    """

    with pytest.raises(ValueError):
        is_palindrome(1881)
