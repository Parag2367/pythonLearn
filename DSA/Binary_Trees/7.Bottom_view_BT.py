class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


from collections import deque


def bottomView(root):
    ans = []
    queue = deque()
    hash_map = dict()

    queue.append([root, 0])

    while queue:
        ele, line = queue.popleft()

        hash_map[line] = ele.val

        if ele.left:
            queue.append([ele.left, line - 1])

        if ele.right:
            queue.append([ele.right, line + 1])

    for k, v in sorted(hash_map.items()):
        ans.append(v)

    return ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print(bottomView(root))
