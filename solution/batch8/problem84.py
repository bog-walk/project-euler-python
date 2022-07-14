""" Problem 84: Monopoly Odds

https://projecteuler.net/problem=84

Goal: Given a standard Monopoly board & the rules detailed below, find the K
squares with the highest probability of being landed on when using a N-sided dice.
The squares should be represented as a (K * 2)-digit modal string in descending
order of popularity.

Constraints: 4 <= N < 40, 3 <= K <= 40

A Monopoly board can be represented as:

        [GO, A1, CC1, A2, T1, R1, B1, CH1, B2, B3]
        [JAIL, C1, U1, C2, C3, R2, D1, CC2, D2, D3]
        [FP, E1, CH2, E2, E3, R3, F1, F2, U2, F3]
        [G2J, G1, G2, CC3, G3, R4, CH3, H1, T2, H2]

If a player starts on GO & adds the scores of 2 6-sided dice to advance clockwise,
without any further rules, they would expect to visit each square with equal
probability of 2.5%. However, landing on G2J sends the player to JAIL, as would
picking the 1 jail card in both the CC and CH piles. A player is also sent to jail
if they roll 3 doubles in a row. The only CC cards that involve movement (2/16)
either end at GO or JAIL. The 10/16 CH cards cause the following  movements:
GO, JAIL, C1, E3, H2, R1, next R, next R, next U, back 3 squares.

Since this problem only cares about the probability of finishing on a square after
a roll, G2J will be the only square that has a probability of 0. The CH squares
will have the lowest probabilities as 10/16 = 5/8 cause movement to another square.

N.B. There should be no distinction between "Just Visiting" and being sent to JAIL
and, unlike the normal rules, a player cannot leave jail by rolling a double (they
are assumed to pay on their next turn).

e.g.: N = 6, K = 3
      JAIL (6.24%) at square 10
      E3 (3.18%) at square 24
      GO (3.09%) at square 00
      result = "102400"
"""


def get_dice_probability(sides: int) -> [float]:
    outcomes = sides ** 2
    # outcomes of 0 or 1 are not possible but remain for easier indexing
    probabilities = [0.0]*(sides * 2 + 1)
    for i in range(1, sides+1):
        for j in range(1, sides+1):
            probabilities[i+j] += 1
    return [p / outcomes for p in probabilities]


def adjust_for_chance(row: [float], square: int, roll_prob: float):
    row[square] += roll_prob * 3 / 8  # stay on CH
    # move to [GO, R1, JAIL, C1, E3, H2]
    for i in [0, 5, 10, 11, 24, 39]:
        row[i] += roll_prob / 16
    match square:
        case 7:
            row[15] += roll_prob / 8  # next R = R2
            row[12] += roll_prob / 16  # next U = U1
            row[square - 3] += roll_prob / 16  # move back 3
        case 22:
            row[25] += roll_prob / 8  # next R = R3
            row[28] += roll_prob / 16  # next U = U2
            row[square - 3] += roll_prob / 16  # move back 3
        case 36:
            row[5] += roll_prob / 8  # next R = R1
            row[12] += roll_prob / 16  # next U = U1
            # move back 3 lands on CC3
            adjust_for_chest(row, 33, roll_prob / 16)


def adjust_for_chest(row: [float], square: int, roll_prob: float):
    row[square] += roll_prob * 7 / 8  # stay on CC
    for i in [0, 10]:  # move to [GO, JAIL]
        row[i] += roll_prob / 16


def transpose(matrix: [[float]]) -> [[float]]:
    # alt to [[row[c] for row in matrix] for c in range(len(matrix[0]))]
    return [list(row) for row in zip(*matrix)]


def product(row1: [float], row2: [float]) -> float:
    return sum(x * y for x, y in zip(row1, row2))


def markov_chain_odds(n: int, k: int) -> str:
    """
    A Markov Chain is a memory-less stochastic process in that the probability of
    transitioning to any particular state is dependent solely on the current state &
    time elapsed (the latter is unimportant if the chain is also time-homogenous).
    Given this Markov property, this solution must ignore the Monopoly rule
    concerning 3 doubles in a row sending a player to jail.

    For any positive integer n and possible states i_0, i_1, ..., i_n, a Markov
    Chain is a sequence that satisfies the rule of conditional independence,
    such that:

    P(X_n = i_n | X_n-1 = i_n-1) = P(X_n = i_n | X_0 = i_0, X_1 = i_1, ..., X_n-1 = i_n-1)

    This allows for non-stationary transition probabilities & time-inhomogenous chains
    (i.e. as the number of steps increase, the probability of moving to another
    state may change).

    A transition matrix P_t for Markov Chain {X} at time t is built using:

    (P_t)_i,j = P(X_t+1 = j | X_t = i)

    with each matrix row being a probability vector with a row sum of 1.

    The product of subsequent matrices describes the transition along time-intervals,
    such that:

    the (i, j)th position of P_t * P_t+1 * ... * P_t+k -> P(X_t+k+1 = j | X_t = i)

    e.g. P_0 * P_1 has in its (i, j)th position the probability that X_2 = j
    given that X_0 = i.
    """

    matrix = [[0.0]*40 for _ in range(40)]
    roll_stats = get_dice_probability(n)
    for square in range(40):
        for i, prob in enumerate(roll_stats):
            if i < 2:
                continue
            next_square = (square + i) % 40
            match next_square:
                case 30:
                    matrix[square][10] += prob
                case 7 | 22 | 36:
                    adjust_for_chance(matrix[square], next_square, prob)
                case 2 | 17 | 33:
                    adjust_for_chest(matrix[square], next_square, prob)
                case _:
                    matrix[square][next_square] += prob
                
    # flip columns to rows for easier access
    transposed = transpose(matrix)
    # initialise with the probability of landing on square 0 (GO) after
    # 0 rolls being 1.0
    odds = [0.0]*40
    odds[0] = 1.0
    for _ in range(40):
        odds = [product(odds, transposed[r]) for r in range(40)]

    top_squares = sorted(
        list((str(i).zfill(2), prob) for i, prob in zip(range(40), odds)),
        key=lambda e: e[1],
        reverse=True
    )[:k]
    return "".join(sq[0] for sq in top_squares)
