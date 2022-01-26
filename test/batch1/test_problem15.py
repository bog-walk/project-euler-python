import unittest
from solution.batch1.problem15 import lattice_path_routes


class LatticePaths(unittest.TestCase):
    def test_lattice_is_square(self):
        dimen = [1, 2, 3, 20]
        expected = [2, 6, 20, 846_527_861]
        for i, d in enumerate(dimen):
            self.assertEqual(expected[i], lattice_path_routes(d, d))

    def test_lattice_not_square(self):
        n, m = 3, 2
        expected = 10
        self.assertEqual(expected, lattice_path_routes(n, m))


if __name__ == '__main__':
    unittest.main()
