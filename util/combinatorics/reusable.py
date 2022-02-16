def permutation_id(n: int) -> tuple[int]:
    """
    Generates a hash key N based on the amount of repeated digits, represented as
    an ordered LTR tuple.

    Hash key must be stored as a tuple rather than a number to allow for the
    possibility that N may have a digit that is repeated more than 9 times.

    e.g. 1487 -> (0, 1, 0, 0, 1, 0, 0, 1, 1)
         2214 -> (0, 1, 2, 0, 4)
         1_000_000_000_000 -> (12, 1)

    N.B. An alternative hash key would be the sorted string cast of the number,
    using "".join(sorted(str(num))). e.g. 1487 -> "1478", 2023 -> "0223".
    """

    p_id = [0]*(int(max(str(n))) + 1)
    while n:
        p_id[n % 10] += 1
        n //= 10
    return tuple(p_id)
