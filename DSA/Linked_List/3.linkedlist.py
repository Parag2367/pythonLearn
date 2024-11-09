class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    # appending new node
    def append(self, data):
        new_node = Node(data)

        if not self.head:  # condition if no head is present means SLL is empty
            self.head = new_node

        else:
            current = self.head
            # we append the new value at last that is why found next as None
            while current.next is not None:
                current = current.next
            current.next = new_node

    # traversing the elinked list
    def traverse(self):
        if not self.head:
            print("SLL is empty")

        else:
            current = self.head

            while current is not None:
                print(current.val, end=" ")
                current = (
                    current.next
                )  # using .next as an increment just like we use +=1
        print()

    # inserting at any position
    def insert_at(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node

        else:
            current = self.head
            prev = None
            count = 0

            # we have to insert at a postion which will have a prev and a current node , that is why we have taken prev, current and count
            # count will take care if position is more than the number of elements in linked list
            while current is not None and count < position:
                prev = current
                current = current.next
                count += 1
            new_node.next = current

            # if prev is not None:
            prev.next = new_node

    # Deleting
    # Delete head
    def delete_head(self):
        if not self.head:
            print("Cannot delete head , as SLL is empty")

        else:
            self.head = self.head.next

    # Delete by value
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
                    return
                else:
                    print("No such node available")


SLL = SinglyLL()
SLL.traverse()


# appending
SLL.append(100)
SLL.append(50)
SLL.append(30)
SLL.append(20)

SLL.traverse()
SLL.delete_head()
SLL.traverse()

SLL.delete_val(30)
SLL.traverse()

SLL.delete_val(1000)
SLL.insert_at(3000, 1)
SLL.traverse()
