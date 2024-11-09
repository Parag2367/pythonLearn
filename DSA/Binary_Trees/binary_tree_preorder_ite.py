class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    result = []

    if root is None:
        return result

    st = []
    st.append(root)

    while st:
        r = st.pop()  # r is nothing but a node as in st whole node is getting appended
        result.append(r.data)

        if r.right:
            st.append(r.right)

        if r.left:
            st.append(r.left)

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print(preorder(root))
