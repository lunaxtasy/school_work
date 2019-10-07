# pylint: disable=missing-docstring
"""
Assignment 3 - Prime Factor Test File

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
        generate_prime_factors("test")

def test_empty_list():
    """
    ### Step 2:
    Write a test that asserts that when `generate_prime_factors` is called with
    `1`, an empty list is returned. Solve & commit.
    """
    generate_prime_factors(1)

    assert generate_prime_factors(1) == []

def test_list_of_two():
    """
    ### Step 3:
    Write a test that asserts that when `generate_prime_factors` is called with
    `2`, the list `[2]` is returned. Solve & commit.
    """
    generate_prime_factors(2)

    assert generate_prime_factors(2) == [2]

def test_list_of_three():
    """
    ### Step 4:
    Write a test that asserts that when `generate_prime_factors` is called with
    `3`, the list `[3]` is returned. Solve & commit.
    """

    generate_prime_factors(3)

    assert generate_prime_factors(3) == [3]

def test_factor_four():
    """
    ### Step 5:
    Write a test that asserts that when `generate_prime_factors` is called with
    `4`, the list `[2, 2]` is returned. Solve & commit.
    """

    generate_prime_factors(4)

    assert generate_prime_factors(4) == [2, 2]

def test_factor_six():
    """
    ### Step 6:
    Write a test that asserts that when `generate_prime_factors` is called with
    `6`, the list `[2, 3]` is returned. Solve & commit.
    """

    generate_prime_factors(6)

    assert generate_prime_factors(6) == [2, 3]
