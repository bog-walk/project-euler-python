""" Problem 58: Spiral Primes

https://projecteuler.net/problem=58

Goal: By repeatedly completing a new layer on a square spiral grid, as detailed
below, find the side length at which the ratio of primes along both diagonals first
falls below N%.

Constraints: 8 <= N <= 60

Spiral Pattern: Start with 1 & move to the right in an anti-clockwise direction,
incrementing the numbers. This creates a grid with all odd squares (area of
odd-sided grid & therefore composite) along the bottom right diagonal.

e.g.: N = 60
      grid = *17*  16  15  14  *13*
              18  *5*  4  *3*   12
              19   6   1   2    11
              20  *7*  8   9    10
              21   22  23  24   25
      side length = 5, as 5/9 = 55.55% are prime
"""
from util.maths.reusable import is_prime, is_prime_mr


def spiral_prime_ratio(percent: int, speed_toggle: bool = False) -> int:
    """
    Generates new diagonal values (except bottom-right) using previous square
    spiral side length & checks their primality.

    A toggle parameter is included to compare performance using the original
    is_prime() helper and a newer Miller-Rabin algorithm version, especially
    meant for very large values. The diagonal values in this problem reach very
    high as the layers increase.

    e.g. side length 26241, at which point the ratio only just falls below 10%,
    has a bottom-right diagonal value of 688_590_081.

    :param percent: Integer value representing the percentage under which the
        ratio should first fall before returning the final result.
    :param speed_toggle: Default False for original is_prime() and True for the
        newer is_prime_mr(). This purely exists to allow speed tests on otherwise
        duplicate code.

    SPEED (ORIGINAL - WORSE)
        2.713s for N = 10
    SPEED (MILLER-RABIN - BETTER)
        0.313s for N = 10
    """

    prime_check = is_prime_mr if speed_toggle else is_prime
    ratio = percent / 100
    side, diagonals, primes = 3, 5, 3
    while ratio <= primes / diagonals:
        # check new diagonal elements of next layer using previous side length
        prev_area = side * side
        primes += sum(prime_check(prev_area + i * (side + 1)) for i in range(1, 4))
        side += 2
        diagonals += 4
    return side
