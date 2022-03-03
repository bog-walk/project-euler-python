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
from multiprocessing import Pool
from util.maths.reusable import is_prime_mr, prime_numbers

limit = 20000
# all non-single digit primes end in {1, 3, 7, 9} so 2 and 5 are ruled out
# elevated to global scope to all prime check for smaller numbers
all_primes = prime_numbers(limit - 1)
all_primes.remove(2)
all_primes.remove(5)


def is_concatenable_prime(prime_1: int, prime_2: int) -> bool:
    """
    Converting to and back from strings for concatenation can become slow.
    Instead, the first prime is multiplied to an appropriate power based on the
    amount of digits in the second prime, then they are added.
    """

    power_1, power_2 = 10, 10
    while power_1 <= prime_2:
        power_1 *= 10
    concat_1 = prime_1 * power_1 + prime_2
    is_concat_1_p = (concat_1 in all_primes
                     if concat_1 < limit
                     else is_prime_mr(concat_1))
    if not is_concat_1_p:
        return False
    while power_2 <= prime_1:
        power_2 *= 10
    concat_2 = prime_2 * power_2 + prime_1
    is_concat_2_p = (concat_2 in all_primes
                     if concat_2 < limit
                     else is_prime_mr(concat_2))
    return is_concat_2_p


def prime_pair_set_sums(n: int, k: int, m: int) -> list[int]:
    """
    Solution optimised by the following:

    -   Caching the results of concatenation & primality checks to avoid doing so
        for every nested iteration. The cache has every visited prime as a key
        and, as its value, a set of all greater primes with which it produces a
        prime after concatenation.

    -   Set intersection is used in lieu of checking for each nested prime in all
        preceding prime pair sets. An empty set after intersection means that the
        latest prime checked is not eligible and can be skipped, with the set
        intersection being reverted to its previous value.

    -   Refactored to be used in a multiprocessing function below by reducing list
        of primes to either include those that are congruent to 1 mod 3 or 2 mod 3.
        These lists can be processed separately as p_1, where p_1 % 3 == 1, and p_2,
        where p_2 % 3 == 2, will always concatenate to a number that is evenly
        divisible by 3, and thereby not a prime. This is based on the concatenation
        being congruent to the sum of p_1 and p_2 mod 3.

    SPEED (BETTER - for processing all primes < n)
        26.58s for N = 2e4, K = 5

    :param m: Modulo used to split all primes < n, to avoid unnecessary
        is_concatenable_prime() checks.
    :returns: Unsorted list of the totals of all k-prime sets whose
        members are eligible, as detailed above.
    """

    concatenated_pairs: dict[int, set[int]] = dict()
    primes = [3] + [p for p in all_primes if p < n and p % 3 == m]
    num_of_primes = len(primes)

    def get_pairs(prime_i: int):
        prime = primes[prime_i]
        pairs = set()
        for p in range(prime_i + 1, num_of_primes):
            other = primes[p]
            if is_concatenable_prime(prime, other):
                pairs.add(other)
        concatenated_pairs[prime] = pairs

    totals = []
    for a in range(num_of_primes - k + 1):
        k_a = primes[a]
        if k_a not in concatenated_pairs.keys():
            get_pairs(a)
        common = concatenated_pairs[k_a]
        for b in range(a + 1, num_of_primes - k + 2):
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
                    totals.append(k_a + k_b + k_c)
            else:
                for c in range(b + 1, num_of_primes - k + 3):
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
                            totals.append(k_a + k_b + k_c + k_d)
                    else:
                        for d in range(c + 1, num_of_primes - k + 4):
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
                                totals.append(k_a + k_b + k_c + k_d + k_e)
                            common = common_c
                    common = common_b
            common = common_a
    return totals


def multiprocessing_prime_pair_set_sum(n: int, k: int):
    """ Multiprocessing module solution processes 2 prime lists in parallel.

    A process Pool object controls the jobs given to the worker processes and
    allows results to be returned through a parallel map implementation.

    SPEED (BEST)
        11.84s for N = 2e4, K = 5

    :returns: Sorted list (ascending order) of the totals of all k-prime sets whose
        members are eligible, as detailed above.
    """

    pool = Pool(2)
    totals = pool.starmap(prime_pair_set_sums, [(n, k, 1), (n, k, 2)])
    pool.close()  # prevents more tasks from being submitted to pool
    # all complete tasks mean all processes will exit
    pool.join()  # main process waits for all worker processes to exit
    # flatmap Pool results
    totals = [total for result in totals for total in result]
    return sorted(totals)


def prime_pair_set_sum_concise(n: int, k: int) -> list[int]:
    """
    This solution is identical to the solution above, but uses a while loop
    instead of 4 nested for loops for improved legibility. Its process mimics that
    used in combinations() from the itertools module, except altered to skip multiple
    combinations, as enacted by the 'continue' statements in the nested loops above.

    In spite of its reduced length, this solution is 5x slower & was created
    purely as an algorithmic test.

    SPEED (WORSE)
        110.31s for N = 2e4, K = 5

    :returns: Sorted list (ascending order) of the totals of all k-prime sets whose
        members are eligible, as detailed above.
    """

    concatenated_pairs: dict[int, set[int]] = dict()
    primes = [3, 7]
    num_of_primes = 2
    for pr in all_primes:
        if pr < 11:
            continue
        if pr >= n:
            break
        primes.append(pr)
        num_of_primes += 1

    def get_pairs(prime_i: int):
        prime = primes[prime_i]
        pairs = []
        for p in range(prime_i + 1, num_of_primes):
            other = primes[p]
            if is_concatenable_prime(prime, other):
                pairs.append(other)
        concatenated_pairs[prime] = set(pairs)

    totals = []
    k_indices = list(range(k))
    get_pairs(0)
    common = concatenated_pairs[3]
    while True:
        skip_k_i, total = -1, 0
        for k_i, p_i in enumerate(k_indices):
            k_p = primes[p_i]
            if k_i == 0:
                if k_p not in concatenated_pairs.keys():
                    get_pairs(p_i)
                common = concatenated_pairs[k_p]
                total = k_p
                continue
            if k_p not in common:
                skip_k_i = k_i
                break
            if k_i == k - 1:
                for common_k in common:
                    totals.append(total + common_k)
                skip_k_i = k_i - 2
                break
            if k_p not in concatenated_pairs.keys():
                get_pairs(k_indices[k_i])
            common = common.intersection(concatenated_pairs[k_p])
            if len(common) == 0:
                skip_k_i = k_i
                break
            total += k_p
        # this loop cycles through all combinations from a set starting point
        for i in reversed(range(k)):
            if k_indices[i] == i + num_of_primes - k:
                if i - skip_k_i <= 1:
                    skip_k_i = -1
                continue
            if k_indices[i] != i + num_of_primes - k:
                if skip_k_i > -1:
                    i = skip_k_i
                break
        else:
            # leave while loop when all combinations exhausted
            break
        # this 'i' refers to non-local for loop target that leaks out of for block
        k_indices[i] += 1
        # this loop returns to the smallest combination from a new starting point
        for j in range(i + 1, k):
            k_indices[j] = k_indices[j-1] + 1
    return sorted(totals)
