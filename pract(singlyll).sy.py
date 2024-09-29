# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the Linked List
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at the end of the Linked List
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Method to print the Linked List
    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate the end of the list

    # Method to remove the first node from the Linked List
    def remove_first_node(self):
        if self.head is None:
            print("The list is empty, no node to remove.")
            return
        self.head = self.head.next

    # Method to remove the last node from the Linked List
    def remove_last_node(self):
        if self.head is None:
            print("The list is empty, no node to remove.")
            return

        # If there's only one node, remove it
        if self.head.next is None:
            self.head = None
            return

        # Traverse the list to find the second-to-last node
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        # Remove the last node
        current_node.next = None

# Create a new Linked List instance
llist = LinkedList()

# Add nodes to the Linked List
llist.insert_at_begin('b')
llist.insert_at_begin('a')
llist.insert_at_end('c')
llist.insert_at_begin('s')

# Print the Linked List
print("Node Data:")
llist.print_ll()

# Remove the first node from the Linked List and print the result
llist.remove_first_node()
print("After removing the first node:")
llist.print_ll()

# Remove the last node from the Linked List and print the result
llist.remove_last_node()
print("After removing the last node:")
llist.print_ll()
