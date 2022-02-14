""" Problem 54: Poker Hands

https://projecteuler.net/problem=54

Goal: Determine the winner when presented with 2 poker hands, based on the rules
detailed below and assuming that all cards are valid and a winner is possible.

Constraints: None

Poker Hand Rankings: From lowest to highest ->
[High Cards, One Pair, Two Pairs, Three of a kind, Straight, Flush, Full House,
Four of a kind, Straight Flush, Royal Flush]

If both hands have the same ranked hand, the rank made up of the highest value
wins. If both ranks tie, then the highest value of the next highest rank is
assessed until the only rank left to assess is the high card rank.

e.g.: hand 1 = "5H 6H 2S KS 3D" -> High card King
      hand 2 = "5D JD 7H JS 8H" -> One pair Joker
      winner = player 2

      hand 1 = "AH AC AS 7S 7C" -> Full house 3 Aces, One pair 7
      hand 2 = "AS 3S 3D AD AH" -> Full house 3 Aces, One pair 3
      winner = player 1
"""


def normalise_count(values: tuple[str]) -> list[int]:
    """
    Normalises card values to range from 1 to 14 & counts the amount of
    each card in the hand. Note that Ace cards are counted as both high & low.

    :returns: List of card counts with card value == index.
        e.g. [0, 0, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0, 1, 0] represents a hand with
        2 fives, 1 six, 1 seven, and 1 King.
    """

    non_nums = ["T", "J", "Q", "K", "A"]
    count = [0]*15
    for value in values:
        num = ord(value) - 48 if value < ":" else 10 + non_nums.index(value)
        count[num] += 1
        if num == 14:  # count Ace as a high or low card
            count[1] += 1
    return count


def rank_hand(hand: list[str]) -> list[list]:
    """
    Rank a five card hand based on the following order, lowest to highest:

    [High Cards, One Pair, Two Pairs, Three of a kind, Straight, Flush, Full
    House, Four of a kind, Straight Flush, Royal Flush]

    All existing ranks are presented as their highest relevant card to allow
    potential ties between hands to be broken without needing to re-rank them.

    e.g.
        ["4C", "4D", "4S", "9S", "9D"] is presented as:

        [[], [9], [], [4], [], [], [4], [], [], []], which, when evaluated from
        RtL means the hand has Full House with 3 Fours, then 3 Fours, then 2 Nines.

        ["3D", "6D", "7H", "QD", "QS"] is presented as:

        [[7, 6, 3], [12], [], [], [], [], [], [], [], []], which, when evaluated from
        RtL means the hand has 2 Queens, then High card 7, then 6, then 3.
    """

    ranks = [[] for _ in range(10)]  # nested list to allow multiple high cards
    values, suits = list(zip(*hand))
    unique_suits = len(set(suits))
    count = normalise_count(values)
    streak, pair, triple = 0, 0, 0
    for i in range(14, 1, -1):  # move backwards to sort high cards in reverse
        match count[i]:
            case 0:  # no cards of value i
                streak = 0
                continue
            case 4:  # 4 of a kind
                ranks[7].append(i)
            case 3:  # 3 of a kind
                ranks[3].append(i)
                triple = i
            case 2:  # 1 pair, at minimum
                if pair != 0:  # 2 pair
                    # give the 2 pair ranking the higher value pair
                    ranks[1], ranks[2] = sorted([[i], ranks[1]])
                else:
                    ranks[1].append(i)
                    pair = i
            case 1:  # high card
                ranks[0].append(i)
        streak += 1
        if streak == 5 or (streak == 4 and i == 2 and count[1] > 0):  # straight
            if streak == 4:  # low ace straight
                ranks[4].append(5)
            else:
                ranks[4].append(i + 4)
            if unique_suits == 1:  # straight flush
                ranks[8].append(i + 4)
                if i == 10:  # royal flush
                    ranks[9].append(14)
            break  # no further cards if streak achieved
    if triple and pair:  # full house
        ranks[6].append(triple)  # give the fh ranking the 3 of a kind value
    if unique_suits == 1:  # flush
        # break flush ties with highest card
        ranks[5].append(max(ranks[0]))
    return ranks


def poker_hand_winner(hand_1: list[str], hand_2: list[str]) -> int:
    """
    Compares lists representing all possible ranks for both hands, in reverse
    order, as this allows higher ranking possibilities to be compared first. If a
    rank has equal values, the next highest rank possibility will be compared
    using Python's intrinsic list comparison tools. If comparison comes down to
    individual high cards, they have already been returned in reverse order by the
    helper function for intrinsic list comparison.

    :returns: 1 if [hand_1] is the winner; otherwise, 2.
    """

    hand_1_ranks = rank_hand(hand_1)
    hand_2_ranks = rank_hand(hand_2)
    return 1 if hand_1_ranks[::-1] > hand_2_ranks[::-1] else 2
