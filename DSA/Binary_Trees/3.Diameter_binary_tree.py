class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    diam = 0

    def diameter(self, root):
        if not root:
            return 0

        left_d = self.diameter(root.left)
        right_d = self.diameter(root.right)
        self.diam = max(self.diam, left_d + right_d)
        return 1 + max(left_d, right_d)

    def solu(self, root: TreeNode):
        self.diameter(root)
        return self.diam
