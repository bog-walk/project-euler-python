import unittest
from util.tests.reusable import compare_speed, get_test_resource
from solution.batch9.problem99 import k_smallest_exponential, \
    k_smallest_exponential_alt, largest_exponential


class LargestExponential(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resource: list[str] = get_test_resource(
            "../resources/largest_exponential.txt"
        )

    def test_HR_problem_with_small_exponentials(self):
        inputs = ["4 7", "3 7", "2 11"]
        k = 2
        expected = (3, 7)

        self.assertTupleEqual(expected, k_smallest_exponential(inputs, k))
        self.assertTupleEqual(expected, k_smallest_exponential_alt(inputs, k))

    def test_HR_problem_with_medium_exponentials(self):
        inputs = ["2 350", "5 150", "9 50", "7 850"]
        k = 1
        expected = (9, 50)

        self.assertTupleEqual(expected, k_smallest_exponential(inputs, k))
        self.assertTupleEqual(expected, k_smallest_exponential_alt(inputs, k))

    def test_HR_problem_with_large_exponentials(self):
        inputs = ["895447 504922", "44840 646067", "45860 644715", "463487 530404",
                  "398164 536654", "894483 504959", "619415 518874"]
        k = 7
        expected = (895_447, 504_922)

        self.assertTupleEqual(expected, k_smallest_exponential(inputs, k))
        self.assertTupleEqual(expected, k_smallest_exponential_alt(inputs, k))

    def test_HR_problem_speed(self):
        inputs = list(map(lambda s: s.replace(",", " "), self.resource))
        k = 1000
        expected = (895_447, 504_922)
        solutions = {
            "Original": [k_smallest_exponential, inputs, k],
            "Alt": [k_smallest_exponential_alt, inputs, k],
        }
        results = compare_speed(solutions)
        self.assertTrue(all(expected == actual for actual in results.values()))

    def test_PE_problem(self):
        expected = (895_447, 504_922, 709)

        self.assertTupleEqual(expected, largest_exponential(self.resource))


if __name__ == '__main__':
    unittest.main()
