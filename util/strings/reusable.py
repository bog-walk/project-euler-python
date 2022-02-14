def is_palindrome_recursive(n: str) -> bool:
    """
    SPEED (WORST)
        6.3e4ns for 18-digit N
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
    SPEED (BETTER)
        3.3e4ns for 18-digit N
    """

    num = int(n)
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return n == str(rev)


def is_palindrome(n: str) -> bool:
    """ This version will be used in future solutions.

    SPEED (BEST)
        5000ns for 18-digit N
    """

    return n == n[::-1]


def is_pandigital(string: str, n: int) -> bool:
    """ Checks if a string contains all digits between 1 and n inclusive.

    While its default argument clears all leading/trailing whitespace,
    strip([chars]) removes characters from the left & right of the invoking string
    until none in the argument match the left-/right-most character.

    This provides a trick to check whether a string contains only characters in
    another string, as, e.g. "1234".strip("4231") == "" == False.
    """

    return len(string) == n and not "1234567890"[:n].strip(string)
