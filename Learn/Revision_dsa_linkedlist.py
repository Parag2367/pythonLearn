class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None


# created node
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)

# crated sll, and given a head, as it will have a head parameter
ll = SinglyLL()
ll.head = n1


# linked the list
n1.next = n2
n2.next = n3


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


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LL:
    def __init__(self):
        self.head = None


class Solution:  # tortoise and hare
    def middle(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


"""
linked list cycle
"""


def llcycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

        return False


"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""


def detect(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # this means it is a cycle
            slow = head  # this is again taking slow to head
            while slow is not fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


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


# we will be using a stack to store value and sort it and againg refer that to print sorted linked list


def sortedll(head):
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
