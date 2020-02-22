class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root = root

    def search(self, key):
        """O(logN) on balanced tree. O(N) on one sided tree"""
        cur = self.root
        while cur:
            if cur.key == key:
                return cur

            elif key < cur.key:
                cur = cur.left

            else:
                cur = cur.right
        # not found
        return None

    def insert(self, node):
        """Best: O(logN), Worst: O(N)"""
        if self.root is None:
            self.root = node
            return

        cur = self.root
        while cur:
            if node.key < cur.key:
                # if no left child, add there
                if cur.left is None:
                    cur.left = node
                    break
                else:
                    cur = cur.left  # go left
            else:
                if cur.right is None:
                    cur.right = node
                    break
                else:
                    cur = cur.right  # go right

    def remove(self, key):
        parent = None
        cur = self.root

        while cur:
            if cur.key == key:
                # case leaf
                if cur.left is None and cur.right is None:
                    if parent is None:  # is root
                        self.root = None
                    elif parent.left is cur:
                        parent.left = None
                    else:
                        parent.right = None
                    return

                # case 1 child left
                if cur.left is not None and cur.right is None:
                    if parent is None:
                        self.root = cur.left
                    elif parent.left is cur:
                        parent.left = cur.left
                    else:
                        parent.right = cur.left
                    return

                # case 1 child right
                if cur.left is None and cur.right is not None:
                    if parent is None:
                        self.root = cur.right
                    elif parent.left is cur:
                        parent.left = cur.right
                    else:
                        parent.right = cur.right
                    return

                # case 2 children
                successor = cur.right
                while successor.left:
                    successor = successor.left
                cur.key = successor.key  # copy successor to current node
                # removal of successor from right subtree
                key = successor.key  # new key
                parent = cur
                cur = cur.right
                # loop continues and removes the successor
            elif cur.key < key:
                # search right
                parent = cur
                cur = cur.right
            else:
                parent = cur
                cur = cur.left

        return  # not found


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
