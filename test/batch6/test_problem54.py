import unittest
from util.tests.reusable import get_test_resource
from solution.batch6.problem54 import poker_hand_winner


class PokerHands(unittest.TestCase):
    def test_no_tie(self):
        hand_1_s = [
            ["5H", "5C", "6S", "7S", "KD"], ["5D", "8C", "9S", "JS", "AC"],
            ["2D", "9C", "AS", "AH", "AC"], ["QS", "TS", "KS", "JS", "AS"]
        ]
        hand_2_s = [
            ["2C", "3S", "8S", "8D", "TD"], ["2C", "5C", "7D", "8S", "QH"],
            ["3D", "6D", "7D", "TD", "QD"], ["TD", "TC", "TS", "AH", "TH"]
        ]
        expected = [2, 1, 2, 1]
        for i, e in enumerate(expected):
            self.assertEqual(e, poker_hand_winner(hand_1_s[i], hand_2_s[i]))

    def test_one_tie(self):
        hand_1_s = [
            ["4D", "6S", "9h", "QH", "QC"], ["2H", "2D", "4C", "4D", "4S"]
        ]
        hand_2_s = [
            ["3D", "6D", "7H", "QD", "QS"], ["3C", "3D", "3S", "9S", "9D"]
        ]
        expected = [1, 1]
        for i, e in enumerate(expected):
            self.assertEqual(e, poker_hand_winner(hand_1_s[i], hand_2_s[i]))

    def test_multiple_ties(self):
        hand_1_s = [
            ["2H", "2D", "4C", "4D", "4S"], ["2H", "3D", "5C", "7D", "9S"]
        ]
        hand_2_s = [
            ["4C", "4D", "4S", "9S", "9D"], ["1C", "3D", "5S", "7S", "9D"]
        ]
        expected = [2, 1]
        for i, e in enumerate(expected):
            self.assertEqual(e, poker_hand_winner(hand_1_s[i], hand_2_s[i]))

    def test_ace_low(self):
        hand_1 = ["2H", "3D", "4C", "AD", "5S"]
        hand_2 = ["2H", "2D", "4C", "4D", "8S"]
        expected = 1
        self.assertEqual(expected, poker_hand_winner(hand_1, hand_2))

    def test_PE_problem(self):
        expected = 376
        plays: list[list[str]] = get_test_resource(
            "../resources/poker_hands", transformation=str
        )
        player_1_wins = sum(
            poker_hand_winner(play[:5], play[5:]) == 1
            for play in plays
        )
        self.assertEqual(expected, player_1_wins)


if __name__ == '__main__':
    unittest.main()
