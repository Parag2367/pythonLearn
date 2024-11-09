from collections import deque

q = deque()
print(q)

q.append(100)
q.append(200)
q.append(300)
print(q)

q.appendleft(1000)
q.appendleft(800)
print(q)


q.pop()
print(q)


q.popleft()
print(q)


# implement stack using queue
class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue)

    # implementing stack using queue, as queue is fifo(last in first out) so to convert it to lifo, we did below

    def push(self, item):
        if self.is_empty():
            print("The stack is empty")

        self.queue.append(item)

        for _ in range(len(self.queue) - 1):
            # changing , as to male added item to move in front
            self.queue.append(self.queue.popleft())

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")

        return self.queue.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.queue[0]


class QueueUsingStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]
