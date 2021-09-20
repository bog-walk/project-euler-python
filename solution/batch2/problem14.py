""" Problem 14: Longest Collatz Sequence

https://projecteuler.net/problem=14

Goal: Find the largest starting number <= N that produces the longest Collatz sequence.

Constraints: 1 <= N <= 5e6

Collatz Sequence: thought to all finish at 1, a sequence of positive integers, such that:
- (even n) n -> n / 2
- (odd n)  n -> 3*n + 1

e.g.: N = 5
      1
      2 -> 1
      3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
      4 -> 2 -> 1
      5 -> 16 -> 8 -> 4 -> 2 -> 1
      longest chain when starting number = 3
"""
from math import log2


def collatz_length(start):
    count = 1
    while start != 1:
        # if start is even (alt to modulus)
        if not(start & 1):
            start //= 2
        else:
            start = start * 3 + 1
        # Bitwise AND will equal 0 if is a power of 2
        if start != 0 and not(start & (start - 1)):
            count += log2(start) + 1
            break
        else:
            count += 1
    return count


def generate_collatz_lengths(n_max):
    collatz_lengths = [0] * n_max
    collatz_lengths[0] = 1
    collatz_lengths[1] = 2

    def collatz_memo(n):
        if n <= n_max and collatz_lengths[n-1] != 0:
            return collatz_lengths[n-1]
        else:
            # if n is odd using Bitwise AND
            if n & 1:
                count = 2 + collatz_memo((n * 3 + 1) // 2)
            else:
                count = 1 + collatz_memo(n // 2)
            return count

    for start in range(3, n_max + 1):
        collatz_lengths[start-1] = collatz_memo(start)
    return collatz_lengths


def longest_collatz_under_N(n: int, all_lengths: list[int]):
    collatz_to_assess = all_lengths[n//2:n]
    longest = max(collatz_to_assess)
    return n - collatz_to_assess[::-1].index(longest)
