""" Problem 31: Coin Sums

https://projecteuler.net/problem=31

Goal: Count the number of ways (mod 1e9 + 7) that N pence can be made using any
combination of English coins.

Constraints: 1 <= N <= 1e5

English currency: There are 8 types of coins in circulation ->
{1p, 2p, 5p, 10p, 20p, 50p, 1 pound (= 100p), 2 pound (= 200p)}.

e.g.: N = 5 (i.e. goal is 5 pence in coins)
      combos = [{5p}, {2p, 2p, 1p}, {2p, 1p, 1p, 1p}, {1p, 1p, 1p, 1p, 1p}]
      count = 4
"""
coins = [1, 2, 5, 10, 20, 50, 100, 200]
modulus = 1_000_000_007


def count_coin_combos_recursive(n: int, coin: int = 7) -> int:
    """
    Recursive solution uses nested function to allow memoisation, thereby
    optimising this top-down approach.

    :param n: Total amount that needs to be achieved by all combinations.
    :param coin: Index of coin value from global [coins]. Default is the
        largest coin available (2 pounds). This parameter allows flexibility in the
        method purpose.
        e.g. Count combos for making 10p using 2p (& lower coins) = 6,
        instead of making 10p using all possible coins = 11 combos.

    SPEED (WORSE)
        234.71s for N = 1e5
    """

    # cannot use [[0]*8]*(n+1) to make a 2D array because this would create a
    # shallow list, which creates only 1 integer object to which all array indices
    # point, so changing e.g. cache[0][0] would affect all values in the 1st column
    # equally, since cache[0] is cache[1] == True.
    # the following way is better as it creates (n + 1) independent lists, each
    # with 8 elements.
    cache = [[0]*8 for _ in range(n + 1)]

    def recursive_combos(num: int, coin_index: int) -> int:
        """
        Repeatedly subtract each coin value from the target value & sum any combos
        previously calculated for smaller targets.
        """

        if coin_index < 1:
            return 1
        if cache[num][coin_index] > 0:
            return cache[num][coin_index]
        target = num
        combos = 0
        while target >= 0:
            combos += recursive_combos(target, coin_index - 1)
            target -= coins[coin_index]
        cache[num][coin_index] = combos
        return combos

    return recursive_combos(n, coin) % modulus


def count_coin_combos(n: int) -> int:
    """
    Solution uses bottom-up approach that determines a target's combo based on:

    -   The previous combo calculated for the coin with a smaller target, &
    -   The previous combo calculated for a coin of lesser value.

    SPEED (BETTER)
        0.11s for N = 1e5
        Better performance due to less expensive loops (vs more expensive recursive
        function calls) & use of less memory with better cache-access.
    """

    # index 0 exists for when 0p is needed
    combos_by_coin = [1] + [0]*n
    for coin in coins:
        for i in range(coin, n + 1):
            combos_by_coin[i] += combos_by_coin[i - coin]
    return combos_by_coin[n] % modulus
