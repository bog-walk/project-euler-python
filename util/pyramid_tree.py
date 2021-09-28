class PyramidNode:

    def __init__(self, value):
        self.value = value
        self.left_adjacent = None
        self.right_adjacent = None

    def draw_node(self, prefix: list[str], is_tail: bool, string: list[str]) -> list[str]:
        """
        Allows graph to be printed showing children of all nodes.
        Note that shared adjacent nodes will be duplicated because of this.
        """
        vertical = "|   "
        space = "    "
        down = "└── "
        up = "┌── "
        if self.right_adjacent is not None:
            self.right_adjacent.draw_node(
                ["".join(prefix), vertical if is_tail else space], False, string
            )
        string += prefix + [down if is_tail else up, str(self.value), "\n"]
        if self.left_adjacent is not None:
            self.left_adjacent.draw_node(
                ["".join(prefix), space if is_tail else vertical], True, string
            )
        return string


class PyramidTree:
    """
    A Tree (more appropriately a graph) with each node having 2 children
    except for leaf nodes. Every node that is not along the left or right
    edges will have 2 parents. i.e. Internal children are shared by 2 nodes,
    with nodeX.rightAdjacent == nodeY.leftAdjacent.
    This means each level in the tree will have an amount of nodes equivalent
    to the level number.
    This tree is not ordered as for a BinaryTree.
    """

    def __init__(self, rows, elements):
        self.rows = rows
        self.nodes = self.__generate_tree(elements)
        self.root = self.nodes[0]

    def __generate_tree(self, elements: list[int]) -> list[PyramidNode]:
        nodes = [PyramidNode(e) for e in elements]
        index = 0
        for row in range(1, self.rows):
            for _ in range(row):
                nodes[index].left_adjacent = nodes[index + row]
                nodes[index].right_adjacent = nodes[index + row + 1]
                index += 1
        return nodes

    def __str__(self):
        return "".join(self.root.draw_node([], True, []))

    def max_sum_post_order_traversal(self, node) -> int:
        if isinstance(node.left_adjacent, PyramidNode):
            left = self.max_sum_post_order_traversal(node.left_adjacent)
        else:
            left = 0
        if isinstance(node.right_adjacent, PyramidNode):
            right = self.max_sum_post_order_traversal(node.right_adjacent)
        else:
            right = 0
        return max(left, right) + node.value
