from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzag(root):

    if not root:
        return

    queue = deque()
    queue.append(root)

    reverse = True
    while queue:

        node = queue.popleft()
        print(node.data, end=" ")

        if not reverse:
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        else:
            if node.right is not None:
                queue.append(node.right)

            if node.left is not None:
                queue.append(node.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

zigzag(root)
