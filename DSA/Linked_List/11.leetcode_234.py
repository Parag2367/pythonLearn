"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true
Example 2:

Input: head = [1,2]
Output: false
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # brute force
    """
    TC: O(n)
    SC: O(n)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # stack = []
        # temp = head

        # while temp is not None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # temp = head

        # while temp is not None:
        #     if temp.val != stack.pop():
        #         return False

        # return True

        # optimal
        # for reversing
        def reverse(head):
            temp = head
            prev = None

            while temp:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front

            return prev

        # for finding middle node
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = reverse(slow.next)  # second half

        first = head
        second = new_head

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        reverse(new_head)
        return True


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(3)


obj1 = Solution()
print(obj1.isPalindrome(n1))
