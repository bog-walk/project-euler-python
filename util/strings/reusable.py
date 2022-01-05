def is_palindrome(n: str) -> bool:
    """
    This version, not the 2 alternatives below, will be used
    in future solutions.

    SPEED (BEST): 7.0e-4s for 18-digit N tested 1000 times
    """
    return n == n[::-1]


def is_palindrome_recursive(n: str) -> bool:
    """
    SPEED: 6.1e-3s for 18-digit N tested 1000 times
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
    SPEED: 4.6e-3s for 18-digit N tested 1000 times
    """
    num = int(n)
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return n == str(rev)
