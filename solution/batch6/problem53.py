""" Problem 53: Combinatoric Selections 

https://projecteuler.net/problem=53

Goal: Count the values of C(n, r), for 1 <= n <= N, that are
greater than K. Values do not have to be distinct.

Constraints: 2 <= N <= 1000, 1 <= K <= 1e18

Binomial Coefficient: C(n, r) = n! / (r! * (n - r)!), where r <= n.
There are 10 combinations when 3 digits are chosen from 5 digits,
with no repetition & order not mattering: C(5, 3) = 10.
It is not until n = 23 that the amount of combinations first
exceeds 1e6, namely C(23, 10) = 1_144_066.

e.g.: N = 23, K = 1e6
      answer = 4
"""
from math import factorial

# Acceptable in PY due to overflow not being an issue, since
# 13! overflows 32 bits and 21! overflows 64 bits and
# 59! > 1e80 (postulated to be the number of particles in the universe).
factorials = [factorial(i) for i in range(1001)]


def binomial_coefficient(n, r):
    return factorials[n] // (factorials[r] * factorials[n - r])


def count_large_combinatorics(n, k):
    """
    Solution optimised based on the symmetry of Pascal's Triangle:

    - C(n, 0) = 1 & C(n, 1) = n. k could be less than n, so must start
    r-loop at 1.

    - C(n, r) = C(n, n-r) & peaks for each row at the mid-point.

    - So if C(n, r) > k, then all C(n, x) for x in [r+1, n-r] will also be > k.
    Based on the incrementing row count (n + 1), this can be calculated as
    n - 2 * r + 1, so the rest of the row values do not need to be also calculated.

    - Starting from the bottom of the triangle & moving up, if no value in a row
    is greater than k, then no row (of lesser n) will have valid values & the
    outer loop can be broken.

    SPEED (WORSE): 0.0485s for N = 1e3, K = 1e3 over 10 iterations
    """
    count = 0
    not_found = False
    while n > 0:
        for r in range(1, n // 2 + 1):
            if binomial_coefficient(n, r) > k:
                count += n - 2 * r + 1
                break
            if r == n // 2:
                not_found = True
        if not_found:
            break
        n -= 1
    return count


def count_large_combinatorics_improved(n, k):
    """
    Solution improved by not depending on factorials to pre-compute the
    binomial coefficient, thereby also needing types that can handle >64 bits.

    Solution is still based on the symmetry of Pascal's Triangle & its
    rules as detailed in the function above, with some additions:

    - C(n, r+1) = C(n, r) * ((n-r) / (r+1)) and C(n-1, r) = C(n, r) * ((n-r) / n).
    Movement through the triangle (bottom-up & only checking border values) mimics
    that in the above function, but C(n, r) values when moving right in a row or up
    a row are determined with these formulae, instead of factorials.

    - Starting from the bottom of the triangle & moving up, if the value of r is
    allowed to exceed its midline value, then it means no value > k was found and
    the outer loop can be broken.

    SPEED (BETTER): 0.0049s for N = 1e3, K = 1e3 over 10 iterations
    """
    count = 0
    r, n_c_r = 0, 1  # start at left-most border
    while r <= n // 2:
        next_in_row = n_c_r * (n - r) // (r + 1)
        if next_in_row > k:
            # count formula differs from above function
            # because r is 1 less than r in next_in_row
            count += n - 2 * r - 1
            n_c_r = n_c_r * (n - r) // n
            n -= 1
        else:
            r, n_c_r = r + 1, next_in_row
    return count
