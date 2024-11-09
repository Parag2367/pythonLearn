class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height_balance(root):
    if not root:
        return 0

    left_h = height_balance(root.left)
    right_h = height_balance(root.right)

    if (
        left_h == -1 or right_h == -1
    ):  # this will be checked on the basis of below abs(difference)
        return -1

    if abs(left_h - right_h) > 1:
        return -1

    return 1 + max(left_h, right_h)


def solution(root):
    ans = height_balance(root)
    if ans >= 0:
        return True
    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)
root.right.right.left.left = Node(9)

print(solution(root))
