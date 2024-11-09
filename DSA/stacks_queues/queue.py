class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items)

    def enqueue(self, e):
        if self.is_empty():
            raise IndexError("Queue is empty")
        self.items.append(e)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        return self.items[0]

    def rear(self):
        if self.is_empty():
            print("Queue is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
