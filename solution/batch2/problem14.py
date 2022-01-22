""" Problem 14: Longest Collatz Sequence

https://projecteuler.net/problem=14

Goal: Find the largest starting number <= N that produces the longest Collatz
sequence.

Constraints: 1 <= N <= 5e6

Collatz Sequence: Thought to all finish at 1, a sequence of positive integers is
generated using the hailstone calculator algorithm, such that:

    [even n] :math:`n \\to n / 2`

    [odd n]  :math:`n \\to 3n + 1`

e.g.: N = 5
      1
      2 -> 1
      3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
      4 -> 2 -> 1
      5 -> 16 -> 8 -> 4 -> 2 -> 1
      longest chain when starting number = 3
"""
from math import log2


def collatz_length(start: int) -> int:
    """
    :returns: Length of Collatz sequence given a starting number.
    """

    count = 1
    while start != 1:
        # if start is even (alternative to modulus)
        if not (start & 1):
            start //= 2
        else:
            start = start * 3 + 1
        # bitwise AND will equal 0 if is a power of 2
        if start != 0 and not (start & (start - 1)):
            count += log2(start) + 1
            break
        else:
            count += 1
    return count


def generate_longest_starters(n_max: int) -> list[int]:
    """ Generates a list of starting numbers that produce the longest sequence.

    :returns: List of the starting number <= index n that generates the
        longest sequence at that point.
    """

    # cache for all previously counted collatz sequences
    collatz_lengths = [0, 1] + [0]*n_max

    def collatz_memo(n: int) -> int:
        if n <= n_max and collatz_lengths[n]:
            return collatz_lengths[n]
        else:
            # if n is odd using Bitwise AND
            if n & 1:
                # add a division by 2 as odd_n * 3 + 1 gives an even
                # number, so both steps can be combined
                count = collatz_memo((n * 3 + 1) // 2) + 1
            else:
                # n // 2 (if casting expensive) is equivalent to n >> 1
                count = collatz_memo(n // 2) + 1
            if n <= n_max:
                collatz_lengths[n] = count
            return count

    # cache for the starter for the longest sequence so far
    longest_collatz = [1]
    longest_count = 1
    for start in range(2, n_max + 1):
        current_length = collatz_memo(start)
        if current_length >= longest_count:
            longest_collatz.append(start)
            longest_count = current_length
    # sort in descending order to facilitate search in calling function
    return longest_collatz[::-1]


def largest_collatz_starter(starters: list[int], n: int) -> int:
    """
    :returns: Largest starter that is <= n, from a list of starters
        that generate the longest Collatz sequences.
    """

    return min(starters, key=lambda s: s > n)
