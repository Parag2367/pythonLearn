"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.


Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force
        """
        TC: O(n): while + O(nlogn):sort + O(n): while
        SC: O(n): stack
        """
        stack = []
        temp = head
        index = 0

        while temp:
            stack.append(temp.val)
            temp = temp.next
        stack.sort()
        temp = head

        while temp:
            temp.val = stack[index]
            index += 1
            temp = temp.next

        return head


h = ListNode(2, 1)
h1 = ListNode(1, 3)
h2 = ListNode(3, 4)

head = h
h.next = h1
h1.next = h2

sol = Solution()
print(sol.sortList(h))
