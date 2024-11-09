class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None


n1 = Node(100)
n2 = Node(92)
n3 = Node(45)


sll = SinglyLL()
sll.head = n1

n1.next = n2
n2.next = n3

# 100
print(sll.head)  # will be equal to n1 address as mentioned above
print(sll.head.val)  # will be equal to n1 address as mentioned above

# 100 -> 92
print(sll.head.next)  # will be equal to n2 address
print(sll.head.next.val)  # will be equal to n2 address

# 100 -> 92 -> 45
print(sll.head.next.next)  # will be equal to n3 address
print(sll.head.next.next.val)  # will be equal to n3 address


print(sll.head.next.next.next)

print(sll.head)
