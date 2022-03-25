""" Problem 80: Square Root Digital Expansion

https://projecteuler.net/problem=80

Goal: For the first N natural numbers, find the total of the digit sums of the
first P digits for all irrational square roots x, such that x <= N. Note that
this includes digits before & after the decimal point.

Constraints: 1 <= N <= 1e3 && 1 <= P <= 1e3 OR
             1 <= N <= 100 && 1 <= P <= 1e4

e.g.: N = = 2, P = 20
      sqrt(1) = 1 (not irrational)
      sqrt(2) = 1.4142135623730950488...
      total = 76
"""
from decimal import getcontext, Decimal
from math import sqrt


def irrational_square_digit_sum(n: int, p: int) -> int:
    """
    Solution takes advantage of the decimal module's intrinsic precision
    capabilities to return a value of sqrt(n) that has only p digits.

    Since Decimal class precision involves only digits after the decimal point,
    the precision is set to exceed p. This means the String version of the
    calculated root has to be truncated to the requested size before summing the
    digits.

    SPEED (WORSE)
        5.53s for N = 100, P = 1e4
    """

    precision = getcontext()
    # max N is 1000, so max sqrt has 2 digits before the decimal point & an extra
    # 8 digits should prevent any rounding issues when sqrt() is performed
    precision.prec = p + 10
    total = 0
    for num in range(2, n + 1):
        if sqrt(num) % 1 == 0.0:  # skip perfect squares
            continue
        root = Decimal(num).sqrt(precision)
        # truncate string to requested size plus 1 for the point character
        total += sum(int(d) for d in str(root)[:p+1] if d != '.')
    return total


def irrational_square_digit_sum_improved(n: int, p: int) -> int:
    """
    Solution follows the same idea as the original above, except for the following:

    - All square roots are cached in an array to allow quick access for future
    calculations.

    - The square root of a number is only calculated if the number is prime.
    Otherwise, it is calculated using the product of the cached square roots of
    its prime factors. Any potential rounding errors from this multiplication will
    be offset by the precision of each cached root being set to exceed p.

    SPEED (BETTER)
        1.71s for N = 100, P = 1e4
    """

    precision = getcontext()
    precision.prec = p + 10
    all_roots = [Decimal(0)]*(n + 1)
    total = 0
    for num in range(2, n + 1):
        approx = 1
        while approx * approx < num:
            approx += 1
        if approx * approx == num:
            # store then skip perfect squares
            all_roots[num] = Decimal(approx)
            continue
        factor = approx - 1
        while num % factor:
            factor -= 1
        if factor > 1:
            # if num is composite, multiply the first factors found
            root = all_roots[factor] * all_roots[num//factor]
        else:
            # if num is prime, calculate the root
            root = Decimal(num).sqrt(precision)
        all_roots[num] = root
        total += sum(int(d) for d in str(root)[:p+1] if d != '.')
    return total
