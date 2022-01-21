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
from random import randint
from util.maths.reusable import is_prime


def is_prime_mr(num: int, k: int = 5) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    def miller_rabin(d: int, n: int) -> bool:
        a = 2 + randint(1, n - 4)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = x * x % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d_r = num - 1
    while d_r % 2 == 0:
        d_r //= 2
    for _ in range(k):
        if not miller_rabin(d_r, num):
            return False
    return True


def spiral_prime_ratio(percent: int) -> int:
    limit = percent / 100
    n, side, diagonals, primes = 1, 3, 5, 3
    while limit <= primes / diagonals:
        n += 1
        side = 2 * n + 1
        diagonals += 4
        area = side * side
        primes += sum(is_prime(area - (side - 1) * i) for i in range(1, 4))
        # print(f"Side {side} -> {primes / diagonals * 100}%")
    return side


def spiral_prime_ratio_mr(percent: int) -> int:
    limit = percent / 100
    n, side, diagonals, primes = 1, 3, 5, 3
    while limit <= primes / diagonals:
        n += 1
        side = 2 * n + 1
        diagonals += 4
        area = side * side
        primes += sum(is_prime_mr(area - (side - 1) * i) for i in range(1, 4))
        # print(f"Side {side} -> {primes / diagonals * 100}%")
    return side
