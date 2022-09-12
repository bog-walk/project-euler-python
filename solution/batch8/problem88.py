""" Problem 88: Product-Sum Numbers

https://projecteuler.net/problem=88

Goal: Find the sum of all unique product-sum numbers for 2 <= k <= N.

Constraints: 10 <= N <= 2e5

Product-Sum Number: A natural number that can be written as both the sum and the
product of a given set of at least 2 natural numbers,
such that N = a1+a2+..+ak = a1*a2*..*ak.

Minimal Product-Sum Number: For a given set of size k, the smallest N that is a
product-sum number;
        e.g. k = 2: 4 = 2 + 2 + 2 * 2
             k = 3: 6 = 1 + 2 + 3 = 1 * 2 * 3
             k = 4: 8 = 1 + 1 + 2 + 4 = 1 * 1 * 2 * 4
             k = 5: 8 = 1 + 1 + 2 + 2 + 2 = 1 * 1 * 2 * 2 * 2
             k = 6: 12 = 1 + 1 + 1 + 1 + 2 + 6 = 1 * 1 * 1 * 1 * 2 * 6
             Therefore, for 2 <= k <= 6, the sum of unique minimal product-sum
             numbers is 30.

e.g.: N = 12
      2 <= k <= 12 -> {4, 6, 8, 8, 12, 12, 12, 15, 16, 16, 16}
      sum = 61
"""
from math import inf, isqrt

limit = 200_000
# exclude 0 and 1 from cache, so minimalPS for k found at cache[k-2]
minimal_ps_cache = [inf]*(limit - 1)


def sum_of_ps_numbers(max_k: int) -> int:
    return sum(set(minimal_ps_cache[:max_k-1]))


def is_minimal_ps_num(n: int, k: int) -> bool:
    if k > limit:
        return False

    if n < minimal_ps_cache[k-2]:
        minimal_ps_cache[k-2] = n
        return True

    return False


def count_k_if_ps(n: int, product: int, total: int,
                  factors: int = 0, min_factor: int = 2) -> int:
    """
    Recursively remove factors from a number (and from its corresponding sum) &
    store it if it is a valid product-sum number for any k.
    """

    if product == 1:  # remaining sum must be all 1s
        return is_minimal_ps_num(n, factors + total)

    result = 0
    if factors > 0:  # at least 1 factor has been removed
        if product == total:
            return is_minimal_ps_num(n, factors + 1)
        if is_minimal_ps_num(n, factors + total - product + 1):
            result += 1
    for i in range(min_factor, isqrt(product) + 1):
        if not product % i:
            result += count_k_if_ps(n, product // i, total - i, factors + 1, i)
    return result


def generate_ps_numbers():
    generated = 0
    num = 4  # minimal_ps_num for k = 2
    while generated < limit - 1:
        # a number can be a minimal_ps_num for multiple k
        generated += count_k_if_ps(num, num, num)
        num += 1


