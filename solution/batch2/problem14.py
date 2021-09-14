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