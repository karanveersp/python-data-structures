class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root


def bst_search(tree, key):
    cur = tree.root
    while cur:
        if key == cur.key:
            return cur
        elif key < cur.key:
            cur = cur.left
        else:
            cur = cur.right
    return None


def bst_insert(tree, node):
    """Best: O(logN), Worst: O(N)"""
    node.left = None
    node.right = None
    if tree.root is None:
        tree.root = node
        return

    cur = tree.root
    while cur:
        if node.key < cur.key:
            if cur.left is None:
                cur.left = node
                return
            else:
                cur = cur.left
        else:
            if cur.right is None:
                cur.right = node
                return
            else:
                cur = cur.right


if __name__ == "__main__":
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    tree = Tree()
    bst_insert(tree, a)
    bst_insert(tree, b)
    bst_insert(tree, c)
