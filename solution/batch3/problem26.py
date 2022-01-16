""" Problem 26: Reciprocal Cycles

https://projecteuler.net/problem=26

Goal: Find the value of the smallest d less than N for which 1/d contains the
longest recurring cycle in its decimal fraction part.

Constraints: 4 <= N <= 1e4

Repetend/Reptend: the infinitely repeated digit sequence of the decimal
representation of a number.

e.g.: N = 10
      1/2 = 0.5
      1/3 = 0.(3) -> 1-digit recurring cycle
      1/4 = 0.25
      1/5 = 0.2
      1/6 = 0.1(6) -> 1-digit recurring cycle
      1/7 = 0.(142857) -> 6-digit recurring cycle
      1/8 = 0.125
      1/9 = 0.(1) -> 1-digit recurring cycle
      result = 7
"""
from util.maths.reusable import prime_numbers_og


def longest_repetend_denominator_primes(n: int) -> int:
    """
    Solution based on the following:

    - If a fraction contains a repetend, the latter's length (K) will never be
    greater than the fraction's denominator minus 1.

    - A denominator of 3 produces the first repetend, with K = 1.

    - All fractions that are a power of 1/2 or the product of 1/5 times a power
    of 1/2 will have exact decimal equivalents, not repetends.

    - Multiples of a denominator will have the same K value (multiples of 7 are
    special in that both K and repetend will be equal).

    - For each 1/p, where p is a prime number but not 2 or 5, for k in [1, p),
    10^k % p produces a repetend, when the remainder is 1.
    e.g. p = 11 -> (10^1 - 1) % 11 != 0, but (10^2 - 1) / 11 has 99 evenly
    divided by 11 giving 9. Since k = 2, there must be 2 repeating digits,
    so repetend = 09.

    SPEED (WORST): 5.1501s for N = 1e4.
    """

    # only prime numbers considered as only the smallest N is required &
    # anything larger would be a multiple of a smaller prime with equivalent K.
    primes = [x for x in prime_numbers_og(n - 1) if x not in [2, 3, 5]]
    d = 3
    longest_k = 1
    for p in primes:
        for k in range(1, p):
            if (pow(10, k, p)) == 1:
                if k > longest_k:
                    longest_k, d = k, p
                break
    return d


def longest_repetend_denominator_primes_improved(n: int) -> int:
    """
    Solution using primes above is optimised based on the following:

    - Full Repetend Primes are primes that, as 1 / p, will have the longest repetend
    of k = p - 1. A prime qualifies if, for k in [1, p-1], only the last k
    returns True for 10^k % p == 1.
    e.g. p = 7 -> for k in [1, 7), 10^k % p = [3, 2, 6, 4, 5, 1], so 7 is a full
    repetend prime.

    - Other than N = 3 and N = 6 both having K = 1, repetend length increases as
    primes increase since the longest repetends will be produced by full repetend
    primes & not be repeated. So the loop can be started from the largest prime
    and broken once the first full repetend prime is found.

    SPEED (BETTER): 0.0170s for N = 1e4.
    """

    if n < 8:
        return 3
    primes = prime_numbers_og(n - 1)[::-1]
    d = 3
    for p in primes:
        k = 1
        while (pow(10, k, p)) != 1:
            k += 1
        if k == p - 1:
            d = p
            break
    return d


def longest_repetend_denominator(n: int) -> int:
    """
    Repeatedly divides & stores decimal parts until a decimal part is repeated
    & compares length of stored parts.

    SPEED (BEST): 0.0078s for N = 1e4.
    """

    longest_k = 0
    d = n
    upper_n = n - 1 if n % 2 == 0 else n - 2
    lower_n = upper_n // 2 - 1
    for i in range(upper_n, lower_n, -2):
        if longest_k >= i:
            break
        remainders = [0]*i
        remainder = 1
        position = 0
        while remainders[remainder] == 0 and remainder != 0:
            remainders[remainder] = position
            remainder = remainder * 10 % i
            position += 1
        if position - remainders[remainder] >= longest_k:
            longest_k = position - remainders[remainder]
            d = i
    return d
