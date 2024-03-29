""" Problem 95: Amicable Chains

https://projecteuler.net/problem=95

Goal: Find the smallest member of the longest amicable chain possible without any
member exceeding N.

Constraints: 6 <= N <= 1e6

Perfect Number: A chain of only 1 member denotes a perfect number; i.e. the sum
of this number's proper divisors is the number itself.
e.g. [6], [28], [496].
Amicable Pair: A chain of only 2 members.
e.g. [220, 284], [1184, 1210], [2620, 2924].
Amicable Chain: A chain of numbers generated by calculating the sum of each
number's proper divisors.
e.g. 12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...).

e.g.: N = 10
      6 -> {1, 2, 3} = [6]
      output = 6
"""
from util.maths.reusable import sum_proper_divisors


def longest_amicable_chain(limit: int) -> list[int]:
    """
    Solution optimised by storing the results of previous chain members in a cache
    to avoid redundant invocation of the helper function.

    Potential chains are also terminated early if any member is smaller than the
    starter number (as the former would have already been assessed and deemed
    valid, invalid, or a prime). This is supported by the observation that the few
    chains (with >2 members) follow a normal distribution curve, with the smallest
    element being the first starter.

    Iteration through starters is also reduced by only considering even numbers,
    based on the observation that amicable chains only consist of even numbers.
    """

    # None signifies that the starter has yet to be assessed
    # [] means no valid chain from starter at that index (most likely ends in
    # a prime)
    # [x,...] means a valid chain was found by a smaller starter
    cache: list[list | None] = [[] if i < 10 else None for i in range(limit + 1)]
    cache[6] = [6]
    longest = [6]
    for n in range(10, limit + 1, 2):
        if cache[n] is None:
            chain = [n]
            prev = n
            while True:
                prev = sum_proper_divisors(prev)
                # either a perfect number or a closed chain
                if prev == n:
                    for num in chain:
                        cache[num] = chain
                    if len(chain) > len(longest):
                        longest = chain
                    break
                # either determined invalid by a smaller starter, is amicable pair
                # or is perfect, or is already part of an amicable chain
                # e.g. 25 -> {1, 5} -> [6]
                # e.g. 1692 leads to pair [2924, 2620] that first appears in
                # 1188 chain
                if prev not in range(n + 1, limit + 1) or cache[prev] is not None:
                    for num in chain:
                        cache[num] = []
                    break
                # found smaller sub-chain (could be longer than a pair)
                if prev in chain:
                    index = chain.index(prev)
                    sub_chain = chain[index:]
                    if len(sub_chain) > len(longest):
                        longest = sub_chain
                    for i, num in enumerate(chain):
                        cache[num] = [] if i < index else sub_chain
                    break
                chain.append(prev)

    return longest
