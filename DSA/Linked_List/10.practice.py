"""
Problem statement
You’re given a linked list. The last node might point to null, or it might point to a node in the list, thus forming a cycle.

Find out whether the linked list has a cycle or not, and the length of the cycle if it does.

If there is no cycle, return 0, otherwise return the length of the cycle.

Example:
Input: Linked List: 4 -> 10 -> 3 -> 5 -> 10(at position 2)

Output: Length of cycle = 3

Explanation: The cycle is 10, 3, 5.
"""


class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:

    # brute force
    """
    TC : O(n)
    SC : O(n)
    """
    # temp = head
    # travel = 0
    # mydict = dict()

    # while temp:
    #     if temp in mydict:
    #         return travel - mydict[temp]

    #     mydict[temp] = travel
    #     travel += 1
    #     temp = temp.next

    # return 0

    # optimal

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            count = 1

            while slow is not fast:
                count += 1
                slow = slow.next
            return count
    return 0
