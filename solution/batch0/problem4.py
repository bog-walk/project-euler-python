""" Problem 4: Largest Palindrome Product

https://projecteuler.net/problem=4

Goal: Find the largest palindrome less than N that is made from the product of
two 3-digit numbers.

Constraints: 101_101 < N < 1e6

e.g.: N = 800_000
      869 * 913 = 793_397
"""
from util.strings.reusable import is_palindrome


def largest_palindrome_product(n: int) -> int:
    """
    A palindrome of the product of two 3-digit integers must be 6-digits long &
    one of the integers must be a multiple of 11, based on the following algebra:

    P = 100_000x + 10_000y + 1000z + 100z + 10y + x

    P = 100_001x + 10_010y + 1100z

    P = 11 * (9091x + 910y + 100z)
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
