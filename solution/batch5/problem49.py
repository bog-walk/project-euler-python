""" Problem 49: Prime Permutations

https://projecteuler.net/problem=49

Goal: Return all concatenated integers formed by joining K terms,
such that the first term is below N and all K terms are permutations
of each other, as well as being prime, as well as being in constant
arithmetic progression.

Constraints: 2000 <= N <= 1e6, K in {3, 4}

e.g.: N = 2000, K = 3
      sequence = {1487, 4817, 8147}, with step = 3330
      output = 148748178147
"""
from itertools import permutations
from util.reusable import is_prime, prime_numbers


def prime_perm_sequence(n, k):
    """
    Note that there are no arithmetic sequences that match these
    properties with terms having less than 4 digits.
    """
    primes = prime_numbers(n - 1)
    sequences = []
    for first in primes[186:]:
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
                concat = "".join([str(first + (m * diff)) for m in range(k)])
                sequences.append(concat)
    return sequences


def alt(n, k):
    primes = prime_numbers(pow(10, len(str(n))) - 1)
    prime_perms = dict()
    for prime in primes[186:]:
        if prime >= n:
            break
        if prime in prime_perms:
            continue
        perms = sorted([
            int("".join(perm))
            for perm in set(permutations(str(prime)))
            if perm[0] != '0' and int("".join(perm)) in primes
        ])
        for i in range(len(perms) - k + 1):
            if perms[i] >= n:
                break
            prime_perms[perms[i]] = perms[i+1:]
    sequences = []
    for prime, perms in sorted(prime_perms.items()):
        if len(perms) >= k - 1:
            for i in range(len(perms) - k + 2):
                second = perms[i]
                diff = second - prime
                extra = second
                constant = True
                for _ in range(k - 2):
                    extra += diff
                    if extra not in perms[i + 1:]:
                        constant = False
                        break
                if constant:
                    concat = "".join([str(prime + (m * diff)) for m in range(k)])
                    sequences.append(concat)
    return sequences


if __name__ == '__main__':
    print(len(prime_perm_sequence(1000000, 4)))
