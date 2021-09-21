import unittest
from solution.batch2.problem15 import lattice_path_routes


class LatticePaths(unittest.TestCase):
    def test_lattice_path_routes_square(self):
        dimen = [1, 2, 3, 20]
        expected = [2, 6, 20, 846527861]
        for index, d in enumerate(dimen):
            self.assertEqual(expected[index], lattice_path_routes(d, d))

    def test_lattice_path_routes_not_square(self):
        self.assertEqual(10, lattice_path_routes(3, 2))


if __name__ == '__main__':
    unittest.main()
