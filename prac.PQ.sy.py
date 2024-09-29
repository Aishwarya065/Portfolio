# Define the node for Priority Queue
class PQNode:
    def __init__(self, value, pr):
        self.data = value      # The data of the node
        self.priority = pr     # The priority of the node
        self.next = None       # Pointer to the next node

# Define the Priority Queue class using a linked list
class PQ:
    def __init__(self):
        self.front = None      # Initialize the front pointer to None (Empty queue)

    # Method to check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Method to add an item to the priority queue
    def push(self, value, priority):
        # Create a new node with the given value and priority
        new_node = PQNode(value, priority)

        # Check if the queue is empty or if the new node has higher priority than the front node
        if self.is_empty() or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
            return 1

        # Traverse the queue to find the appropriate position for the new node
        temp = self.front
        while temp.next and temp.next.priority <= priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        return 1

    # Method to remove the node with the highest priority (front node)
    def pop(self):
        if self.is_empty():
            return "Queue is Empty!"
        else:
            self.front = self.front.next
            return 1

    # Method to get the data of the node with the highest priority
    def peek(self):
        if self.is_empty():
            return "Queue is Empty!"
        else:
            return self.front.data

    # Method to traverse and print the priority queue
    def traverse(self):
        if self.is_empty():
            print("Queue is Empty!")
        else:
            temp = self.front
            while temp:
                print(f"({temp.data}, Priority: {temp.priority})", end=" -> ")
                temp = temp.next
            print("None")

# Create an instance of the Priority Queue
pq = PQ()

# Add elements to the queue
pq.push(4, 1)
pq.push(5, 2)
pq.push(6, 3)
pq.push(7, 0)

# Traverse the queue
print("Initial Queue:")
pq.traverse()

# Remove the highest priority item (front item)
pq.pop()
print("\nQueue after removing the highest priority item:")
pq.traverse()
