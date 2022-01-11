""" Problem 24: Lexicographic Permutations

https://projecteuler.net/problem=24

Goal: Return the Nth lexicographic permutation of "abcdefghijklm".

Constraints: 1 <= N <= 13!

Lexicographic Permutation: the alphabetically/numerically ordered
arrangements of an object.
e.g. "abc" -> {"abc", "acb", "bac", "bca", "cab", "cba"}

e.g.: N = 1 -> "abcdefghijklm"
      N = 2 -> "abcdefghijkml"
"""
from math import factorial
from itertools import permutations


def lexicographic_perms_builtin(n, string):
    """
    SPEED: 1163.88ms for 10-digit string

    Most likely due to itertool.permutations() generating all possible
    full-length permutations sorted lexicographically rather than
    stopping once the required permutation is found.
    """
    all_perms = list(map("".join, permutations(string)))
    return all_perms[n]


def lexicographic_perms(n, string: str, permutation=""):
    """
    Recursive solution uses factorial (permutations without repetition)
    to calculate next character in permutation based on batch position.
    e.g. "abcd" has 4! = 24 permutations & each letter will have 6
    permutations in which that letter will be the 1st in the order.

    :param [n] the nth permutation requested; should be zero-indexed.
    :param [string] the object to generate permutations of; should be
    already sorted in ascending lexicographic order.

    SPEED: 43300ns for 10-digit string
    """
    if not n:
        return permutation + string
    else:
        batch_size = factorial(len(string)) // len(string)
        i = n // batch_size
        return lexicographic_perms(
            n % batch_size,
            string[:i] + string[i+1:],
            permutation + string[i]
        )


def lexicographic_perms_improved(n, string: str):
    """
    Recursive solution improved by refactoring unnecessary code creation.

    :param [n] the nth permutation requested; should be zero-indexed.
    :param [string] the object to generate permutations of; should be
    already sorted in ascending lexicographic order.

    SPEED (BEST): 15000ns for 10-digit string
    """
    if len(string) == 1:
        return string
    else:
        # batch_size = factorial(len(string)) // len(string)
        batch_size = factorial(len(string) - 1)
        i = n // batch_size
        return string[i] + lexicographic_perms_improved(
            n % batch_size,
            string[:i] + string[i+1:]
        )
