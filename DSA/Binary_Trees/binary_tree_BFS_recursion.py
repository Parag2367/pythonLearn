from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):

    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

        # print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
level_order_traversal(root)
