""" Problem 9: Special Pythagorean Triplet

https://projecteuler.net/problem=9

Goal: If there exists any Pythagorean triplet for which a + b + c = N, find the
maximum product among all such triplets, otherwise return -1.

Constraints: 1 <= N <= 3000

Pythagorean Triplet: a set of 3 natural numbers,
such that a < b < c && a^2 + b^2 = c^2.

e.g.: N = 12
      triplets = {{3,4,5}}; as 3 + 4 + 5 == 12
      product = 3 * 4 * 5 = 60
"""
from math import sqrt, ceil, gcd
from util.maths.reusable import pythagorean_triplet


def is_pythagoras(a: int, b: int, c: int) -> bool:
    return sqrt(a ** 2 + b ** 2) == c


def max_triplet_product_loop_c_b(num: int) -> (int, ...):
    """ Solution iterates through values of c and b with some limits:

    - Set {3,4,5} is the smallest existing triplet, so c must be >= 5 and can be
    at most num / 2 - 1.

    - b cannot be <= a.

    - Triplet elements must either be all evens OR 2 odds with 1 even.
    Therefore, the sum of a triplet (num) must be even as the sum of evens is an
    even number and the sum of 2 odds is an even number as well.

    :returns: Tuple(max_product, a, b, c) if one exists, or Tuple(-1,).

    Speed (WORSE): 228.86ms for N = 3000.
    """

    max_triplet = -1,
    if num % 2 != 0:
        return max_triplet
    c = num // 2 - 1
    while c >= 5:
        diff = num - c
        b = c - 1
        while b >= diff // 2:
            a = diff - b
            if b <= a:
                break
            if is_pythagoras(a, b, c):
                product = a * b * c
                if product > max_triplet[0]:
                    max_triplet = product, a, b, c
            b -= 1
        c -= 1
    return max_triplet


def max_triplet_product_loop_a(num: int) -> (int, ...):
    """ Solution iterates through values of a only based on:

    - Set {3,4,5} being the smallest existing triplet, so a must be >= 3 and can
    be at most num / 3 - 1.

    - Inserting c = num - a - b into the formula a^2 + b^2 = c^2 reduces to:
    2 * a * b + 2 * b * num = num^2 - 2 * a * num
    b = (num * (n - 2 * a)) / (2 * (n - a))

    - Exhaustive search shows that the first maximum triplet found will be the
    only solution, so the loop van be broken early.

    - Triplet elements must either be all evens OR 2 odds with 1 even.
    Therefore, the sum of a triplet (num) must be even as the sum of evens is an
    even number and the sum of 2 odds is an even number as well.

    :returns: Tuple(max_product, a, b, c) if one exists, or Tuple(-1,).

    Speed (BETTER): 2.3e5ns for N = 3000.
    """

    max_triplet = -1,
    if num % 2 != 0:
        return max_triplet
    a = num // 3 - 1
    while a >= 3:
        b = num * (num - 2 * a) // (2 * (num - a))
        c = num - a - b
        if a < b and is_pythagoras(a, b, c):
            product = a * b * c
            if product > max_triplet[0]:
                max_triplet = product, a, b, c
                break
        a -= 1
    return max_triplet


def max_triplet_product_optimised(num: int) -> (int, ...):
    """ Solution optimised based on:

    - All Pythagorean triplets can be reduced to a primitive one by dividing out
    gcd(a,b,c) = d, such that: a + b + c = 2 * m * (m + n) * d, with n > m > 0.

    - A triplet is primitive if m XOR n is even and gcd(m,n) = 1. The latter occurs
    because gdc(a,b) = gcd(b,c) = gcd(c,a) = 1.

    - Exhaustive search shows that the first maximum triplet found will be the
    only solution, so the loop van be broken early.

    :returns: Tuple(max_product, a, b, c) if one exists, or Tuple(-1,).

    Speed (BEST): 31900ns for N = 3000.
    """

    max_triplet = -1,
    if num % 2 != 0:
        return max_triplet
    limit = num // 2
    m_max = ceil(sqrt(limit))
    found = False
    for m in range(2, m_max):
        if limit % m == 0:
            # find even divisor m (> 1) of num // 2
            k_max = limit // m
            while k_max % 2 == 0:
                # find odd divisor k (= m + n) of num // 2m
                k_max //= 2
            k = m + 2 if m % 2 == 1 else m + 1
            while k < 2 * m and k <= k_max:
                if k_max % k == 0 and gcd(k, m) == 1:
                    a, b, c = pythagorean_triplet(m, k - m, limit // (k * m))
                    product = a * b * c
                    if product > max_triplet[0]:
                        max_triplet = product, a, b, c
                        found = True
                        break
                k += 2
            if found:
                break
    return max_triplet
