from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height_bt_it(root):  # iterative approach
    level = 0
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            r = queue.popleft()

            if r.left:
                queue.append(r.left)

            if r.right:
                queue.append(r.right)

        level += 1

    return level


def height_bt_re(root):
    if not root:
        return 0

    left_h = height_bt_re(root.left)
    right_h = height_bt_re(root.right)

    return 1 + max(left_h, right_h)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)
root.right.right.right = Node(8)
root.right.right.right.left = Node(9)


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.right.right.left = Node(8)
root1.right.right.left.left = Node(9)

print(height_bt_it(root))
print(height_bt_re(root1))
