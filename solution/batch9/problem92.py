""" Problem 92: Square Digit Chains

https://projecteuler.net/problem=92

Goal: Return the count of starting numbers below 10^K will arrive at 89
(modulo 10^9 + 7).

Constraints: 1 <= K <= 200

Square Digit Chain: Sequence created by adding the square of the digits in a
number to form a new number until it has been seen before.
        e.g. 44 -> 32 -> 13 -> 10 -> 1 -> 1
             85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
All starting numbers will eventually end in an infinite loop of 1 or 89.

Happy Number: A positive integer whose square digit chain ends in 1. The first
few are: {1, 7, 10, 13, 19, 23}. If a number is known to be happy, any number in
its sequence is also happy, as are any permutations of that number.
Unhappy Number: A positive integer whose square digit chain does not end in 1. The
first few are: {2, 3, 4, 5, 6, 8}.

e.g.: K = 1
      1 -> 1
      2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
      3 -> 9 -> 81 -> 65 -> 61 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 ->
            37 -> 58 -> 89
      4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
      5 -> 25 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
      6 -> 36 -> 45 -> 41 -> 17 -> 50 -> 25 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 ->
            4 -> 16 -> 37 -> 58 -> 89
      7 -> 49 -> 97 -> 130 -> 10 -> 1 -> 1
      8 -> 64 -> 52 -> 29 -> 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
      9 -> 81 -> 65 -> 61 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 ->
            58 -> 89
      count = 7
"""


modulo = 1_000_000_007
squares = [i * i for i in range(10)]


def digit_squared_sum(number: str) -> int:
    return sum(squares[int(ch)] for ch in number)


def count_sd_chains_brute(k: int) -> int:
    """
    Iterates through all starters to find the end chain value and stores results
    in a cache to reduce chain formation in later starters.

    SPEED (WORSE)
        32.13s for K = 7
    """

    sum_limit = 200 * 9 * 9
    cache = [0]*(sum_limit + 1)
    count = 0

    limit = 10**k
    starter = 2
    while starter < limit:
        number = digit_squared_sum(str(starter))
        while number != 1 and number != 89:
            match cache[number]:
                case 1:
                    number = 1
                    break
                case 89:
                    number = 89
                    break
                case 0:
                    number = digit_squared_sum(str(number))
        if number == 89:
            count += 1
            count %= modulo
        if starter < sum_limit:
            cache[starter] = number
        starter += 1

    return count


def count_sd_chains(k: int) -> int:
    """
    Iterates through all potential sums of squared [k] digits and stores in a
    cache the amount of starters that will result in each sum. Each potential sum
    is then iterated over and, if found to have the desired end chain value,
    its stored count is accumulated.

    SPEED (BETTER)
        10.24ms for K = 7
    """

    limit = k * 9 * 9 + 1
    cache = [0]*limit
    # single digit sums
    for square in squares:
        cache[square] += 1

    for digits in range(2, k + 1):
        for total in range(digits * 9 * 9, 0, -1):
            for d in range(1, 10):
                square = d * d
                if square > total:
                    break
                # since sums are iterating backwards, add count of all sums without
                # the most recent digit d
                cache[total] += cache[total-square]
                cache[total] %= modulo

    count = 0

    for i in range(2, limit):
        if cache[i] == 0:
            continue
        total = i
        while total != 1 and total != 89:
            total = digit_squared_sum(str(total))
        if total == 89:
            count += cache[i]
            count %= modulo

    return count
