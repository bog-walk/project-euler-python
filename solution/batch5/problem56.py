""" Problem 56: Powerful Digit Sum

https://projecteuler.net/problem=56

Goal: Considering natural numbers of the form :math:`a^b`, where a, b < N,
find the maximum digit sum.

Constraints: 5 <= N <= 200

Googol: A massive number that is 1 followed by 100 zeroes, i.e. :math:`10^100`.
Another unimaginably large number is :math:`100^100`, which is 1 followed by 200
zeroes. Despite both their sizes, the sum of each number's digits equals 1.

e.g.: N = 5
      :math:`4^4 = 256 \\to 2 + 5 + 6 = 13`
      max sum = 13
"""
from util.maths.reusable import power_digit_sum


def max_digit_sum(n: int) -> int:
    """
    While Python can calculate upper constraints in 1.6s, this solution is
    optimised, to 35ms for N = 200, by setting loop limits based on the pattern
    observed of the a, b combinations that achieved the maximum digit sums:

    -   a is never less than n / 2, even for outliers with large deltas, e.g. n =
        42 achieved a max sum at :math:`24^41`.

    -   b is never more than 5 digits less than n, e.g. n = 100 achieved a max sum
        at :math:`99^95`.
    """

    max_sum = 1
    min_a = n // 2
    min_b = max(1, n - 5)
    for a in range(min_a, n):
        for b in range(min_b, n):
            pds = power_digit_sum(a, b)
            max_sum = max(max_sum, pds)
    return max_sum
