# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest
from prime import generate_prime_factors

def test_is_integer():
    """
    ### Step 1:
    Write a test that asserts that when `generate_prime_factors` is called with a
    data type that is not an integer (e.g. a string or float), a ValueError is
    raised. Write the appropriate code to solve this and then commit the changes.
    """
    with pytest.raises(ValueError):
        generate_prime_factors("hello")
