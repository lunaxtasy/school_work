def is_palindrome(word):
    """
    This function checks to see if an entered string is a palindrome or not.

    Returns True for palindromes and False for non-palindromes
    """

    #string checker, will raise ValueError if anything else but a string

    if isinstance(word, str) is False:
        raise ValueError