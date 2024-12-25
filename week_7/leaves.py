"""
Your task is to count the number of leaves in a given tree. A node is a leaf if it has no children.

In a file leaves.py, implement a function count that returns the number of leaves.
"""


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def count(node):
    if not node.children:
        return 1

    total_leaves = 0
    for child in node.children:
        total_leaves += count(child)
    return total_leaves


if __name__ == "__main__":
    tree = Node(
        1,
        [Node(2), Node(3, [Node(4, [Node(5), Node(6)])]), Node(7, [Node(8), Node(9)])],
    )

    print(count(tree))  # 5
