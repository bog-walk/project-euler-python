""" Problem 64: Odd Period Square Roots

https://projecteuler.net/problem=64

Goal: Count how many continued fraction representations of irrational square roots
of numbers <= N have an odd-length period (repeated sequence).

Constraints: 10 <= N <= 3e4

Square Root: This can be expressed as an infinite continued fraction ->

sqrt(N) = a_0 + 1/(a_1 + 1/(a_2 + 1/(...)))

e.g. sqrt(3) = 1 + 1/(1 + 1/(2 + 1/(...))) == [1;(1,2)]
Note that (1,2) is not a reptend, but the values of a_i for each infinite iteration.

e.g.: N = 10
      count = 3
      sqrt(2) = [1;(2)], sqrt(5) = [2;(4)], sqrt(10) = [3;(6)]
"""
from math import modf, sqrt


def odd_square_roots(num: int) -> int:
    """
    Solution is based on the expression of the square root of x:

    sqrt(x) = a + r/(a + sqrt(x))

    where a is the floored root (integer part) of x and r is the remainder
    (fractional part). Initialisation of the expression shows:

    sqrt(x) = 0 + (x - 0)/1 , with remainder numerator (n) = 0 & denominator (d) = 1

    if the floored root of x is substituted as a_0, the remainder can be found:

    n_k = d_{k-1} * a_{k-1} - n_{k-1}
    d_k = floor((x - (n_k)^2)/d_{k-1})

    thereby helping find the next a_1, which corresponds to the first period number,

    a_k = floor((a_0 + n_k)/d_k)

    These 3 values together will be unique unless the period has entered a new
    repeated sequence.

    N.B. A repeated loop will also be entered once a_k = 2 * a_0, which proves
    true in the solution, & can replace the list[tuples] loop break.
    """

    count = 0
    for x in range(2, num + 1):
        fractional, a_0 = modf(sqrt(x))
        if fractional == 0.0:  # skip perfect squares
            continue
        period = 0
        a, n, d = (a_0, 0, 1)
        visited: list[tuple] = []
        while True:
            n = d * a - n
            d = (x - n * n) // d
            a = (a_0 + n) // d
            expression = (a, n, d)
            if expression in visited:
                break
            visited.append(expression)
            period += 1
        if period % 2:
            count += 1
    return count
