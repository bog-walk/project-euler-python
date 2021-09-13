import unittest


def get_test_grid(filename):
    with open(filename) as gridFile:
        grid = [row.strip().split() for row in gridFile]
    return grid


class LargestProductInGrid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.small_grid = get_test_grid("../resources/largest_product_in_grid_4by4")
        cls.mid_grid = get_test_grid("../resources/largest_product_in_grid_6by6")
        cls.large_grid = get_test_grid("../resources/largest_product_in_grid_20by20")

    def test_grid_setup(self):
        print(type(self.small_grid[0]))
        self.assertEqual(4, len(self.small_grid))


if __name__ == '__main__':
    unittest.main()
