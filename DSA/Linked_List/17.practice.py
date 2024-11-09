"""
Problem statement
A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.


You are given a sorted doubly linked list of size 'n', consisting of distinct positive integers, and a number 'k'.


Find out all the pairs in the doubly linked list with sum equal to 'k'.


Example :
Input: Linked List: 1 <-> 2 <-> 3 <-> 4 <-> 9 and 'k' = 5

Output: (1, 4) and (2, 3)

Explanation: There are 2 pairs in the linked list having sum 'k' = 5.
"""

from typing import List


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def findPairs(head: Node, k: int):
    # better
    # myset = set()
    # temp = head
    # result = []

    # while temp:
    #     remaining = k - temp.data

    #     if remaining in myset:
    #         result.append([remaining, temp.data])

    #     myset.add(temp.data)
    #     temp = temp.next
    # return result

    # optimal: two pointer

    result = []
    left = head
    right = head

    # this is to take right pointer to last
    while right.next:
        right = right.next

    while left.data < right.data:
        total = left.data + right.data

        if total == k:
            left = left.next
            right = right.prev

        elif total > k:
            right = right.prev

        else:
            left = left.next

    return result
