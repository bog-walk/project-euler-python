""" Problem 49: Prime Permutations

https://projecteuler.net/problem=49

Goal: Return all concatenated integers formed by joining K terms, such that the
first term is below N and all K terms are permutations of each other, as well as
being prime and in constant arithmetic progression.

Constraints: 2000 <= N <= 1e6, K in [3, 4]

e.g.: N = 2000, K = 3
      sequence = {1487, 4817, 8147}, with step = 3330
      output = "148748178147"
"""
from itertools import permutations
from util.maths.reusable import is_prime, prime_numbers


def prime_perm_sequence(n: int, k: int) -> list[list[int]]:
    """
    Solution uses itertools.permutations() to find all permutations of a prime
    & filter potential candidates for a sequence.

    SPEED (WORSE)
        103.80s for N = 1e6, K = 3
        Slower due to permutations being (re-)generated unnecessarily
    """

    primes = prime_numbers(n - 1)
    sequences = []
    for first in primes:
        # there are no arithmetic sequences that match these
        # properties with terms having less than 4 digits.
        if first < 1117:
            continue
        num_str = str(first)
        perms = sorted(list(
            filter(
                lambda x: x > first and is_prime(x),
                map(lambda p: int("".join(p)),
                    [perm for perm in set(permutations(num_str)) if perm[0] != '0']
                    )
            )
        ))
        for i in range(len(perms) - k + 2):
            second = perms[i]
            diff = second - first
            extra = second
            constant = True
            for _ in range(k - 2):
                extra += diff
                if extra not in perms[i + 1:]:
                    constant = False
                    break
            if constant:
                concat = [first + (m * diff) for m in range(k)]
                sequences.append(concat)
    return sequences


def perm_id(n: int) -> int:
    """
    Generate a hash key for a prime number based on the amount of repeated digits,
    represented as a numerical version of an indexed RTL array.

    e.g. 1487 -> 110010010 <- 4817
         2214 -> 10210 <- 4212
    """

    p_id = 0
    while n:
        digit = n % 10
        p_id += pow(10, digit)
        n //= 10
    return p_id


def prime_perm_sequence_improved(n: int, k: int) -> list[list[int]]:
    """
    Solution optimised by using perm_id() helper function that maps all primes
    with same type and amount of digits to a permutation id. Then every list of
    primes that share a permutation id and has >= K elements is iterated over to
    check for an arithmetic progression sequence.

    Pre-generating all primes with same number of digits also eliminates the need
    to check for primality.

    SPEED (BETTER)
        8.81s for N = 1e6, K = 3
    """

    primes = prime_numbers(pow(10, len(str(n))) - 1)
    prime_perms: dict[int, list[int]] = dict()
    sequences = []
    for prime in primes:
        if prime < 1117:
            continue
        p_id = perm_id(prime)
        prime_perms[p_id] = prime_perms.setdefault(p_id, []) + [prime]
    for perms in prime_perms.values():
        if len(perms) >= k:
            for i in range(len(perms) - k + 1):
                first = perms[i]
                if first >= n:
                    break
                for j in range(i + 1, len(perms) - k + 2):
                    diff = perms[j] - first
                    constant = True
                    for x in range(2, k):
                        if first + (x * diff) not in perms[j + 1:]:
                            constant = False
                            break
                    if constant:
                        concat = [first + (m * diff) for m in range(k)]
                        sequences.append(concat)
    return sequences


def concat_prime_perms(n: int, k: int, improved: bool) -> list[str]:
    if improved:
        results = sorted(prime_perm_sequence_improved(n, k))
    else:
        results = prime_perm_sequence(n, k)
    return ["".join(map(str, result)) for result in results]
