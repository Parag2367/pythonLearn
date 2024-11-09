class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Stack is empty")

        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(
        self,
    ):  # as we know when we call print(stack) it goes in and check for __str__ method and return address, but here we changed it to its contents
        # return a string representation of a stack
        return str(self.items)
