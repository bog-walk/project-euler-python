""" Problem 39: Integer Right Triangles

https://projecteuler.net/problem=39

Goal: If P is the perimeter of a right-angle triangle, find the smallest value
of P <= N that has the maximum number of (a, b, c) solutions.

Constraints: 12 <= N <= 5e6

e.g. P = 120 has 3 solutions: (20, 48, 52), (24, 45, 51) & (30, 40, 50).

e.g.: N = 12
      P = 12 as 12 is the only sum of a Pythagorean triplet (3, 4, 5)
"""
from math import isqrt
from util.maths.reusable import is_coprime, pythagorean_triplet


def most_triplet_solutions_brute(n: int) -> int:
    """
    Brute force solution based on the following:

    -   Pythagorean Triplets must either be all evens OR 2 odds with 1 even.
        So, the sum of triplets will only ever be an even number as the sum of evens
        is an even number, as is the sum of 2 odds.

    -   Since a < b < c and a + b + c = P, a will not be higher than P / 3.

    -   If c = P - a - b is inserted into the equation a^2 + b^2 = c^2, then:

        a^2 + b^2 = P^2 - 2aP - 2bP + 2ab + a^2 + b^2

        b = P(P - 2a) / 2(P - a)

        which means values of P and a that result in an integer value b represent a
        valid Triplet.

    SPEED (WORST)
        329.84s for N = 1e5
    """

    best_p, most_sols = 12, 1
    for p in range(14, n + 1, 2):
        num_sols = 0
        for a in range(4, p // 3):
            b = (p * (p - 2 * a)) % (2 * (p - a))
            if b == 0:
                num_sols += 1
        if num_sols > most_sols:
            best_p, most_sols = p, num_sols
    return best_p


def most_triplet_solutions(n: int) -> int:
    """
    Solution is influenced by the previously determined solution for finding
    primitive Pythagorean Triplets (Batch 0 - Problem 9).

    Original solution calculated the ceiling of the square root of the limit.
    This was replaced with the implementation of math.isqrt() for positive n,
    introduced in Py 3.8.

    SPEED (BETTER)
        1.17s for N = 1e5
    """

    best_p, most_sols = 12, 1
    for p in range(14, n + 1, 2):
        sols = 0
        limit = p // 2
        m_max = 1 + isqrt(limit - 1)
        for m in range(2, m_max):
            if limit % m == 0:
                k_max = p // (2 * m)
                k = m + 2 if m % 2 == 1 else m + 1
                while k < 2 * m and k <= k_max:
                    if k_max % k == 0 and is_coprime(k, m):
                        sols += 1
                    k += 2
        if sols > most_sols:
            best_p, most_sols = p, sols
    return best_p


def most_triplet_solutions_improved(limit: int) -> int:
    """
    Solution above is optimised further by relying solely on Euclid's formula to
    generate all primitive Pythagorean triplets.

    Every perimeter that has a triplet will be represented as a count at
    p_sols[perimeter]. This array is finally converted to another that accumulates
    the perimeter (below the given limit) with the most counts, best[limit].

    N.B. The upper bound for m is found by substituting Euclid's formulae into the
    perimeter formula & reducing it to:

    p = 2dm(m + n)

    which means when d = 1 & n = 1, at most 2m^2 must be below the given limit.

    SPEED (BEST)
        158ms for N = 1e5
    """

    p_sols = [0]*(limit + 1)
    m = 2
    while 2 * m * m < limit:
        for n in range(1, m):
            d = 1
            try:
                while True:
                    p = sum(pythagorean_triplet(m, n, d))
                    if p > limit:
                        break
                    p_sols[p] += 1
                    d += 1
            except ValueError:
                # ensure that both m and n are not odd
                # and that m and n are co-prime (gcd == 1)
                continue
        m += 1
    best = [0]*(limit + 1)
    best_p, best_count = 12, 1
    for i in range(12, limit + 1):
        count = p_sols[i]
        if count > best_count:
            best_p, best_count = i, count
        best[i] = best_p
    return best[limit]
