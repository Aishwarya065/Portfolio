# Node class to represent each node in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Creating the DoublyLinkedList class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Inserting node at the beginning of the linked list
    def insert_at_begin(self, data):
        new_node = Node(data)
        # If the linked list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
        else:
            # Update the previous head node
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # Deleting the node at the beginning of the linked list
    def delete_at_begin(self):
        if self.head is None:
            print("List is empty")
            return
        elif self.head.next is None:
            # Only one element in the list
            self.head = None
        else:
            # Update the head to the next node
            self.head = self.head.next
            self.head.prev = None

    # Printing the entire linked list
    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Driver code
dll = DoublyLinkedList()

# Insert nodes at the beginning of the list
dll.insert_at_begin(10)
dll.insert_at_begin(20)
dll.insert_at_begin(30)

print("After inserting nodes at the beginning:")
dll.print_all()

# Delete the first node
print("After deleting the first node:")
dll.delete_at_begin()
dll.print_all()
