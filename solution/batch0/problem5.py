""" Problem 5: Smallest Multiple

https://projecteuler.net/problem=5

Goal: Find the smallest positive number that can be evenly divided by each
number in range [1, N].

Constraints: 1 <= N <= 40

e.g.: N = 3
      {1, 2, 3} evenly divides 6 to give quotient {6, 3, 2}
"""
from math import lcm, log2, pow

from util.maths.reusable import prime_numbers_og


def lcm_of_range(n: int) -> int:
    """
    Repeatedly calculates the least common multiple of the range elements,
    starting from the largest and stepping backwards until the middle of the range,
    as the smaller half of a range will already be factors of the larger half.

    Original solution used manual implementation of lcm(), but this was replaced
    with math.lcm(), introduced in PY 3.9.

    SPEED (BETTER)
        1.2e+04ns for N = 40
    """

    common_multiple = n
    for i in range(n - 1, n // 2, -1):
        common_multiple = lcm(common_multiple, i)
    return common_multiple


def lcm_of_range_builtin(n: int) -> int:
    """
    Same process as above function, but uses math.lcm() to its full capabilities.

    Original solution used manual implementation of lcm(), which only took 2
    integers, but this was replaced with math.lcm(), introduced in PY 3.9,
    which takes varargs *integers. So no need to use functools.reduce() to
    iterate over the multiple arguments::
        reduce(lcm, range(n, n // 2, -1))

    SPEED (BEST)
        6400ns for N = 40
    """

    return lcm(*range(n, n // 2, -1))


def lcm_of_range_using_primes(n: int) -> int:
    """
    Uses prime numbers to calculate the lcm of a range, based on the formula:

    p_i^a_i <= n

    a_i * log(p_i) <= log(n)

    a_i = floor(log(n) / log(p_i))

    e.g. N = 6, primes < N = {2, 3, 5};
    the exponent of the 1st prime will be 2 as 2^2 < 6 but 2^3 > 6;
    the exponent of the 2nd prime will be 1 as 3^1 < 6 but 3^2 > 6;
    the exponent of the 3rd prime will be 1 as 5^1 < 6 but 5^2 > 6;
    therefore, lcm = 2^2 * 3^1 * 5^1 = 60.

    This is an adaptation of the prime factorisation method for calculating the LCM.

     SPEED (WORST)
        18.66ms for N = 40
    """

    current_lcm = 1
    for prime in prime_numbers_og(n):
        exponent = 1 if prime * prime > n else int(log2(n) / log2(prime))
        current_lcm *= pow(prime, exponent)
    return current_lcm
