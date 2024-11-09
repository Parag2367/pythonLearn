class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def check(root1, root2):
    if (root1 and not root2) or (root2 and not root1):
        return False

    if not root1 and not root2:
        return True

    if root1.val != root2.val:
        return False

    return check(root1.left, root2.right) and check(root1.right, root2.left)
