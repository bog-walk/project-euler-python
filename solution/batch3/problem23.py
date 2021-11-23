""" Problem 23: Non-Abundant Sums

https://projecteuler.net/problem=23

Goal: Return whether or not N can be expressed as the sum of 2 abundant numbers.

Constraints: 0 <= N <= 1e5

Perfect Number: the sum of its proper divisors equals itself.
e.g. proper_D(6) = {1,2,3}.sum() = 6

Deficient Number: the sum of its proper divisors is less than itself.
e.g. proper_D(4) = {1, 2}.sum() = 3

Abundant Number: the sum of its proper divisors exceeds itself.
e.g. proper_D(12) = {1,2,3,4,6}.sum() = 16

By mathematical analysis, all integers > 28123 can be expressed as the sum
of 2 abundant numbers. This upper limit cannot, however, be reduced further
even though it is known that the largest number that cannot be expressed as
the sum of 2 abundant numbers is less than this upper limit.

e.g.: N = 24
      smallest abundant number = 12,
      so smallest integer that can be expressed = 12 + 12 = 24
      result = True
"""
from itertools import chain
from util.reusable import sum_proper_divisors


def is_abundant(n):
    return sum_proper_divisors(n) > n


def is_sum_of_abundants(n):
    """
    This solution is optimised based on:
    - 12 being the smallest abundant number to exist, so the smallest
    integer expressed as a sum of abundants is 24.
    - 945 being the smallest odd abundant number.
    - An odd number has to be the sum of an even & odd number, so
    all odd numbers under 957 (945 + 12) cannot be the sum of abundants,
    since all abundants below it will be even.
    - All integers > 20161 can be expressed as sum of 2 abundant numbers.
    - x_max of x + y = N would be N / 2, to avoid duplicate checks.
    """
    if n < 24 or (n < 957 and n % 2):
        # In Python, n % 2 != 0 is equivalent to being True
        return False
    if n > 20161:
        return True
    x_max = n // 2
    # Could consider removing prime numbers > 944 from loop as primes
    # cannot be abundant numbers, but the speed difference is negligible.
    loop_range = range(12, x_max + 1, 2) if x_max < 945 else chain(
        range(12, 945, 2), range(945, x_max + 1)
    )
    for x in loop_range:
        if is_abundant(x) and is_abundant(n - x):
            return True
    return False


def sum_of_all_non_abundants():
    """
    Project Euler specific solution meant to find the sum of all
    positive integers that cannot be written as the sum of 2 abundant numbers.
    NOTE: 20161 being the largest integer that cannot be expressed as such
    is shown in the final test case.
    """
    return sum(map(lambda n: n if not is_sum_of_abundants(n) else 0, range(20162)))
