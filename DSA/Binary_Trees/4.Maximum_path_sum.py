class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class maximumPath:
    maxi = float("-inf")

    def path_sum(self, root):
        if not root:
            return 0

        left_s = max(0, self.path_sum(root.left))
        right_s = max(0, self.path_sum(root.right))

        self.maxi = max(self.maxi, (left_s + right_s + root.data))

        return max(left_s, right_s) + root.data

    def solution(self, root: Treenode):
        self.path_sum(root)
        return self.maxi
