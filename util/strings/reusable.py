def is_palindrome(n: str) -> bool:
    """
    This version, not the 2 alternatives below, will be used
    in future solutions.

    SPEED (BEST): 7.0e-4s for 18-digit N over 1000 iterations.
    """

    return n == n[::-1]


def is_palindrome_recursive(n: str) -> bool:
    """
    SPEED (WORST): 6.1e-3s for 18-digit N over 1000 iterations.
    """

    digits = len(n)
    if digits < 2:
        return True
    elif n[0] == n[digits - 1]:
        return is_palindrome_recursive(n[1:digits - 1])
    else:
        return False


def is_palindrome_number(n: str) -> bool:
    """
    SPEED (BETTER): 4.6e-3s for 18-digit N over 1000 iterations.
    """

    num = int(n)
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return n == str(rev)


def is_pandigital(string: str, n: int) -> bool:
    """
    While its default arguement clears all leading/trailing whitespace,
    strip([chars]) removes characters from the left & right of the invoking string
    until none in the arguement match the left-/right-most character.

    This provides a trick to check whether a string contains only characters in
    another string, as, e.g. "1234".strip("4231") == "" == False.
    """

    return len(string) == n and not "1234567890"[:n].strip(string)
