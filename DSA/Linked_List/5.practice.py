class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Do not change code above.

def insertAtFirst(list: Node, newValue: int) -> Node:
    