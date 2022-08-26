import unittest
from util.tests.reusable import compare_speed
from solution.batch8.problem86 import count_distinct_cuboids, \
    cuboid_counts_quick_draw, get_least_m


class CuboidRoute(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_counts = cuboid_counts_quick_draw()

    def test_HR_problem_lower_constraints(self):
        inputs = [1, 2, 3, 10, 99, 100]
        expected = [0, 0, 2, 14, 1975, 2060]
        for m, e in zip(inputs, expected):
            self.assertEqual(e, count_distinct_cuboids(m))
            self.assertEqual(e, self.all_counts[m])

    def test_HR_problem_mid_constraints(self):
        inputs = [1999, 5612]
        expected = [1_226_406, 10_848_941]
        for m, e in zip(inputs, expected):
            self.assertEqual(e, count_distinct_cuboids(m))
            self.assertEqual(e, self.all_counts[m])

    def test_HR_problem_speed(self):
        m = 10_000
        expected = 36_553_574
        solutions = {
            "Original": [count_distinct_cuboids, m],
            "Quick draw": [cuboid_counts_quick_draw],
        }
        results = compare_speed(solutions)
        self.assertEqual(expected, results.get("Original"))
        self.assertEqual(expected, results.get("Quick draw")[m])

    def test_HR_problem_upper_constraints(self):
        inputs = [100_000, 200_000, 400_000]
        expected = [4_487_105_091, 18_954_950_955, 79_838_573_329]
        for m, e in zip(inputs, expected):
            self.assertEqual(e, self.all_counts[m])

    def test_PE_problem(self):
        target = 1_000_000
        expected = 1818
        self.assertEqual(expected, get_least_m(target))


if __name__ == '__main__':
    unittest.main()
