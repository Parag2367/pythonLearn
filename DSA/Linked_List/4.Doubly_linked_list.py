class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None  # putting 0 instead of None
        self.prev = None  # putting 0 instead of None


class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserAtHead(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insertAtTail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        if not self.head:
            print("DLL is empty")

        else:
            current = self.head

            while current is not None:
                print(current.val, end=" ")
                current = current.next
        print()

    def insertAt(self, position, data):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        else:
            current = self.head
            previ = None
            count = 0

            while current is not None and count < position:
                previ = current
                current = current.next
                count += 1

            previ.next = new_node
            current.prev = new_node

            new_node.prev = previ
            new_node.next = current

    def delete_head(self):
        if not self.head:
            print("Cannot remove as no head")

        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self):
        if not self.head:
            print("Cannot delete as no tail")

        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_val(self, data):
        temp = self.head

        if temp.next is not None:
            if temp.val == data:
                self.head = temp.next
                return

            else:
                found = False

                while temp is not None:
                    if temp.val == data:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    temp.next.prev = prev
                    return
                else:
                    print("No such value")


dll = DoublyLL()
dll.inserAtHead(100)
dll.inserAtHead(200)
dll.inserAtHead(300)
dll.inserAtHead(400)

dll.traverse()

dll.insertAt(2, 500)
dll.traverse()

# dll.delete_head()
# dll.delete_tail()
dll.delete_val(200)
dll.traverse()

dll.delete_val(500)
dll.traverse()
