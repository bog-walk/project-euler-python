""" Problem 36: Double-Base Palindromes

https://projecteuler.net/problem=36

Goal: Find the sum of all natural numbers (without leading zeroes) less than N
that are palindromic in both base 10 and base K.

Constraints: 10 <= N <= 1e6 & 2 <= K <= 9

e.g.: N = 10, K = 2
      result = {(1, 1), (3, 11), (5, 101), (7, 111), (9, 1001)}
      sum = 25
"""
from util.strings.reusable import is_palindrome


def switch_base(n: int, base: int) -> str:
    """
    Converting from another base to base 10 is easily done using int(n, base).
    Converting from base 10 to base 2/8/16 is done using bin(n)/oct(n)/hex(n).

    Conversions above base 10 would risk inclusion of alphabet characters & would
    warrant storage of a character string to pull from.

    Note that numpy library also has an in-built function: base_repr(n, base).

    :returns: String representation of decimal converted to the specified base.
    """

    if base == 2:
        return bin(n)[2:]
    elif base == 8:
        return oct(n)[2:]
    else:
        result = ""
        while n > 0:
            result += str(n % base)
            n //= base
        return result[::-1]


def sum_of_palindromes_brute(n: int, k: int) -> int:
    """
    SPEED (WORSE)
        509.14s for N = 1e9, K = 2
    """

    total = 0
    for num in range(1, n):
        if is_palindrome(str(num)) and is_palindrome(switch_base(num, k)):
            total += num
    return total


def get_palindrome(n: int, base: int, odd: bool = True) -> int:
    """
    :returns: The nth odd-/even-length palindrome in the specified base.
        e.g. The 2nd odd-length base 2 palindrome is 101 == 5.
    """

    palindrome = n
    if odd:
        n //= base
    while n > 0:
        palindrome = palindrome * base + n % base
        n //= base
    return palindrome


def sum_of_palindromes(n: int, k: int) -> int:
    """
    Solution is optimised by only iterating over generated base-k palindromes less
    than N. This also means that, unlike in the brute force solution, only 1 number
    (the base-10 result) needs to be checked as a palindrome.

    SPEED (BETTER)
        220.00ms for N = 1e9, K = 2
    """

    total = 0
    odd_turn = True
    # generate both odd & even length palindromes
    for _ in range(2):
        i = 1
        while True:
            # generate decimal representation of base-k palindrome
            dec_repr = get_palindrome(i, k, odd_turn)
            # check if decimal is also a palindrome
            if is_palindrome(str(dec_repr)):
                total += dec_repr
            if dec_repr >= n:
                break
            i += 1
        odd_turn = False
    return total
