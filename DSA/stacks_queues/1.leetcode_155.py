"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""


class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            mini = min(val, self.items[-1][-1])
            self.items.append([val, mini])

    def pop(self) -> None:
        if not self.items:
            return
        self.items.pop()

    def top(self) -> int:
        if not self.items:
            return 0
        return self.items[-1][0]

    def getMin(self) -> int:
        if not self.items:
            return 0
        return self.items[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
