import unittest
from util.custom.pyramid_tree import *


class PyramidTreeTest(unittest.TestCase):
    def test_pyramid_only_root(self):
        pyramid = PyramidTree(1, [10])
        self.assertEqual(10, pyramid.root.value)
        self.assertIsNone(pyramid.root.left_adjacent)
        self.assertIsNone(pyramid.root.right_adjacent)
        self.assertEqual(10, pyramid.max_sum_post_order_traversal(pyramid.root))

    def test_pyramid_two_rows(self):
        pyramid = PyramidTree(2, [1, 2, 3])
        root = pyramid.root
        self.assertEqual(1, root.value)
        self.assertEqual(2, root.left_adjacent.value)
        self.assertEqual(3, root.right_adjacent.value)
        self.assertEqual(4, pyramid.max_sum_post_order_traversal(root))

    def test_pyramid_max_rows_one_route(self):
        elements = [0]*120
        elements[100] = 99
        pyramid = PyramidTree(15, elements)
        self.assertEqual(99, pyramid.max_sum_post_order_traversal(pyramid.root))

    def test_pyramid_max_rows_two_routes(self):
        elements = [1]*120
        elements[108] = 11
        elements[116] = 99
        pyramid = PyramidTree(15, elements)
        self.assertEqual(113, pyramid.max_sum_post_order_traversal(pyramid.root))


if __name__ == '__main__':
    unittest.main()
