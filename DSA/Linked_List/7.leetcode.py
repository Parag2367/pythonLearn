"""
Reverse a linked list
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force

        # temp = head
        # stack = []

        # while temp is not None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head

        # while temp:
        #     temp.val = stack.pop()
        #     temp = temp.next
        # return head

        # optimal

        temp = head
        prev = None

        while temp:
            front = temp.next  # did this ti go to next node
            temp.next = (
                prev  # did this to None the temp.next as it will be my last node
            )
            prev = temp  # did this for taking previous value
            temp = front  # did this for next value

        return prev


n1 = ListNode(100)
n2 = ListNode(50)
n3 = ListNode(60)
n4 = ListNode(80)
n5 = ListNode(90)


obj1 = Solution()
print(obj1.reverse(n1))
