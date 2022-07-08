""" Problem 4: Largest Palindrome Product

https://projecteuler.net/problem=4

Goal: Find the largest palindrome less than N that is made from the product of
two 3-digit numbers.

Constraints: 101_101 < N < 1e6

e.g.: N = 800_000
      869 * 913 = 793_397
"""
from math import isqrt
from util.strings.reusable import is_palindrome


def largest_palindrome_product_brute(n: int) -> int:
    """
    Brute iteration through all products of 3-digit numbers while storing the
    largest confirmed palindrome product so far.

    SPEED (WORST)
        78.56ms for N = 999_999
    """

    largest = 0
    for x in range(101, 1000):
        for y in range(x, 1000):
            product = x * y
            if product >= n:
                break
            if product > largest and is_palindrome(str(product)):
                largest = product
    return largest


def largest_palindrome_product_brute_backwards(n: int) -> int:
    """
    Brute iteration through all products of 3-digit numbers starting with the
    largest numbers and terminating the inner loop early if product starts to
    get too small.

    SPEED (WORSE)
        2.56ms for N = 999_999
    """

    largest = 0
    for x in range(999, 100, -1):
        for y in range(999, x-1, -1):
            product = x * y
            # combo will be too small to pursue further
            if product <= largest:
                break
            if product < n and is_palindrome(str(product)):
                largest = product
                break
    return largest


def largest_palindrome_product(n: int) -> int:
    """
    A palindrome of the product of two 3-digit integers can be at most 6-digits
    long & one of the integers must be a multiple of 11, based on the following
    algebra:

    P = 100_000x + 10_000y + 1000z + 100z + 10y + x

    P = 100_001x + 10_010y + 1100z

    P = 11*(9091x + 910y + 100z)

    Rather than stepping down to each palindrome & searching for a valid product,
    this solution tries all product combos that involve one of the integers being
    a multiple of 11.

    SPEED (BETTER)
        5.9e+05ns for N = 999_999
    """

    largest = 0
    x = 999
    while x > 100:
        y, delta_y = (999, 1) if x % 11 == 0 else (990, 11)
        while y >= x:
            product = y * x
            if product <= largest:
                # combo will be too small to pursue
                break
            if product < n and is_palindrome(str(product)):
                largest = product
            y -= delta_y
        x -= 1
    return largest


def num_to_palindrome(n: int) -> int:
    """
    Converts a 3-digit integer to a 6-digit palindrome.
    """

    return n * 1000 + n % 10 * 100 + n // 10 % 10 * 10 + n // 100


def is_3dig_product(n: int) -> bool:
    for factor_1 in range(999, isqrt(n) - 1, -1):
        if n % factor_1 == 0 and n // factor_1 in range(101, 1000):
            return True
    return False


def largest_palindrome_product_alt(n: int) -> int:
    """
    Brute iteration through all palindromes less than NS checks if each
    palindrome could be a valid product of two 3-digit numbers.

    SPEED (BEST)
        3.2e+05ns for N = 999_999
    """

    if num_to_palindrome(n // 1000) > n:
        n = n // 1000 - 1
    else:
        n //= 1000
    while n > 101:
        palindrome = num_to_palindrome(n)
        if is_3dig_product(palindrome):
            return palindrome
        n -= 1
    return 101_101
