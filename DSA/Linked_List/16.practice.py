"""
Problem statement
A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.



You’re given a doubly-linked list and a key 'k'.



Delete all the nodes having data equal to ‘k’.



Example:
Input: Linked List: 10 <-> 4 <-> 10 <-> 3 <-> 5 <-> 20 <-> 10 and ‘k’ = 10

Output: Modified Linked List: 4 <-> 3 <-> 5 <-> 20

Explanation: All the nodes having ‘data’ = 10 are removed from the linked list.
"""


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def deleteAllOccurrences(head: Node, k: int) -> Node:

    if head.data == k:
        head = head.next
        head.prev = None

    temp = head

    while temp.next:
        if temp.data == k:
            temp.prev.next = temp.next.prev
        temp = temp.next

    if temp.data == k:
        temp.prev.next = None

    return head


n1 = Node(10)
n2 = Node(2)
n3 = Node(4)
n4 = Node(7)
n5 = Node(9)

n1.next = n2
n2.prev = n1

n2.next = n3
n3.prev = n2

n3.next = n4
n4.prev = n3

n4.next = n5
n5.prev = n4


print(deleteAllOccurrences(n1, 2))
