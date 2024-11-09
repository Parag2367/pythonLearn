"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Brute force
        # count = 0
        # temp = head

        # while temp is not None:
        #     count += 1
        #     temp = temp.next

        # temp = head

        # for i in range(count // 2):
        #     temp = temp.next

        # return temp

        # optimal : tortoise and Hare
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # slow.next = slow.next.next  # for removing middle

        return slow


n1 = ListNode(100)
n2 = ListNode(50)
n3 = ListNode(60)
n4 = ListNode(80)
n5 = ListNode(90)


obj1 = Solution()
print(obj1.middleNode(n1))
