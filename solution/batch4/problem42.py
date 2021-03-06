""" Problem 42: Coded Triangle Numbers

https://projecteuler.net/problem=42

Goal: Given an integer, if it is a triangle number t_n, return its corresponding
term n, otherwise, return -1.

Constraints: 1 <= t_n <= 1e18

Triangle Number: The nth term is given by ->
t_n = n(n + 1) / 2 -> 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...

e.g.: N = 2
      return -1, as 2 is not a triangle number; however,
      N = 3
      return 2, as 3 is the 2nd triangle number to exist.
"""
from math import lcm, isqrt
from util.maths.reusable import is_triangular_number


def triangle_term(t_n: int) -> int:
    """
    Triangle Number Sequence follows the pattern (odd, odd, even, even,...) &
    each t_n is the sum of the previous t_n & the current n.

    Rather than brute force pre-computation of all triangle numbers below 1e18,
    this solution is based on the formula:

    t_n = n(n + 1) / 2

    2t_n = n(n + 1)

    2t_n / n = n + 1 and 2t_n / (n + 1) = n, therefore:

    2t_n == lcm(n, n + 1) and

    n must at minimum be sqrt(2t_n)

    Original solution used a floored square root to get an integer value, as well
    as a manual implementation of lcm(). These were replaced with math.isqrt()
    and math.lcm(), introduced in PY 3.8 and PY 3.9 respectively.
    """

    t_n_2 = 2 * t_n
    n = isqrt(t_n_2)
    return n if t_n_2 == lcm(n, n + 1) else -1


def triangle_term_improved(t_n: int) -> int:
    """ Solution formula optimised by using its derived inverse function. """

    term = is_triangular_number(t_n)
    return -1 if term is None else term


def count_triangle_words(words: list[str]) -> int:
    """
    Project Euler specific implementation that returns the count, from an
    input of <2000 words, of words whose summed alphabetical character value
    corresponds to a triangle number.
        e.g. "SKY" = 19 + 11 + 25 = 55 = t_10
    """

    # get alphabetical position based on 'A' code = 65
    word_values = map(lambda word: sum(ord(ch) - 64 for ch in word), words)
    return len(
        list(filter(lambda v: is_triangular_number(v) is not None, word_values))
    )
