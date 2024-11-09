"""
linked list cycle
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def llcycle(self, head: Optional[ListNode]) -> bool:
        # brute force
        # temp = head
        # myset = set()

        # while temp is not None:
        #     if temp in myset:
        #         return True
        #     myset.add(temp)
        #     temp = temp.next
        # return False

        # optimal : Toroise and hare

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
