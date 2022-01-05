""" Problem 42: Coded Triangle Numbers

https://projecteuler.net/problem=42

Goal: Given an integer, if it is a triangle number t_n, return its
corresponding term n; otherwise, return -1.

Constraints: 1 <= t_n <= 1e18

Triangle Number Sequence: The nth term is given by ->
t_n = 0.5 * n * (n + 1) ->
1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...

e.g.: N = 2
      return -1, as 2 is not a triangle number; however,
      N = 3
      return 2, as 3 is the 2nd triangle number to exist.
"""
from math import sqrt
from util.maths.reusable import least_common_multiple, is_triangular_number


def triangle_term(t_n) -> int | None:
    """
    Triangle Number Sequence has interesting properties, e.g. the
    sequence follows the pattern (odd, odd, even, even,...) & each
    t_n is the sum of (t_n - 1) & current n.

    Rather than brute iteration that pre-computes all triangle numbers
    below 1e18, this solution is based on the following:
    t_n = 0.5 * n * (n + 1) ->
    2 * t_n = n * (n + 1), which means
    (2 * t_n) / n = n + 1 and (2 * t_n) / (n + 1) = n, therefore
    2 * t_n == lcm(n, n+ 1) and
    n must at minimum be sqrt(2 * t_n)
    """
    t_n_2 = 2 * t_n
    n = int(sqrt(t_n_2))
    if t_n_2 == least_common_multiple(n, n + 1):
        return n
    return -1


def triangle_term_improved(t_n):
    """
    Optimised solution uses derived inverse function.
    """
    term = is_triangular_number(t_n)
    return -1 if term is None else term


def count_triangle_words(words: list[str]):
    """
    Project Euler specific implementation that returns the count, from an
    input of <2000 words, of words whose summed alphabetical character value
    corresponds to a triangle number. e.g. "SKY" = 19 + 11 + 25 = 55 = t_10.
    """
    # get alphabetical position based on 'A' code = 65
    word_values = list(
        map(lambda word: sum(ord(ch) - 64 for ch in word), words)
    )
    return len(
        list(
            filter(lambda v: is_triangular_number(v) is not None, word_values)
        )
    )
