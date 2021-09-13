""" Problem 9: Special Pythagorean Triplet

https://projecteuler.net/problem=9

Goal: If there exists any Pythagorean triplet for which a + b + c = N,
find the maximum product among all such triplets, otherwise return -1.

Constraints: 1 <= N <= 3000

Pythagorean Triplet: a set of 3 natural numbers, such that
a < b < c && a^2 + b^2 = c^2.

e.g.: N = 12
      triplets = {{3,4,5}}; as 3 + 4 + 5 == 12
      product = 3*4*5 = 60
"""
from math import prod, sqrt, ceil, gcd


def is_pythagoras(a, b, c):
    return sqrt(a ** 2 + b ** 2) == c


def max_triplet_brute(n):
    """
    Limits iterations through values of c and b based on:
    - Set {3,4,5} being the smallest existing triplet, means c >= 5.
    - b cannot be <= a.
    - Set of triples must either be all evens OR 2 odds with 1 even.
    Therefore, the sum of triples will only ever be even numbers as
    the sum of evens is an even number and the sum of 2 odds is an even
    number as well.

    Speed:
        2.24582s for 10 iterations of  N = 3000

    Returns:
        tuple: representing (a, b, c), if exists,
        OR
        None
    """
    if n % 2 != 0:
        return
    max_triplet = None
    max_product = 0
    c = n // 2 - 1
    while c >= 5:
        diff = n - c
        b = c - 1
        while b >= diff // 2:
            a = diff - b
            if b <= a:
                break
            if is_pythagoras(a, b, c):
                triplet = a, b, c
                product = prod(triplet)
                if product >= max_product:
                    max_triplet = triplet
                    max_product = product
            b -= 1
        c -= 1
    return max_triplet


def pythagorean_triplet(m, n, d):
    """
    All Pythagorean triplets can be found from 2 numbers m and n, with m > n > 0.
    All triplets originate from a primitive one by multiplying them by d = gcd(a,b,c).
    """
    a = (m * m - n * n) * d
    b = 2 * m * n * d
    c = (m * m + n * n) * d
    return min(a, b), max(a, b), c


def max_triplet_optimised(num):
    """
    Optimised solution based on:
    - A primitive Pythagorean triplet having gcd(a,b,c) = 1,
    as gdc(a,b) = gcd(b,c) = gcd(c,a) = 1.
    - A triplet being primitive if m XOR n is even and gcd(m,n) = 1.
    - All triplets can be reduced to a primitive one by dividing out
    the gcd(a,b,c) = d, such that:
    a + b + c = 2 * m * (m + n) * d, with n > m > 0.

    Speed:
        0.00020s for 10 iterations of  N = 3000
    """
    if num % 2 != 0:
        return
    max_triplet = None
    max_product = 0
    limit = num // 2
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
                    if sum(triplet) == num:
                        product = prod(triplet)
                        if product >= max_product:
                            max_triplet = triplet
                            max_product = product
                k += 2
    return max_triplet


def max_triplet_product(n):
    triplet = max_triplet_optimised(n)
    if triplet is None:
        return -1
    else:
        return prod(triplet)
