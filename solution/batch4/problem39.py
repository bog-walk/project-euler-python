""" Problem 39: Integer Right Triangles

https://projecteuler.net/problem=39

Goal: If P is the perimeter of a right-angle triangle, find the
smallest value of P <= N that has the maximum number of (a, b, c) solutions.

Constraints: 12 <= N <= 5e6

e.g. P = 120 has 3 solutions: (20, 48, 52), (24, 45, 51) & (30, 40, 50).

e.g.: N = 12
      P = 12 as 12 is the only sum of a Pythagorean triplet (3, 4, 5)
"""
from math import ceil, sqrt, gcd


def pythagorean_triplet(m, n, d):
    a = (m * m - n * n) * d
    b = 2 * m * n * d
    c = (m * m + n * n) * d
    return min(a, b), max(a, b), c


def get_triplet_solutions(p):
    """
    Optimised solution based on:
    - A primitive Pythagorean triplet having gcd(a,b,c) = 1,
    as gdc(a,b) = gcd(b,c) = gcd(c,a) = 1.
    - A triplet being primitive if m XOR n is even and gcd(m,n) = 1.
    - All triplets can be reduced to a primitive one by dividing out
    the gcd(a,b,c) = d, such that:
    a + b + c = 2 * m * (m + n) * d, with n > m > 0.
    """
    p_sols = []
    limit = p // 2
    m_max = ceil(sqrt(limit))
    for m in range(2, m_max):
        if limit % m == 0:
            # Find even divisor m (> 1) of num // 2
            k_max = limit // m
            while k_max % 2 == 0:
                # Find odd divisor k (= m + n) of num // 2m
                k_max //= 2
            k = m + 2 if m % 2 == 1 else m + 1
            while k < 2 * m and k <= k_max:
                if k_max % k == 0 and gcd(k, m) == 1:
                    triplet = pythagorean_triplet(m, k - m, limit // (k * m))
                    if sum(triplet) == p:
                        p_sols.append(triplet)
                k += 2
    return p_sols


def best_triplet_perimeter(n):
    best_p, best_len = 12, 1
    for p in range(13, n + 1):
        p_len = len(get_triplet_solutions(p))
        if p_len > best_len:
            best_p, best_len = p, p_len
    return best_p
