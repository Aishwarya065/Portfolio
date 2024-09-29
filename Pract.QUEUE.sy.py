# Define a Queue class using a circular array
class Queue:
    def __init__(self, capacity):
        # Initialize the front pointer, size, and rear pointer
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity   # Create a list of `None` values to represent the queue
        self.capacity = capacity     # Maximum capacity of the queue

    # Method to check if the queue is full
    def isFull(self):
        return self.size == self.capacity

    # Method to check if the queue is empty
    def isEmpty(self):
        return self.size == 0

    # Method to add an item to the queue
    def Enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        # Calculate the new rear position using modulo operation to ensure circular behavior
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1
        print(f"{item} enqueued to queue")

    # Method to remove an item from the queue
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        # Remove the front item and update front pointer
        print(f"{self.Q[self.front]} dequeued from queue")
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    # Method to display the front item
    def frontItem(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(f"Front item is: {self.Q[self.front]}")

    # Method to display the rear item
    def rearItem(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(f"Rear item is: {self.Q[self.rear]}")

# Create a queue of capacity 10
q = Queue(10)

# Perform enqueue operations
q.Enqueue(30)
q.Enqueue(20)
q.Enqueue(10)
q.Enqueue(5)

# Dequeue an element
q.Dequeue()

# Check front and rear items
q.frontItem()
q.rearItem()
