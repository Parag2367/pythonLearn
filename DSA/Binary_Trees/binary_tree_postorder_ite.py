class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# with using two stacks
def postorder(root):
    result = []
    st1 = []
    st2 = []
    st1.append(root)

    while st1:
        r = st1.pop()
        st2.append(r)

        if r.left:
            st1.append(r.left)

        if r.right:
            st1.append(r.right)

    for i in range(len(st2) - 1, -1, -1):
        result.append(st2[i].data)
        st2.pop()

    return result


# this is similar to inorder iterative
def postorder_onestack(root):
    stack = []
    result = []
    current = root
    prev = None

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack[-1]

        if current.right is None or current.right == prev:
            prev = stack.pop()
            result.append(prev.data)
            current = None

        else:
            current = current.right

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.right.right = Node(8)


print(postorder(root))
print(postorder_onestack(root))
