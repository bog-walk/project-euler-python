""" Problem 31: Coin Sums

https://projecteuler.net/problem=31

Goal: Count the number of ways (mod 1e9 + 7) that N pence
can be made using any combination of English coins.

Constraints: 1 <= N <= 1e5

English currency: There are 8 types of coins in circulation ->
{1p, 2p, 5p, 10p, 20p, 50p, 1 pound (= 100p), 2 pound (= 200p)}.

e.g.: N = 5 (i.e. goal is 5 pence in coins)
      combos = [{5p}, {2p, 2p, 1p}, {2p, 1p, 1p, 1p}, {1p, 1p, 1p, 1p, 1p}]
      count = 4
"""
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def count_coin_combos_recursive(n, coin=7):
    """
    Nested function used to retain internal state of cache between tests,
    particularly for speed test.

    SPEED: 266.6644s for N = 1e5
    """
    # Cannot use [[0]*8]*(n+1) because this would create a shallow list,
    # which creates only 1 integer object to which all array indices point,
    # so changing cache[0][0] e.g. would affect all values in 1st column equally,
    # since cache[0] is cache[1] == True.
    # The following way is better as it creates (n+1) separate list objects.
    recursive_cache = [[0 for _ in range(8)] for _ in range(n + 1)]

    def recursive_combos(num, coin_index):
        """
        Recursive solution optimised with memoisation using top-down approach.
        Repeatedly subtract each coin value from the target & sum combos previously
        calculated for smaller targets.

        :param [coin] Index of coin value from [coins] above. Default is the
        largest coin available (2 pounds).
        This parameter allows flexibility in method purpose ->
        e.g. Could find combos for making 10p using 2p (& lower coins) = 6,
        instead of making 10p using all possible coins = 11 combos.
        """
        if coin_index < 1:
            return 1
        if recursive_cache[num][coin_index] > 0:
            return recursive_cache[num][coin_index]
        target = num
        combos = 0
        while target >= 0:
            combos += recursive_combos(target, coin_index - 1)
            target -= coins[coin_index]
        recursive_cache[num][coin_index] = combos
        return combos

    return recursive_combos(n, coin) % 1_000_000_007


def count_coin_combos(n):
    """
    Bottom-up approach that determines a target's combo based on:
    - the previous combo calculated for the coin with a smaller target, &
    - the previous combo calculated for a coin of lesser value.

    SPEED (BEST): 0.1358s for N = 1e5
    Better performance due less expensive loops (vs recursive function calls)
    & use of less memory with better cache-access.
    """
    combos_by_coin = [0] * (n + 1)
    # Base case for when 0p is needed
    combos_by_coin[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            combos_by_coin[i] += combos_by_coin[i - coin]
    return combos_by_coin[n] % 1_000_000_007

