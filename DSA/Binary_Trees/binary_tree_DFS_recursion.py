class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)


def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.data, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("preorder_traversal: ")
preorder_traversal(root)
print("\npostorder_traversal: ")
postorder_traversal(root)
print("\ninorder_traversal: ")
inorder_traversal(root)
