"""
remove duplicate in dobly linked list
"""


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteduplicates(head: Node, k: int) -> Node:
    temp = head

    while temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next

        else:
            temp = temp.next

    return head
