""" Problem 23: Non-Abundant Sums

https://projecteuler.net/problem=23

Goal: Return whether N can be expressed as the sum of 2 abundant numbers.

Constraints: 0 <= N <= 1e5

Perfect Number: The sum of its proper divisors equals itself.
e.g. proper_D(6) = {1,2,3}.sum() = 6

Deficient Number: The sum of its proper divisors is less than itself.
e.g. proper_D(4) = {1, 2}.sum() = 3

Abundant Number: The sum of its proper divisors exceeds itself.
e.g. proper_D(12) = {1,2,3,4,6}.sum() = 16

By mathematical analysis, all integers > 28123 can be expressed as the sum of 2
abundant numbers. This upper limit cannot, however, be reduced further even though
it is known that the largest number that cannot be expressed as the sum of 2
abundant numbers is less than this upper limit.

e.g.: N = 24
      smallest abundant number = 12,
      so smallest integer that can be expressed = 12 + 12 = 24
      result = True
"""
from itertools import chain
from util.maths.reusable import sum_proper_divisors


def is_abundant(n: int) -> bool:
    return sum_proper_divisors(n) > n


def is_sum_of_abundants(n: int) -> bool:
    """
    Solution is optimised based on:

    -   12 being the smallest abundant number to exist, so the smallest integer
        expressed as a sum of abundants is 24.

    -   945 being the smallest odd abundant number.

    -   An odd number has to be the sum of an even & odd number, so all odd numbers
        under 957 (945 + 12) cannot be the sum of abundants, since all other
        abundants below 945 are even.

    -   All integers > 20161 can be expressed as sum of 2 abundant numbers, shown in
        final test case, test_all_integers_expressed(self).

    -   x_max of x + y = N would be N / 2, to avoid duplicate checks.
    """

    if n < 24 or (n < 957 and n % 2):
        # in Python, n % 2 != 0 is equivalent to being True
        return False
    if n > 20161:
        return True
    x_max = n // 2
    # could consider removing prime numbers > 944 from loop as primes
    # cannot be abundant numbers, but the speed difference is negligible.
    loop_range = range(12, x_max + 1, 2) if x_max < 945 else chain(
        range(12, 945, 2), range(945, x_max + 1)
    )
    for x in loop_range:
        if is_abundant(x) and is_abundant(n - x):
            return True
    return False


def sum_of_all_non_abundants() -> int:
    """
    Project Euler specific implementation meant to find the sum of all positive
    integers that cannot be written as the sum of 2 abundant numbers.

    N.B. The final test case, test_all_integers_expressed(self), shows that 20161
    is the largest integer that cannot be expressed as such, even though 28123 is
    provided as the upper limit.
    """

    return sum(
        map(
            lambda n: n if not is_sum_of_abundants(n) else 0,
            range(20162)
        )
    )
