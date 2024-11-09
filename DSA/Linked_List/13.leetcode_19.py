"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force
        """
        TC: O(n) + O(l-n) == O(n)
        SC : O(n)
        """
        # def total(head):
        #     temp = head
        #     count = 0

        #     while temp is not None:
        #         count += 1
        #         temp = temp.next

        #     return count

        # if total(head) == 1:
        #     return

        # position = total(head) - n

        # # edge case where count == n:
        # if position == 0:
        #     return head.next

        # current = head
        # count = 0
        # prev = None

        # while current is not None and count < position:
        #     prev = current
        #     current = current.next
        #     count += 1
        # prev.next = current.next

        # return head

        # optimal: slidng window

        slow = head
        fast = head

        # for moving fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # edge case where n =  length of linked list

        if fast is None:
            return head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


n1 = ListNode(11)
n2 = ListNode(11)
n3 = ListNode(11)
n4 = ListNode(11)
n5 = ListNode(11)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


obj1 = Solution()
print(obj1.removeNthFromEnd(n1, 2))
