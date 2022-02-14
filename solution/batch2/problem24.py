""" Problem 24: Lexicographic Permutations

https://projecteuler.net/problem=24

Goal: Return the Nth lexicographic permutation of "abcdefghijklm".

Constraints: 1 <= N <= 13!

Lexicographic Permutation: The alphabetically/numerically ordered arrangements
of an object.
e.g. "abc" -> {"abc", "acb", "bac", "bca", "cab", "cba"}

e.g.: N = 1 -> "abcdefghijklm"
      N = 2 -> "abcdefghijkml"
"""
from itertools import permutations
from math import factorial


def nth_lexicographic_perm_builtin(n: int, string: str) -> str:
    """
    SPEED (WORST)
        863.21ms for 10-digit string
        Most likely due to permutations() generating all possible full-length
        permutations sorted lexicographically rather than stopping once the
        required permutation is found.

    :param n: The nth permutation requested should be zero-indexed.
    :param string: The object to generate permutations of should be already
        sorted in ascending order.
    """

    all_perms = list(map("".join, permutations(string)))
    return all_perms[n]


def nth_lexicographic_perm(n: int, string: str, permutation: str = "") -> str:
    """
    Recursive solution uses factorial (permutations without repetition) to
    calculate the next character in the permutation based on batch position.

    e.g. "abcd" has 4! = 24 permutations & each letter will have 6 permutations
    in which that letter will be the 1st in the order. If n = 13, this permutation
    will be in batch 2 (starts with "c") at position 1 (both 0-indexed). So "c" is
    removed and n = 1 is used with the new string "abd". This continues until
    n = 0 and "cabd" is returned by the base case.

    SPEED (BETTER)
        4.1e4ns for 10-digit string

    :param n: The nth permutation requested should be zero-indexed.
    :param string: The object to generate permutations of should be already
        sorted in ascending order.
    """

    if not n:
        return permutation + string
    else:
        batch_size = factorial(len(string)) // len(string)
        batch, batch_n = divmod(n, batch_size)
        return nth_lexicographic_perm(
            batch_n,
            string[:batch] + string[batch+1:],
            permutation + string[batch]
        )


def nth_lexicographic_perm_improved(n: int, string: str) -> str:
    """
    Recursive solution improved by removing the unnecessary creation of a storage
    string to pass into every recursive call, as well as reducing the factorial
    call, since (x! / x) = (x - 1)!.

    SPEED (BEST)
        1.9e4ns for 10-digit string

    :param n: The nth permutation requested should be zero-indexed.
    :param string: The object to generate permutations of should be already
        sorted in ascending order.
    """

    if len(string) == 1:
        return string
    else:
        batch_size = factorial(len(string) - 1)
        batch, batch_n = divmod(n, batch_size)
        return string[batch] + nth_lexicographic_perm_improved(
            batch_n,
            string[:batch] + string[batch+1:]
        )
