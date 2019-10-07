"""
Assignment 3 - Prime Factors

prime.py -- Write the application code here
"""

def generate_prime_factors(unprime):
    """
    This function will generate the prime factors of a provided integer

    Hopefully
    """

    if isinstance(unprime, int) is False:
        raise ValueError

    factors = []

    #for calls of 1, which is not prime
    while unprime < 2:
        break
    #for calls of 2, which is prime
    else:
        i = 2
        if i == unprime:
            if unprime % i == 0: #checking that the remainder is 0
                factors.append(i)

    return factors
