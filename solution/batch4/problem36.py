""" Problem 36: Double-Base Palindromes

https://projecteuler.net/problem=36

Goal: Find the sum of all natural numbers (without leading zeroes)
less than N that are palindromic in both base 10 and base K.

Constraints: 10 <= N <= 1e6 & 2 <= K <= 9

e.g.: N = 10, K = 2
      result = {(1, 1), (3, 11), (5, 101), (7, 111), (9, 1001)}
      sum = 25
"""
from util.strings.reusable import is_palindrome


def switch_base(n, base):
    """
    Converting from another base to base 10 is easily done using int(n, base).
    Converting from base 10 to base 2/8/16 is done using bin(n), oct(n), hex(n).
    Note that numpy also has an in-built function: base_repr(n, base).
    Conversions above base 10 would risk inclusion of alphabet characters & would
    warrant storage of a character string to pull from.

    :return: String representation of decimal converted to the specified base.
    """
    result = ""
    while n > 0:
        result += str(n % base)
        n //= base
    return result[::-1]


def sum_of_palindromes_brute(n, k):
    """
    Naive/Exhaustive iterative approach.

    SPEED (WORSE): 494.48s for N = 1e9, K = 2
    """
    total = 0
    for num in range(1, n):
        if is_palindrome(str(num)) and is_palindrome(switch_base(num, k)):
            total += num
    return total


def get_palindrome(n, base, odd: bool = True):
    """
    Generates the nth palindrome in the given base.
    e.g. The 2nd odd-length base 2 palindrome is 101 == 5.

    :return: Decimal representation of the nth odd-/even- length palindrome
    in the specified base.
    """
    palindrome = n
    if odd:
        n //= base
    while n > 0:
        palindrome = palindrome * base + n % base
        n //= base
    return palindrome


def sum_of_palindromes(n, k):
    """
    Using the helper method above avoids the need to iterate through every
    natural number less than N. Instead, loop elements are reduced to only
    generated base-k palindromes less than N. This also means that only 1
    number needs to be checked as a palindrome (the base-10 result).

    SPEED (BETTER): 0.18s for N = 1e9, K = 2
    """
    total = 0
    odd_turn = True
    # generate both odd & even length palindromes
    for _ in range(2):
        i = 1
        while True:
            # generate decimal repr of base-k palindrome
            dec_repr = get_palindrome(i, k, odd_turn)
            # check if decimal is also a palindrome
            if is_palindrome(str(dec_repr)):
                total += dec_repr
            if dec_repr >= n:
                break
            i += 1
        odd_turn = False
    return total
