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


def generate_longest_collatz(n_max):
    # Cache for all previously counted collatz sequences
    collatz_lengths = [0] * n_max
    collatz_lengths[0] = 1
    # Cache for the starter for the longest sequence so far
    longest_collatz = [0] * n_max
    longest_collatz[0] = 1

    def collatz_memo(n):
        if n <= n_max and collatz_lengths[n-1] != 0:
            return collatz_lengths[n-1]
        else:
            # if n is odd using Bitwise AND
            if n & 1:
                count = 2 + collatz_memo((n * 3 + 1) // 2)
            else:
                # n // 2 (if casting expensive) is equivalent to n >> 1
                count = 1 + collatz_memo(n // 2)
            # Speeds up memoisation as more than just original n cached
            if n <= n_max:
                collatz_lengths[n - 1] = count
            return count

    longest_starter = 1
    longest_count = 1
    for start in range(2, n_max + 1):
        current_collatz = collatz_memo(start)
        if current_collatz >= longest_count:
            longest_count = current_collatz
            longest_starter = start
        longest_collatz[start-1] = longest_starter
    return longest_collatz
