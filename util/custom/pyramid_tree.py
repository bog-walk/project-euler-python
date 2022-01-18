class PyramidNode:
    """
    A Node for the following PyramidTree class that stores its integer value, as
    well as a reference to its 2 children, if it is not a leaf node. Its sole
    method, draw_node(), allows all Nodes in a PyramidTree to be drawn recursively.
    """

    def __init__(self, value: int):
        self.value: int = value
        self.left_adjacent: PyramidNode | None = None
        self.right_adjacent: PyramidNode | None = None

    def draw_node(
            self, prefix: list[str], is_tail: bool, string: list[str]
    ) -> list[str]:
        """
        Note that shared adjacent nodes will be duplicated in this algorithm,
        as the PyramidTree class is not a proper binary tree.

        :returns: String representation of the node & its children.
        """

        vertical = "|   "
        space = "    "
        down = "└── "
        up = "┌── "
        if isinstance(self.right_adjacent, PyramidNode):
            self.right_adjacent.draw_node(
                ["".join(prefix), vertical if is_tail else space], False, string
            )
        string += prefix + [down if is_tail else up, str(self.value), "\n"]
        if isinstance(self.left_adjacent, PyramidNode):
            self.left_adjacent.draw_node(
                ["".join(prefix), space if is_tail else vertical], True, string
            )
        return string


class PyramidTree:
    """
    A Tree (more appropriately a graph) with each node having 2 children except
    for leaf nodes. Every node that is not along the left or right edges will have
    2 parents, unlike in a standard BinaryTree. i.e. Internal children are shared
    by 2 nodes, with nodeX.rightAdjacent == nodeY.leftAdjacent. Therefore, each
    level in the tree will have an amount of nodes equivalent to the level number.
    Also unlike a BinaryTree, nodes in a PyramidTree are not ordered.
    """

    def __init__(self, rows: int, elements: list[int]):
        self.rows = rows
        self.nodes = self.__generate_tree(elements)
        self.root = self.nodes[0]

    def __str__(self) -> str:
        return "".join(self.root.draw_node([], True, []))

    def __generate_tree(self, elements: list[int]) -> list[PyramidNode]:
        nodes = [PyramidNode(e) for e in elements]
        index = 0
        for row in range(1, self.rows):
            for _ in range(row):
                nodes[index].left_adjacent = nodes[index + row]
                nodes[index].right_adjacent = nodes[index + row + 1]
                index += 1
        return nodes

    def max_sum_post_order_traversal(self, node: PyramidNode) -> int:
        """
        Post-order traversal visits the left subtree before the right subtree,
        returning the maximum sum before processing the start node.
        """

        if isinstance(node.left_adjacent, PyramidNode):
            left = self.max_sum_post_order_traversal(node.left_adjacent)
        else:
            left = 0
        if isinstance(node.right_adjacent, PyramidNode):
            right = self.max_sum_post_order_traversal(node.right_adjacent)
        else:
            right = 0
        return max(left, right) + node.value
