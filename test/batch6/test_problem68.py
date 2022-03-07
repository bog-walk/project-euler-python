import unittest
from util.tests.reusable import compare_speed
from solution.batch6.problem68 import *


class Magic5GonRing(unittest.TestCase):
    def test_HR_problem_for_magic_3_gon_ring(self):
        n = 3
        expected = [
            ["423531612", "432621513"], ["235451613", "253631415"],
            ["146362524", "164542326"], ["156264345", "165354246"]
        ]
        for i, s in enumerate(range(9, 13)):
            self.assertListEqual(expected[i], magic_ring_solutions(n, s))
            self.assertListEqual(expected[i], magic_ring_solutions_improved(n, s))
            self.assertListEqual(expected[i], magic_ring_solutions_optimised(n, s))
            self.assertListEqual(
                expected[i], magic_ring_solutions_optimised_alt(n, s)
            )

    def test_HR_problem_for_magic_4_gon_ring(self):
        n = 4
        expected = [
            ["426561813732", "462723831516"],
            ["256364841715", "265751814346", "328481715652", "382625751418"],
            ["158284743635", "185653734248", "248581617374", "284347671518"],
            ["168483537276", "186267573438"], []
        ]
        for i, s in enumerate(range(12, 17)):
            self.assertListEqual(expected[i], magic_ring_solutions(n, s))
            self.assertListEqual(expected[i], magic_ring_solutions_improved(n, s))
            self.assertListEqual(expected[i], magic_ring_solutions_optimised(n, s))
            self.assertListEqual(
                expected[i], magic_ring_solutions_optimised_alt(n, s)
            )

    def test_HR_problem_for_magic_6_gon_ring(self):
        n = 6
        expected = [
            [
                "467872122393511511016", "467971111510521223836",
                "476106111159531232827", "476863123210251151917",
                "629791111585410431232", "692122310348451151719"
            ],
            ["3105115212246489817110", "3510710191868412421125"],
            [
                "1117107282969412435311", "1117973123410458562611",
                "1711211686510541243937", "1711511312346498921027",
                "2116126110184879735311", "2125115393747810816112",
                "2125658108111179734312", "2512412393711711018685",
                "2512612110184879731135", "2611511393747810811216",
                "2896941243531171111018", "2981081711151131234649"
            ]
        ]
        for i, s in enumerate(range(17, 20)):
            self.assertListEqual(expected[i], magic_ring_solutions(n, s))
            self.assertListEqual(expected[i], magic_ring_solutions_improved(n, s))
            self.assertListEqual(expected[i], magic_ring_solutions_optimised(n, s))
            self.assertListEqual(
                expected[i], magic_ring_solutions_optimised_alt(n, s)
            )

    def test_speed_for_magic_7_gon_ring(self):
        n = 7
        s = 23
        expected_size = 58
        solutions = {
            "Original": [magic_ring_solutions, n, s],
            "Improved": [magic_ring_solutions_improved, n, s],
            "Optimised": [magic_ring_solutions_optimised, n, s],
            "Alt": [magic_ring_solutions_optimised_alt, n, s]
        }
        results = list(compare_speed(solutions).values())
        self.assertTrue(all(len(r) == expected_size for r in results))
        self.assertListEqual(results[0], results[1])
        self.assertListEqual(results[1], results[2])
        self.assertListEqual(results[2], results[3])

    def test_PE_problem(self):
        expected = "6531031914842725"
        self.assertEqual(expected, max_magic_5_gon_solution())


if __name__ == '__main__':
    unittest.main()
