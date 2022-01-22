""" Problem 5: Smallest Multiple

https://projecteuler.net/problem=5

Goal: Find the smallest positive number that can be evenly divided by each
number in [1, N].

Constraints: 1 <= N <= 40

e.g.: N = 3
      [1, 2, 3] evenly divides 6 to give quotient {6, 3, 2}
"""
from math import lcm


def lcm_of_range(n: int) -> int:
    """
    Repeatedly calculates the least common multiple of the range elements,
    starting from the largest and stepping backwards until the middle of the range,
    as the smaller half of a range will already be factors of the larger half.

    Original solution used manual implementation of lcm(), but this was replaced
    with math.lcm(), introduced in PY 3.9.

    SPEED (EQUAL)
        8.13ms for N = 40 over 1000 iterations
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

    SPEED (EQUAL)
        7.69ms for N = 40 over 1000 iterations
    """

    return lcm(*range(n, n // 2, -1))
