""" Problem 78: Coin Partitions

https://projecteuler.net/problem=78

Goal: Count the number of ways (mod 1e9 + 7) that N coins can be separated into
piles.

Constraints: 2 <= N <= 6e4

e.g.: N = 5
      count = 7
      if @ represents a coin, 5 coins can be separated in 7 different ways:
      @@@@@
      @@@@ @
      @@@ @@
      @@@ @ @
      @@ @@ @
      @@ @ @ @
      @ @ @ @ @
"""
modulus = 1_000_000_007


def coin_pile_combos(n: int) -> list[int]:
    """
    Solution is identical to the bottom-up approach used in Batch 7 - Problem 76
    (and is similar to solutions for Problems 31 & 77).

    SPEED (WORSE)
        108.06ms for N = 1e3
    SPEED (WORSE)
        9.57s for N = 1e4
    This solution does not scale at all well for N > 1e4.

    :returns: List of partitions (mod 1e9 + 7) of all N <= limit, with
        index == N.
    """

    combos_by_coin = [1] + [0]*(n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 2):
            combos_by_coin[j] += combos_by_coin[j-i]
    return [count % modulus for count in combos_by_coin]


def coin_pile_combos_theorem(limit: int, mod_value: int = modulus) -> list[int]:
    """
    Solution is based on the Pentagonal Number Theorem that states:

    (1 - x)(1 - x^2)(1 - x^3)... =
                            1 - x - x^2 + x^5 + x^7 - x^12 - x^15 + x^22 + x^26 - ...

    The right-side exponents are generalised pentagonal numbers given by the formula:

    g_k = k(3k - 1) / 2, for k = 1, -1, 2, -2, 3, -3, ...

    This holds as an identity for calculating the number of partitions of limit
    based on:

    p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7) + ..., which is expressed as:

    p(n) = Sigma{k!=0} ((-1)^{k-1} * p(n - g_k))

    SPEED (BETTER)
        17.47ms for N = 1e3
    SPEED (BETTER)
        582.54s for N = 1e4

    :returns: List of partitions (mod 1e9 + 7) of all N <= limit, with
        index == N.
    """

    partitions = [1] + [0]*limit
    for n in range(1, limit + 1):
        count = 0
        k = 1
        while True:
            pentagonal = k * (3 * k - 1) // 2
            if pentagonal > n:
                break
            if k % 2 == 1:
                count += partitions[n-pentagonal]
            else:
                count -= partitions[n-pentagonal]
            k *= -1
            if k > 0:
                k += 1
        partitions[n] = count % mod_value
    return partitions


def first_coin_combo() -> int:
    """
    Project Euler specific implementation that requests the first integer N for
    which the number of ways N can be partitioned is divisible by 1e6.
    """

    small_mod = 1_000_000
    limit = 0
    while True:
        limit += 10_000
        all_partitions = coin_pile_combos_theorem(limit, small_mod)
        for i, count in enumerate(all_partitions):
            if count % small_mod == 0:
                return i
