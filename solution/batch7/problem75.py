""" Problem 75: Singular Integer Right Triangles

https://projecteuler.net/problem=75

Goal: Given a length L, find how many values of L <= N can form exactly 1
integer-sided right-angle triangle.

Constraints: 12 <= N <= 5e6

12 is the smallest length (of wire e.g. if attempting to bend it into a triangle)
that can form an integer-sided right-angle triangle in exactly 1 way. In contrast,
some lengths, like 20, cannot form such a triangle, and other lengths, like 120,
allow the formation of such a triangle in multiple ways ->
{120: (30,40,50), (20,48,52), (24,45,51)}.

e.g.: N = 50
      count = 6
      {12: (3,4,5), 24: (6,8,10), 30: (5,12,13), 36: (9,12,15),
      40: (8, 15,17), 48: (12,16,20)}
"""
from util.maths.reusable import pythagorean_triplet


def singularTriplets(limit: int) -> int:
    """
    Solution is identical to the previously determined solution for finding the
    smallest perimeter of integer right-angle triangles (Batch 3 - Problem 39).

    Euclid's formula generates all primitive Pythagorean triplets & stores the
    count of triplets for every length. This cache is then converted to another
    that accumulates the count of singular triplet lengths below the given limit.
    """

    p_sols = [0]*(limit + 1)
    m = 2
    # upper bound represents p = 2dm(m + n)
    # i.e. Euclid's formula inserted into perimeter()
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
                # primitive triplet must have m XOR n as even
                # & m and n co-prime (gcd == 1)
                continue
        m += 1
    singular_count = [0]*(limit + 1)
    cumulative = 0
    for i in range(12, limit + 1):
        if p_sols[i] == 1:
            cumulative += 1
        singular_count[i] = cumulative
    return singular_count[limit]
