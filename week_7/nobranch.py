"""
Your task is to find out if a given tree is branchless, i.e., if every node has at most one child.

In a file nobranch.py, implement a function check that reports whether the tree is branchless or not.
"""


class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


"""
cleaner way
def check(node):
    if node.children == []:
        return True
    if len(node.children) > 1:
        return False
    return check(node.children[0])
"""


# my code
def check(node):
    if len(node.children) > 1:
        return False

    if not node.children:
        return True

    is_branchless = True
    for child in node.children:
        if len(child.children) > 1:
            return False
        is_branchless = check(child)
    return is_branchless


if __name__ == "__main__":
    tree1 = Node(
        1,
        [Node(2), Node(3, [Node(4, [Node(5), Node(6)])]), Node(7, [Node(8), Node(9)])],
    )

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    tree3 = Node(3, [Node(1), Node(2)])

    print(check(tree1))  # False
    print(check(tree2))  # True
    print(check(tree3))  # False
