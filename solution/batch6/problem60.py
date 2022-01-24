""" Problem 60: Prime Pair Sets

https://projecteuler.net/problem=60

Goal: Find the sums of every set of K-primes (where every prime < N) for which any
of the 2 primes, when concatenated in any order, result in another prime.

Constraints: 100 <= N <= 2e4, 3 <= K <= 5

Lowest sum for a set of 4 primes = 792 -> {3, 7, 109, 673}
e.g. 7109 and 1097 are primes, as are 37 and 73.

e.g.: N = 100, K = 3
      sums = [107, 123]
      107 -> {3, 37, 67} & 123 -> {7, 19, 97}
"""
from util.maths.reusable import is_prime_mr, prime_numbers


def is_concatenable_prime(prime_1: int, prime_2: int) -> bool:
    """
    Converting to and back from strings for concatenation can become slow.
    Instead, the first prime is multiplied to an appropriate power based on the
    amount of digits in the second prime, then they are added.
    """

    power_1, power_2 = 10, 10
    while power_1 <= prime_2:
        power_1 *= 10
    while power_2 <= prime_1:
        power_2 *= 10
    return (
            is_prime_mr(prime_1 * power_1 + prime_2) and
            is_prime_mr(prime_2 * power_2 + prime_1)
    )


def prime_pair_sets(n: int, k: int) -> list[int]:
    # avoid concatenating & checking primality multiple times
    # key = prime, values = primes > k that makes a concatenable pair
    concatenated_pairs: dict[int, set[int]] = dict()
    # all non-single digit primes end in {1, 3, 7, 9} so 2 and 5 are ruled out
    primes = prime_numbers(n - 1)
    primes.remove(2)
    primes.remove(5)
    num_of_primes = len(primes)

    def get_pairs(prime_i: int):
        prime = primes[prime_i]
        pairs = []
        for p in range(prime_i + 1, num_of_primes):
            other = primes[p]
            if is_concatenable_prime(prime, other):
                pairs.append(other)
        concatenated_pairs[prime] = set(pairs)

    totals = []
    starters = []
    for a in range(num_of_primes):
        k_a = primes[a]
        if k_a not in concatenated_pairs.keys():
            get_pairs(a)
        common = concatenated_pairs[k_a]
        for b in range(a + 1, num_of_primes):
            k_b = primes[b]
            if k_b not in common:
                continue
            if k_b not in concatenated_pairs.keys():
                get_pairs(b)
            common_a = common
            common = common.intersection(concatenated_pairs[k_b])
            if len(common) == 0:
                common = common_a
                continue
            if k - 2 == 1:
                for k_c in common:
                    totals.append(sum((k_a, k_b, k_c)))
                    starters.append(k_a)
            else:
                for c in range(b + 1, num_of_primes):
                    k_c = primes[c]
                    if k_c not in common:
                        continue
                    if k_c not in concatenated_pairs.keys():
                        get_pairs(c)
                    common_b = common
                    common = common.intersection(concatenated_pairs[k_c])
                    if len(common) == 0:
                        common = common_b
                        continue
                    if k - 3 == 1:
                        for k_d in common:
                            totals.append(sum((k_a, k_b, k_c, k_d)))
                            starters.append(k_a)
                    else:
                        for d in range(c + 1, num_of_primes):
                            k_d = primes[d]
                            if k_d not in common:
                                continue
                            if k_d not in concatenated_pairs.keys():
                                get_pairs(d)
                            common_c = common
                            common = common.intersection(concatenated_pairs[k_d])
                            if len(common) == 0:
                                common = common_c
                                continue
                            for k_e in common:
                                totals.append(sum((k_a, k_b, k_c, k_d, k_e)))
                                starters.append(k_a)
                            common = common_c
                    common = common_b
            common = common_a
    print(max(starters))
    return totals


def sum_of_prime_pair_sets(n: int, k: int) -> list[int]:
    totals = prime_pair_sets(n, k)
    return sorted(totals)


if __name__ == '__main__':
    all_p = prime_numbers(20000 - 1)
    print(all_p.index(14197))
    print(all_p.index(13))
