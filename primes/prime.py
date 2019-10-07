"""
Assignment 3 - Prime Factors

prime.py -- Write the application code here
"""

def generate_prime_factors(unprime):
    """
    This function will generate the prime factors of a provided integer
    """

    if isinstance(unprime, int) is False:
        raise ValueError
