""" Problem 5: Smallest Multiple

https://projecteuler.net/problem=5

Goal: Find the smallest positive number that can be evenly divided by each
number in [1, N].

Constraints: 1 <= N <= 40

e.g.: N = 3
      [1, 2, 3] evenly divides 6 to give quotient {6, 3, 2}
"""
from functools import reduce
from util.maths.reusable import lcm


def lcm_of_range(n: int) -> int:
    """
    Repeatedly calculates the least common multiple of the range elements,
    starting from the largest and stepping backwards until the middle of the range.

    SPEED (WORSE): 55.84ms for N = 40 over 1000 iterations.
    """
    common_multiple = n
    for i in range(n - 1, n // 2, -1):
        common_multiple = lcm(common_multiple, i)
    return common_multiple


def lcm_of_range_builtin(n: int) -> int:
    """
    Same process as above function, but uses built-in reduce() function.

    SPEED (BETTER): 25.56ms for N = 40 over 1000 iterations.
    """
    return reduce(lcm, range(n, 0, -1))
