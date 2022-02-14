""" Problem 57: Square Root Convergents

https://projecteuler.net/problem=57

Goal: Given N, in the 1st N expansions of the square root of 2's infinite continued
fraction, find the iteration numbers where the numerator has more digits than the
denominator.

Constraints: 8 <= N <= 1e4

Square Root of 2: This can be expressed as an infinite continued fraction ->

Iteration 1 -> sqrt(2) = 1 + 1/2 = 3/2 = 1.5
Iteration 2 -> 1 + 1/(2 + 1/2) = 7/5 = 1.4
Iteration 3 -> 1 + 1/(2 + (1/(2+1/2))) = 17/12 = 1.41666...
Iteration 4 -> 1 + 1/(2 + (1/(2 + 1/(2 + 1/2)))) = 41/29 = 1.41379...

The next 4 expansions are 99/70, 239/169, 577/408, 1393/985. The latter 8th
expansion is the 1st expansion where the number of digits in the numerator exceed
that of the denominator.

e.g.: N = 14
      iterations = [8, 13]
      expansions are: 1393 / 985 and 114243 / 80782
"""
from math import gcd, lcm, log10


def add_fractions(n_1: int, d_1: int, n_2: int, d_2: int) -> (int, int):
    """ Add 2 fractions manually and return in a reduced form.

    :returns: Tuple of (numerator, denominator).
    """

    denominator = lcm(d_1, d_2)
    numerator = denominator // d_1 * n_1 + denominator // d_2 * n_2
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def square_root_fractions_manual(n: int) -> list[int]:
    """
    The infinite continued fractional part is repeatedly calculated by adding its
    previous value to 2 (= 4/2) then dividing 1 by the result, simply by swapping
    the numerator and denominator. The result is then added to 1.

    e.g. 3rd iteration, with 2nd iteration fractional part = 2/5:
         1 + (1 / (4/2 + 2/5)) = 1 + (1 / (12/5))
         fractional part becomes 5/12
         expansion = 1 + 5/12 = 17/12

    Number of digits is compared by calling log10() instead of casting to
    string. Remember that log_10(10) = 1.0 because 10^1 = 10 and
    every 2-digit number will be a fraction between 1 and 2. Casting the result
    to int truncates the float, leaving only the integral part.

    SPEED (WORSE)
        316.50ms for N = 2e3

    :returns: List of integers representing the iteration where number of
        digits in the numerator exceeds number of digits in the denominator.
    """

    iterations = []
    inf_n, inf_d = 1, 2  # 1st iteration fractional part
    for i in range(2, n + 1):
        # continued fraction of 1 / (2 + previous fraction)
        inf_n, inf_d = add_fractions(4, 2, inf_n, inf_d)[::-1]
        numerator, denominator = add_fractions(1, 1, inf_n, inf_d)
        if int(log10(numerator)) > int(log10(denominator)):
            iterations.append(i)
    return iterations


def square_root_fractions_optimised(n: int) -> list[int]:
    """
    Solution optimised based on the following:

    -   Further reducing the above formula:
        if a_0 = 1 + 1/2, a_1 = 1 + 1/(2 + 1/2)
        then a_(i+1) = 1 + 1/(1 + a_i)

        if a_i = n_i / d_i is inserted, the formula becomes:

        a_(i+1) = (2d_i + n_i) / (d_i + n_i)

    -   Storing the ceiling for current number of digits, i.e. 10 for 1-digit
        numbers, 100 for 2-digit numbers, etc. This is compared instead of
        repeatedly calling log10().

    SPEED (BETTER)
        2.72ms for N = 2e3

    :returns: List of integers representing the iteration where number of
        digits in the numerator exceeds number of digits in the denominator.
    """

    iterations = []
    inf_n, inf_d = 3, 2  # 1st iteration expansion
    n_ceil, d_ceil = 10, 10  # both start as 1-digit numbers
    for i in range(2, n + 1):
        inf_n, inf_d = 2 * inf_d + inf_n, inf_n + inf_d
        if inf_n >= n_ceil:
            n_ceil *= 10
        if inf_d >= d_ceil:
            d_ceil *= 10
        if n_ceil > d_ceil:
            iterations.append(i)
    return iterations
