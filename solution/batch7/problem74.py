""" Problem 74: Digit Factorial Chains

https://projecteuler.net/problem=74

Goal: For a given length L and limit N, return all integers <= N that start a
digit factorial non-repeating chain of length L.

Constraints: 10 <= N <= 1e6, 1 <= L <= 60

Other than the factorions 145 & 40585 that loop with themselves
(1! + 4! + 5! = 145), only 3 loops exist:

    169 -> 363601 -> 1454 -> 169
    871 -> 45361 -> 871
    872 -> 45362 -> 872

Every starting number eventually becomes stuck in a loop, e.g:

    69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)

The above chain is of length 5 and the longest non-repeating chain with a starting
number < 1e6 has 60 terms.

e.g.: N = 221, L = 7
      output = {24, 42, 104, 114, 140, 141}
"""
from math import factorial
from util.combinatorics.reusable import permutation_id


# pre-calculation of all digit factorials to increase performance
factorials = [factorial(x) for x in range(10)]
# store all special case numbers that either loop to themselves (factorions)
# or to others
loop_nums = [145, 169, 871, 872, 1454, 40585, 45361, 45362, 363601]
# pre-generate the id of these special case numbers
loop_perms = [permutation_id(n) for n in loop_nums]


def digit_factorial_chain_starters(limit: int, length: int) -> list[int]:
    """
    Solution based on the following:

    - 1! & 2! will cause an infinite loop with themselves. The only non-single
    digit factorions are: 145 and 40585.

    - If a chain encounters an element in the 3 aforementioned loops or a
    factorion, it will become stuck & the search can be broken early without
    waiting for a repeated element to be found.

    - A starter will also be discarded early if it has not encountered a loop but
    has exceeded the requested length.

    - A cache of permutation_id(n) to chain length is created to reduce digit
    factorial sum calculations of every starter <= limit.

    - Getting the permutation of a number & checking it against the class
    variables of special case numbers prevents wrong results caused by
    permutations that don't actually start loops.
    e.g. 27 -> 5042 -> 147 -> 5065 -> 961 -> {363601 -> loop}. 961 has the same
    id as 169 but technically does not start the loop, so the count must be
    incremented.

    - All new chain elements (less than limit & up until a loop element is
    encountered) are stored so that they can be cached with a count using
    backtracking.
    e.g. 69 -> 363600 -> loop element = count 5;
        so cache[id(363600)] = 4 & cache[id(69)] = 5.

    SPEED (BETTER)
        3.23s for N = 1e6, L = 10
    """

    starters = []
    cache = {
        permutation_id(1): 1,
        permutation_id(2): 1,
        loop_perms[0]: 1, loop_perms[1]: 3, loop_perms[2]: 2,
        loop_perms[3]: 2, loop_perms[4]: 3, loop_perms[5]: 1,
        loop_perms[6]: 2, loop_perms[7]: 2, loop_perms[8]: 3
    }
    for n in range(limit + 1):
        perm_id = permutation_id(n)
        if perm_id in cache:
            cached_length = cache[perm_id]
            if perm_id in loop_perms and n not in loop_nums:
                cached_length += 1
            if cached_length == length:
                starters.append(n)
            continue
        chain = [perm_id]
        count = 1
        prev = n
        exceeded = False
        while True:
            prev = sum(map(lambda ch: factorials[int(ch)], str(prev)))
            perm_id = permutation_id(prev)
            if perm_id in cache:
                count += cache[perm_id]
                if perm_id in loop_perms and prev not in loop_nums:
                    count += 1
                break
            else:
                if prev <= limit:
                    chain.append(perm_id)
                else:
                    chain.append("")
                count += 1
                if count > length:
                    exceeded = True
                    break
        if exceeded:
            continue
        for i, element in enumerate(chain):
            if len(element):
                cache[element] = count - i
        if count == length:
            starters.append(n)
    return starters


def digit_factorial_chain_starters_improved(limit: int, length: int) -> list[int]:
    """
    Solution improved by not checking every chain element for a match with a
    special case loop starter. The search is instead stopped early if the element
    cannot be added to the chain set because it already exists.

    This forces the cache to have to store the special case number count values
    already falsely incremented & to catch these special cases again before
    checking final count length.

    SPEED (BETTER)
        3.32s for N = 1e6, L = 10
    """

    starters = []
    cache = {
        # 145, 169, 40585
        loop_perms[0]: 2, loop_perms[1]: 4, loop_perms[5]: 2
    }
    for n in range(limit + 1):
        perm_id = permutation_id(n)
        if perm_id not in cache:
            chain = set()
            prev = n
            while prev not in chain and len(chain) <= length:
                chain.add(prev)
                prev = sum(map(lambda ch: factorials[int(ch)], str(prev)))
            cache[perm_id] = len(chain)
        if n == 145 or n == 40585:
            valid = length == 1
        elif n in [169, 1454, 363601]:
            valid = length == 3
        elif n in [871, 872, 45361, 45362]:
            valid = length == 2
        else:
            valid = cache[perm_id] == length
        if valid:
            starters.append(n)
    return starters


def digit_factorial_chain_starters_optimised(
        limit: int,
        length: int
) -> list[int]:
    """
    Solution identical to the original except that it does not attempt to add all
    chain elements to the cache, only the starter element.

    Optimise this solution even further by creating an array of size 60 with each
    index representing (length - 1) & storing a list of starters that produce
    this chain length. The array would be propagated in the main loop by not
    breaking the loop for a set length & adding each n to this array instead of
    the starters list. That way, the array can be made for all 1e6 starters &
    multiple test cases can be picked by simply filtering the list stored at
    index (length - 1). The value 0 would need to be added to the starters list
    as a special case if length == 2.

    SPEED (BEST)
        2.97s for N = 1e6, L = 10
    """

    starters = []
    cache = {
        permutation_id(1): 1,
        permutation_id(2): 1,
        loop_perms[0]: 1, loop_perms[1]: 3, loop_perms[2]: 2,
        loop_perms[3]: 2, loop_perms[4]: 3, loop_perms[5]: 1,
        loop_perms[6]: 2, loop_perms[7]: 2, loop_perms[8]: 3
    }
    for n in range(limit + 1):
        n_perm_id = permutation_id(n)
        if n_perm_id not in cache:
            count = 1
            prev = n
            exceeded = False
            while True:
                prev = sum(map(lambda ch: factorials[int(ch)], str(prev)))
                perm_id = permutation_id(prev)
                if perm_id in cache:
                    count += cache[perm_id]
                    if perm_id in loop_perms and prev not in loop_nums:
                        count += 1
                    break
                else:
                    count += 1
                    if count > length:
                        exceeded = True
                        break
            if exceeded:
                continue
            cache[n_perm_id] = count
        cached_length = cache[n_perm_id]
        if n_perm_id in loop_perms and n not in loop_nums:
            cached_length += 1
        if cached_length == length:
            starters.append(n)
    return starters
