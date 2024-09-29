# Initialize the stack
stack = []

# Pushing the elements into the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Displaying the stack items
print("The stack items are:")
for i in stack:
    print(i)

# Pop operation
def pop(stack):
    if len(stack) == 0:
        return None
    else:
        return stack.pop()

# Display the initial stack
print("Initial Stack:")
print(stack)

# Pop an element from the stack
popped_element = pop(stack)
print("Popped Element:", popped_element)

# Function to get the top element of the stack
def top():
    if len(stack) == 0:
        return None
    return stack[-1]

# Display the top element of the stack
print("Top element of stack is:", top())

# Function to check if the stack is empty
def is_empty():
    return len(stack) == 0

# Display if the stack is empty
print("Is the stack empty?", is_empty())
