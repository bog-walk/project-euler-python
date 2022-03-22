""" Problem 71: Ordered Fractions

https://projecteuler.net/problem=71

Goal: By listing the set of reduced proper fractions for d <= N in ascending
order of size, find the numerator and denominator of the fraction immediately to
the left of n/d.

Constraints: 1 <= n < d <= 1e9, gcd(n, d) == 1, d < N <= 1e15

Reduced Proper Fraction: A fraction n/d, where n & d are positive integers,
n < d, and gcd(n, d) == 1.

Farey Sequence: A sequence of completely reduced fractions, either between 0 and
1, or which when in reduced terms have denominators <= N, arranged in order of
increasing size. The sequence optionally begins with 0/1 and ends with 1/1 if
restricted. The middle term of a Farey sequence is always 1/2 for N > 1.

        e.g. if d <= 8, the Farey sequence would be ->
             1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5,
             5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

e.g.: N = 8, n = 3, d = 7
      ans = 2/5
"""
from fractions import Fraction
from math import gcd


def left_farey_neighbour(limit: int, n: int, d: int) -> tuple[int, int]:
    """
    Solution finds Farey sequence neighbours based on the following:

    If a/b and n/d are neighbours, with a/b < n/d, then their difference:

    n/d - a/b = (nb - ad)/(db)

    with nb - ad = 1, it becomes ->

    n/d - a/b = 1/(db)

    A mediant fraction can be found between 2 neighbours using:

    p/q = (a + n)/(b + d)

    This solution could also be implemented similarly using a Stern-Brocot Tree
    fraction search algorithm that uses binary search to recursively find the
    target fraction n/d starting from the left & right ancestors, 0/1 & 1/0. Once
    found, the last left boundary is used with the target to find all mediants
    until a new mediant's denominator exceeds limit.

    SPEED (WORSE)
        12.03s for N = 1e7
    SPEED (Impossible for N > 1e10)

    :returns: Tuple of (numerator, denominator) representing the fraction to the
        left of n/d.
    """

    upper_bound = Fraction(n, d)
    lower_bound = Fraction(n, d + 1) if d != limit else Fraction(n - 1, d)
    half = Fraction(1, 2)
    if lower_bound < half < upper_bound:
        lower_bound = half
    neighbour = Fraction()
    while True:
        delta = upper_bound - lower_bound
        neighbour_delta = Fraction(1, lower_bound.denominator * d)
        if delta == neighbour_delta:
            neighbour = lower_bound
        lower_bound = Fraction(
            lower_bound.numerator + n,
            lower_bound.denominator + d
        )
        if lower_bound.denominator > limit and neighbour != Fraction():
            break
    return neighbour.numerator, neighbour.denominator


def compare_fractions(
        fraction_a: tuple[int, int],
        fraction_b: tuple[int, int]
) -> int:
    """
    Rather than compare Doubles, whole numbers are compared based on the
    property that:

    if a/b < n/d, then ad < bn

    :returns: -1 if fraction_a < fraction_b; 1 if fraction_a > fraction_b; 0 if
        both equal.
    """

    left = fraction_a[0] * fraction_b[1]
    right = fraction_a[1] * fraction_b[0]
    if left == right:
        return 0
    return -1 if left < right else 1


def reduce_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def left_farey_neighbour_improved(limit: int, n: int, d: int) -> tuple[int, int]:
    """
    Solution improved based on the following:

    For each denominator b up to N, the only fraction that needs to be considered
    is the one with the largest numerator a for which a/b < n/d.

    a/b < n/d becomes ad < bn, which means ad <= bn - 1

    a <= floor((bn - 1)/d)

    for b <= N, floor((bn - 1)/d)/b is the largest fraction.

    Fractions with larger denominators are spaced more closely than those with
    smaller denominators, so iterating backwards starting at N means the largest
    neighbour below n/d will be found sooner. The loop is broken based on the
    aforementioned property that:

    the difference between 2 neighbours is given as 1/(db)

    for a new fraction r/s to be closer to n/d than a/b ->

    1/(ds) < (nb - da)/(db) -> s > b/(nb - da)

    if delta = nb - da = 1, this means s > b, & the loop can be broken as all
    denominators between b and N have already been examined.

    N.B. Using the Fraction class from the fractions library is helpful as an
    instance intrinsically reduces itself & comparisons & arithmetic operations
    are more easily implemented; however, its use reduced the execution speed to
    405.98s for N = 1e15, a ~4x reduction in performance.

    SPEED (BETTER)
        3.9e4ns for N = 1e7
    SPEED (BETTER)
        93.99s for N = 1e15

    :returns: Tuple of (numerator, denominator) representing the fraction to the
        left of n/d.
    """

    closest_neighbour = 0, 1
    b = limit  # current denominator starts at provided limit
    min_b = 1
    while b >= min_b:
        a = (b * n - 1) // d  # current numerator
        current = a, b
        # if closest_a / closest_b < current_a / current_b
        if compare_fractions(closest_neighbour, current) == -1:
            closest_neighbour = reduce_fraction(a, b)
            delta = n * b - d * a
            min_b = b // delta + 1
        b -= 1
    return closest_neighbour


def extended_gcd(n1: int, n2: int) -> tuple[int, int, int]:
    """
    Implements the Extended Euclidean Algorithm that calculates, in addition to
    gcd(n1, n2), the coefficients of Bezout's identity, integers x and y
    such that:

    ax + by = gcd(a, b)

    :returns: Tuple of (gcd, x, y).
    :raises ValueError: If either n1 or n2 is less than 0.
    """

    if n1 < 0 or n2 < 0:
        raise ValueError("Integers should not be negative")
    if n1 == 0:
        return n2, 0, 1
    e_gcd, x, y = extended_gcd(n2 % n1, n1)
    return e_gcd, y - n2 // n1 * x, x


def left_farey_neighbour_optimised(limit: int, n: int, d: int) -> tuple[int, int]:
    """
    Solution optimised by taking advantage of the Extended Euclidean Algorithm
    that generates coefficients x and y, in addition to the gcd.

    When a and b are co-prime, x will be the modular multiplicative inverse of
    a % b and y will be the modular multiplicative inverse of b % a. Remember
    that the modular multiplicative inverse of an integer a is an integer x such
    that the product ax is congruent to 1 with respect to the modulus b.

    SPEED (BEST)
        5700ns for N = 1e7
    SPEED (BEST)
        1.9e4ns for N = 1e15

    :returns: Tuple of (numerator, denominator) representing the fraction to the
        left of n/d.
    """

    # Python modulus intrinsically handles cases when x is negative
    mod_inverse_of_n = extended_gcd(n, d)[1] % d
    new_d = limit % d - mod_inverse_of_n
    if new_d < 0:
        new_d += d
    neighbour_denom = limit - new_d
    neighbour_num = (neighbour_denom * n - 1) // d
    return neighbour_num, neighbour_denom
